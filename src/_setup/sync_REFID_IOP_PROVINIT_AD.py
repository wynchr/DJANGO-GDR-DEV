"""
=======================================================================================================================
.DESCRIPTION
    Import AD search to ORACLE PROVINIT_AD
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version


.NOTES

.COMMENTS
    Copy AD to ORACLE
    ------------------------------------------------------------------------------------------------
    AD(OU=IAM,OU=Users,OU=OSIRIS,DC=chu-brugmann,DC=be)		ORACLE (REFID_IOP_PROVINIT_AD)
    ------------------------------------------------------------------------------------------------

    sAMAccountName				SAMACCOUNTNAME
    sn							SN
    givenName					GIVENNAME
    ''							PASSWORD
    company						COMPANY
    physicalDeliveryOfficeName	PHYSICALDELIVERYOFFICENAME
    BusinessCategory			BUSINESSCATEGORY
    employeeType				EMPLOYEETYPE
    department					DEPARTMENT
    preferredLanguage			PREFERREDLANGUAGE
    employeeNumber				EMPLOYEENUMBER
    extensionAttribute1			EXTENSIONATTRIBUTE1
    extensionAttribute2			EXTENSIONATTRIBUTE2
    extensionAttribute11 		EXTENSIONATTRIBUTE11
    telephoneNumber				TELEPHONENUMBER
    pager						PAGER
    ''							ROLES
    ''							UNITES
    ''							SPECIALITES
    homeDirectory				HOMEDIR
    homeDrive					HOMEDRIVE
    description					DESCRIPTION
    info						INFO
    accountExpires				ACCOUNTEXPIRES
    ?							CHANGEPASSWORDATLOGON
    enabled						ENABLED
    ?							ENABLEMAIL
    mail						MAIL
    -							GROUPS
    -							DISTRIBUTIONLIST
    -							ENV
    -							ORG
    'SYS'						USERCRE
    whenCreated					DATECRE
    'SYS'						USERUPD
    whenchanged					DATEUPD
    ''							MSGREFID
    ''							ACTIONTYPE
    ''							MSGDB
    ''							MSGAD
    whenchanged					DATESYNCAD
    '1'							FLAGSYNCAD
    ''							MSGEXCHANGE
    msExchWhenMailboxCreated	DATESYNCEXCHANGE
    '1'							FLAGSYNCEXCHANGE
    objectSid					OBJECTSID
    objectGUID					OBJECTGUID


    ------------------------------------------------------------------------------------------------
=======================================================================================================================
"""
# =========================================
# Import modules
import os
import sys
import datetime
import logging
from database_tools import OracleConnexion
import ldap

# =========================================
# Init Logging

# check if argument is passed
if len(sys.argv) > 1:
    # the first argument is the script name, so we start from the second argument
    filename = sys.argv[1]
    # print("filename:", filename)
else:
    # print("No arguments passed - Create a new filename")
    folder_path = f"../_log/{datetime.datetime.now().strftime('%Y-%m-%d')}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filename = f"{folder_path}/refid_sync_{datetime.datetime.now().strftime('%H%M%S')}.log"

logging.basicConfig(level=logging.DEBUG,
                    format='%(process)d:%(name)s ; %(asctime)s ; %(levelname)s ; %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=filename,
                    filemode='a'
                    )

# =========================================
# Init Global Variables

logging.info(f'==> script[{os.path.basename(__file__)}]')
print(f'==> script[{os.path.basename(__file__)}]')

DBIT = "DB-IT"
oracle_IT = OracleConnexion(DBIT)

ldapdb = 'OSIRIS-PROD'
if ldapdb == 'OSIRIS-TEST':
    LDAP_SEARCHBASE = 'OU=REFID,OU=Users,OU=TESTOSIRIS,DC=chu-brugmann,DC=be'

if ldapdb == 'OSIRIS-PROD':
    LDAP_SEARCHBASE = 'OU=IAM,OU=Users,OU=OSIRIS,DC=chu-brugmann,DC=be'


# =========================================
# Functions / Classes


def Get_AD_Entries():
    # query = "(&(employeeID=*)(businessCategory=*)(department=Informatique))"
    query = "(&(employeeID=*)(businessCategory=*))"
    logging.info(f"ldap_query: {query}")
    users = ldap.exec_ldap_search_paged('OSIRIS-PROD', query)
    return users


def Get_REFID_IOP_PROVINIT_AD():
    sql_query = "select * from SA.REFID_IOP_PROVINIT_AD"
    dataset = oracle_IT.fetch_data_from_db(sql_query)
    return dataset


def Convert_Date(iDate):
    # iDate = "12/15/1988 00:00:00"
    # iDate = $null

    if len(str(iDate)) >= 1:
        iDateM = iDate[0:2]
        iDateD = iDate[3:4]
        iDateY = iDate[6:10]
        # oDate = f"{iDateY}-{iDateM}-{iDateD} 00:00:00"
        oDate = f"{iDateY}-{iDateM}-{iDateD} 00:00:00"
    else:
        oDate = ''

    logging.info(f"iDate:{iDate} > oDate:{oDate}")

    return oDate


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

# os.system("python create_REFID_IOP_PROVINIT_AD.py")

logging.info(f"Synchronize Oracle Table (SA.REFID_IOP_PROVINIT_AD) with AD")

try:
    logging.info(f"Get_AD_Entries")
    users = Get_AD_Entries()
    total_entries = len(users)

    logging.info(f"Please wait a few times to load all the data ({total_entries} rows to insert) ...")

    i = 0
    for data in users:
        i += 1
        if i in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]:
            logging.info(f"i={str(i)}")
            # print(f"i={str(i)}")

        user = {}
        user['SAMACCOUNTNAME'] = str(data['attributes']['sAMAccountName'])

        user['SN'] = str(data['attributes']['sn']).replace("'", "").replace("[]", "")
        user['GIVENNAME'] = str(data['attributes']['givenName']).replace("'", "").replace("[]", "")
        user['USUALSN'] = str(data['attributes']['sn']).replace("'", "").replace("[]", "")
        user['USUALGIVENNAME'] = str(data['attributes']['givenName']).replace("'", "").replace("[]", "")

        user['PASSWORD'] = '***********'

        user['COMPANY'] = str(data['attributes']['company'])
        user['PHYSICALDELIVERYOFFICENAME'] = str(data['attributes']['physicalDeliveryOfficeName'])
        user['DEPARTMENT'] = str(data['attributes']['department']).replace("[]", "")

        user['BUSINESSCATEGORY'] = data['attributes']['BusinessCategory'][0]
        user['EMPLOYEETYPE'] = str(data['attributes']['employeeType']).replace("[]", "")

        user['PREFERREDLANGUAGE'] = str(data['attributes']['preferredLanguage']).replace("[]", "")
        user['EMPLOYEENUMBER'] = str(data['attributes']['employeeNumber']).replace("[]", "")
        user['EXTENSIONATTRIBUTE1'] = str(data['attributes']['extensionAttribute1']).replace("[]", "")
        user['EXTENSIONATTRIBUTE2'] = str(data['attributes']['extensionAttribute2']).replace("[]", "")
        user['EXTENSIONATTRIBUTE11'] = str(data['attributes']['extensionAttribute11']).replace("[]", "")

        user['TELEPHONENUMBER'] = str(data['attributes']['telephoneNumber']).replace("[]", "")
        user['PAGER'] = str(data['attributes']['pager']).replace("[]", "")

        user['HOMEDIRECTORY'] = str(data['attributes']['homeDirectory']).replace("[]", "")
        user['HOMEDRIVE'] = str(data['attributes']['homeDrive']).replace("[]", "")

        user['DESCRIPTION'] = str(data['attributes']['description']).replace("[]", "").replace("[", "").replace("]",
                                                                                                                "").replace(
            "'", "")
        user['INFO'] = str(data['attributes']['info']).replace("[]", "")
        user['EXTENSIONATTRIBUTE15'] = 'REFID-User'

        # user['ACCOUNTEXPIRES'] = str(data['attributes']['accountExpires'])[0:10]
        if str(data['attributes']['accountExpires'])[0:10] == '1601-01-01':
            user['ACCOUNTEXPIRES'] = ''
        elif str(data['attributes']['accountExpires'])[0:10] == '9999-12-31':
            user['ACCOUNTEXPIRES'] = ''
        else:
            user['ACCOUNTEXPIRES'] = str(data['attributes']['accountExpires'])[0:10]

        user['ENABLEACCOUNTEXPIRES'] = '0'
        user['CHANGEPASSWORDATLOGON'] = '0'

        if str(data['attributes']['userAccountControl']) == '512':
            user['ENABLED'] = '1'
        elif str(data['attributes']['userAccountControl']) == '514':
            user['ENABLED'] = '0'
        else:
            user['ENABLED'] = '1'

        user['MAIL'] = str(data['attributes']['mail']).replace("'", "").replace("[]", "")
        user['ENABLEMAIL'] = '0'

        # Get Groups
        user['GROUPS'] = ''
        user['DISTRIBUTIONLIST'] = ''

        user['GROUPSAD'] = ''
        user['DISTRIBUTIONLISTAD'] = ''

        groups = data['attributes']['memberOf']
        for group in groups:
            # print(group)
            if "OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be" in group:
                grouptype = "Distribution"
                user['DISTRIBUTIONLISTAD'] += ldap.extract_samaccountname(group) + ';'
            elif "OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be" in group:
                grouptype = "Applications"
                user['GROUPSAD'] += ldap.extract_samaccountname(group) + ';'
            elif "OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be" in group:
                grouptype = "Security"
                user['GROUPSAD'] += ldap.extract_samaccountname(group) + ';'
            else:
                grouptype = "Other"
                user['GROUPSAD'] += ldap.extract_samaccountname(group) + ';'

            # Take only 4000 bytes !!!
            user['DISTRIBUTIONLISTAD'] = user['DISTRIBUTIONLISTAD'][:4000].replace("'", " ")
            user['GROUPSAD'] = user['GROUPSAD'][:4000].replace("'", " ")

        user['ENV'] = 'PROD'
        user['ORG'] = 'OSIRIS'

        user['SRC'] = 'INIT'

        user['USERCRE'] = 'SYSINIT'
        user['DATECRE'] = str(data['attributes']['whenCreated'])[0:19]
        user['USERUPD'] = 'SYSINIT'
        user['DATEUPD'] = str(data['attributes']['whenchanged'])[0:19]

        user['ACTIONTYPE'] = 'INIT'

        user['MSGAD'] = 'ok'
        user['DATESYNCAD'] = str(data['attributes']['whenchanged'])[0:19]
        user['FLAGSYNCAD'] = '1'

        user['MSGEXCHANGE'] = 'ok'
        user['DATESYNCEXCHANGE'] = str(data['attributes']['msExchWhenMailboxCreated'])[0:19].replace("[]", "")
        user['FLAGSYNCEXCHANGE'] = '1'

        user['OBJECTGUID'] = str(data['attributes']['objectGUID']).replace("[]", "")
        user['OBJECTSID'] = str(data['attributes']['objectSid']).replace("[]", "")

        if str(data['attributes']['pwdLastSet'])[0:19].replace("[]", "") == '':
            user['CHANGEPASSWORDATLOGON'] = '1'
        else:
            user['CHANGEPASSWORDATLOGON'] = '0'

        if user['ACCOUNTEXPIRES'] >= '1601-01-01 01:00:00':
            user['ENABLEACCOUNTEXPIRES'] = '1'
        else:
            user['ENABLEACCOUNTEXPIRES'] = '0'

        if len(str(data['attributes']['msExchWhenMailboxCreated'])[0:19].replace("[]", "")) >= 0:
            user['ENABLEMAIL'] = '1'
        else:
            user['ENABLEMAIL'] = '0'

        user['WHENCREATED'] = str(data['attributes']['whenCreated'])[0:19].replace("[]", "")
        user['WHENCHANGED'] = str(data['attributes']['whenchanged'])[0:19].replace("[]", "")
        user['LASTLOGONTIMESTAMP'] = str(data['attributes']['LastLogonTimeStamp'])[0:19].replace("[]", "")
        user['LASTLOGON'] = str(data['attributes']['LastLogon'])[0:19].replace("[]", "")
        user['PWDLASTSET'] = str(data['attributes']['pwdLastSet'])[0:19].replace("[]", "")
        user['BADPASSWORDTIME'] = str(data['attributes']['badPasswordTime'])[0:19].replace("[]", "")
        user['MSEXCHWHENMAILBOXCREATED'] = str(data['attributes']['msExchWhenMailboxCreated'])[0:19].replace("[]", "")

        user['RFIDATESYNC'] = now_start.strftime("%Y-%m-%d %H:%M:%S")
        user['MESSAGES'] = "Create PROVINIT From AD OSIRIS OU=IAM"

        sql_query = f"""
        INSERT INTO SA.REFID_IOP_PROVINIT_AD (
            SAMACCOUNTNAME,
            SN,
            GIVENNAME,
            USUALSN,
            USUALGIVENNAME,
            PASSWORD,
            COMPANY,
            PHYSICALDELIVERYOFFICENAME,
            BUSINESSCATEGORY,
            EMPLOYEETYPE,
            DEPARTMENT,
            PREFERREDLANGUAGE,
            EMPLOYEENUMBER,
            EXTENSIONATTRIBUTE1,
            EXTENSIONATTRIBUTE2,
            EXTENSIONATTRIBUTE11,
            TELEPHONENUMBER,
            PAGER,
            HOMEDIR,
            HOMEDRIVE,
            DESCRIPTION,
            INFO,
            EXTENSIONATTRIBUTE15,
            ENABLEACCOUNTEXPIRES,
            ACCOUNTEXPIRES,
            CHANGEPASSWORDATLOGON,
            ENABLED,
            ENABLEMAIL,
            MAIL, 
            GROUPS,
            DISTRIBUTIONLIST,
            GROUPSAD,
            DISTRIBUTIONLISTAD,            
            ENV,
            ORG,
            USERCRE, 
            DATECRE, 
            USERUPD , 
            DATEUPD, 
            ACTIONTYPE,
            MSGAD, 
            DATESYNCAD,
            FLAGSYNCAD, 
            MSGEXCHANGE, 
            DATESYNCEXCHANGE,
            FLAGSYNCEXCHANGE,
            OBJECTSID,
            OBJECTGUID,
            WHENCREATED,
            WHENCHANGED,
            LASTLOGONTIMESTAMP,
            LASTLOGON,
            PWDLASTSET,
            BADPASSWORDTIME,
            MSEXCHWHENMAILBOXCREATED,
            RFIDATESYNC,
            MESSAGES 
            )
        VALUES (
            '{user['SAMACCOUNTNAME']}',
            '{user['SN']}',
            '{user['GIVENNAME']}',
            '{user['USUALSN']}',
            '{user['USUALGIVENNAME']}',
            '{user['PASSWORD']}',
            '{user['COMPANY']}',
            '{user['PHYSICALDELIVERYOFFICENAME']}',
            '{user['BUSINESSCATEGORY']}',
            '{user['EMPLOYEETYPE']}',
            '{user['DEPARTMENT']}',
            '{user['PREFERREDLANGUAGE']}',
            '{user['EMPLOYEENUMBER']}',
            '{user['EXTENSIONATTRIBUTE1']}',
            '{user['EXTENSIONATTRIBUTE2']}',
            '{user['EXTENSIONATTRIBUTE11']}',
            '{user['TELEPHONENUMBER']}',
            '{user['PAGER']}',
            '{user['HOMEDIRECTORY']}',
            '{user['HOMEDRIVE']}',
            '{user['DESCRIPTION']}',
            '{user['INFO']}',
            '{user['EXTENSIONATTRIBUTE15']}',
            '{user['ENABLEACCOUNTEXPIRES']}',
            '{user['ACCOUNTEXPIRES']}',
            '{user['CHANGEPASSWORDATLOGON']}',
            '{user['ENABLED']}',
            '{user['ENABLEMAIL']}',
            '{user['MAIL']}',
            '{user['GROUPS']}',
            '{user['DISTRIBUTIONLIST']}',
            '{user['GROUPSAD']}',
            '{user['DISTRIBUTIONLISTAD']}',            
            '{user['ENV']}',
            '{user['ORG']}',
            '{user['USERCRE']}',
            '{user['DATECRE']}',
            '{user['USERUPD']}',
            '{user['DATEUPD']}',
            '{user['ACTIONTYPE']}',
            '{user['MSGAD']}',
            '{user['DATESYNCAD']}',
            '{user['FLAGSYNCAD']}',
            '{user['MSGEXCHANGE']}',
            '{user['DATESYNCEXCHANGE']}',
            '{user['FLAGSYNCEXCHANGE']}',
            '{user['OBJECTSID']}',
            '{user['OBJECTGUID']}',
            '{user['WHENCREATED']}',
            '{user['WHENCHANGED']}',
            '{user['LASTLOGONTIMESTAMP']}',
            '{user['LASTLOGON']}',
            '{user['PWDLASTSET']}',
            '{user['BADPASSWORDTIME']}',
            '{user['MSEXCHWHENMAILBOXCREATED']}',
            '{user['RFIDATESYNC']}',
            '{user['MESSAGES']}'
        )
        """

        dataset = oracle_IT.exec_ddl_sql(sql_query)

    logging.info(f"{i} on {total_entries} records inserted")
except Exception as e:
    logging.info(user)
    logging.info(sql_query)
    logging.info("An internal error occurred {}".format(e))

try:
    logging.info(f"Get_REFID_IOP_PROVINIT_AD")
    dataset = Get_REFID_IOP_PROVINIT_AD()
    logging.info(f"{len(dataset)} rows")
except Exception as e:
    logging.info("An internal error occurred {}".format(e))

# Stop Script

now_stop = datetime.datetime.now()
logging.info(f"Stop at : {now_stop.strftime('%Y-%m-%d %H:%M:%S')} ")

delta = now_stop - now_start
logging.info(f"Delta time : {delta}")

# =========================================
# End of Script

logging.info(f"<== End of Script ==>")
