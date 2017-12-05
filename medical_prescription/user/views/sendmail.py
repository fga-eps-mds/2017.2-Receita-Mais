# standard library
import threading

# django
from django.core.mail import send_mail

# local django
from user import constants


class SendMail(threading.Thread):
    """
    Responsible to send email in background.
    """
    def __init__(self, email, HealthProfessional, SendInvitationProfile):
        self.email = email
        self.HealthProfessional = HealthProfessional
        self.SendInvitationProfile = SendInvitationProfile
        threading.Thread.__init__(self)

    def run(self):
        email_subject = constants.INVITATION_EMAIL_SUBJECT
        email_body = constants.INVITATION_EMAIL_BODY

        send_mail(email_subject, email_body % (self.HealthProfessional.name,
                                               self.SendInvitationProfile.activation_key),
                  'medicalprescriptionapp@gmail.com', [self.email], fail_silently=False)
