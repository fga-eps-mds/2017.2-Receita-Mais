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

# Pacient invalid constants
PATIENT_INVALID = "This field is required."

# Empty constants
EMPTY = 0
