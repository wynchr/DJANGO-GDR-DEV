"""
=======================================================================================================================
.DESCRIPTION
    Gestion des règles d'attribution de groupes sur base de metadata

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	22/02/2023  CWY	Initial Version

.COMMENTS
    brintratest.chu-brugmann.be/Intranet/refidv1/scripts/generation_rule.php

.DESCRIPTION

    -- Generate Groups and DistibutionList

    SELECT 	rir.GROUPCATEGORY ,
            rira.INSTITUTION ,
            CASE
                WHEN rira.SITE IS NULL THEN '-'
                ELSE rira.SITE END AS SITE,
            rira.EMPLOYEETYPE,
            rir.SAMACCOUNTNAME ,
            rir.DISTINGUISHEDNAME
    FROM REFID_IOP_RULE_ATTRIBUTION_WITH_KEY rira
    LEFT JOIN REFID_IOP_REFADGROUPS rir ON rira.ID_groupe = rir.ID
    WHERE rir.DISTINGUISHEDNAME IS NOT NULL
    --AND upper(rira.INSTITUTION) = upper('huderf')
    --AND upper(rira.SITE) = upper('')
    --AND upper(rira.EMPLOYEETYPE) = upper('medical')
    --AND upper(rira.ca) = upper('')
    ORDER BY 1,2,3,4,5


    GROUPCATEGORY|INSTITUTION |SITE  |EMPLOYEETYPE |SAMACCOUNTNAME                 |DISTINGUISHEDNAME
    -------------+------------+------+-------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------
    Distribution |CHU-BRUGMANN|ASTRID|ADMINISTRATIF|Tout le PATO de Reine Astrid   |CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Distribution |CHU-BRUGMANN|ASTRID|OTHER        |Tout le PATO de Reine Astrid   |CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Distribution |CHU-BRUGMANN|ASTRID|PARAMEDICAL  |Tout le PATO de Reine Astrid   |CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Distribution |CHU-BRUGMANN|ASTRID|TECHNIQUE    |Tout le PATO de Reine Astrid   |CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Distribution |CHU-BRUGMANN|BRIEN |ADMINISTRATIF|Tout le PATO de Brien          |CN=Tout le PATO de Brien,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Distribution |CHU-BRUGMANN|BRIEN |OTHER        |Tout le PATO de Brien          |CN=Tout le PATO de Brien,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Distribution |CHU-BRUGMANN|BRIEN |PARAMEDICAL  |Tout le PATO de Brien          |CN=Tout le PATO de Brien,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Distribution |CHU-BRUGMANN|BRIEN |TECHNIQUE    |Tout le PATO de Brien          |CN=Tout le PATO de Brien,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|-     |MEDICAL      |OSIRIS - MVSL - Medical        |CN=OSIRIS - MVSL - Medical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|-     |MEDICAL      |Tous les medecins de Brugmann  |CN=Tous les medecins de Brugmann,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|-     |MEDICAL      |Wireless Users                 |CN=Wireless Users,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|-     |NURSING      |OSIRIS - MVSL - Nursing        |CN=OSIRIS - MVSL - Nursing,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|-     |PARAMEDICAL  |OSIRIS - MVSL - Paramedical    |CN=OSIRIS - MVSL - Paramedical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|ASTRID|MEDICAL      |Tous les medecins de Brugmann  |CN=Tous les medecins de Brugmann,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|ASTRID|MEDICAL      |Tout le nursing de Reine Astrid|CN=Tout le nursing de Reine Astrid,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|ASTRID|NURSING      |Tout le nursing de Reine Astrid|CN=Tout le nursing de Reine Astrid,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|BRIEN |MEDICAL      |Tous les medecins de Brien     |CN=Tous les medecins de Brien,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|BRIEN |NURSING      |Tout le nursing de Brien       |CN=Tout le nursing de Brien,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|HORTA |ADMINISTRATIF|Tout le PATO de Horta          |CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|HORTA |MEDICAL      |Tous les medecins de Horta     |CN=Tous les medecins de Horta,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|HORTA |NURSING      |Tout le nursing de Horta       |CN=Tout le nursing de Horta,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|HORTA |OTHER        |Tout le PATO de Horta          |CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|HORTA |PARAMEDICAL  |Tout le PATO de Horta          |CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |CHU-BRUGMANN|HORTA |TECHNIQUE    |Tout le PATO de Horta          |CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |ADMINISTRATIF|Tout le PATO de l Huderf       |CN=Tout le PATO de l Huderf,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |MEDICAL      |OSIRIS - MVSL - Medical        |CN=OSIRIS - MVSL - Medical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |MEDICAL      |Tous les medecins de l Huderf  |CN=Tous les medecins de l Huderf,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |MEDICAL      |Wireless Users                 |CN=Wireless Users,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |NURSING      |OSIRIS - MVSL - Nursing        |CN=OSIRIS - MVSL - Nursing,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |NURSING      |Tout le nursing de l Huderf    |CN=Tout le nursing de l Huderf,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |OTHER        |Tout le PATO de l Huderf       |CN=Tout le PATO de l Huderf,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |PARAMEDICAL  |OSIRIS - MVSL - Paramedical    |CN=OSIRIS - MVSL - Paramedical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |PARAMEDICAL  |Tout le PATO de l Huderf       |CN=Tout le PATO de l Huderf,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    Security     |HUDERF      |-     |TECHNIQUE    |Tout le PATO de l Huderf       |CN=Tout le PATO de l Huderf,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be

=======================================================================================================================
"""
import time
import ldap
import utils
from database_tools import OracleConnexion

oracle_IT = OracleConnexion("DB-IT")

WAIT = 2


class GenGroupsByRules:

    @classmethod
    def find_rule_by_key(cls, institution, site="", employetype="", ca=""):
        try:
            if site != "":
                site = f"and  upper(rira.SITE) = upper('{site}')"

            if ca != "":
                ca = f" and  upper(rira.ca) = upper('{ca}')"

            sql_query = f"""
                        SELECT rir.DISTINGUISHEDNAME 
                        FROM REFID_IOP_RULE_ATTRIBUTION_WITH_KEY rira
                        LEFT JOIN REFID_IOP_REFADGROUPS rir ON rira.ID_groupe = rir.ID
                        WHERE rir.DISTINGUISHEDNAME IS NOT null
                        AND upper(rira.INSTITUTION) = upper('{institution}')
                        AND upper(rira.EMPLOYEETYPE) = upper('{employetype}')            
                        {site}
                        {ca} 
            """

            # print(sql_query)
            oracle_connected = oracle_IT.connection
            cursor = oracle_connected.cursor()
            cursor.execute(sql_query)
            list_of_groupe = []
            for groupe in cursor:
                list_of_groupe.append(groupe[0])
            cursor.close()
            return list_of_groupe

            # dataset = oracle_IT.fetch_data_from_db(sql_query)
            # return dataset

        except Exception as e:
            return {"message": "An internal error occurred {}".format(e)}


def update_ldap_user_groups(userid, company, physicaldeliveryofficename, employeetype):
    if physicaldeliveryofficename is None:
        physicaldeliveryofficename = ''
    if company.upper() == 'HUDERF':
        physicaldeliveryofficename = ''

    print(f"\nuserid : {userid}")
    print(f"company : {company}")
    print(f"physicaldeliveryofficename : {physicaldeliveryofficename}")
    print(f"employeetype : {employeetype}\n")

    groups = GenGroupsByRules.find_rule_by_key(company, physicaldeliveryofficename, employeetype)

    ALLDISTRIBUTIONLIST = ""
    ALLGROUPS = ""
    for group in groups:
        print(group)
        if "OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be" in group:
            ALLDISTRIBUTIONLIST += ldap.extract_samaccountname(group) + ';'
        elif "OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be" in group:
            ALLGROUPS += ldap.extract_samaccountname(group) + ';'
        elif "OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be" in group:
            ALLGROUPS += ldap.extract_samaccountname(group) + ';'
        else:
            ALLGROUPS += ldap.extract_samaccountname(group) + ';'

    # GROUPS
    sql_query = f"""
        UPDATE SA.REFID_IOP_PROV_AD SET GROUPS = '{ALLGROUPS}'
        WHERE SAMACCOUNTNAME = '{userid}'
        """
    print(sql_query)
    result = oracle_IT.exec_ddl_sql(sql_query)
    print(result)

    #  DISTRIBUTIONLIST
    sql_query = f"""
        UPDATE SA.REFID_IOP_PROV_AD SET DISTRIBUTIONLIST = '{ALLDISTRIBUTIONLIST}'
        WHERE SAMACCOUNTNAME = '{userid}'
        """
    print(sql_query)
    result = oracle_IT.exec_ddl_sql(sql_query)
    print(result)

    return result


if __name__ == '__main__':

    while True:
        options = ["print test",
                   "update_ldap_groups",
                   "Exit"]
        res = utils.let_user_pick("ldap", options)
        if options[res] == "Exit":
            break
        choice = options[res]
        print(choice)

        # ==== update_ldap_groups(company, physicaldeliveryofficename, employeetype):====
        if choice == "print test":
            print(f"['CHU-BRUGMANN','','MEDICAL'] => {GenGroupsByRules.find_rule_by_key('CHU-BRUGMANN', '', 'MEDICAL')}")
            print(f"['huderf','','medical'] => {GenGroupsByRules.find_rule_by_key('huderf', '', 'medical')}")
            print(f"['huderf','','Nursing'] => {GenGroupsByRules.find_rule_by_key('huderf', '', 'Nursing')}")

        # ==== update_ldap_user_groups(company, physicaldeliveryofficename, employeetype):====
        if choice == "update_ldap_user_groups":
            userid = 'ZZDEVIN'
            company = "Huderf"
            physicaldeliveryofficename = ""
            employeetype = "Paramedical"
            groups = update_ldap_user_groups(userid, company, physicaldeliveryofficename, employeetype)


        time.sleep(WAIT)

    # ___EOF___
