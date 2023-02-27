"""
=======================================================================================================================
.DESCRIPTION
    Import AD search to ORACLE Cache AD
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version


.NOTES

.COMMENTS
    Copy AD to ORACLE
    ------------------------------------------------------------------------------------------------
    AD(OU=IAM,OU=Users,OU=OSIRIS,DC=chu-brugmann,DC=be)		ORACLE (RFI_CACHE_AD_OSIRIS)
    ------------------------------------------------------------------------------------------------
    sAMAccountName										SAMACCOUNTNAME
    sn 													SN
    givenName 											GIVENNAME
    company												COMPANY
    physicalDeliveryOfficeName							PHYSICALDELIVERYOFFICENAME
    BusinessCategory									BUSINESSCATEGORY
    employeeType										EMPLOYEETYPE
    department											DEPARTMENT
    preferredLanguage									PREFERREDLANGUAGE
    employeeNumber										EMPLOYEENUMBER
    extensionAttribute1									EXTENSIONATTRIBUTE1
    extensionAttribute2									EXTENSIONATTRIBUTE2
    telephoneNumber										TELEPHONENUMBER
    pager												PAGER
    description 										DESCRIPTION
    accountExpires										ACCOUNTEXPIRES
    enabled												ENABLED
    name												NAME
    cn 													CN
    userPrincipalName									USERPRINCIPALNAME
    displayName 										DISPLAYNAME
    employeeID											EMPLOYEEID
    info												INFO
    extensionAttribute3									EXTENSIONATTRIBUTE3
    homeDirectory										HOMEDIRECTORY
    homeDrive											HOMEDRIVE
    distinguishedName 									DISTINGUISHEDNAME
    config.LDAP.SEARCHBASE								NETWORKDOMAINID 				Generated
    objectGUID											OBJECTGUID
    objectSid											OBJECTSID
    whenCreated											WHENCREATED
    whenchanged											WHENCHANGED
    LastLogonTimeStamp									LASTLOGONTIMESTAMP
    LastLogon											LASTLOGON
    pwdLastSet											PWDLASTSET
    badPasswordTime										BADPASSWORDTIME
    userAccountControl									USERACCOUNTCONTROL
    mail												MAIL
    msExchWhenMailboxCreated							MSEXCHWHENMAILBOXCREATED
    RFIdateSync											RFIDATESYNC						Generated
    ------------------------------------------------------------------------------------------------
=======================================================================================================================
"""
# =========================================
# Import modules
import os
import sys
import datetime
import logging

from ldap import exec_ldap_search_paged
from database_tools import OracleConnexion


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
    users = exec_ldap_search_paged('OSIRIS-PROD', query)
    return users


def Get_REFID_IOP_CACHE_AD():
    sql_query = "select * from SA.REFID_IOP_CACHE_AD_OSIRIS"
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

    # logging.info(f"iDate:{iDate} > oDate:{oDate}")

    return oDate

def Convert_Date_AccountExpires(iDate):
    # iDate = "12/15/1988 00:00:00"
    # iDate = 1601-01-01 9999-12-31
    if (str(iDate)[0:4] == '1601') or (str(iDate)[0:4] == '9999'):
        oDate = ''
    else:
        oDate = str(iDate)[0:10]

    # logging.info(f"iDate:{iDate} > oDate:{oDate}")

    return oDate

def Convert_Date_AD(iDate):
    # iDate = "12/15/1988 00:00:00"
    # iDate = 1601-01-01 9999-12-31
    iDate = str(iDate).replace("[]", "")

    if (str(iDate)[0:4] == '1601') or (str(iDate)[0:4] == '9999'):
        oDate = ''
    else:
        oDate = str(iDate)[0:19]

    # logging.info(f"iDate:{iDate} > oDate:{oDate}")

    return oDate

# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

# os.system("python create_REFID_IOP_CACHE_AD_OSIRIS.py")

logging.info(f"Synchronize Oracle Table (SA.REFID_IOP_CACHE_AD) with AD")

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

        user = {}
        user['SAMACCOUNTNAME'] = str(data['attributes']['sAMAccountName'])
        user['SN'] = str(data['attributes']['sn']).replace("'", "")
        user['GIVENNAME'] = str(data['attributes']['givenName']).replace("'", "")
        user['COMPANY'] = str(data['attributes']['company'])
        user['PHYSICALDELIVERYOFFICENAME'] = str(data['attributes']['physicalDeliveryOfficeName'])
        user['BUSINESSCATEGORY'] = data['attributes']['BusinessCategory'][0]
        user['EMPLOYEETYPE'] = str(data['attributes']['employeeType']).replace("[]", "")
        user['DEPARTMENT'] = str(data['attributes']['department']).replace("[]", "")
        user['PREFERREDLANGUAGE'] = str(data['attributes']['preferredLanguage']).replace("[]", "")
        user['EMPLOYEENUMBER'] = str(data['attributes']['employeeNumber']).replace("[]", "")
        user['EXTENSIONATTRIBUTE1'] = str(data['attributes']['extensionAttribute1']).replace("[]", "")
        user['EXTENSIONATTRIBUTE2'] = str(data['attributes']['extensionAttribute2']).replace("[]", "")
        user['EXTENSIONATTRIBUTE10'] = str(data['attributes']['extensionAttribute10']).replace("[]", "")
        user['EXTENSIONATTRIBUTE11'] = str(data['attributes']['extensionAttribute11']).replace("[]", "")
        user['TELEPHONENUMBER'] = str(data['attributes']['telephoneNumber']).replace("[]", "")
        user['PAGER'] = str(data['attributes']['pager']).replace("[]", "")
        user['DESCRIPTION'] = str(data['attributes']['description']).replace("[]", "").replace("[", "").replace("]", "").replace("'", "")

        user['ACCOUNTEXPIRES'] = Convert_Date_AccountExpires(data['attributes']['accountExpires'])

        if str(data['attributes']['userAccountControl']) == '512':
            user['ENABLED'] = '1'
        elif str(data['attributes']['userAccountControl']) == '514':
            user['ENABLED'] = '0'
        else:
            user['ENABLED'] = '1'

        user['NAME'] = str(data['attributes']['name']).replace("'", "")
        user['CN'] = str(data['attributes']['cn']).replace("'", "")
        user['USERPRINCIPALNAME'] = str(data['attributes']['userPrincipalName']).replace("'", "")
        user['DISPLAYNAME'] = str(data['attributes']['displayName']).replace("'", "")
        user['EMPLOYEEID'] = str(data['attributes']['employeeID']).replace("[]", "")
        user['INFO'] = str(data['attributes']['info']).replace("[]", "")
        user['EXTENSIONATTRIBUTE15'] = str(data['attributes']['extensionAttribute15']).replace("[]", "")
        user['EXTENSIONATTRIBUTE3'] = str(data['attributes']['extensionAttribute3']).replace("[]", "")
        user['HOMEDIRECTORY'] = str(data['attributes']['homeDirectory']).replace("[]", "")
        user['HOMEDRIVE'] = str(data['attributes']['homeDrive']).replace("[]", "")
        user['DISTINGUISHEDNAME'] = str(data['attributes']['distinguishedName']).replace("'", "")
        user['NETWORKDOMAINID'] = LDAP_SEARCHBASE
        user['OBJECTGUID'] = str(data['attributes']['objectGUID']).replace("[]", "")
        user['OBJECTSID'] = str(data['attributes']['objectSid']).replace("[]", "")
        user['WHENCREATED'] = str(data['attributes']['whenCreated'])[0:19]
        user['WHENCHANGED'] = str(data['attributes']['whenchanged'])[0:19]
        user['LASTLOGONTIMESTAMP'] = Convert_Date_AD(data['attributes']['LastLogonTimeStamp'])
        user['LASTLOGON'] = Convert_Date_AD(data['attributes']['LastLogon'])
        user['PWDLASTSET'] = Convert_Date_AD(data['attributes']['pwdLastSet'])
        user['BADPASSWORDTIME'] = Convert_Date_AD(data['attributes']['badPasswordTime'])
        user['USERACCOUNTCONTROL'] = str(data['attributes']['userAccountControl']).replace("[]", "")
        user['MAIL'] = str(data['attributes']['mail']).replace("'", "").replace("[]", "")
        user['MSEXCHWHENMAILBOXCREATED'] = str(data['attributes']['msExchWhenMailboxCreated'])[0:19].replace("[]", "")
        user['RFIDATESYNC'] = now_start.strftime("%Y-%m-%d %H:%M:%S")

        sql_query = f"""
        INSERT INTO SA.REFID_IOP_CACHE_AD_OSIRIS (
            SAMACCOUNTNAME,
            SN,
            GIVENNAME,
            COMPANY,
            PHYSICALDELIVERYOFFICENAME,
            BUSINESSCATEGORY,
            EMPLOYEETYPE,
            DEPARTMENT,
            PREFERREDLANGUAGE,
            EMPLOYEENUMBER,
            EXTENSIONATTRIBUTE1,
            EXTENSIONATTRIBUTE2,
            EXTENSIONATTRIBUTE10,
            EXTENSIONATTRIBUTE11,
            TELEPHONENUMBER,
            PAGER,
            DESCRIPTION,
            ACCOUNTEXPIRES,
            ENABLED,
            NAME,
            CN,
            USERPRINCIPALNAME,
            DISPLAYNAME,
            EMPLOYEEID,
            INFO,
            EXTENSIONATTRIBUTE15,
            EXTENSIONATTRIBUTE3,
            HOMEDIRECTORY,
            HOMEDRIVE,
            DISTINGUISHEDNAME,
            NETWORKDOMAINID,
            OBJECTGUID,
            OBJECTSID,
            WHENCREATED,
            WHENCHANGED,
            LASTLOGONTIMESTAMP,
            LASTLOGON,
            PWDLASTSET,
            BADPASSWORDTIME,
            USERACCOUNTCONTROL,
            MAIL,
            MSEXCHWHENMAILBOXCREATED,
            RFIDATESYNC
            )
        VALUES (
            '{user['SAMACCOUNTNAME']}',
            '{user['SN']}',
            '{user['GIVENNAME']}',
            '{user['COMPANY']}',
            '{user['PHYSICALDELIVERYOFFICENAME']}',
            '{user['BUSINESSCATEGORY']}',
            '{user['EMPLOYEETYPE']}',
            '{user['DEPARTMENT']}',
            '{user['PREFERREDLANGUAGE']}',
            '{user['EMPLOYEENUMBER']}',
            '{user['EXTENSIONATTRIBUTE1']}',
            '{user['EXTENSIONATTRIBUTE2']}',
            '{user['EXTENSIONATTRIBUTE10']}',
            '{user['EXTENSIONATTRIBUTE11']}',
            '{user['TELEPHONENUMBER']}',
            '{user['PAGER']}',
            '{user['DESCRIPTION']}',
            '{user['ACCOUNTEXPIRES']}',
            '{user['ENABLED']}',
            '{user['NAME']}',
            '{user['CN']}',
            '{user['USERPRINCIPALNAME']}',
            '{user['DISPLAYNAME']}',
            '{user['EMPLOYEEID']}',
            '{user['INFO']}',
            '{user['EXTENSIONATTRIBUTE15']}',
            '{user['EXTENSIONATTRIBUTE3']}',
            '{user['HOMEDIRECTORY']}',
            '{user['HOMEDRIVE']}',
            '{user['DISTINGUISHEDNAME']}',
            '{user['NETWORKDOMAINID']}',
            '{user['OBJECTGUID']}',
            '{user['OBJECTSID']}',
            '{user['WHENCREATED']}',
            '{user['WHENCHANGED']}',
            '{user['LASTLOGONTIMESTAMP']}',
            '{user['LASTLOGON']}',
            '{user['PWDLASTSET']}',
            '{user['BADPASSWORDTIME']}',
            '{user['USERACCOUNTCONTROL']}',
            '{user['MAIL']}',
            '{user['MSEXCHWHENMAILBOXCREATED']}',
            '{user['RFIDATESYNC']}'
        )
        """

        dataset = oracle_IT.exec_ddl_sql(sql_query)

    logging.info(f"{i} on {total_entries} records inserted")
except Exception as e:
    logging.info(user)
    logging.info(sql_query)
    logging.info("An internal error occurred {}".format(e))

try:
    logging.info(f"Get_REFID_IOP_CACHE_AD")
    dataset = Get_REFID_IOP_CACHE_AD()
    logging.info(f"{len(dataset)} rows")
except Exception as e:
    logging.info(f"message: An internal error occurred : {e}")
    exit(0)

# Stop Script

now_stop = datetime.datetime.now()
logging.info(f"Stop at : {now_stop.strftime('%Y-%m-%d %H:%M:%S')} ")

delta = now_stop - now_start
logging.info(f"Delta time : {delta}")


# =========================================
# End of Script

logging.info(f"<== End of Script ==>")
