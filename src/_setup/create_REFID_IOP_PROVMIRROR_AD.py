"""
=======================================================================================================================
.DESCRIPTION

    Create Oracle Table (SA.REFID_IOP_PROVMIRROR_AD)
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version


.NOTES

.COMMENTS
    CREATE TABLE SA.REFID_IOP_PROVMIRROR_AD (
    SAMACCOUNTNAME 				VARCHAR2(10),
    SN 							VARCHAR2(50),
    GIVENNAME 					VARCHAR2(50),
    PASSWORD					VARCHAR2(50),
    COMPANY 					VARCHAR2(50),
    PHYSICALDELIVERYOFFICENAME 	VARCHAR2(50),
    BUSINESSCATEGORY 			VARCHAR2(20),
    EMPLOYEETYPE 				VARCHAR2(20),
    DEPARTMENT 					VARCHAR2(50),
    PREFERREDLANGUAGE 			VARCHAR2(2),
    EMPLOYEENUMBER 				VARCHAR2(20),
    EXTENSIONATTRIBUTE1 		VARCHAR2(20),
    EXTENSIONATTRIBUTE2 		VARCHAR2(3),
    EXTENSIONATTRIBUTE11 		VARCHAR2(11),
    TELEPHONENUMBER 			VARCHAR2(50),
    PAGER 						VARCHAR2(20),
    ROLES						VARCHAR2(200),
    UNITES						VARCHAR2(200),
    SPECIALITES					VARCHAR2(200),
    HOMEDIR						VARCHAR2(200),
    HOMEDRIVE					VARCHAR2(5),
    DESCRIPTION 				VARCHAR2(500),
    INFO						VARCHAR2(50),
    EXTENSIONATTRIBUTE15		VARCHAR2(50),
    ENABLEACCOUNTEXPIRES 		CHAR(1),
    ACCOUNTEXPIRES 				VARCHAR2(20),
    CHANGEPASSWORDATLOGON		CHAR(1),
    ENABLED 					CHAR(1),
    ENABLEMAIL 					CHAR(1),
    MAIL	 					VARCHAR2(100),
    GROUPS						VARCHAR2(4000),
    DISTRIBUTIONLIST			VARCHAR2(4000),
    ENV							VARCHAR2(10),
    ORG							VARCHAR2(10),
    USERCRE 					VARCHAR2(10),
    DATECRE 					VARCHAR2(20),
    USERUPD 					VARCHAR2(10),
    DATEUPD 					VARCHAR2(20),
    MSGREFID					VARCHAR2(500),
    ACTIONTYPE					VARCHAR2(10),
    MSGDB 						VARCHAR2(500),
    MSGAD 						VARCHAR2(500),
    DATESYNCAD					VARCHAR2(20),
    FLAGSYNCAD 					CHAR(1),
    MSGEXCHANGE 				VARCHAR2(500),
    DATESYNCEXCHANGE			VARCHAR2(20),
    FLAGSYNCEXCHANGE			CHAR(1),
    OBJECTSID					CHAR(50),
    OBJECTGUID					CHAR(50),
    CONSTRAINT REFID_IOP_PROVMIRROR_AD_PK PRIMARY KEY (SAMACCOUNTNAME)
    )
=======================================================================================================================
"""
# =========================================
# Import modules
import os
import sys
import datetime
import logging
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

DB = "DB-IT"
oracle_IT = OracleConnexion(DB)


# =========================================
# Functions / Classes


def Get_REFID_IOP_PROVMIRROR_AD():
    sql_query = "select * from SA.REFID_IOP_PROVMIRROR_AD"
    dataset = oracle_IT.fetch_data_from_db(sql_query)
    return dataset


def Drop_REFID_IOP_PROVMIRROR_AD():
    sql_query = "DROP TABLE SA.REFID_IOP_PROVMIRROR_AD"
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


def Create_REFID_IOP_PROVMIRROR_AD():
    sql_query = f"""
    CREATE TABLE SA.REFID_IOP_PROVMIRROR_AD (
        SAMACCOUNTNAME 				VARCHAR2(10), 
    
        SN 							VARCHAR2(50), 
        GIVENNAME 					VARCHAR2(50), 
    
        USUALSN						VARCHAR2(50),
        USUALGIVENNAME				VARCHAR2(50),
    
        COMPANY 					VARCHAR2(50), 
        PHYSICALDELIVERYOFFICENAME 	VARCHAR2(50), 
        DEPARTMENT 					VARCHAR2(50), 
    
        BUSINESSCATEGORY 			VARCHAR2(20), 
        EMPLOYEETYPE 				VARCHAR2(20), 
    
        QUALITY						VARCHAR2(3),
        PREFERREDLANGUAGE 			VARCHAR2(2),
        GENDER						CHAR(1),
        BIRTHDATE					VARCHAR2(15),
    
        CARDTYPE					VARCHAR2(15),
        EMPLOYEENUMBER 				VARCHAR2(30), 
        EXTENSIONATTRIBUTE1 		VARCHAR2(30), 
        EXTENSIONATTRIBUTE2 		VARCHAR2(3),
        EXTENSIONATTRIBUTE11 		VARCHAR2(11),
    
        TELEPHONENUMBER 			VARCHAR2(50), 
        PAGER 						VARCHAR2(20), 
    
        LOCALISATION				VARCHAR2(20),
    
        ROLES						VARCHAR2(200),
        UNITES						VARCHAR2(200),
        SPECIALITES					VARCHAR2(200),
    
        HOMEDIR						VARCHAR2(200),
        HOMEDRIVE					VARCHAR2(5),
    
        DESCRIPTION 				VARCHAR2(500), 
        INFO 						VARCHAR2(50),
        EXTENSIONATTRIBUTE15		VARCHAR2(50),
        METADATA					VARCHAR2(50),
    
        ENABLEACCOUNTEXPIRES 		CHAR(1),		
        ACCOUNTEXPIRES 				VARCHAR2(20), 
        CHANGEPASSWORDATLOGON		CHAR(1),
        ENABLED 					CHAR(1), 
    
        ENABLEMAIL 					CHAR(1),
        MAIL	 					VARCHAR2(100), 
    
        GROUPS						VARCHAR2(4000),
        DISTRIBUTIONLIST			VARCHAR2(4000),

        GROUPSAD					VARCHAR2(4000),
        DISTRIBUTIONLISTAD			VARCHAR2(4000),
                
        ENV							VARCHAR2(10),
        ORG							VARCHAR2(10),
        SRC							VARCHAR2(10),
    
        USERCRE 					VARCHAR2(15), 
        DATECRE 					VARCHAR2(20), 
        USERUPD 					VARCHAR2(15), 
        DATEUPD 					VARCHAR2(20), 
    
        MSGREFID					VARCHAR2(500),
        ACTIONTYPE					VARCHAR2(15),
        MSGDB 						VARCHAR2(500), 
    
        MSGAD 						VARCHAR2(500), 
        DATESYNCAD					VARCHAR2(20), 
        FLAGSYNCAD 					CHAR(1), 
    
        MSGEXCHANGE 				VARCHAR2(500), 
        DATESYNCEXCHANGE			VARCHAR2(20), 
        FLAGSYNCEXCHANGE			CHAR(1), 
    
        PASSWORD					VARCHAR2(50),
    
        OBJECTSID					CHAR(50), 
        OBJECTGUID					CHAR(50), 
    
        WHENCREATED			        VARCHAR2(20), 
        WHENCHANGED			        VARCHAR2(20), 
        LASTLOGONTIMESTAMP			VARCHAR2(20), 
        LASTLOGON			        VARCHAR2(20), 
        PWDLASTSET			        VARCHAR2(20), 
        BADPASSWORDTIME			    VARCHAR2(20), 
        MSEXCHWHENMAILBOXCREATED	VARCHAR2(20),          
 
        CHUIDORIGINSOURCE 			VARCHAR2(50),
        EVDIDMSTATE 				CHAR(1),
        EVDPMSCHEDULERSTATUS 		VARCHAR2(50),
        ENATELBEGINTIME 			VARCHAR2(25),
        ENATELENDTIME 				VARCHAR2(25),
                   
        RHMATRICULE					VARCHAR2(30), 
        RHNOM						VARCHAR2(50),
        RHPRENOM					VARCHAR2(50),
        RHSEXE						CHAR(1),
        RHDNAIS						VARCHAR2(15),
        RHLANGUE					VARCHAR2(2),
        RHNUMCARDID					VARCHAR2(30),
        RHNUMNATIONAL				VARCHAR2(30),
        RHDATEDEB					VARCHAR2(20), 
        RHDATEFIN					VARCHAR2(20), 
        RHSTATUTCONTRAT				VARCHAR2(20), 
        
        RHCODESOCIETE				VARCHAR2(15),
        RHCODEPROFIL				VARCHAR2(10),
        RHPROFIL					VARCHAR2(100),
        RHCAQUALIFICATION			VARCHAR2(8),
        RHCACODE					VARCHAR2(55),
        RHCALIB						VARCHAR2(100),
        RHINAMI						VARCHAR2(11),
        RHMETADATA 					VARCHAR2(500), 
        
        RFIDATESYNC 				VARCHAR2(21),
        MESSAGES					VARCHAR2(100), 
    CONSTRAINT REFID_IOP_PROVMIRROR_AD_PK PRIMARY KEY (SAMACCOUNTNAME)
    )
    """
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

logging.info(f"Create Oracle Table (SA.REFID_IOP_PROVMIRROR_AD) for DB:{DB}")

try:
    logging.info(f"Get_REFID_IOP_PROVMIRROR_AD")
    dataset = Get_REFID_IOP_PROVMIRROR_AD()
    logging.info(f"{len(dataset)} rows")
except:
    logging.info(f"Table do not exist")

try:
    logging.info(f"Drop_REFID_IOP_PROVMIRROR_AD")
    dataset = Drop_REFID_IOP_PROVMIRROR_AD()
    logging.info(f"{dataset}")
except:
    logging.info(f"Table do not exist")

try:
    logging.info(f"Create_REFID_IOP_PROVMIRROR_AD")
    dataset = Create_REFID_IOP_PROVMIRROR_AD()
    logging.info(f"{dataset}")
except:
    logging.info(f"Cannot create table")

try:
    logging.info(f"Get_REFID_IOP_PROVMIRROR_AD")
    dataset = Get_REFID_IOP_PROVMIRROR_AD()
    logging.info(f"{len(dataset)} rows")
    logging.info(dataset)
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
