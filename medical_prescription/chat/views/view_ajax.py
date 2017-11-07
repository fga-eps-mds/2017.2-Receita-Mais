from __future__ import unicode_literals

import json
import inspect
import datetime
import re

from django.core import serializers
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import six
from django import VERSION as DJANGO_VERSION
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login, logout_then_login
from django.http import (HttpResponseRedirect, HttpResponsePermanentRedirect,
                         Http404, HttpResponse, StreamingHttpResponse, HttpResponseBadRequest)
from django.shortcuts import resolve_url
from django.utils.encoding import force_text
from django.utils.timezone import now


class JSONResponseMixin(object):
    """
    A mixin that allows you to easily serialize simple data such as a dict or
    Django models.
    """
    content_type = None
    json_dumps_kwargs = None
    json_encoder_class = DjangoJSONEncoder

    def get_content_type(self):
        if (self.content_type is not None and
            not isinstance(self.content_type,
                           (six.string_types, six.text_type))):
            raise ImproperlyConfigured(
                '{0} is missing a content type. Define {0}.content_type, '
                'or override {0}.get_content_type().'.format(
                    self.__class__.__name__))
        return self.content_type or "application/json"

    def get_json_dumps_kwargs(self):
        if self.json_dumps_kwargs is None:
            self.json_dumps_kwargs = {}
        self.json_dumps_kwargs.setdefault('ensure_ascii', False)
        return self.json_dumps_kwargs

    def render_json_response(self, context_dict, status=200):
        """
        Limited serialization for shipping plain data. Do not use for models
        or other complex or custom objects.
        """
        json_context = json.dumps(
            context_dict,
            cls=self.json_encoder_class,
            **self.get_json_dumps_kwargs()).encode('utf-8')
        return HttpResponse(json_context,
                            content_type=self.get_content_type(),
                            status=status)

    def render_json_object_response(self, objects, **kwargs):
        """
        Serializes objects using Django's builtin JSON serializer. Additional
        kwargs can be used the same way for django.core.serializers.serialize.
        """
        json_data = serializers.serialize("json", objects, **kwargs)
        return HttpResponse(json_data, content_type=self.get_content_type())


class AjaxResponseMixin(object):
    """
    Mixin allows you to define alternative methods for ajax requests. Similar
    to the normal get, post, and put methods, you can use get_ajax, post_ajax,
    and put_ajax.
    """
    def dispatch(self, request, *args, **kwargs):
        request_method = request.method.lower()

        if request.is_ajax() and request_method in self.http_method_names:
            handler = getattr(self, "{0}_ajax".format(request_method),
                              self.http_method_not_allowed)
            self.request = request
            self.args = args
            self.kwargs = kwargs
            return handler(request, *args, **kwargs)

        return super(AjaxResponseMixin, self).dispatch(
            request, *args, **kwargs)

    def get_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def post_ajax(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def put_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def delete_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class JsonRequestResponseMixin(JSONResponseMixin):
    """
    Extends JSONResponseMixin.  Attempts to parse request as JSON.  If request
    is properly formatted, the json is saved to self.request_json as a Python
    object.  request_json will be None for imparsible requests.
    Set the attribute require_json to True to return a 400 "Bad Request" error
    for requests that don't contain JSON.
    Note: To allow public access to your view, you'll need to use the
    csrf_exempt decorator or CsrfExemptMixin.
    Example Usage:
        class SomeView(CsrfExemptMixin, JsonRequestResponseMixin):
            def post(self, request, *args, **kwargs):
                do_stuff_with_contents_of_request_json()
                return self.render_json_response(
                    {'message': 'Thanks!'})
    """
    require_json = False
    error_response_dict = {"errors": ["Improperly formatted request"]}

    def render_bad_request_response(self, error_dict=None):
        if error_dict is None:
            error_dict = self.error_response_dict
        json_context = json.dumps(
            error_dict,
            cls=self.json_encoder_class,
            **self.get_json_dumps_kwargs()
        ).encode('utf-8')
        return HttpResponseBadRequest(
            json_context, content_type=self.get_content_type())

    def get_request_json(self):
        try:
            return json.loads(self.request.body.decode('utf-8'))
        except ValueError:
            return None

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs

        self.request_json = self.get_request_json()
        if self.require_json and self.request_json is None:
            return self.render_bad_request_response()
        return super(JsonRequestResponseMixin, self).dispatch(
            request, *args, **kwargs)


class JSONRequestResponseMixin(JsonRequestResponseMixin):
    pass


if DJANGO_VERSION >= (1, 10, 0):
    _is_authenticated = lambda user: user.is_authenticated  # noqa
else:
    # Django<1.10 compatibility
    _is_authenticated = lambda user: user.is_authenticated()  # noqa


class AccessMixin(object):
    """
    'Abstract' mixin that gives access mixins the same customizable
    functionality.
    """
    login_url = None
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth
    redirect_unauthenticated_users = False

    def get_login_url(self):
        """
        Override this method to customize the login_url.
        """
        login_url = self.login_url or settings.LOGIN_URL
        if not login_url:
            raise ImproperlyConfigured(
                'Define {0}.login_url or settings.LOGIN_URL or override '
                '{0}.get_login_url().'.format(self.__class__.__name__))

        return force_text(login_url)

    def get_redirect_field_name(self):
        """
        Override this method to customize the redirect_field_name.
        """
        if self.redirect_field_name is None:
            raise ImproperlyConfigured(
                '{0} is missing the '
                'redirect_field_name. Define {0}.redirect_field_name or '
                'override {0}.get_redirect_field_name().'.format(
                    self.__class__.__name__))
        return self.redirect_field_name

    def handle_no_permission(self, request):
        if self.raise_exception:
            if (self.redirect_unauthenticated_users
                    and not _is_authenticated(request.user)):
                return self.no_permissions_fail(request)
            else:
                if (inspect.isclass(self.raise_exception)
                        and issubclass(self.raise_exception, Exception)):
                    raise self.raise_exception
                if callable(self.raise_exception):
                    ret = self.raise_exception(request)
                    if isinstance(ret, (HttpResponse, StreamingHttpResponse)):
                        return ret
                raise PermissionDenied

        return self.no_permissions_fail(request)

    def no_permissions_fail(self, request=None):
        """
        Called when the user has no permissions and no exception was raised.
        This should only return a valid HTTP response.
        By default we redirect to login.
        """
        return redirect_to_login(request.get_full_path(),
                                 self.get_login_url(),
                                 self.get_redirect_field_name())


class LoginRequiredMixin(AccessMixin):
    """
    View mixin which verifies that the user is authenticated.
    NOTE:
        This should be the left-most mixin of a view, except when
        combined with CsrfExemptMixin - which in that case should
        be the left-most mixin.
    """
    def dispatch(self, request, *args, **kwargs):
        if not _is_authenticated(request.user):
            return self.handle_no_permission(request)

        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class AnonymousRequiredMixin(object):
    """
    View mixin which redirects to a specified URL if authenticated.
    Can be useful if you wanted to prevent authenticated users from
    accessing signup pages etc.
    NOTE:
        This should be the left-most mixin of a view.
    Example Usage
        class SomeView(AnonymousRequiredMixin, ListView):
            ...
            # required
            authenticated_redirect_url = "/accounts/profile/"
            ...
    """
    authenticated_redirect_url = settings.LOGIN_REDIRECT_URL

    def dispatch(self, request, *args, **kwargs):
        if _is_authenticated(request.user):
            return HttpResponseRedirect(self.get_authenticated_redirect_url())
        return super(AnonymousRequiredMixin, self).dispatch(
            request, *args, **kwargs)

    def get_authenticated_redirect_url(self):
        """ Return the reversed authenticated redirect url. """
        if not self.authenticated_redirect_url:
            raise ImproperlyConfigured(
                '{0} is missing an authenticated_redirect_url '
                'url to redirect to. Define '
                '{0}.authenticated_redirect_url or override '
                '{0}.get_authenticated_redirect_url().'.format(
                    self.__class__.__name__))
        return resolve_url(self.authenticated_redirect_url)


class PermissionRequiredMixin(AccessMixin):
    """
    View mixin which verifies that the logged in user has the specified
    permission.
    Class Settings
    `permission_required` - the permission to check for.
    `login_url` - the login url of site
    `redirect_field_name` - defaults to "next"
    `raise_exception` - defaults to False - raise 403 if set to True
    Example Usage
        class SomeView(PermissionRequiredMixin, ListView):
            ...
            # required
            permission_required = "app.permission"
            # optional
            login_url = "/signup/"
            redirect_field_name = "hollaback"
            raise_exception = True
            ...
    """
    permission_required = None  # Default required perms to none

    def get_permission_required(self, request=None):
        """
        Get the required permissions and return them.
        Override this to allow for custom permission_required values.
        """
        # Make sure that the permission_required attribute is set on the
        # view, or raise a configuration error.
        if self.permission_required is None:
            raise ImproperlyConfigured(
                '{0} requires the "permission_required" attribute to be '
                'set.'.format(self.__class__.__name__))

        return self.permission_required

    def check_permissions(self, request):
        """
        Returns whether or not the user has permissions
        """
        perms = self.get_permission_required(request)
        return request.user.has_perm(perms)

    def dispatch(self, request, *args, **kwargs):
        """
        Check to see if the user in the request has the required
        permission.
        """
        has_permission = self.check_permissions(request)

        if not has_permission:
            return self.handle_no_permission(request)

        return super(PermissionRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class MultiplePermissionsRequiredMixin(PermissionRequiredMixin):
    """
    View mixin which allows you to specify two types of permission
    requirements. The `permissions` attribute must be a dict which
    specifies two keys, `all` and `any`. You can use either one on
    its own or combine them. The value of each key is required to be a
    list or tuple of permissions. The standard Django permissions
    style is not strictly enforced. If you have created your own
    permissions in a different format, they should still work.
    By specifying the `all` key, the user must have all of
    the permissions in the passed in list.
    By specifying The `any` key , the user must have ONE of the set
    permissions in the list.
    Class Settings
        `permissions` - This is required to be a dict with one or both
            keys of `all` and/or `any` containing a list or tuple of
            permissions.
        `login_url` - the login url of site
        `redirect_field_name` - defaults to "next"
        `raise_exception` - defaults to False - raise 403 if set to True
    Example Usage
        class SomeView(MultiplePermissionsRequiredMixin, ListView):
            ...
            #required
            permissions = {
                "all": ("blog.add_post", "blog.change_post"),
                "any": ("blog.delete_post", "user.change_user")
            }
            #optional
            login_url = "/signup/"
            redirect_field_name = "hollaback"
            raise_exception = True
    """
    permissions = None  # Default required perms to none

    def get_permission_required(self, request=None):
        self._check_permissions_attr()
        return self.permissions

    def check_permissions(self, request):
        permissions = self.get_permission_required(request)
        perms_all = permissions.get('all') or None
        perms_any = permissions.get('any') or None

        self._check_permissions_keys_set(perms_all, perms_any)
        self._check_perms_keys("all", perms_all)
        self._check_perms_keys("any", perms_any)

        # If perms_all, check that user has all permissions in the list/tuple
        if perms_all:
            if not request.user.has_perms(perms_all):
                return False

        # If perms_any, check that user has at least one in the list/tuple
        if perms_any:
            has_one_perm = False
            for perm in perms_any:
                if request.user.has_perm(perm):
                    has_one_perm = True
                    break

            if not has_one_perm:
                return False

        return True

    def _check_permissions_attr(self):
        """
        Check permissions attribute is set and that it is a dict.
        """
        if self.permissions is None or not isinstance(self.permissions, dict):
            raise ImproperlyConfigured(
                '{0} requires the "permissions" attribute to be set as a '
                'dict.'.format(self.__class__.__name__))

    def _check_permissions_keys_set(self, perms_all=None, perms_any=None):
        """
        Check to make sure the keys `any` or `all` are not both blank.
        If both are blank either an empty dict came in or the wrong keys
        came in. Both are invalid and should raise an exception.
        """
        if perms_all is None and perms_any is None:
            raise ImproperlyConfigured(
                '{0} requires the "permissions" attribute to be set to a '
                'dict and the "any" or "all" key to be set.'.format(
                    self.__class__.__name__))

    def _check_perms_keys(self, key=None, perms=None):
        """
        If the permissions list/tuple passed in is set, check to make
        sure that it is of the type list or tuple.
        """
        if perms and not isinstance(perms, (list, tuple)):
            raise ImproperlyConfigured(
                '{0} requires the permisions dict {1} value to be a '
                'list or tuple.'.format(self.__class__.__name__, key))


class GroupRequiredMixin(AccessMixin):
    group_required = None

    def get_group_required(self):
        if self.group_required is None or (
                not isinstance(self.group_required,
                               (list, tuple) + six.string_types)
        ):

            raise ImproperlyConfigured(
                '{0} requires the "group_required" attribute to be set and be '
                'one of the following types: string, unicode, list or '
                'tuple'.format(self.__class__.__name__))
        if not isinstance(self.group_required, (list, tuple)):
            self.group_required = (self.group_required,)
        return self.group_required

    def check_membership(self, groups):
        """ Check required group(s) """
        if self.request.user.is_superuser:
            return True
        user_groups = self.request.user.groups.values_list("name", flat=True)
        return set(groups).intersection(set(user_groups))

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        in_group = False
        if _is_authenticated(request.user):
            in_group = self.check_membership(self.get_group_required())

        if not in_group:
            return self.handle_no_permission(request)

        return super(GroupRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class UserPassesTestMixin(AccessMixin):
    """
    CBV Mixin allows you to define test that every user should pass
    to get access into view.
    Class Settings
        `test_func` - This is required to be a method that takes user
            instance and return True or False after checking conditions.
        `login_url` - the login url of site
        `redirect_field_name` - defaults to "next"
        `raise_exception` - defaults to False - raise 403 if set to True
    """

    def test_func(self, user):
        raise NotImplementedError(
            '{0} is missing implementation of the '
            'test_func method. You should write one.'.format(
                self.__class__.__name__))

    def get_test_func(self):
        return getattr(self, "test_func")

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()(request.user)

        if not user_test_result:
            return self.handle_no_permission(request)

        return super(UserPassesTestMixin, self).dispatch(
            request, *args, **kwargs)


class SuperuserRequiredMixin(AccessMixin):
    """
    Mixin allows you to require a user with `is_superuser` set to True.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission(request)

        return super(SuperuserRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class StaffuserRequiredMixin(AccessMixin):
    """
    Mixin allows you to require a user with `is_staff` set to True.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission(request)

        return super(StaffuserRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class SSLRequiredMixin(object):
    """
    Simple mixin that allows you to force a view to be accessed
    via https.
    """
    raise_exception = False  # Default whether to raise an exception to none

    def dispatch(self, request, *args, **kwargs):
        if getattr(settings, 'DEBUG', False):
            return super(SSLRequiredMixin, self).dispatch(
                request, *args, **kwargs)

        if not request.is_secure():
            if self.raise_exception:
                raise Http404

            return HttpResponsePermanentRedirect(
                self._build_https_url(request))

        return super(SSLRequiredMixin, self).dispatch(request, *args, **kwargs)

    def _build_https_url(self, request):
        """ Get the full url, replace http with https """
        url = request.build_absolute_uri(request.get_full_path())
        return re.sub(r'^http', 'https', url)


class RecentLoginRequiredMixin(LoginRequiredMixin):
    """
    Mixin allows you to require a login to be within a number of seconds.
    """
    max_last_login_delta = 1800  # Defaults to 30 minutes

    def dispatch(self, request, *args, **kwargs):
        resp = super(RecentLoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)

        if resp.status_code == 200:
            delta = datetime.timedelta(seconds=self.max_last_login_delta)
            if now() > (request.user.last_login + delta):
                return logout_then_login(request, self.get_login_url())
            else:
                return resp
        return resp
