"""
====================================================================================================
.DESCRIPTION
    Update gender & birthdate in PROVINII_AD from CACHE_EVIDIAN

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		19/01/2023  CWY Initial Version

.COMMENTS
    -- Adjust QUALITY from  GENDER & EMPLOYEETYPE in PROVINIT_AD


    -- REFID_IOP_PROVINIT_AD
    UPDATE SA.REFID_IOP_PROVINIT_AD T1
      SET QUALITY = CASE WHEN (EMPLOYEETYPE = 'Medical')  THEN 'Dr'
                         WHEN (GENDER = 'M')  THEN 'Mr'
                         WHEN (GENDER = 'F')  THEN 'Mme'
                         ELSE '' END
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

sql_query = """
    UPDATE SA.REFID_IOP_PROVINIT_AD T1
        SET QUALITY = CASE WHEN (EMPLOYEETYPE = 'Medical')  THEN 'Dr'
                         WHEN (GENDER = 'M')  THEN 'Mr' 
                         WHEN (GENDER = 'F')  THEN 'Mme' 
                         ELSE '' END
"""
# result = db.exec_update_sql('ITDEV', sql)
result = oracle_IT.exec_ddl_sql(sql_query)
logging.info(f"Update QUALITY : {result}")

# =========================================
# End of Script

logging.info(f"<== End of Script ==>")