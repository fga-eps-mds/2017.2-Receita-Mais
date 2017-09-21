#Constants file

# CRM FIELDS
CRM = 'CRM'
CRM_LENGTH = 5

# CRM MESSAGES VALIDATION MESSAGES
CRM_SIZE = 'CRM must have 5 characteres.'
CRM_FORMAT = 'CRM must contain /only numbers.'

# UF FIELDS
UF = "UF"

# NAME FIELDS
NAME = "Name"
NAME_FIELD_LENGTH = 50
NAME_MIN_LENGTH = 5
NAME_MAX_LENGHT = 50

# NAME VALIDATION MESSAGES
NAME_CHARACTERS = 'Name must not contain special characteres'
NAME_FORMAT = 'Name must contain o nly letters'
NAME_SIZE = 'Name must be between 5 and 50 characteres'

# EMAIL FIELDS
EMAIL = "E-mail"
EMAIL_FIELD_LENGTH = 50
EMAIL_MIN_LENGTH = 5
EMAIL_MAX_LENGTH = 50

# EMAIL VALIDATION MESSAGES
EMAIL_FORMAT = 'E-mail must be a valid e-mail. Example: example@example.com'
EMAIL_SIZE = 'E-mail must be between 5 and 50 characteres'

# DATE_OF_BIRTH FIELDS
DATE_OF_BIRTH = "Date of birth"

# DATE_OF_BIRTH VALIDATION MESSAGES
DATE_OF_BIRTH_FORMAT = "Date of birth must be in format: dd/mm/yyyy"

# PHONE_NUMBER FIELDS
PHONE_NUMBER = "Phone number"
PHONE_NUMBER_FIELD_LENGTH = 11

# PHONE_NUMBER VALIDATION MESSAGES
PHONE_NUMBER_SIZE = 'Phone number must contain a maximum of 11 characteres'
PHONE_NUMBER_FORMAT = 'Phone number must contain only numbers'

# SEX FIELDS
SEX = 'Sex'

# SEX VALIDATION MESSAGES
SEX_VALUE = "Sex must be M for male F for female"

# PASSWORD and PASSWORD CONFIRMATION FIELDS
PASSWORD = 'Password'
PASSWORD_CONFIRMATION = 'Confirm password'
PASSWORD_FIELD_LENGTH = 12
PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 12

# PASSWORD VALIDATION MESSAGES
PASSWORD_SIZE = 'Password must be between 6 and 12 characteres.'
PASSWORD_MATCH = 'Passwords do not match'
