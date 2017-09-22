# Constants file

# CRM FIELDS
CRM = 'CRM'
CRM_LENGTH = 5
CRM_STATE_LENGTH = 2

# CRM MESSAGES VALIDATION MESSAGES
CRM_SIZE_ERROR = 'CRM must have 5 characters.'
CRM_STATE_SIZE_ERROR = 'CRM must have 2 characters.'
CRM_FORMAT_ERROR = 'CRM must contain /only numbers.'
CRM_EXIST_ERROR = 'CRM already exists'

# UF FIELDS
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

# NAME FIELDS
NAME = "Name"
NAME_FIELD_LENGTH = 50
NAME_MIN_LENGTH = 5
NAME_MAX_LENGHT = 50

# NAME VALIDATION MESSAGES
NAME_CHARACTERS_ERROR = 'Name must not contain special characters'
NAME_FORMAT_ERROR = 'Name must contain only letters'
NAME_SIZE_ERROR = 'Name must be between 5 and 50 characters'

# EMAIL FIELDS
EMAIL = "E-mail"
EMAIL_FIELD_LENGTH = 50
EMAIL_MIN_LENGTH = 5
EMAIL_MAX_LENGTH = 50

# EMAIL VALIDATION MESSAGES
EMAIL_FORMAT_ERROR = "E-mail must be a valid e-mail. Example: example@example.com"
EMAIL_SIZE_ERROR = "E-mail must be between 5 and 50 characters"
EMAIL_EXISTS_ERROR = "Email already exists"

# DATE_OF_BIRTH FIELDS
DATE_OF_BIRTH = "Date of birth"
DATE_OF_BIRTH_MIN = 18

# DATE_OF_BIRTH VALIDATION MESSAGES
DATE_OF_BIRTH_FORMAT_ERROR = "Date of birth must be in format: dd/mm/yyyy"
DATE_OF_BIRTH_MIN_ERROR = "User must be 18 years"

# PHONE_NUMBER FIELDS
PHONE_NUMBER = "Phone number"
PHONE_NUMBER_FIELD_LENGTH = 11

# PHONE_NUMBER VALIDATION MESSAGES
PHONE_NUMBER_SIZE_ERROR = 'Phone number must contain a maximum of 11 characters'
PHONE_NUMBER_FORMAT_ERROR = 'Phone number must contain only numbers'

# SEX FIELDS
SEX = 'Sex'
SEX_M = 'M'
SEX_F = 'F'

SEX_CHOICE = ((SEX_M, 'Masculino'), (SEX_F, 'Feminino'))

# SEX VALIDATION MESSAGES
SEX_VALUE_ERROR = "Sex must be M for male F for female"

# PASSWORD and PASSWORD CONFIRMATION FIELDS
PASSWORD = 'Password'
PASSWORD_CONFIRMATION = 'Confirm password'
PASSWORD_FIELD_LENGTH = 12
PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 12

# PASSWORD VALIDATION MESSAGES
PASSWORD_SIZE_ERROR = 'Password must be between 6 and 12 characters.'
PASSWORD_MATCH_ERROR = 'Passwords do not match'
