"""
=======================================================================================================================
.DESCRIPTION
    Synchronize REFADGROUPS with Oracle Table
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version


.NOTES

.COMMENTS
    Copy AD to ORACLE
    ------------------------------------------------------------------------------------------------
                    attributes = [
                        'SamAccountName',
                        'DistinguishedName',
                        'mail',
                        'whenCreated',
                        'whenChanged',
                        'description',
                        'info',
                        'extensionAttribute15',
                        'ObjectGUID',
                        'ObjectSID',]
     ------------------------------------------------------------------------------------------------   
        if grouptype == "PROD-DISTRIBUTION":
            LDAP_SEARCHBASE = 'OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be'
            filter = "(&(objectClass=group)(info=IAM-DistributionGroup))"
        elif grouptype == "PROD-APPLICATION":
            LDAP_SEARCHBASE = 'OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be'
            filter = "(&(objectClass=group)(info=IAM-Application))"
        if grouptype == "DEV-DISTRIBUTION":
            LDAP_SEARCHBASE = 'OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be'
            filter = "(&(objectClass=group)(extensionAttribute15=REFID-DistributionGroup))"
        elif grouptype == "DEV-APPLICATION":
            LDAP_SEARCHBASE = 'OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be'
            filter = "(&(objectClass=group)(extensionAttribute15=REFID-Application))"
    ------------------------------------------------------------------------------------------------
=======================================================================================================================
"""
# =========================================
# Import modules
import os
import sys
import datetime
import logging

from ldap import exec_ldap_search_groups
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

# =========================================
# Functions / Classes


def Get_AD_Groups(grouptype):
    logging.info(f"grouptype: {grouptype}")
    groups = exec_ldap_search_groups(grouptype)
    return groups


def Add_Groups_in_DB(groups, grouptype):
    i = 0
    for group in groups['entries']:
        i += 1
        if i in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
            logging.info(f"i={str(i)}")

        groupdb = {}
        groupdb['SAMACCOUNTNAME'] = str(group['attributes']['sAMAccountName']).replace("'", "")
        groupdb['DISTINGUISHEDNAME'] = str(group['attributes']['distinguishedName']).replace("'", "")
        groupdb['MAIL'] = str(group['attributes']['mail']).replace("[]", "").replace("'", "")
        groupdb['WHENCREATED'] = str(group['attributes']['whenCreated'])[0:19].replace("[]", "")
        groupdb['WHENCHANGED'] = str(group['attributes']['whenChanged'])[0:19].replace("[]", "")
        groupdb['DESCRIPTION'] = str(group['attributes']['description']).replace("[]", "").replace("[", "").replace("]", "").replace("'", "")
        groupdb['INFO'] = str(group['attributes']['info']).replace("[]", "").replace("'", "")
        groupdb['EXTENSIONATTRIBUTE15'] = str(group['attributes']['extensionAttribute15']).replace("[]", "")
        groupdb['OBJECTGUID'] = str(group['attributes']['objectGUID'])
        groupdb['OBJECTSID'] = str(group['attributes']['objectSid'])
        if "DISTRIBUTION" in grouptype:
            groupdb['GROUPCATEGORY'] = "Distribution"
        elif "APPLICATION" in grouptype:
            groupdb['GROUPCATEGORY'] = "Security"
        if "PROD" in grouptype:
            groupdb['ENV'] = "PROD"
        elif "DEV" in grouptype:
            groupdb['ENV'] = "DEV"


        sql_query = f"""
            INSERT INTO SA.REFID_IOP_REFADGROUPS (
                    SAMACCOUNTNAME,
                    DISTINGUISHEDNAME,
                    MAIL,
                    GROUPCATEGORY,
                    WHENCREATED,
                    WHENCHANGED,
                    DESCRIPTION,
                    INFO,
                    EXTENSIONATTRIBUTE15,
                    OBJECTGUID,
                    OBJECTSID,
                    ENV
                )
            VALUES (
                    '{groupdb['SAMACCOUNTNAME']}',
                    '{groupdb['DISTINGUISHEDNAME']}',
                    '{groupdb['MAIL']}',
                    '{groupdb['GROUPCATEGORY']}',
                    '{groupdb['WHENCREATED']}',
                    '{groupdb['WHENCHANGED']}',
                    '{groupdb['DESCRIPTION']}',
                    '{groupdb['INFO']}',
                    '{groupdb['EXTENSIONATTRIBUTE15']}',
                    '{groupdb['OBJECTGUID']}',
                    '{groupdb['OBJECTSID']}',
                    '{groupdb['ENV']}'
            )
            """
        # print(sql_query)
        oracle_IT.exec_ddl_sql(sql_query)
        # logging.info(f"{i} on {total_entries} records inserted")
    return i



def Get_REFID_IOP_REFADGROUPS():
    sql_query = "select * from SA.REFID_IOP_REFADGROUPS"
    dataset = oracle_IT.fetch_data_from_db(sql_query)
    return dataset


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

os.system("python create_REFID_IOP_REFADGROUPS.py")

logging.info(f"Synchronize Oracle Table (SA.REFID_IOP_CACHE_AD) with AD")

try:
    logging.info(f"Get_AD_Groups")

    # PROD-DISTRIBUTION
    logging.info(f"Get_AD_Groups PROD-DISTRIBUTION")
    groups = Get_AD_Groups("PROD-DISTRIBUTION")
    result = Add_Groups_in_DB(groups, "PROD-DISTRIBUTION")
    logging.info(f"{result} records inserted")

    # PROD-APPLICATION
    logging.info(f"Get_AD_Groups PROD-APPLICATION")
    groups = Get_AD_Groups("PROD-APPLICATION")
    result = Add_Groups_in_DB(groups, "PROD-APPLICATION")
    logging.info(f"{result} records inserted")

    # DEV-DISTRIBUTION
    logging.info(f"Get_AD_Groups DEV-DISTRIBUTION")
    groups = Get_AD_Groups("DEV-DISTRIBUTION")
    result = Add_Groups_in_DB(groups, "DEV-DISTRIBUTION")
    logging.info(f"{result} records inserted")

    # DEV-APPLICATION
    logging.info(f"Get_AD_Groups DEV-APPLICATION")
    groups = Get_AD_Groups("DEV-APPLICATION")
    result = Add_Groups_in_DB(groups, "DEV-APPLICATION")
    logging.info(f"{result} records inserted")


except Exception as e:
    logging.info("An internal error occurred {}".format(e))

try:
    logging.info(f"Get_REFID_IOP_REFADGROUPS")
    dataset = Get_REFID_IOP_REFADGROUPS()
    logging.info(f"{len(dataset)} rows")
except:
    logging.info(f"Table do not exist")

# Stop Script

now_stop = datetime.datetime.now()
logging.info(f"Stop at : {now_stop.strftime('%Y-%m-%d %H:%M:%S')} ")

delta = now_stop - now_start
logging.info(f"Delta time : {delta}")


# =========================================
# End of Script

logging.info(f"<== End of Script ==>")
