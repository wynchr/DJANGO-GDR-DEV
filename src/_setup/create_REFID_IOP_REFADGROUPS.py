"""
=======================================================================================================================
.DESCRIPTION

    Create Oracle Table (SA.REFID_IOP_REFADGROUPS)
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version


.NOTES

.COMMENTS
    CREATE TABLE SA.REFID_IOP_REFADGROUPS (
        SAMACCOUNTNAME				VARCHAR2(20), 
        DISTINGUISHEDNAME			VARCHAR2(200),
        MAIL 						VARCHAR2(100), 
        GROUPCATEGORY				VARCHAR2(20),
        WHENCREATED 				VARCHAR2(21),
        WHENCHNAGED					VARCHAR2(21),
        DESCRIPTION					VARCHAR2(100),
        INFO						VARCHAR2(50),
        OBJECTGUID					VARCHAR2(50),
        OBJECTSID					VARCHAR2(50),
        ENV							VARCHAR2(5)
    CONSTRAINT REFID_IOP_REFADGROUPS_PK PRIMARY KEY (SAMACCOUNTNAME)
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


def Get_REFID_IOP_REFADGROUPS():
    sql_query = "select * from SA.REFID_IOP_REFADGROUPS"
    dataset = oracle_IT.fetch_data_from_db(sql_query)
    return dataset


def Drop_REFID_IOP_REFADGROUPS():
    sql_query = "DROP TABLE SA.REFID_IOP_REFADGROUPS"
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


def Create_REFID_IOP_REFADGROUPS():
    sql_query = f"""
    CREATE TABLE SA.REFID_IOP_REFADGROUPS (
				ID 							NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY,
				SAMACCOUNTNAME				VARCHAR2(100), 
				DISTINGUISHEDNAME			VARCHAR2(200),
				MAIL 						VARCHAR2(100), 
				GROUPCATEGORY				VARCHAR2(20),
				WHENCREATED 				VARCHAR2(21),
				WHENCHANGED					VARCHAR2(21),
				DESCRIPTION					VARCHAR2(100),
				INFO						VARCHAR2(50),
				EXTENSIONATTRIBUTE15				VARCHAR2(50),
				OBJECTGUID					VARCHAR2(50),
				OBJECTSID					VARCHAR2(50),
				ENV							VARCHAR2(5),
				CONSTRAINT REFID_IDREFADGROUPS_PK PRIMARY KEY (ID)
			   )
    """
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


def CreateIndex_REFID_IOP_REFADGROUPS():
    sql_query = "CREATE INDEX SA.REFID_REFADGROUPS_PK ON SA.REFID_IOP_REFADGROUPS (SAMACCOUNTNAME)"
    dataset = oracle_IT.exec_ddl_sql(sql_query)
    return dataset


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

logging.info(f"Create Oracle Table (SA.REFID_IOP_REFADGROUPS) for DB:{DB}")

try:
    logging.info(f"Get_REFID_IOP_REFADGROUPS")
    dataset = Get_REFID_IOP_REFADGROUPS()
    logging.info(f"{len(dataset)} rows")
except:
    logging.info(f"Table do not exist")

try:
    logging.info(f"Drop_REFID_IOP_REFADGROUPS")
    dataset = Drop_REFID_IOP_REFADGROUPS()
    logging.info(f"{dataset}")
except:
    logging.info(f"Table do not exist")

try:
    logging.info(f"Create_REFID_IOP_REFADGROUPS")
    dataset = Create_REFID_IOP_REFADGROUPS()
    logging.info(f"{dataset}")
except:
    logging.info(f"Cannot create table")

try:
    logging.info(f"CreateIndex_REFID_IOP_REFADGROUPS")
    dataset = CreateIndex_REFID_IOP_REFADGROUPS()
    logging.info(f"{dataset}")
except:
    logging.info(f"Cannot create table")

try:
    logging.info(f"Get_REFID_IOP_REFADGROUPS")
    dataset = Get_REFID_IOP_REFADGROUPS()
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
