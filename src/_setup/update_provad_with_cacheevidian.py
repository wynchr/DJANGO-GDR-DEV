"""
====================================================================================================
.DESCRIPTION
    Update gender & birthdate in PROV_AD from CACHE_EVIDIAN

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		19/01/2023  CWY Initial Version

.COMMENTS
    -- Copy gender & birthdate from CACHE_EVIDIAN to PROV_AD

    -- REFID_IOP_CACHE_EVIDIAN
    SELECT STPADLOGIN, SN, GIVENNAME, OSIRISEVIDIANSEX, SUBSTR(STPBIRTHDATE,1,10) FROM REFID_IOP_CACHE_EVIDIAN

    -- REFID_IOP_PROV_AD
    SELECT SAMACCOUNTNAME, SN, GIVENNAME, GENDER, BIRTHDATE FROM SA.REFID_IOP_PROV_AD

    -- UPDATE SA.REFID_IOP_PROV_AD SET GENDER='',BIRTHDATE=''
    UPDATE SA.REFID_IOP_PROV_AD SET GENDER='',BIRTHDATE=''

    -- REFID_IOP_PROV_AD
    UPDATE SA.REFID_IOP_PROV_AD T1
      SET (GENDER, BIRTHDATE) = (SELECT OSIRISEVIDIANSEX,  SUBSTR(STPBIRTHDATE,1,10)
                                    FROM  SA.REFID_IOP_CACHE_EVIDIAN T2
                                    WHERE T1.SAMACCOUNTNAME = T2.STPADLOGIN AND ROWNUM <= 1)

    -- REFID_IOP_PROV_AD
    UPDATE SA.REFID_IOP_PROV_AD T1
      SET QUALITY = CASE WHEN (EMPLOYEETYPE = 'Medical')  THEN 'Dr'
                         WHEN (GENDER = 'M')  THEN 'Mr'
                         WHEN (GENDER = 'F')  THEN 'Mme'
                         ELSE '' END


    -- Check gor gender or bithdate IS NULL
    SELECT SAMACCOUNTNAME, SN, GIVENNAME, GENDER, BIRTHDATE, EMPLOYEETYPE, EXTENSIONATTRIBUTE11, QUALITY
    FROM SA.REFID_IOP_PROV_AD
    WHERE GENDER IS NULL
    OR BIRTHDATE IS NULL

    SELECT SAMACCOUNTNAME, SN, GIVENNAME, GENDER, BIRTHDATE, EMPLOYEETYPE, EXTENSIONATTRIBUTE11, QUALITY
    FROM SA.REFID_IOP_PROV_AD
    WHERE GENDER IS NOT NULL
    AND BIRTHDATE IS NOT NULL

    SELECT SAMACCOUNTNAME, SN, GIVENNAME, GENDER, BIRTHDATE, EMPLOYEETYPE, EXTENSIONATTRIBUTE11, QUALITY
    FROM SA.REFID_IOP_PROV_AD
    WHERE GENDER IS NOT NULL
    AND BIRTHDATE IS NOT NULL
    AND EMPLOYEETYPE = 'Medical'
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

sql_query = "UPDATE SA.REFID_IOP_CACHE_EVIDIAN SET ENATELBEGINTIME = '' WHERE ENATELBEGINTIME = '1970-01-01 00:00:00'"
result = oracle_IT.exec_ddl_sql(sql_query)
logging.info(f"ENATELBEGINTIME : {result}")


sql_query = "UPDATE SA.REFID_IOP_CACHE_EVIDIAN SET ENATELENDTIME = '' WHERE ENATELENDTIME = '1970-01-01 00:00:00'"
result = oracle_IT.exec_ddl_sql(sql_query)
logging.info(f"ENATELENDTIME : {result}")


sql_query = """
UPDATE SA.REFID_IOP_PROV_AD T1
                SET (GENDER,
                    BIRTHDATE,
                    CHUIDORIGINSOURCE,
                    EVDIDMSTATE,
                    EVDPMSCHEDULERSTATUS,
                    ENATELBEGINTIME,
                    ENATELENDTIME             
           ) = (SELECT 
                    OSIRISEVIDIANSEX,
                    SUBSTR(STPBIRTHDATE,1,10),
                    CHUIDORIGINSOURCE,
                    EVDIDMSTATE,
                    EVDPMSCHEDULERSTATUS,
                    SUBSTR(ENATELBEGINTIME,1,10),
                    SUBSTR(ENATELENDTIME,1,10)               
                FROM  SA.REFID_IOP_CACHE_EVIDIAN T2
                WHERE T1.SAMACCOUNTNAME = T2.STPADLOGIN AND ROWNUM <= 1)
"""
result = oracle_IT.exec_ddl_sql(sql_query)
logging.info(f"Update GENDER & BIRTHDATE : {result}")

# =========================================
# End of Script

logging.info(f"<== End of Script ==>")