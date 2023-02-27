"""
=======================================================================================================================
.DESCRIPTION
    Create Oracle Table (SA.REFID_IOP_CACHE_AD_OSIRIS)
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version

.COMMENTS
    CREATE TABLE SA.REFID_IOP_CACHE_AD_OSIRIS (
    SAMACCOUNTNAME				VARCHAR2(20),
    SN							VARCHAR2(50),
    GIVENNAME					VARCHAR2(50),
    COMPANY						VARCHAR2(50),
    PHYSICALDELIVERYOFFICENAME	VARCHAR2(50),
    BUSINESSCATEGORY			VARCHAR2(50),
    EMPLOYEETYPE				VARCHAR2(50),
    DEPARTMENT					VARCHAR2(50),
    PREFERREDLANGUAGE			CHAR(5),
    EMPLOYEENUMBER				VARCHAR2(50),
    EXTENSIONATTRIBUTE1			VARCHAR2(50),
    EXTENSIONATTRIBUTE2			VARCHAR2(50),
    TELEPHONENUMBER				VARCHAR2(30),
    PAGER						VARCHAR2(30),
    DESCRIPTION					VARCHAR2(200),
    ACCOUNTEXPIRES				VARCHAR2(25),
    ENABLED						VARCHAR2(5),
    NAME						VARCHAR2(150),
    CN							VARCHAR2(150),
    USERPRINCIPALNAME			VARCHAR2(100),
    DISPLAYNAME					VARCHAR2(150),
    EMPLOYEEID					VARCHAR2(20),
    INFO						VARCHAR2(50),
    EXTENSIONATTRIBUTE15		VARCHAR2(50),
    EXTENSIONATTRIBUTE3			VARCHAR2(50),
    BUSINESSROLES				VARCHAR2(50),
    HOMEDIRECTORY				VARCHAR2(50),
    HOMEDRIVE					CHAR(2),
    DISTINGUISHEDNAME			VARCHAR2(150),
    NETWORKDOMAINID				VARCHAR2(150),
    OBJECTGUID 					VARCHAR2(150),
    OBJECTSID 					VARCHAR2(150),
    WHENCREATED					VARCHAR2(21),
    WHENCHANGED 				VARCHAR2(21),
    LASTLOGONTIMESTAMP 			VARCHAR2(21),
    LASTLOGON 					VARCHAR2(21),
    PWDLASTSET 					VARCHAR2(21),
    BADPASSWORDTIME 			VARCHAR2(21),
    USERACCOUNTCONTROL 			VARCHAR2(50),
    MAIL 						VARCHAR2(150),
    MSEXCHWHENMAILBOXCREATED	VARCHAR2(21),
    RFIDATESYNC 				VARCHAR2(21),
    MESSAGES					VARCHAR2(100),
    CONSTRAINT REFID_IOP_CACHE_AD_OSIRIS_PK PRIMARY KEY (SAMACCOUNTNAME)
    )
=======================================================================================================================
"""
# =========================================
# Import modules
import os
import datetime
import logging
from database_tools import OracleConnexion
import sys


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

DB = "DB-IT"
oracle_IT = OracleConnexion(DB)

# =========================================
# Functions / Classes


def Get_REFID_IOP_CACHE_AD():
    sql_query = "select * from SA.REFID_IOP_CACHE_AD_OSIRIS"
    # dataset = db.exec_sql(DB, sql_query)
    dataset = oracle_IT.fetch_data_from_db(sql_query)
    return dataset


def Drop_REFID_IOP_CACHE_AD():
    sql_query = "DROP TABLE SA.REFID_IOP_CACHE_AD_OSIRIS"
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


def Create_REFID_IOP_CACHE_AD():
    sql_query = f"""
        CREATE TABLE SA.REFID_IOP_CACHE_AD_OSIRIS (
            SAMACCOUNTNAME				VARCHAR2(20),
            SN							VARCHAR2(50),
            GIVENNAME					VARCHAR2(50),
            COMPANY						VARCHAR2(50),
            PHYSICALDELIVERYOFFICENAME	VARCHAR2(50),
            BUSINESSCATEGORY			VARCHAR2(50),
            EMPLOYEETYPE				VARCHAR2(50),
            DEPARTMENT					VARCHAR2(50),
            PREFERREDLANGUAGE			CHAR(5),
            EMPLOYEENUMBER				VARCHAR2(50),
            EXTENSIONATTRIBUTE1			VARCHAR2(50),
            EXTENSIONATTRIBUTE2			VARCHAR2(50),
            EXTENSIONATTRIBUTE10		VARCHAR2(50),
            EXTENSIONATTRIBUTE11		VARCHAR2(50),
            TELEPHONENUMBER				VARCHAR2(30),
            PAGER						VARCHAR2(30),
            DESCRIPTION					VARCHAR2(200),
            ACCOUNTEXPIRES				VARCHAR2(25),
            ENABLED						VARCHAR2(5),
            NAME						VARCHAR2(150),
            CN							VARCHAR2(150),
            USERPRINCIPALNAME			VARCHAR2(100),
            DISPLAYNAME					VARCHAR2(150),
            EMPLOYEEID					VARCHAR2(20),
            INFO						VARCHAR2(50),
            EXTENSIONATTRIBUTE15		VARCHAR2(50),
            EXTENSIONATTRIBUTE3			VARCHAR2(50),
            BUSINESSROLES				VARCHAR2(50),
            HOMEDIRECTORY				VARCHAR2(50),
            HOMEDRIVE					CHAR(2),
            DISTINGUISHEDNAME			VARCHAR2(150),
            NETWORKDOMAINID				VARCHAR2(150),
            OBJECTGUID 					VARCHAR2(150),
            OBJECTSID 					VARCHAR2(150),
            WHENCREATED					VARCHAR2(21),
            WHENCHANGED 				VARCHAR2(21),
            LASTLOGONTIMESTAMP 			VARCHAR2(21),
            LASTLOGON 					VARCHAR2(21),
            PWDLASTSET 					VARCHAR2(21),
            BADPASSWORDTIME 			VARCHAR2(21),
            USERACCOUNTCONTROL 			VARCHAR2(50),
            MAIL 						VARCHAR2(150),
            MSEXCHWHENMAILBOXCREATED	VARCHAR2(21),
            RFIDATESYNC 				VARCHAR2(21),
            MESSAGES					VARCHAR2(100),
            CONSTRAINT REFID_IOP_CACHE_AD_OSIRIS_PK PRIMARY KEY (SAMACCOUNTNAME)
            )
        """

    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

logging.info(f"Create Oracle Table (SA.REFID_IOP_CACHE_AD_OSIRIS) on {DB}")

try:
    logging.info(f"Get_REFID_IOP_CACHE_AD")
    dataset = Get_REFID_IOP_CACHE_AD()
    logging.info(f"{len(dataset)} rows")
except Exception as e:
    logging.info(f"message: An internal error occurred : {e}")


try:
    logging.info(f"Drop_REFID_IOP_CACHE_AD")
    dataset = Drop_REFID_IOP_CACHE_AD()
    logging.info(f"{dataset}")
except Exception as e:
    logging.info(f"message: An internal error occurred : {e}")


try:
    logging.info(f"Create_REFID_IOP_CACHE_AD")
    dataset = Create_REFID_IOP_CACHE_AD()
    logging.info(f"{dataset}")
except Exception as e:
    logging.info(f"message: An internal error occurred : {e}")


try:
    logging.info(f"Get_REFID_IOP_CACHE_AD")
    dataset = Get_REFID_IOP_CACHE_AD()
    logging.info(f"{len(dataset)} rows")
except Exception as e:
    logging.info(f"message: An internal error occurred : {e}")


# Stop Script

now_stop = datetime.datetime.now()
logging.info(f"Stop at : {now_stop.strftime('%Y-%m-%d %H:%M:%S')} ")

delta = now_stop - now_start
logging.info(f"Delta time : {delta}")


# =========================================
# End of Script

logging.info(f"<== End of Script ==>")
