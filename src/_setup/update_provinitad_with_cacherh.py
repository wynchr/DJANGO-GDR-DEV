"""
====================================================================================================
.DESCRIPTION
    Update gender & birthdate in PROVINIT_AD from CACHE_EVIDIAN

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		19/01/2023  CWY Initial Version

.COMMENTS
    -- Copy RH Fields from CACHE_RH to PROVINIT_AD on MATRICULE


    -- REFID_IOP_CACHE_RH
    SELECT V100_RH_MATRICULE,
            V100_RH_NOM,
            V100_RH_PRENOM,
            V100_RH_SEXE,
            V100_RH_DATE_NAISSANCE,
            V100_RH_LANGUE,
            V100_RH_NUM_CARTE_ID,
            V100_RH_REGISTRE_NATIONAL,
            V300_RH_DATE_DEBUT_CONTRAT,
            V300_RH_DATE_FIN_CONTRAT,
            V100_RH_STATUT_CONTRAT,
            V200_CONTRAT_CODE_SOCIETE,
            V955_CONTRAT_CODE_PROFIL,
            V955_CONTRAT_PROFIL_FR,
            V600_CA_VENTIL_QUALIFICATION,
            V600_CA_VENTIL_CODE,
            V600_CA_VENTIL_FR,
            V125_RH_INAMI_11
    FROM REFID_IOP_CACHE_RH


    -- REFID_IOP_PROVINIT_AD
    SELECT EXTENSIONATTRIBUTE1,
            GENDER,
            BIRTHDATE,
            RHMATRICULE,
            RHNOM,
            RHPRENOM,
            RHSEXE,
            RHDNAIS,
            RHLANGUE,
            RHNUMCARDID,
            RHNUMNATIONAL,
            RHDATEDEB,
            RHDATEFIN,
            RHSTATUTCONTRAT,
            RHCODESOCIETE,
            RHCODEPROFIL,
            RHPROFIL,
            RHCAQUALIFICATION,
            RHCACODE,
            RHCALIB,
            RHINAMI,
            RHMETADATA
    FROM SA.REFID_IOP_PROVINIT_AD

    -- UPDATE SA.REFID_IOP_PROVINIT_AD SET GENDER='',BIRTHDATE=''
    UPDATE SA.REFID_IOP_PROVINIT_AD
    SET RHMATRICULE='',
        RHNOM='',
        RHPRENOM='',
        RHSEXE='',
        RHDNAIS='',
        RHLANGUE='',
        RHNUMCARDID='',
        RHNUMNATIONAL='',
        RHDATEDEB='',
        RHDATEFIN='',
        RHSTATUTCONTRAT='',
        RHCODESOCIETE='',
        RHCODEPROFIL='',
        RHPROFIL='',
        RHCAQUALIFICATION='',
        RHCACODE='',
        RHCALIB='',
        RHINAMI='',
        RHMETADATA=''


    -- REFID_IOP_PROVINIT_AD
    UPDATE SA.REFID_IOP_PROVINIT_AD T1
      SET (	GENDER,
            BIRTHDATE,
            RHMATRICULE,
            RHNOM,
            RHPRENOM,
            RHSEXE,
            RHDNAIS,
            RHLANGUE,
            RHNUMCARDID,
            RHNUMNATIONAL,
            RHDATEDEB,
            RHDATEFIN,
            RHSTATUTCONTRAT,
            RHCODESOCIETE,
            RHCODEPROFIL,
            RHPROFIL,
            RHCAQUALIFICATION,
            RHCACODE,
            RHCALIB,
            RHINAMI) =
      (SELECT V100_RH_SEXE,
                SUBSTR(V100_RH_DATE_NAISSANCE,1,10),
                V100_RH_MATRICULE,
                V100_RH_NOM,
                V100_RH_PRENOM,
                V100_RH_SEXE,
                SUBSTR(V100_RH_DATE_NAISSANCE,1,10),
                V100_RH_LANGUE,
                V100_RH_NUM_CARTE_ID,
                V100_RH_REGISTRE_NATIONAL,
                SUBSTR(V300_RH_DATE_DEBUT_CONTRAT,1,10),
                SUBSTR(V300_RH_DATE_FIN_CONTRAT,1,10),
                V100_RH_STATUT_CONTRAT,
                V200_CONTRAT_CODE_SOCIETE,
                V955_CONTRAT_CODE_PROFIL,
                V955_CONTRAT_PROFIL_FR,
                V600_CA_VENTIL_QUALIFICATION,
                V600_CA_VENTIL_CODE,
                V600_CA_VENTIL_FR,
                V125_RH_INAMI_11
        FROM  SA.REFID_IOP_CACHE_RH T2
        WHERE T1.EXTENSIONATTRIBUTE1 = T2.V100_RH_MATRICULE AND ROWNUM <= 1)

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

sql_query = "UPDATE SA.REFID_IOP_CACHE_RH SET V300_RH_DATE_FIN_CONTRAT  = '' WHERE V300_RH_DATE_FIN_CONTRAT = '9999-12-31 00:00:00'"
result = oracle_IT.exec_ddl_sql(sql_query)
logging.info(f"V300_RH_DATE_FIN_CONTRAT : {result}")


# Link on MATRICULE
sql_query = """
UPDATE SA.REFID_IOP_PROVINIT_AD T1
  SET (	GENDER,
		BIRTHDATE,
  		RHMATRICULE,
  		RHNOM, 
  		RHPRENOM,
  		RHSEXE, 
  		RHDNAIS,
  		RHLANGUE,
  		RHNUMCARDID,
		RHNUMNATIONAL,
		RHDATEDEB,
		RHDATEFIN,
		RHSTATUTCONTRAT,
		RHCODESOCIETE,
		RHCODEPROFIL,
		RHPROFIL,
		RHCAQUALIFICATION,
		RHCACODE,
		RHCALIB,
		RHINAMI) = 
  (SELECT V100_RH_SEXE, 
			SUBSTR(V100_RH_DATE_NAISSANCE,1,10),
			V100_RH_MATRICULE,
			V100_RH_NOM, 
			V100_RH_PRENOM,
			V100_RH_SEXE, 
			SUBSTR(V100_RH_DATE_NAISSANCE,1,10),
			V100_RH_LANGUE,
			V100_RH_NUM_CARTE_ID, 
			V100_RH_REGISTRE_NATIONAL,  
			SUBSTR(V300_RH_DATE_DEBUT_CONTRAT,1,10),
			SUBSTR(V300_RH_DATE_FIN_CONTRAT,1,10),
			V100_RH_STATUT_CONTRAT,
			V200_CONTRAT_CODE_SOCIETE,
			V955_CONTRAT_CODE_PROFIL,
			V955_CONTRAT_PROFIL_FR,
			V600_CA_VENTIL_QUALIFICATION,
			V600_CA_VENTIL_CODE,
			V600_CA_VENTIL_FR,
			V125_RH_INAMI_11		  
	FROM  SA.REFID_IOP_CACHE_RH T2
	WHERE T1.EXTENSIONATTRIBUTE1 = T2.V100_RH_MATRICULE AND ROWNUM <= 1)
"""
result = oracle_IT.exec_ddl_sql(sql_query)
logging.info(f"Update RH Fields on MATRICULE: {result}")

# Link on NISS
sql_query = f"""
    UPDATE SA.REFID_IOP_PROVINIT_AD T1
    SET (GENDER,
        BIRTHDATE,
        RHMATRICULE,
        RHNOM, 
        RHPRENOM,
        RHSEXE, 
        RHDNAIS,
        RHLANGUE,
        RHNUMCARDID,
        RHNUMNATIONAL,
        RHDATEDEB,
        RHDATEFIN,
        RHSTATUTCONTRAT,
        RHCODESOCIETE,
        RHCODEPROFIL,
        RHPROFIL,
        RHCAQUALIFICATION,
        RHCACODE,
        RHCALIB,
        RHINAMI
        ) = 
    (SELECT V100_RH_SEXE, 
            SUBSTR(V100_RH_DATE_NAISSANCE,1,10),
            V100_RH_MATRICULE,
            V100_RH_NOM, 
            V100_RH_PRENOM,
            V100_RH_SEXE, 
            SUBSTR(V100_RH_DATE_NAISSANCE,1,10),
            V100_RH_LANGUE,
            V100_RH_NUM_CARTE_ID, 
            V100_RH_REGISTRE_NATIONAL,  
            SUBSTR(V300_RH_DATE_DEBUT_CONTRAT,1,10),
            SUBSTR(V300_RH_DATE_FIN_CONTRAT,1,10),
            V100_RH_STATUT_CONTRAT,
            V200_CONTRAT_CODE_SOCIETE,
            V955_CONTRAT_CODE_PROFIL,
            V955_CONTRAT_PROFIL_FR,
            V600_CA_VENTIL_QUALIFICATION,
            V600_CA_VENTIL_CODE,
            V600_CA_VENTIL_FR,
            V125_RH_INAMI_11		  
    FROM  SA.REFID_IOP_CACHE_RH T2
    WHERE T1.EMPLOYEENUMBER = T2.V100_RH_REGISTRE_NATIONAL AND ROWNUM <= 1)
"""
result = oracle_IT.exec_ddl_sql(sql_query)
logging.info(f"Update RH Fields on NISS: {result}")

logging.info(f"<== End of Script ==>")