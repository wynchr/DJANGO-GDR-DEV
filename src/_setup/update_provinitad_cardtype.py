"""
====================================================================================================
.DESCRIPTION
    Update gender & birthdate in PROVINII_AD from CACHE_EVIDIAN

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		19/01/2023  CWY Initial Version

.COMMENTS
    -- Update CardType = NISS if len(NISS) = 11 PROVINIT_AD


    -- REFID_IOP_PROVINIT_AD
    SELECT SAMACCOUNTNAME, SN, GIVENNAME, EXTENSIONATTRIBUTE1, EMPLOYEENUMBER, LENGTH(EMPLOYEENUMBER), CARDTYPE
    FROM SA.REFID_IOP_PROVINIT_AD
    WHERE LENGTH(EMPLOYEENUMBER) != 11

    SELECT SAMACCOUNTNAME, SN, GIVENNAME, EXTENSIONATTRIBUTE1, EMPLOYEENUMBER, LENGTH(EMPLOYEENUMBER), CARDTYPE
    FROM SA.REFID_IOP_PROVINIT_AD
    WHERE LENGTH(EMPLOYEENUMBER) = 11

    -- REFID_IOP_PROVINIT_AD
    UPDATE SA.REFID_IOP_PROVINIT_AD SET CARDTYPE = 'NISS' WHERE LENGTH(EMPLOYEENUMBER) = 11

    UPDATE SA.REFID_IOP_PROVINIT_AD SET CARDTYPE = 'AUTRE' WHERE LENGTH(EMPLOYEENUMBER) != 11
====================================================================================================
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
# Main

sql_query = "UPDATE SA.REFID_IOP_PROVINIT_AD SET CARDTYPE = 'NISS' WHERE LENGTH(EMPLOYEENUMBER) = 11"
result = oracle_IT.exec_ddl_sql(sql_query)
logging.info(f"Update CardType = NISS : {result}")

sql_query = "UPDATE SA.REFID_IOP_PROVINIT_AD SET CARDTYPE = 'AUTRE' WHERE LENGTH(EMPLOYEENUMBER) != 11"
result = oracle_IT.exec_ddl_sql(sql_query)
logging.info(f"Update CardType = AUTRE : {result}")

# =========================================
# End of Script

logging.info(f"<== End of Script ==>")
