"""
=======================================================================================================================
.DESCRIPTION
    Import view EVIDIAN.ARNO_CONTACTS from ORACLE RH to ORACLE IT
    Copy from PS

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		03/02/2023  CWY	Initial Version


.NOTES

.COMMENTS
    ------------------------------------------------------------------------------------------------
    ORACLE (EVIDIAN.ARNO_CONTACTS)							ORACLE (SA.REFID_IOP_CACHE_RH)
    ------------------------------------------------------------------------------------------------
    V100_RH_MATRICULE 										V100_RH_MATRICULE
    V100_RH_NOM 											V100_RH_NOM
    V100_RH_PRENOM 											V100_RH_PRENOM
    V100_RH_SEXE 											V100_RH_SEXE
    V100_RH_REGISTRE_NATIONAL 								V100_RH_REGISTRE_NATIONAL
    V100_RH_DATE_NAISSANCE 									V100_RH_DATE_NAISSANCE
    V100_RH_LANGUE 											V100_RH_LANGUE
    V100_RH_NUM_CARTE_ID 									V100_RH_NUM_CARTE_ID
    V300_RH_DATE_DEBUT_CONTRAT 								V300_RH_DATE_DEBUT_CONTRAT
    V300_RH_DATE_FIN_CONTRAT 								V300_RH_DATE_FIN_CONTRAT
    V100_RH_STATUT_CONTRAT 									V100_RH_STATUT_CONTRAT
    V300_RH_DATE_FIN_CONTRAT_CALC 							V300_RH_DATE_FIN_CONTRAT_CALC
    ------------------------------------------------------------------------------------------------
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

DBIT = "DB-IT"
DBRH = "DB-RH"
oracle_IT = OracleConnexion(DBIT)
oracle_RH = OracleConnexion(DBRH)

# =========================================
# Functions / Classes


def Get_VIEW_RH():
    sql_query = f"""
        SELECT DISTINCT acc.V100_RH_MATRICULE,
                            acc.V100_RH_NOM,
                            acc.V100_RH_PRENOM,
                            acc.V100_RH_SEXE,
                            acc.V100_RH_REGISTRE_NATIONAL,
                            acc.V100_RH_DATE_NAISSANCE,
                            acc.V100_RH_LANGUE,
                            acc.V100_RH_NUM_CARTE_ID,
                            acc.V300_RH_DATE_DEBUT_CONTRAT,
                            acc.V300_RH_DATE_FIN_CONTRAT,
                            acc.V100_RH_STATUT_CONTRAT,
                            acc.V200_CONTRAT_CODE_SOCIETE,
                            acc.V955_CONTRAT_CODE_PROFIL,
                            acc.V955_CONTRAT_PROFIL_FR,
                            avc.V600_CA_VENTIL_QUALIFICATION,
                            avc.V600_CA_VENTIL_CODE,
                            avc.V600_CA_VENTIL_FR,
                            aaci.V125_RH_INAMI_11
                    FROM EVIDIAN.ARNO_CONTACT_CONTRAT acc
                    LEFT JOIN EVIDIAN.ARNO_VENTILATIONS_CA avc ON acc.V300_CONTRAT_ID = avc.V300_CA_CONTRAT_ID
                    LEFT JOIN EVIDIAN.ARNO_ARCHIVE_CONTACTS_INAMI aaci ON acc.V100_RH_ID = aaci.V100_RH_ID
    """
    dataset = oracle_RH.fetch_data_from_db(sql_query)
    return dataset


def Get_REFID_IOP_CACHE_RH():
    sql_query = "select * from SA.REFID_IOP_CACHE_RH"
    dataset = oracle_IT.fetch_data_from_db(sql_query)
    return dataset


def Convert_Date_RH(iDate):
    # iDate = "12/15/1988 00:00:00"
    # iDate = 1601-01-01 9999-12-31
    iDate = str(iDate).replace("[]", "")

    if (str(iDate)[0:4] == '1601') or (str(iDate)[0:4] == '9999'):
        oDate = ''
    else:
        oDate = str(iDate)[0:10]

    # logging.info(f"iDate:{iDate} > oDate:{oDate}")

    return oDate


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

# os.system("python create_REFID_IOP_CACHE_RH.py")

logging.info(f"Synchronize Oracle Table (SA.REFID_IOP_CACHE_RH) with DB:{DBRH}")

try:
    logging.info(f"Get_VIEW_RH")
    dataset = Get_VIEW_RH()
    logging.info(f"Please wait a few times to load all the data ({len(dataset)} rows to insert) ...")

    i = 0
    for data in dataset:
        i += 1
        if i in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]:
            logging.info(f"i={str(i)}")

        user = {}
        user['V100_RH_MATRICULE'] = data['v100_rh_matricule']
        user['V100_RH_NOM'] = "" if data['v100_rh_nom'] is None else data['v100_rh_nom'].replace("'", "''")
        user['V100_RH_PRENOM'] = "" if data['v100_rh_prenom'] is None else data['v100_rh_prenom'].replace("'", "''")
        user['V100_RH_SEXE'] = "" if data['v100_rh_sexe'] is None else data['v100_rh_sexe']
        user['V100_RH_REGISTRE_NATIONAL'] = "" if data['v100_rh_registre_national'] is None else data['v100_rh_registre_national']
        user['V100_RH_DATE_NAISSANCE'] = "" if data['v100_rh_date_naissance'] is None else str(data['v100_rh_date_naissance'])[0:10]
        user['V100_RH_LANGUE'] = "" if data['v100_rh_langue'] is None else data['v100_rh_langue']
        user['V100_RH_NUM_CARTE_ID'] = "" if data['v100_rh_num_carte_id'] is None else data['v100_rh_num_carte_id']
        user['V300_RH_DATE_DEBUT_CONTRAT'] = "" if data['v300_rh_date_debut_contrat'] is None else Convert_Date_RH(data['v300_rh_date_debut_contrat'])
        user['V300_RH_DATE_FIN_CONTRAT'] = "" if data['v300_rh_date_fin_contrat'] is None else Convert_Date_RH(data['v300_rh_date_fin_contrat'])
        user['V100_RH_STATUT_CONTRAT'] = "" if data['v100_rh_statut_contrat'] is None else data['v100_rh_statut_contrat']

        user['V200_CONTRAT_CODE_SOCIETE'] = "" if data['v200_contrat_code_societe'] is None else data['v200_contrat_code_societe']
        user['V955_CONTRAT_CODE_PROFIL'] = "" if data['v955_contrat_code_profil'] is None else data['v955_contrat_code_profil']
        user['V955_CONTRAT_PROFIL_FR'] = "" if data['v955_contrat_profil_fr'] is None else data['v955_contrat_profil_fr'].replace("'", "''")
        user['V600_CA_VENTIL_QUALIFICATION'] = "" if data['v600_ca_ventil_qualification'] is None else data['v600_ca_ventil_qualification']
        user['V600_CA_VENTIL_CODE'] = "" if data['v600_ca_ventil_code'] is None else data['v600_ca_ventil_code']
        user['V600_CA_VENTIL_FR'] = "" if data['v600_ca_ventil_fr'] is None else data['v600_ca_ventil_fr'].replace("'", "''")
        user['V125_RH_INAMI_11'] = "" if data['v125_rh_inami_11'] is None else data['v125_rh_inami_11']
        user['RFIDATESYNC'] = now_start.strftime("%Y-%m-%d %H:%M:%S")
        user['MESSAGES'] = "Create RH Cache From ARNO Query"

        sql_query = f"""
        INSERT INTO SA.REFID_IOP_CACHE_RH (
				V100_RH_MATRICULE,				
				V100_RH_NOM, 					
				V100_RH_PRENOM,					
				V100_RH_SEXE,					
				V100_RH_REGISTRE_NATIONAL,		
				V100_RH_DATE_NAISSANCE,			
				V100_RH_LANGUE,				
				V100_RH_NUM_CARTE_ID,	
				V300_RH_DATE_DEBUT_CONTRAT,
				V300_RH_DATE_FIN_CONTRAT,	
				V100_RH_STATUT_CONTRAT,
				V200_CONTRAT_CODE_SOCIETE,
				V955_CONTRAT_CODE_PROFIL,
				V955_CONTRAT_PROFIL_FR,
				V600_CA_VENTIL_QUALIFICATION,
				V600_CA_VENTIL_CODE,
				V600_CA_VENTIL_FR,
				V125_RH_INAMI_11,
				RFIDATESYNC,
				MESSAGES
        )
        VALUES (
            '{user['V100_RH_MATRICULE']}',	
            '{user['V100_RH_NOM']}',				
            '{user['V100_RH_PRENOM']}',			
            '{user['V100_RH_SEXE']}',	
            '{user['V100_RH_REGISTRE_NATIONAL']}',
            '{user['V100_RH_DATE_NAISSANCE']}',
            '{user['V100_RH_LANGUE']}',	
            '{user['V100_RH_NUM_CARTE_ID']}',
            '{user['V300_RH_DATE_DEBUT_CONTRAT']}',
            '{user['V300_RH_DATE_FIN_CONTRAT']}',
            '{user['V100_RH_STATUT_CONTRAT']}',
            '{user['V200_CONTRAT_CODE_SOCIETE']}',
            '{user['V955_CONTRAT_CODE_PROFIL']}',
            '{user['V955_CONTRAT_PROFIL_FR']}',
            '{user['V600_CA_VENTIL_QUALIFICATION']}',
            '{user['V600_CA_VENTIL_CODE']}',
            '{user['V600_CA_VENTIL_FR']}',
            '{user['V125_RH_INAMI_11']}',
            '{user['RFIDATESYNC']}',
            '{user['MESSAGES']}'
        )
        """
        # logging.info(sql_query)
        dataset = oracle_IT.exec_ddl_sql(sql_query)

    # logging.info(sql_query)
    logging.info(f"{i} records inserted")
except Exception as e:
    logging.info("An internal error occurred {}".format(e))

try:
    logging.info(f"Get_REFID_IOP_CACHE_RH")
    dataset = Get_REFID_IOP_CACHE_RH()
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
