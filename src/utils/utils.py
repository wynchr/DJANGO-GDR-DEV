"""
=======================================================================================================================
.DESCRIPTION
    Utils Function for Project

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	12/01/2023  CWY	Initial Version

.COMMENTS
    .
=======================================================================================================================
"""

import logging
import random
import array
import base64
import uuid
import re
import time
import unidecode as unidecode
import ldap

WAIT = 2

# Utils Function ---------------------------------------------------------------

# ================================================================================================================
# Function for LOGGING
# ================================================================================================================

def loginit(filename='app.log'):

    if filename:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(process)d:%(name)s ; %(asctime)s ; %(message)s ; %(levelname)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename='app.log',
                            filemode='w'
                            )
    else:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(process)d:%(name)s ; %(asctime)s ; %(message)s ; %(levelname)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            # filename='app.log',
                            # filemode='w'
                            )

    return None


def logmsg(message, typemessage='debug'):

    loginit()

    if typemessage == 'debug':
        logging.debug(message)
    elif typemessage == 'info':
        logging.info('This is an info message')
    elif typemessage == 'warning':
        logging.warning('This is a warning message')
    elif typemessage == 'error':
        logging.error('This is an error message')
    elif typemessage == 'critical':
        logging.critical('This is a critical message')
    else:
        logging.info('This is an info message')

    return None


# ================================================================================================================
# Function for INPUT
# ================================================================================================================


def let_user_pick(title, options):
    print(f"\n*=== {title} ================================*")
    print("Please choose:")

    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))

    i = input("Enter number: ")

    try:
        if 0 < int(i) <= len(options):
            return int(i) - 1
    except:
        pass
    return None

# ================================================================================================================
# Function to convert Dataset to Dict
# ================================================================================================================


def convert_dataset_to_dict(dataset, key):
    dict = {}
    for data in dataset:
        dict[data[key]] = data
    return dict

# ================================================================================================================
# Function to Print Dict
# ================================================================================================================


def print_dict(my_dict):
    for id, info in my_dict.items():
        print("\nKey:", id)
        for key in info:
            print(key + ':', info[key])

# ================================================================================================================
# Function to Generate Fields for Views Valid Forms
# ================================================================================================================


def gen_userid(nom, prenom):

    last_name = unidecode.unidecode(nom.upper().replace("'", "").replace("-", "").lstrip().rstrip())
    first_name = unidecode.unidecode(prenom.upper().replace("'", "").lstrip().rstrip())

    # ***********************************************************************************************
    # ******* last name part creation ***************************************************************

    if last_name.upper()[0:2] == 'VAN':
        if last_name.find(' ') > -1:
            if last_name.count(' ') > 1:
                last_name_login = last_name[:1] + \
                                  last_name[4:5] + \
                                  last_name[last_name.find(' ', 5) + 1:last_name.find(' ', 5) + 5]
            else:
                last_name_login = last_name[:1] + \
                                  last_name[4:9]
        else:
            last_name_login = last_name[:1] + \
                              last_name[3:7]

    elif len(last_name) >= 5:
        if last_name.find(' ') > -1:
            if last_name.count(' ') > 1:
                list_of_space = [i for i, c in enumerate(last_name) if c == " "]
                last_name_login = last_name[:1] + \
                                  last_name[list_of_space[0] + 1:list_of_space[0] + 2] + \
                                  last_name[list_of_space[1] + 1:list_of_space[1] + 3]
            else:
                if last_name.find(' ') > 5:
                    last_name_login = last_name[:5]
                else:
                    last_name_login = last_name[:last_name.find(' ') - 1] + last_name[
                                                                            last_name.find(' ') + 1:last_name.find(
                                                                                ' ') + 1 + (6 - last_name.find(
                                                                                ' '))]
        else:
            last_name_login = last_name[:5]
    else:
        last_name_login = last_name[:len(last_name)]

    # ***********************************************************************************************
    next_car = 0
    last_name_login_size = len(last_name_login)
    first_name_login = ""
    if first_name.find('-') > -1:
        if last_name_login_size == 6:
            last_name_login = last_name_login[:4]
        else:
            first_name_login = first_name[:1] + first_name[first_name.find('-') + 1:first_name.find('-') + 1 + (
                    (7 - last_name_login_size) - 1)]
        sAMAccountName = last_name_login[:len(last_name_login)] + first_name_login
        next_car = first_name.find('-') + 1 + ((7 - last_name_login_size) - 1)
    elif first_name.find(' ') > -1:
        first_name_login = first_name[:1] + first_name[first_name.find(' ') + 1:first_name.find(' ') + 1 + (
                (7 - last_name_login_size) - 1)]
        if last_name_login_size == 6:
            last_name_login = last_name_login[:4]
        sAMAccountName = last_name_login[:len(last_name_login)] + first_name_login
        next_car = first_name.find(' ') + 1 + ((7 - last_name_login_size) - 1)
    else:
        nbrcar = 7 - last_name_login_size
        first_name_login = first_name[:nbrcar]
        sAMAccountName = last_name_login + first_name_login
        next_car = nbrcar

    ldapdb = 'OSIRIS-ALL'
    sAMAccountname_exist = True
    while sAMAccountname_exist:
        user_exists = ldap.search_ldap_exists_userid(ldapdb, sAMAccountName)
        print(f"\nUser {sAMAccountName.upper()} exists : {user_exists}")
        if user_exists:
            next_car += 1
            sAMAccountName = sAMAccountName[:len(sAMAccountName) - 1] + first_name[next_car:next_car + 1]
        else:
            sAMAccountname_exist = False

    return sAMAccountName


def gen_password(psw_string):
    # print("gen_password:" + psw_string )
    return encodeB64(psw_string)


def gen_mail(nom, prenom, hopital):
    if hopital.upper() == "CHU-BRUGMANN":
        extension = "@chu-brugmann.be"
    elif hopital.upper() == "HUDERF":
        extension = "@huderf.be"
    elif hopital.upper() == "BRUSTP":
        extension = "@brustp.be"
    else:
        extension = "@chu-brugmann.be"
    mail = prenom.lower() + "." + nom.lower() + extension
    return mail


def gen_homedir(userid):
    homedir = r"\\chu-brugmann\share\home\{}".format(userid)
    return homedir


def gen_homedrive():
    homedrive = "H:"
    return homedrive


def check_niss(niss):
    """
    Vérifie si un numéro NISS est valide en Belgique.

    :param niss: le numéro NISS à vérifier (sous forme de chaîne de caractères).
    :return: True si le numéro est valide, False sinon.
    """
    if len(niss) != 11:
        return False

    try:
        niss_int = int(niss)
    except ValueError:
        return False

    # Vérification du modulo 97
    if int(niss[:9]) % 97 == int(niss[9:]):
        # print(niss_int % 97)
        return False

    # Vérification du code de sexe
    if niss[6] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        # print(niss[6])
        return False

    return True


# ================================================================================================================
# Function System
# ================================================================================================================


def encodeB64(chaine):
    # Encode String from B64
    psw_string = chaine
    psw_string_bytes = psw_string.encode("utf-8")
    psw_base64_bytes = base64.b64encode(psw_string_bytes)
    psw_base64_string = psw_base64_bytes.decode("utf-8")
    # print(f"psw_base64_string: {psw_base64_string}")
    return psw_base64_string


def decodeB64(chaine):
    # Decode String from B64
    base64_string = chaine
    base64_bytes = base64_string.encode("utf-8")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("utf-8")
    # print(f"Decoded string: {sample_string}")
    return sample_string


def gen_random_password(len):
    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = len

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'j', 'k', 'm', 'n', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'J', 'K', 'M', 'N', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '~',
               '*', '(', ')']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choices(DIGITS)
    rand_upper = random.choices(UPCASE_CHARACTERS)
    rand_lower = random.choices(LOCASE_CHARACTERS)
    rand_symbol = random.choices(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choices(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x

    return password


def gen_unique_reference():
    reference = 'RFI' + str(uuid.uuid4().hex)[:6]
    print(reference)
    return reference


def check_regex(type, test_string):
    if type == 'letters':
        pattern = r'^[a-zA-Z\'\-\s]*$'
    elif type == 'numbersonly':
        pattern = r'^[0-9]*$'
    elif type == 'numbers':
        pattern = r'^[0-9\/\-\.\;]*$'
    elif type == 'mail':
        pattern = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
    elif type == 'company':
        pattern = r'^org/?P<company_name>\w+/$'
    else:
        pattern = r'^[a-zA-Z\'\-\s]*$'

    if re.match(pattern, test_string) is None:
        result = False
    else:
        result = True

    return result

# ================================================================================================================
# Function System
# ================================================================================================================


def create_choices():

    CHOICES = {}

    CHOICES['ENV'] = (
        ("DEV", "DEV"),
        ("PROD", "PROD"),
    )

    CHOICES['ORG'] = (
        ("OSIRIS", "OSIRIS"),
        ("CHUBXL", "CHUBXL"),
    )

    CHOICES['SOURCE'] = (
        ("REFID-User", "REFID-User"),
        ("INTERNEO-User", "INTERNEO-User"),
        ("IAM-User", "IAM-User"),
    )

    CHOICES['FLAG'] = (
        ("0", "FALSE"),
        ("1", "TRUE"),
    )

    CHOICES['STATE'] = (
        ("0", "WAITING TO BE INTEGRATED"),
        ("1", "INTEGRATED"),
        ("2", "ERROR"),
        ("9", "BLOCKED"),
    )

    CHOICES['ACTION'] = (
        ("CREATE", "CREATE"),
        ("UPDATE", "UPDATE"),
        ("ENABLE", "ENABLE"),
        ("DISABLE", "DISABLE"),
        ("RESETPASSWORD", "RESETPASSWORD"),
        ("INIT", "INIT"),
    )

    CHOICES['HOPITAL'] = (
        ("CHU-Brugmann", "CHU-Brugmann"),
        ("Huderf", "Huderf"),
        ("BRUSTP", "BruStp"),
    )

    CHOICES['SITE'] = (
        ("Horta", "Horta"),
        ("Brien", "Brien"),
        ("Astrid", "Astrid"),
    )

    CHOICES['TYPE'] = (
        ("Administratif", "Administratif"),
        ("Medical", "Medical"),
        ("Medical sans INAMI", "Medical sans INAMI"),
        ("Nursing", "Nursing"),
        ("Paramedical", "Paramedical"),
        ("Technique", "Technique"),
        ("Ouvrier", "Ouvrier"),
        ("Other", "Other"),
        ("Unknown", "Unknown"),
    )

    CHOICES['CATEGORIE'] = (
        ("internal", "Internal"),
        ("external", "External"),
        ("interim", "Interim"),
        ("students", "Students"),
        ("pg", "PG"),
        ("at60", "Article60"),
        ("volunteers", "Volunteers"),
    )

    CHOICES['LANGUE'] = (
        ("fr", "fr"),
        ("nl", "nl"),
        ("en", "en"),
        ("de", "de"),
    )

    CHOICES['QUALITY'] = (
        ("Mr", "Monsieur"),
        ("Mme", "Madame"),
        ("Dr", "Docteur"),
        ("Pr", "Professeur"),
    )

    CHOICES['GENDER'] = (
        ("F", "Féminin"),
        ("M", "Masculin"),
    )

    CHOICES['CARDTYPE'] = (
        ("NISS", "N°NISS"),
        ("NISSBIS", "N°NISS bis"),
        ("EID", "N°Carte d'identité"),
        ("PASSPORT", "N°Passport"),
        ("AUTRE", "Autre"),
    )

    CHOICES['SRC'] = (
        ("RH", "RH"),
        ("INTERNEO", "INTERNEO"),
        ("REFID", "REFID"),
        ("INIT", "INIT"),
        ("AUTRE", "Autre"),
    )

    CHOICES['MOUVEMENT'] = (
        ("IN", "IN"),
        ("OUT", "OUT"),
        ("EXT", "EXT"),
        ("NEW", "NEW"),
        ("UKN", "UKN"),
    )

    CHOICES['DEPARTEMENT'] = (
        ("Achats", "Achats"),
        ("Anesthésie", "Anesthésie"),
        ("Cardiologie", "Cardiologie"),
        ("Centrale électrique", "Centrale électrique"),
        ("Chirurgie", "Chirurgie"),
        ("Chirurgie Vasculaire", "Chirurgie Vasculaire"),
        ("Comptabilité", "Comptabilité"),
        ("Consultations", "Consultations"),
        ("Dialyse", "Dialyse"),
        ("Direction Secrétariat", "Direction Secrétariat"),
        ("Direction département infirmier et paramédical", "Direction département infirmier et paramédical"),
        ("Direction financière", "Direction financière"),
        ("Diététique", "Diététique"),
        ("Facturation", "Facturation"),
        ("Gastro", "Gastro"),
        ("HUDE", "HUDE"),
        ("Informatique", "Informatique"),
        ("Labo Sommeil", "Labo Sommeil"),
        ("Laboratoire", "Laboratoire"),
        ("Maintenance", "Maintenance"),
        ("Nourissons", "Nourissons"),
        ("Nursing", "Nursing"),
        ("Néo-Natal", "Néo-Natal"),
        ("Néphrologie", "Néphrologie"),
        ("O.R.L.", "O.R.L."),
        ("Oncologie", "Oncologie"),
        ("Pharmacie", "Pharmacie"),
        ("Pneumologie", "Pneumologie"),
        ("Polyclinique", "Polyclinique"),
        ("Psychiatrie", "Psychiatrie"),
        ("Radiologie", "Radiologie"),
        ("Revalidation Neurologique", "Revalidation Neurologique"),
        ("Rhumatologie", "Rhumatologie"),
        ("Secrétariat Polyclinique", "Secrétariat Polyclinique"),
        ("Secrétariat médical", "Secrétariat médical"),
        ("Service GRH", "Service GRH"),
        ("Stomatologie", "Stomatologie"),
        ("Tarification", "Tarification"),
        ("Trésorerie", "Trésorerie"),
        ("Urgences", "Urgences"),
    )

    CHOICES['SECURITYGROUP'] = (
        ("CN=REFID_Administratif,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
         "REFID_Administratif"),
        ("CN=REFID_Medecin,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "REFID_Medecin"),
        ("CN=REFID_Nursing,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "REFID_Nursing"),
    )

    CHOICES['DISTRIBUTIONLIST'] = (
        (
        "CN=REFID - Distribution List for IT,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
        "REFID - Distribution List for IT"),
        (
        "CN=REFIDT - Test DL,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
        "REFIDT - Test DL"),
    )
    CHOICES['SECURITYGROUPAD'] = (
        ("CN=REFID_Administratif,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
         "REFID_Administratif"),
        ("CN=REFID_Medecin,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "REFID_Medecin"),
        ("CN=REFID_Nursing,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "REFID_Nursing"),
    )

    CHOICES['DISTRIBUTIONLISTAD'] = (
        (
        "CN=REFID - Distribution List for IT,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
        "REFID - Distribution List for IT"),
        (
        "CN=REFIDT - Test DL,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
        "REFIDT - Test DL"),

    )
    return CHOICES


# Main =============================================================================================================
if __name__ == "__main__":

    while True:
        options = ["Test Random Password & conversion in B64",
                   "Test Reverse B64 String",
                   "Test Gen Userid",
                   "Check NISS",
                   "Test Regex",
                   "log_message",
                   "gen_unique_reference",
                   "Exit",
                   ]
        title = "utils"
        res = let_user_pick(title, options)
        if options[res] == "Exit":
            break
        choice = options[res]
        print(choice)

        if choice == "Test Random Password & conversion in B64":
            psw = gen_random_password(12)
            print(f"psw: {psw}")
            pswB64 = encodeB64(psw)
            print(f"pswB64: {pswB64}")
            psw = decodeB64(pswB64)
            print(f"psw {psw}")

        if choice == "Test Reverse B64 String":
            strin = input("Coded String : ")
            if strin == "":
                strin = 'RGNGVSNnMzk/ODoj'
            print(f"input: {strin}")
            strout = decodeB64(strin)
            print(f"output: {strout}")

        if choice == "Test Gen Userid":
            userid = gen_userid("ZZWyns", "Christian")
            print(f"userid: {userid}")

        if choice == "Check NISS":
            niss = "63020346110"
            # niss = "64082901431"
            result = check_niss(niss)
            if result:
                print(f"{niss} : ok")
            else:
                print(f"{niss} : ko")

        if choice == "Test Regex":
            print(f"Christian-Henri is letters:{check_regex('letters', 'Christian-Henri')}")

        if choice == "log_message":
            logmsg("This is a debug message")

        if choice == "gen_unique_reference":
            print(gen_unique_reference())



        time.sleep(WAIT)
