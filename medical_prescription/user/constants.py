# Constants file.

# CRM FIELDS.
CRM = 'CRM'
CRM_LENGTH = 5
CRM_STATE_LENGTH = 2

# CRM MESSAGES VALIDATION MESSAGES.
CRM_SIZE = 'CRM must have 5 characters.'
CRM_STATE_SIZE = 'CRM must have 2 characters.'
CRM_FORMAT = 'CRM must contain only numbers.'
CRM_EXIST = 'CRM already exists'

# UF FIELDS.
UF = "UF"
UF_CHOICE = (
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
)

# NAME FIELDS.
NAME = "Name"
NAME_FIELD_LENGTH = 50
NAME_MIN_LENGTH = 5
NAME_MAX_LENGHT = 50

# NAME VALIDATION MESSAGES
NAME_CHARACTERS = 'Name must not contain special characteres'
NAME_FORMAT = 'Name must contain only letters'
NAME_SIZE = 'Name must be between 5 and 50 characteres'

# EMAIL FIELDS
EMAIL = "E-mail"
EMAIL_FIELD_LENGTH = 50
EMAIL_MIN_LENGTH = 6
EMAIL_MAX_LENGTH = 50

# EMAIL VALIDATION MESSAGES.
EMAIL_FORMAT = "E-mail must be a valid e-mail. Example: example@example.com"
EMAIL_SIZE = "E-mail must be between 5 and 50 characters"
EMAIL_EXISTS = "E-mail already exists"
EMAIL_NONE = "Must have an E-mail"

# EMAIL MESSAGES
EMAIL_SUBJECT = 'Recuperação de sua senha'
EMAIL_BODY = 'Clique no link a seguir para recuperar sua senha http://0.0.0.0:8000/user/reset_confirm/%s.'
EMAIL_ADRESS = 'medicalprescriptionapp@gmail.com'
EMAIL_SUCESS_MESSAGE = 'Verifique a caixa de entrada do seu email para recuperar sua senha.'
EMAIL_MESSAGE_EXIST = 'Um email de recuperação de senha já foi enviado para este endereço!'

# DATE_OF_BIRTH FIELDS.
DATE_OF_BIRTH = "Date of birth"
DATE_OF_BIRTH_MIN = 18
DATE_OF_BIRTH_MIN_PATIENT = 0

# DATE_OF_BIRTH VALIDATION MESSAGES.
DATE_OF_BIRTH_FORMAT = "Date of birth must be in format: dd/mm/yyyy"
DATE_OF_BIRTH_MIN_ERROR = "User must be 18 years"
DATE_OF_BIRTH_MIN_PATIENT_ERROR = "User cannot be born in the future"
# PHONE_NUMBER FIELDS.
PHONE_NUMBER = "Phone number"
PHONE_NUMBER_FIELD_LENGTH_MAX = 11
PHONE_NUMBER_FIELD_LENGTH_MIN = 10

# PHONE_NUMBER VALIDATION MESSAGES.
PHONE_NUMBER_SIZE = 'Phone number must be between 10 and 11 characters'
PHONE_NUMBER_FORMAT = 'Phone number must contain only numbers'

# SEX FIELDS.
SEX = 'Sex'
SEX_M = 'M'
SEX_F = 'F'

SEX_CHOICE = ((SEX_M, 'M'), (SEX_F, 'F'))

# SEX VALIDATION MESSAGES.
SEX_VALUE = "Sex must be M for male F for female"

# PASSWORD and PASSWORD CONFIRMATION FIELDS.
PASSWORD = 'Password'
PASSWORD_CONFIRMATION = 'Confirm password'
PASSWORD_FIELD_LENGTH = 12
PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 12

# PASSWORD VALIDATION MESSAGES.
PASSWORD_SIZE = 'Password must be between 6 and 12 characters.'
PASSWORD_MATCH = 'Passwords do not match'
PASSWORD_ERROR_ALNUM = 'Characteres must be alphanumeric'
PASSWORD_FORMAT = 'Password must contain only alphanumeric characteres'

# ID DOCUMENT FIELD.
ID_DOCUMENT = 'Id Document'
ID_DOCUMENT_LENGTH = 32
ID_DOCUMENT_MIN_LENGTH = 2
ID_DOCUMENT_MAX_LENGTH = 32

# ID DOCUMENT FIELD VALIDATION MESSAGES.
ID_DOCUMENT_SIZE = 'Your id document must be between 10 and 32 characteres'
ID_DOCUMENT_FORMAT = 'Id document must be only numbers'

# LEVEL LOGGER
DEFAULT_LOGGER = 'default'
