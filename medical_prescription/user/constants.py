"""This is a constant file."""
# NAME FIELDS.
NAME = 'Name'
NAME_FIELD_LENGTH = 55
NAME_MIN_LENGTH = 5
NAME_MAX_LENGHT = 50

# NAME VALIDATION MESSAGES
NAME_CHARACTERS = 'Your name can\'t have special characters'
NAME_FORMAT = 'Your name must have just letters'
NAME_SIZE = 'Name must be between 5 and 50 characteres'

# DATE OF BIRTH FIELDS.
DATE_OF_BIRTH = 'Birth Date'
# DATE OF BIRTH VALIDATION MESSAGES.
DATE_OF_BIRTH_FORMAT = 'Invalid birth date'

# ID DOCUMENT FIELD.
ID_DOCUMENT = 'Id Document'
ID_DOCUMENT_LENGTH = 32
ID_DOCUMENT_MIN_LENGTH = 10
ID_DOCUMENT_MAX_LENGTH = 32

# ID DOCUMENT FIELD VALIDATION MESSAGES.
ID_DOCUMENT_SIZE = 'You id document must be between 10 and 32 characteres'

# PHONE NUMBER FIELDS.
PHONE_NUMBER = 'Phone Number'
PHONE_NUMBER_LENGTH = 11
PHONE_NUMBER_MIN_LENGTH = 10
PHONE_NUMBER_MAX_LENGTH = 11

# PHONE NUMBER VALIDATION MESSAGES.
PHONE_NUMBER_SIZE = 'Your phone number must be between 10 and 11 numbers'
PHONE_NUMBER_FORMAT = 'Your phone number must have just numbers'

# PASSWORDS FIELDS.
PASSWORD = 'Password'
PASSWORD_FIELD_LENGTH = 30
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 12

# PASSWORD VALIDATION MESSAGES.
PASSWORD_SIZE = 'Password must be between 8 and 12 characters'
PASSWORD_NOT_EQUAL = 'Passwords do not match.'

# SEX FIELDS.
SEX = 'Sex'

# SEX VALIDATION MESSAGES.


"""
-RN01	Nome	String (5 a 50 caracteres)	Sim	--
-RN02	Data de Nascimento	Data (10 caracteres)	Sim	dd/mm/yyyy
-RN03	Documento de identificação(CPF, Certidão de nascimento ou RG)
String de até 32 caracteres	Sim	999.000.999-00
-RN04	Número de Telefone	String (até 11 caracteres)	Não	6199999999
-RN05	Senha	String (6 a 12 caracteres alfanuméricos)	Sim	--
-RN06	Confirmação de Senha	String (6 a 12 caracteres alfanuméricos)	Sim	--
-RN07	Sexo	Caixa de seleção	Sim	M ou F
"""
