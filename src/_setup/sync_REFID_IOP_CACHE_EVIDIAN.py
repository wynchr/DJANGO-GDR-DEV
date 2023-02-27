"""
=======================================================================================================================
.DESCRIPTION
    Synchronize EVIDIAN with Oracle Table
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version


.NOTES

.COMMENTS
    Copy EVIDIAN to ORACLE
    ------------------------------------------------------------------------------------------------
    LDAP://sp1121.chubxl.be:10389/CN=3c793374,OU=IAMIDENTITY,O=iam		ORACLE (RFI_CACHE_EVIDIAN)
    ------------------------------------------------------------------------------------------------
    cn																	CN
    STPADlogin															STPADLOGIN
    employeeID															EMPLOYEEID
    STPNISS																STPNISS
    STPINAMINUMBER														STPINAMINUMBER
    sn																	SN
    givenname															GIVENNAME
    osiris-evidian-sex													OSIRISEVIDIANSEX
    STPBirthDate														STPBIRTHDATE
    preferredLanguage													PREFERREDLANGUAGE
    businessCategory													BUSINESSCATEGORY
    company																COMPANY
    physicalDeliveryOfficeName											PHYSICALDELIVERYOFFICENAME
    employeeType														EMPLOYEETYPE
    osiris-hr-contractstatus											OSIRISHRCONTRACTSTATUS
    osiris-hr-contractstartdate											OSIRISHRCONTRACTSTARTDATE
    osiris-hr-contractenddate											OSIRISHRCONTRACTENDDATE
    CHUIdOriginSource													CHUIDORIGINSOURCE
    distinguishedName													DISTINGUISHEDNAME
    evdidmUserIdRep														EVDIDMUSERIDREP
    evdidmState															EVDIDMSTATE
    evdpmSchedulerStatus												EVDPMSCHEDULERSTATUS
    whenCreated															WHENCREATED
    whenChanged															WHENCHANGED
    enatelBeginTime														ENATELBEGINTIME
    enatelEndTime														ENATELENDTIME
    ''																	MESSAGES
    ------------------------------------------------------------------------------------------------
=======================================================================================================================
"""
# =========================================
# Import modules
import os
import sys
import logging
from datetime import datetime

from ldap import exec_ldap_search_evidian_paged
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
    folder_path = f"../_log/{datetime.now().strftime('%Y-%m-%d')}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filename = f"{folder_path}/refid_sync_{datetime.now().strftime('%H%M%S')}.log"

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


def Get_AD_EVIDIAN_Entries():
    ldapsearchbase = "CN=3c793374,OU=IAMIDENTITY,O=iam"

    Filter = "(objectCategory=user)"
    # Filter = "(&(STPADlogin=wynchr))"
    # Filter = "(&(cn=OSIRIS-WU5NP1V))"

    usersevidian = exec_ldap_search_evidian_paged(ldapsearchbase, Filter)
    return usersevidian


def Get_REFID_IOP_CACHE_EVIDIAN():
    sql_query = "select * from SA.REFID_IOP_CACHE_EVIDIAN"
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


def Convert_DateTime(iDate):
    # iDate = '[datetime(1992, 9, 14, 0, 0, tzinfo=datetime.timezone.utc)]',
    # iDate = $null

    # print(iDate)

    iDate = iDate.replace('[', '')
    iDate = iDate.replace(']', '')
    if len(str(iDate)) >= 1:
        iDate = iDate.replace('(', '')
        iDate = iDate.replace(')', '')
        # iDate = iDate.replace(',', '')
        iDate = iDate.replace('.', '')
        iDate = iDate.replace('=', '')
        iDate = iDate.replace('tzinfo', '')
        iDate = iDate.replace('datetime', '')
        iDate = iDate.replace('timezone', '')
        iDate = iDate.replace('utc', '')
        iDate = iDate.replace(' ', '0')

        iDateY = iDate.split(",")[0]

        if len(iDate.split(",")[1]) == 2:
            iDateM = iDate.split(",")[1]
        if len(iDate.split(",")[1]) == 3:
            iDateM = iDate.split(",")[1][1:3]

        if len(iDate.split(",")[2]) == 2:
            iDateD = iDate.split(",")[2]
        if len(iDate.split(",")[2]) == 3:
            iDateD = iDate.split(",")[2][1:3]

        oDate = f"{iDateY}-{iDateM}-{iDateD} 00:00:00"

        # oDate = iDate

        # print(oDate)
    else:
        oDate = ''

    # print(oDate)

    # logging.info(f"iDate:{iDate} > oDate:{oDate}")

    return oDate


def Convert_UnixDateTime(timestamp):
    # iDate = '874195200',
    # iDate = []

    # print(timestamp)

    if (str(timestamp) != '[]') and (timestamp > 0) :
        dt_object = str(datetime.utcfromtimestamp(timestamp).replace(microsecond=0))
    else:
        dt_object = ''

    # print(dt_object)

    # logging.info(f"iDate:{timestamp} > oDate:{dt_object}")

    return dt_object


# =========================================
# Main

# Start Script

now_start = datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

# os.system("python create_REFID_IOP_CACHE_EVIDIAN.py")

logging.info(f"Synchronize Oracle Table (SA.REFID_IOP_CACHE_EVIDIAN) with AD-EVIDIAN")

try:
    logging.info(f"Get_AD_EVIDIAN_Entries")
    usersevidian = Get_AD_EVIDIAN_Entries()
    total_entries = len(usersevidian)

    # print(total_entries)
    
    logging.info(f"Please wait a few times to load all the data ({total_entries} rows to insert) ...")

    i = 0
    for data in usersevidian:
        i += 1
        if i in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]:
            logging.info(f"i={str(i)}")

        # print(f"{i} {str(data['attributes']['cn'])}")

        sql_query = ""

        user = {}

        user['CN'] = str(data['attributes']['cn'])

        if str(data['attributes']['STPADlogin']) != '[]':
            user['STPADLOGIN'] = str(data['attributes']['STPADlogin'][0])
        else:
            user['STPADLOGIN'] = ''

        user['EMPLOYEEID'] = str(data['attributes']['employeeID'])

        if str(data['attributes']['STPNISS']) != '[]':
            user['STPNISS'] = str(data['attributes']['STPNISS'][0])
        else:
            user['STPNISS'] = ''

        if str(data['attributes']['STPINAMINUMBER']) != '[]':
            user['STPINAMINUMBER'] = str(data['attributes']['STPINAMINUMBER'][0])
        else:
            user['STPINAMINUMBER'] = ''


        user['SN'] = str(data['attributes']['sn']).replace("'", " ")
        user['GIVENNAME'] = str(data['attributes']['givenname']).replace("'", " ")

        if str(data['attributes']['osiris-evidian-sex']) != '[]':
            user['OSIRISEVIDIANSEX'] = str(data['attributes']['osiris-evidian-sex'][0])
        else:
            user['OSIRISEVIDIANSEX'] = ''

        user['STPBIRTHDATE'] = Convert_DateTime(str(data['attributes']['STPBirthDate']))[:10]

        if str(data['attributes']['preferredLanguage']) != '[]':
            user['PREFERREDLANGUAGE'] = str(data['attributes']['preferredLanguage'][0])
        else:
            user['PREFERREDLANGUAGE'] = ''

        if str(data['attributes']['businessCategory']) != '[]':
            user['BUSINESSCATEGORY'] = str(data['attributes']['businessCategory'][0])
        else:
            user['BUSINESSCATEGORY'] = ''

        # user['PREFERREDLANGUAGE'] = str(data['attributes']['preferredLanguage'][0])
        # user['BUSINESSCATEGORY'] = str(data['attributes']['businessCategory'][0])

        user['COMPANY'] = str(data['attributes']['company']).replace("[]", "")
        user['PHYSICALDELIVERYOFFICENAME'] = str(data['attributes']['physicalDeliveryOfficeName'])
        user['EMPLOYEETYPE'] = str(data['attributes']['employeeType']).replace("[]", "")

        if str(data['attributes']['osiris-hr-contractstatus']) != '[]':
            # print(str(data['attributes']['osiris-hr-contractstatus'][0]))
            user['OSIRISHRCONTRACTSTATUS'] = str(data['attributes']['osiris-hr-contractstatus'][0])
        else:
            user['OSIRISHRCONTRACTSTATUS'] = ''

        user['OSIRISHRCONTRACTSTARTDATE'] = Convert_DateTime(str(data['attributes']['osiris-hr-contractstartdate']))[:10]
        user['OSIRISHRCONTRACTENDDATE'] = Convert_DateTime(str(data['attributes']['osiris-hr-contractenddate']))[:10]

        user['CHUIDORIGINSOURCE'] = str(data['attributes']['CHUIdOriginSource'][0])
        user['DISTINGUISHEDNAME'] = str(data['attributes']['distinguishedName'])
        user['EVDIDMUSERIDREP'] = str(data['attributes']['evdidmUserIdRep'][0])
        user['EVDIDMSTATE'] = str(data['attributes']['evdidmState'][0])
        user['EVDPMSCHEDULERSTATUS'] = str(data['attributes']['evdpmSchedulerStatus'][0])

        user['WHENCREATED'] = str(data['attributes']['whenCreated'])[0:19]
        user['WHENCHANGED'] = str(data['attributes']['whenChanged'])[0:19]

        user['ENATELBEGINTIME'] = Convert_UnixDateTime(data['attributes']['enatelBeginTime'])
        user['ENATELENDTIME'] = Convert_UnixDateTime(data['attributes']['enatelEndTime'])

        user['RFIDATESYNC'] = now_start.strftime("%Y-%m-%d %H:%M:%S")
        user['MESSAGES'] = "Message from IAM-EVIDIAN"

        sql_query = f"""
        INSERT INTO SA.REFID_IOP_CACHE_EVIDIAN (
                CN,
                STPADLOGIN,
                EMPLOYEEID,
                STPNISS,
                STPINAMINUMBER,
                SN,
                GIVENNAME,
                OSIRISEVIDIANSEX,
                STPBIRTHDATE,
                PREFERREDLANGUAGE,
                BUSINESSCATEGORY,
                COMPANY,
                PHYSICALDELIVERYOFFICENAME,
                EMPLOYEETYPE,
                OSIRISHRCONTRACTSTATUS,
                OSIRISHRCONTRACTSTARTDATE,
                OSIRISHRCONTRACTENDDATE,
                CHUIDORIGINSOURCE,
                DISTINGUISHEDNAME,
                EVDIDMUSERIDREP,
                EVDIDMSTATE,
                EVDPMSCHEDULERSTATUS,
                WHENCREATED,
                WHENCHANGED,
                ENATELBEGINTIME,
                ENATELENDTIME,
                RFIDATESYNC,
                MESSAGES
            )
        VALUES (
                '{user['CN']}',
                '{user['STPADLOGIN']}',
                '{user['EMPLOYEEID']}',
                '{user['STPNISS']}',
                '{user['STPINAMINUMBER']}',
                '{user['SN']}',
                '{user['GIVENNAME']}',
                '{user['OSIRISEVIDIANSEX']}',
                '{user['STPBIRTHDATE']}',
                '{user['PREFERREDLANGUAGE']}',
                '{user['BUSINESSCATEGORY']}',
                '{user['COMPANY']}',
                '{user['PHYSICALDELIVERYOFFICENAME']}',
                '{user['EMPLOYEETYPE']}',
                '{user['OSIRISHRCONTRACTSTATUS']}',
                '{user['OSIRISHRCONTRACTSTARTDATE']}',
                '{user['OSIRISHRCONTRACTENDDATE']}',
                '{user['CHUIDORIGINSOURCE']}',
                '{user['DISTINGUISHEDNAME']}',
                '{user['EVDIDMUSERIDREP']}',
                '{user['EVDIDMSTATE']}',
                '{user['EVDPMSCHEDULERSTATUS']}',
                '{user['WHENCREATED']}',
                '{user['WHENCHANGED']}',
                '{user['ENATELBEGINTIME']}',
                '{user['ENATELENDTIME']}',
                '{user['RFIDATESYNC']}',
                '{user['MESSAGES']}'
        )
        """
        # print(sql_query)

        dataset = oracle_IT.exec_ddl_sql(sql_query)

    logging.info(f"{i} on {total_entries} records inserted")
except Exception as e:
    logging.info(user)
    logging.info(sql_query)
    logging.info("An internal error occurred {}".format(e))
    exit(0)

try:
    logging.info(f"Get_REFID_IOP_CACHE_EVIDIAN")
    dataset = Get_REFID_IOP_CACHE_EVIDIAN()
    logging.info(f"{len(dataset)} rows")
except:
    logging.info(f"Table do not exist")
    exit(0)

# Stop Script

now_stop = datetime.now()
logging.info(f"Stop at : {now_stop.strftime('%Y-%m-%d %H:%M:%S')} ")

delta = now_stop - now_start
logging.info(f"Delta time : {delta}")


# =========================================
# End of Script

logging.info(f"<== End of Script ==>")
