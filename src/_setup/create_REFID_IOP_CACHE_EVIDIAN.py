"""
=======================================================================================================================
.DESCRIPTION
	Create Oracle Table (SA.REFID_IOP_CACHE_EVIDIAN)
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version


.NOTES
    * Attention du apostrophes
    - Gérer les erreurs possibles
    - déplacer les fonctions en génériques

.COMMENTS
    CREATE TABLE SA.REFID_IOP_CACHE_EVIDIAN (
            CN 								VARCHAR2(20),
            STPADLOGIN 						VARCHAR2(20),
            EMPLOYEEID 						VARCHAR2(20),
            STPNISS 						VARCHAR2(20),
            STPINAMINUMBER 					VARCHAR2(20),
            SN 								VARCHAR2(50),
            GIVENNAME 						VARCHAR2(50),
            OSIRISEVIDIANSEX 				CHAR(1),
            STPBIRTHDATE 					VARCHAR2(25),
            PREFERREDLANGUAGE 				CHAR(2),
            BUSINESSCATEGORY 				VARCHAR2(50),
            COMPANY 						VARCHAR2(50),
            PHYSICALDELIVERYOFFICENAME 		VARCHAR2(50),
            EMPLOYEETYPE					VARCHAR2(50),
            OSIRISHRCONTRACTSTATUS 			VARCHAR2(5),
            OSIRISHRCONTRACTSTARTDATE 		VARCHAR2(25),
            OSIRISHRCONTRACTENDDATE 		VARCHAR2(25),
            CHUIDORIGINSOURCE 				VARCHAR2(50),
            DISTINGUISHEDNAME 				VARCHAR2(100),
            EVDIDMUSERIDREP 				VARCHAR2(100),
            EVDIDMSTATE 					CHAR(1),
            EVDPMSCHEDULERSTATUS 			VARCHAR2(50),
            WHENCREATED 					VARCHAR2(25),
            WHENCHANGED 					VARCHAR2(25),
            ENATELBEGINTIME 				VARCHAR2(25),
            ENATELENDTIME 					VARCHAR2(25),
            MESSAGES						VARCHAR2(100),
            CONSTRAINT REFID_IOP_CACHE_EVIDIAN_PK PRIMARY KEY (CN)
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


def Get_REFID_IOP_CACHE_EVIDIAN():
    sql_query = "select * from SA.REFID_IOP_CACHE_EVIDIAN"
    dataset = oracle_IT.fetch_data_from_db(sql_query)
    return dataset


def Drop_REFID_IOP_CACHE_EVIDIAN():
    sql_query = "DROP TABLE SA.REFID_IOP_CACHE_EVIDIAN"
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


def Create_REFID_IOP_CACHE_EVIDIAN():
    sql_query = f"""
    CREATE TABLE SA.REFID_IOP_CACHE_EVIDIAN (
        CN 								VARCHAR2(25),
        STPADLOGIN 						VARCHAR2(20),
        EMPLOYEEID 						VARCHAR2(20),
        STPNISS 						VARCHAR2(30),
        STPINAMINUMBER 					VARCHAR2(20),
        SN 								VARCHAR2(50),
        GIVENNAME 						VARCHAR2(50),
        OSIRISEVIDIANSEX 				CHAR(1),
        STPBIRTHDATE 					VARCHAR2(25),
        PREFERREDLANGUAGE 				CHAR(2),
        BUSINESSCATEGORY 				VARCHAR2(50),
        COMPANY 						VARCHAR2(50),
        PHYSICALDELIVERYOFFICENAME 		VARCHAR2(50),
        EMPLOYEETYPE					VARCHAR2(50),
        OSIRISHRCONTRACTSTATUS 			VARCHAR2(5),
        OSIRISHRCONTRACTSTARTDATE 		VARCHAR2(25),
        OSIRISHRCONTRACTENDDATE 		VARCHAR2(25),
        CHUIDORIGINSOURCE 				VARCHAR2(50),
        DISTINGUISHEDNAME 				VARCHAR2(100),
        EVDIDMUSERIDREP 				VARCHAR2(100),
        EVDIDMSTATE 					CHAR(1),
        EVDPMSCHEDULERSTATUS 			VARCHAR2(50),
        WHENCREATED 					VARCHAR2(25),
        WHENCHANGED 					VARCHAR2(25),
        ENATELBEGINTIME 				VARCHAR2(25),
        ENATELENDTIME 					VARCHAR2(25),
        RFIDATESYNC 				    VARCHAR2(21),        
        MESSAGES						VARCHAR2(100),
        CONSTRAINT REFID_IOP_CACHE_EVIDIAN_PK PRIMARY KEY (CN)
        )
        """
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

logging.info(f"Create Oracle Table (SA.REFID_IOP_CACHE_EVIDIAN) for DB:{DB}")

try:
    logging.info(f"Get_REFID_IOP_CACHE_EVIDIAN")
    dataset = Get_REFID_IOP_CACHE_EVIDIAN()
    logging.info(f"{len(dataset)} rows")
except:
    logging.info(f"Table do not exist")

try:
    logging.info(f"Drop_REFID_IOP_CACHE_EVIDIAN")
    dataset = Drop_REFID_IOP_CACHE_EVIDIAN()
    logging.info(f"{dataset}")
except:
    logging.info(f"Table do not exist")

try:
    logging.info(f"Create_REFID_IOP_CACHE_EVIDIAN")
    dataset = Create_REFID_IOP_CACHE_EVIDIAN()
    logging.info(f"{dataset}")
except:
    logging.info(f"Cacnot create table")


try:
    logging.info(f"Get_REFID_IOP_CACHE_EVIDIAN")
    dataset = Get_REFID_IOP_CACHE_EVIDIAN()
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
