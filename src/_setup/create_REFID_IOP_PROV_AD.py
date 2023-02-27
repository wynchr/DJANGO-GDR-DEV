"""
=======================================================================================================================
.DESCRIPTION

    Create Oracle Table (SA.REFID_IOP_PROV_AD)
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version


.NOTES

.COMMENTS
    CREATE TABLE SA.REFID_IOP_PROV_AD (
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
    CONSTRAINT REFID_IOP_PROV_AD_PK PRIMARY KEY (SAMACCOUNTNAME)
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


def Get_REFID_IOP_PROV_AD():
    sql_query = "select * from SA.REFID_IOP_PROV_AD"
    dataset = oracle_IT.fetch_data_from_db(sql_query)
    return dataset


def Drop_REFID_IOP_PROV_AD():
    sql_query = "DROP TABLE SA.REFID_IOP_PROV_AD"
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


def Create_REFID_IOP_PROV_AD():
    sql_query = f"""
    CREATE TABLE SA.REFID_IOP_PROV_AD (
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
    CONSTRAINT REFID_IOP_PROV_AD_PK PRIMARY KEY (SAMACCOUNTNAME)
    )
    """
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


# def CreateUniqueIndexEMPLOYEENUMBER_REFID_IOP_PROV_AD():
#     sql_query = "CREATE UNIQUE INDEX SA.REFID_IOP_PROV_AD_EMPLOEENUMBER_UN ON SA.REFID_IOP_PROV_AD (EMPLOYEENUMBER)"
#     dataset = oracle_IT.exec_ddl_sql(sql_query)
#     return dataset
#
#
# def CreateUniqueIndexEXTENSIONATTRIBUTE1_REFID_IOP_PROV_AD():
#     sql_query = "CREATE UNIQUE INDEX SA.REFID_IOP_PROV_AD_EXTENSIONATTRIBUTE1_UN ON SA.REFID_IOP_PROV_AD (EXTENSIONATTRIBUTE1)"
#     dataset = oracle_IT.exec_ddl_sql(sql_query)
#     return dataset
#
#
# def CreateUniqueIndexEXTENSIONATTRIBUTE11_REFID_IOP_PROV_AD():
#     sql_query = "CREATE UNIQUE INDEX SA.REFID_IOP_PROV_AD_EXTENSIONATTRIBUTE11_UN ON SA.REFID_IOP_PROV_AD (EXTENSIONATTRIBUTE11)"
#     dataset = oracle_IT.exec_ddl_sql(sql_query)
#     return dataset


def generate_insert_query(dictionary):
    table = dictionary["table"]  # Get name of the table

    # Get all "keys" inside "values" key of dictionary (column names)
    columns = ', '.join(dictionary["values"].keys())

    # Get all "values" inside "values" key of dictionary (insert values)
    values = ", ".join(dictionary["values"].values())

    # Generate INSERT query
    sql_query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
    return sql_query


def Set_REFID_IOP_PROV_AD():
    # Data to be inserted:

    data = [{
        'table': 'SA.REFID_IOP_PROV_AD',
        'values': {
            'SAMACCOUNTNAME': "'ZZDEVIN'",
            'SN': "'ZZDEV'",
            'GIVENNAME': "'Init'",
            'USUALSN': "'ZZDEV'",
            'USUALGIVENNAME': "'Init'",
            'COMPANY': "'CHU-Brugmann'",
            'PHYSICALDELIVERYOFFICENAME': "'Horta'",
            'DEPARTMENT': "'Informatique'",
            'BUSINESSCATEGORY': "'internal'",
            'EMPLOYEETYPE': "'Administratif'",
            'QUALITY': "'Mr'",
            'PREFERREDLANGUAGE': "'fr'",
            'GENDER': "'M'",
            'BIRTHDATE': "'1963-03-02'",
            'CARDTYPE': "''",
            'EMPLOYEENUMBER': "'00098764512'",
            'EXTENSIONATTRIBUTE1': "'543210'",
            'EXTENSIONATTRIBUTE2': "'IN'",
            'EXTENSIONATTRIBUTE11': "'12345678901'",
            'TELEPHONENUMBER': "'79999'",
            'PAGER': "'59999'",
            'LOCALISATION': "''",
            'ROLES': "'Manager'",
            'UNITES': "'BG1,BG2'",
            'SPECIALITES': "'Chirurgie, Medecine'",
            'HOMEDIR': r"'\\chu-brugmann\share\home\REFITUN'",
            'HOMEDRIVE': "'H:'",
            'DESCRIPTION': "'OPTIONS:'",
            'INFO': "''",
            'EXTENSIONATTRIBUTE15': "'REFID-User'",
            'METADATA': "'CA=55010;'",
            'ENABLEACCOUNTEXPIRES': "'1'",
            'ACCOUNTEXPIRES': "'2022-12-31 00:00:00'",
            'CHANGEPASSWORDATLOGON': "'1'",
            'ENABLED': "'1'",
            'ENABLEMAIL': "'1'",
            'MAIL': "''",
            'GROUPS': "'REFID_Administratif'",
            'DISTRIBUTIONLIST': "'REFID - Distribution List for IT'",
            'GROUPSAD': "''",
            'DISTRIBUTIONLISTAD': "''",
            'ENV': "'DEV'",
            'ORG': "'OSIRIS'",
            'SRC': "''",
            'USERCRE': "'ADMIN'",
            'DATECRE': "'2021-12-06 16:47:00'",
            'USERUPD': "''",
            'DATEUPD': "''",
            'MSGREFID': "'Message venant du REFIDT'",
            'ACTIONTYPE': "'CREATE'",
            'MSGDB': "'1'",
            'MSGAD': "''",
            'DATESYNCAD': "''",
            'FLAGSYNCAD': "'0'",
            'MSGEXCHANGE': "''",
            'DATESYNCEXCHANGE': "''",
            'FLAGSYNCEXCHANGE': "'0'",
            'PASSWORD': "'UABhAHMAcwB3AEAAcgBkADAAMQAoACkA'",
            'OBJECTSID': "''",
            'OBJECTGUID': "''",
            'RHMATRICULE': "''",
            'RHNOM': "''",
            'RHPRENOM': "''",
            'RHSEXE': "''",
            'RHDNAIS': "''",
            'RHLANGUE': "''",
            'RHNUMCARDID': "''",
            'RHNUMNATIONAL': "''",
            'RHDATEDEB': "''",
            'RHDATEFIN': "''",
            'RHSTATUTCONTRAT': "''",
            'RHMETADATA': "''",
        }
    },
    {
        'table': 'SA.REFID_IOP_PROV_AD',
        'values': {
            'SAMACCOUNTNAME': "'ZZINTIN'",
            'SN': "'ZZINTERNEO'",
            'GIVENNAME': "'Initdev'",
            'USUALSN': "'ZZDEV'",
            'USUALGIVENNAME': "'Init'",
            'COMPANY': "'CHU-Brugmann'",
            'PHYSICALDELIVERYOFFICENAME': "'Horta'",
            'DEPARTMENT': "'Nursing'",
            'BUSINESSCATEGORY': "'interim'",
            'EMPLOYEETYPE': "'Nursing'",
            'QUALITY': "'Mr'",
            'PREFERREDLANGUAGE': "'fr'",
            'GENDER': "'M'",
            'BIRTHDATE': "'1970-05-02'",
            'CARDTYPE': "''",
            'EMPLOYEENUMBER': "'00012345'",
            'EXTENSIONATTRIBUTE1': "'012345'",
            'EXTENSIONATTRIBUTE2': "''",
            'EXTENSIONATTRIBUTE11': "''",
            'TELEPHONENUMBER': "''",
            'PAGER': "''",
            'LOCALISATION': "''",
            'ROLES': "''",
            'UNITES': "''",
            'SPECIALITES': "''",
            'HOMEDIR': r"'\\chu-brugmann\share\home\INTERIN'",
            'HOMEDRIVE': "'H:'",
            'DESCRIPTION': "'INTERNEO User'",
            'INFO': "''",
            'EXTENSIONATTRIBUTE15': "'INTERNEO-User'",
            'METADATA': "''",
            'ENABLEACCOUNTEXPIRES': "'1'",
            'ACCOUNTEXPIRES': "'2022-12-31 00:00:00'",
            'CHANGEPASSWORDATLOGON': "'1'",
            'ENABLED': "'1'",
            'ENABLEMAIL': "'0'",
            'MAIL': "''",
            'GROUPS': "'REFID_Nursing'",
            'DISTRIBUTIONLIST': "'REFID - Test DL'",
            'GROUPSAD': "''",
            'DISTRIBUTIONLISTAD': "''",
            'ENV': "'DEV'",
            'ORG': "'INTERNEO'",
            'SRC': "''",
            'USERCRE': "'ADMIN'",
            'DATECRE': "'2021-12-06 16:47:00'",
            'USERUPD': "''",
            'DATEUPD': "''",
            'MSGREFID': "'Message venant de INTERNEO'",
            'ACTIONTYPE': "'CREATE'",
            'MSGDB': "'1'",
            'MSGAD': "''",
            'DATESYNCAD': "''",
            'FLAGSYNCAD': "'0'",
            'MSGEXCHANGE': "''",
            'DATESYNCEXCHANGE': "''",
            'FLAGSYNCEXCHANGE': "'0'",
            'PASSWORD': "'UABhAHMAcwB3AEAAcgBkADAAMQAoACkA'",
            'OBJECTSID': "''",
            'OBJECTGUID': "''",
            'RHMATRICULE': "''",
            'RHNOM': "''",
            'RHPRENOM': "''",
            'RHSEXE': "''",
            'RHDNAIS': "''",
            'RHLANGUE': "''",
            'RHNUMCARDID': "''",
            'RHNUMNATIONAL': "''",
            'RHDATEDEB': "''",
            'RHDATEFIN': "''",
            'RHSTATUTCONTRAT': "''",
            'RHMETADATA': "''",
        }
    }
    ]

    # Generate QUERY for each dictionary inside data list
    for query in data:
        sql_query = generate_insert_query(query)
        logging.info(sql_query)
        dataset = oracle_IT.exec_ddl_sql(sql_query)

    return dataset


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

logging.info(f"Create Oracle Table (SA.REFID_IOP_PROV_AD) for DB:{DB}")


try:
    logging.info(f"Get_REFID_IOP_PROV_AD")
    dataset = Get_REFID_IOP_PROV_AD()
    logging.info(f"{len(dataset)} rows")
except:
    logging.info(f"Table do not exist")

try:
    logging.info(f"Drop_REFID_IOP_PROV_AD")
    dataset = Drop_REFID_IOP_PROV_AD()
    logging.info(f"{dataset}")
except:
    logging.info(f"Table do not exist")

try:
    logging.info(f"Create_REFID_IOP_PROV_AD")
    dataset = Create_REFID_IOP_PROV_AD()
    logging.info(f"{dataset}")
except:
    logging.info(f"Cannot create table")

try:
    logging.info(f"CreateUniqueIndexEMPLOYEENUMBER_REFID_IOP_PROV_AD")
    # dataset = CreateUniqueIndexEMPLOYEENUMBER_REFID_IOP_PROV_AD()
    logging.info(f"{dataset}")
except:
    logging.info(f"Cannot index table")

try:
    logging.info(f"CreateUniqueIndexEXTENSIONATTRIBUTE1_REFID_IOP_PROV_AD")
    # dataset = CreateUniqueIndexEXTENSIONATTRIBUTE1_REFID_IOP_PROV_AD()
    logging.info(f"{dataset}")
except:
    logging.info(f"Cannot index table")

try:
    logging.info(f"CreateUniqueIndexEXTENSIONATTRIBUTE11_REFID_IOP_PROV_AD")
    # dataset = CreateUniqueIndexEXTENSIONATTRIBUTE11_REFID_IOP_PROV_AD()
    logging.info(f"{dataset}")
except:
    logging.info(f"Cannot index table")

try:
    logging.info(f"Set_REFID_IOP_PROV_AD")
    dataset = Set_REFID_IOP_PROV_AD()
    logging.info(f"{dataset}")
except:
    logging.info(f"Cannot set the table")

try:
    logging.info(f"Get_REFID_IOP_PROV_AD")
    dataset = Get_REFID_IOP_PROV_AD()
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
