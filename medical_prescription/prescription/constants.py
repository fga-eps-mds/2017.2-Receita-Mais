MAX_LENGTH_POSOLOGY = 250
MAX_LENGTH_DESCRIPTION_AUTOCOMPLETE = 175
MAX_LENGTH_VIA = 30

VIA_CHOICES = (('Via Intravenosa', 'Via Intravenosa'),
               ('Via Intramuscular', 'Via Intramuscular'),
               ('Via Subcutânea', 'Via Subcutânea'),
               ('Via Oral', 'Via Oral'),
               ('Via Sublingual', 'Via Sublingual'),
               ('Via Retal', 'Via Retal'))

QUANTITY_CHOICES = ((0, 'Uso Contínuo'),
                    (1, '1 unidade'),
                    (2, '2 unidades'),
                    (3, '3 unidades'),
                    (4, '4 unidades'),
                    (5, '5 unidades'),
                    (6, '6 unidades'),
                    (7, '7 unidades'),
                    (8, '8 unidades'),
                    (9, '9 unidades'),
                    (10, '10 unidades'),
                    (11, '11 unidades'),
                    (12, '12 unidades'),
                    (13, '13 unidades'),
                    (14, '14 unidades'),
                    (15, '15 unidades'),
                    (16, '16 unidades'),
                    (17, '17 unidades'),
                    (18, '18 unidades'),
                    (19, '19 unidades'),
                    (20, '20 unidades'))
# CID invalid constants
CID_INVALID = "This disease does not exists."

# Exam invalid constants
EXAM_INVALID = "This exams does not exists."

# Patient invalid constants
PATIENT_INVALID = "This field is required."

# Empty constants
EMPTY = 0

# Constants for print prescription
MAX_LENGTH_CLINIC = 50
MAX_LENGTH_HEADER = 150
MAX_LENGTH_FOOTER = 100
MAX_LENGTH_NAME = 50

# Print prescription errors message
LENGTH_CLINIC = "Clinic must have a maximum of  50 characters."
LENGTH_HEADER = "Header must have a maximum of  150 characters."
LENGTH_FOOTER = "Footer must have a maximum of  100 characters."
LENGTH_NAME = "Name must have a maximum of 50 characters."

# Fonts fields
TIMES_ROMAN = 'Times-Roman'
HELVETICA = 'Helvetica'
ARIAL = 'Arial'
COURIER = 'Courier'

FONT_CHOICE = (('Times-Roman', 'Times-Roman'), ('Helvetica', 'Helvetica'), ('Courier', 'Courier'))

# Fonts size fields
FONT_SIZE_CHOICE = (('9', '9'), ('10', '10'), ('12', '12'), ('14', '14'))

# DEFAULT PATH IMAGE.
DEFAULT_IMG = 'medical_prescription/static/img/user.png'

# Page size fields
PAGE_SIZE_CHOICE = (('letter', 'letter'), ('A4', 'A4'), ('A5', 'A5'))

CONTENT_TYPES = ['jpeg', 'png']
FORMAT_ERROR = 'File type is not supported'
FILE_SIZE = 'Please keep filesize under 20MB'
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = 20971520

EMAIL_MIN_LENGTH = 5
EMAIL_MAX_LENGTH = 50
EMAIL_SIZE = "E-mail must be between 5 and 50 characters"
