"""
=======================================================================================================================
.DESCRIPTION
    LDAP Function for Project

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	12/01/2023  CWY	Initial Version

.COMMENTS
    .
=======================================================================================================================
"""
import os
import pprint

from ldap3 import Server, Connection, SUBTREE, ALL_ATTRIBUTES, ALL, MODIFY_REPLACE, MODIFY_ADD
import json
import time
import utils

from config.config import Config

CUR_DIR = os.path.dirname(__file__)
config_start = Config(ENV="development")

WAIT = 2

LDAP_ATTRIBUTES_OSIRIS = ['sAMAccountName',
                           'sn',
                           'givenName',
                           'company',
                           'physicalDeliveryOfficeName',
                           'BusinessCategory',
                           'employeeType',
                           'department',
                           'preferredLanguage',
                           'employeeNumber',
                           'extensionAttribute1',
                           'extensionAttribute2',
                           'extensionAttribute10',
                           'extensionAttribute11',
                           'telephoneNumber',
                           'pager',
                           'description',
                           'accountExpires',
                           'enabled',
                           'name',
                           'cn',
                           'userPrincipalName',
                           'displayName',
                           'employeeID',
                           'info',
                           'extensionAttribute15',
                           'extensionAttribute3',
                           'homeDirectory',
                           'homeDrive',
                           'distinguishedName',
                           'objectGUID',
                           'objectSid',
                           'whenCreated',
                           'whenchanged',
                           'LastLogonTimeStamp',
                           'LastLogon',
                           'pwdLastSet',
                           'badPasswordTime',
                           'userAccountControl',
                           'mail',
                           'msExchWhenMailboxCreated',
                           'memberOf']

LDAP_ATTRIBUTES_EVIDIAN = ["cn",
                            "STPADlogin",
                            "employeeID",
                            "STPNISS",
                            "STPINAMINUMBER",
                            "sn",
                            "givenname",
                            "osiris-evidian-sex",
                            "STPBirthDate",
                            "preferredLanguage",
                            "businessCategory",
                            "company",
                            "physicalDeliveryOfficeName",
                            "employeeType",
                            "osiris-hr-contractstatus",
                            "osiris-hr-contractstartdate",
                            "osiris-hr-contractenddate",
                            "CHUIdOriginSource",
                            "distinguishedName",
                            "evdidmUserIdRep",
                            "evdidmState",
                            "evdpmSchedulerStatus",
                            "whenCreated",
                            "whenChanged",
                            "enatelBeginTime",
                            "enatelEndTime"]

# ===== init ldap params =====


def init_ldapdb():
    params = {}
    params['LDAP_HOST'] = config_start.get_ldap_param()['HOST']
    params['LDAP_USER'] = config_start.get_ldap_param()['USER']
    params['LDAP_PWD'] = config_start.get_ldap_param()['PWD']

    # print(f"LDAP_HOST : {params['LDAP_HOST']}")
    # print(f"LDAP_USER : {params['LDAP_USER']}")
    # print(f"LDAP_PWD : {params['LDAP_PWD']}")

    return params


# ===== connect to the db =====


def connect_ldap(params):
    LDAP_HOST = params.get('LDAP_HOST')
    LDAP_USER = params.get('LDAP_USER')
    LDAP_PWD = params.get('LDAP_PWD')

    cnxldap = Connection(Server(LDAP_HOST),
                         user=LDAP_USER,
                         password=LDAP_PWD,
                         auto_bind=True,
                         read_only=True
                         )
    return cnxldap


# paged search wrapped in a generator

def exec_ldap_search_paged(ldapdb, query):
    params = init_ldapdb()

    cnxldap = Connection(Server(params.get('LDAP_HOST')),
                         user=params.get('LDAP_USER'),
                         password=params.get('LDAP_PWD'),
                         auto_bind=True,
                         read_only=True)

    if ldapdb == 'OSIRIS-TEST':
        LDAP_SEARCHBASE = 'OU=REFID,OU=Users,OU=TESTOSIRIS,DC=chu-brugmann,DC=be'

    if ldapdb == 'OSIRIS-PROD':
        LDAP_SEARCHBASE = 'OU=IAM,OU=Users,OU=OSIRIS,DC=chu-brugmann,DC=be'

    entry_list = cnxldap.extend.standard.paged_search(
        search_base=LDAP_SEARCHBASE,
        search_filter=query,
        search_scope=SUBTREE,
        # attributes=['cn', 'givenName'],
        attributes=LDAP_ATTRIBUTES_OSIRIS,
        paged_size=500,
        generator=False)

    return entry_list


def exec_ldap_search_paged_for_groups(ldapdb, query):
    params = init_ldapdb()

    cnxldap = Connection(Server(params.get('LDAP_HOST')),
                         user=params.get('LDAP_USER'),
                         password=params.get('LDAP_PWD'),
                         auto_bind=True,
                         read_only=True)

    if ldapdb == 'OSIRIS-TEST':
        LDAP_SEARCHBASE = 'OU=REFID,OU=Users,OU=TESTOSIRIS,DC=chu-brugmann,DC=be'

    if ldapdb == 'OSIRIS-PROD':
        LDAP_SEARCHBASE = 'OU=IAM,OU=Users,OU=OSIRIS,DC=chu-brugmann,DC=be'

    entry_list = cnxldap.extend.standard.paged_search(
        search_base=LDAP_SEARCHBASE,
        search_filter=query,
        search_scope=SUBTREE,
        attributes=['sAMAccountName', 'memberOf'],
        # attributes=LDAP_ATTRIBUTES_OSIRIS,
        paged_size=500,
        generator=False)

    return entry_list


def exec_ldap_search_evidian_paged(ldapsearchbase, filter):
    ldap_url = "LDAP://sp1121.chubxl.be:10389"
    username = "CN=iamadmin,OU=IAM Administrators,O=iam"
    password = "iamadmin0410"
    # ldapsearchbase = "CN=3c793374,OU=IAMIDENTITY,O=iam"
    SizeLimit = 15000
    PageSize = 100
    # filter = "(objectCategory=user)"
    # filter = "(&(STPADlogin=wynchr))"
    # filter = "(&(cn=OSIRIS-N6UAK5X))"

    cnxldap = Connection(Server(ldap_url),
                         user=username,
                         password=password,
                         auto_bind=True,
                         read_only=True)

    entry_list = cnxldap.extend.standard.paged_search(
        search_base=ldapsearchbase,
        search_filter=filter,
        search_scope=SUBTREE,
        attributes=LDAP_ATTRIBUTES_EVIDIAN,
        paged_size=PageSize,
        generator=False)

    return entry_list

# ===== exec ldap query =====


def exec_ldap_query(ldapdb, query):
    params = init_ldapdb()

    LDAP_HOST = params.get('LDAP_HOST')
    LDAP_USER = params.get('LDAP_USER')
    LDAP_PWD = params.get('LDAP_PWD')

    try:
        if ldapdb == 'OSIRIS-TEST':
            LDAP_SEARCHBASE = 'OU=REFID,OU=Users,OU=TESTOSIRIS,DC=chu-brugmann,DC=be'
        elif ldapdb == 'OSIRIS-PROD':
            LDAP_SEARCHBASE = 'OU=IAM,OU=Users,OU=OSIRIS,DC=chu-brugmann,DC=be'
        elif ldapdb == 'OSIRIS-ALL':
            LDAP_SEARCHBASE = 'DC=chu-brugmann,DC=be'
        elif ldapdb == 'DISTRIBUTION':
            LDAP_SEARCHBASE = 'OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be'
        elif ldapdb == 'APPLICATION':
            LDAP_SEARCHBASE = 'OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be'
        elif ldapdb == 'SECURITY':
            LDAP_SEARCHBASE = 'OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be'

        with Connection(Server(LDAP_HOST),
                        user=LDAP_USER,
                        password=LDAP_PWD,
                        auto_bind=True,
                        read_only=True) as cnxldap:

            cnxldap.search(
                search_base=LDAP_SEARCHBASE,
                # search_filter='(&(samAccountName=' + SAMACCOUNTNAME + '))',
                search_filter=query,
                search_scope=SUBTREE,
                # attributes='*',
                # attributes = ['cn', 'givenName']
                attributes=LDAP_ATTRIBUTES_OSIRIS
                # get_operational_attributes=True,
                # paged_size=None,
                # size_limit=2000
            )
    finally:
        pass

    response = cnxldap
    response_json = response.response_to_json()
    result = json.loads(response_json)

    return result


def exec_ldap_search_groups(grouptype):
    params = init_ldapdb()

    LDAP_HOST = params.get('LDAP_HOST')
    LDAP_USER = params.get('LDAP_USER')
    LDAP_PWD = params.get('LDAP_PWD')

    try:
        if grouptype == "PROD-DISTRIBUTION":
            LDAP_SEARCHBASE = 'OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be'
            # filter = "(&(objectClass=group)(info=IAM-DistributionGroup))"
            filter = "(&(objectClass=group)(extensionAttribute15=REFID-DistributionGroup))"
        elif grouptype == "PROD-APPLICATION":
            LDAP_SEARCHBASE = 'OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be'
            # filter = "(&(objectClass=group)(info=IAM-Application))"
            filter = "(&(objectClass=group)(extensionAttribute15=REFID-DistributionGroup))"
        if grouptype == "DEV-DISTRIBUTION":
            # LDAP_SEARCHBASE = 'OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be'
            LDAP_SEARCHBASE = 'OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be'
            filter = "(&(objectClass=group)(extensionAttribute15=REFID-DistributionGroup))"
        elif grouptype == "DEV-APPLICATION":
            # LDAP_SEARCHBASE = 'OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be'
            LDAP_SEARCHBASE = 'OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be'
            filter = "(&(objectClass=group)(extensionAttribute15=REFID-Application))"


        with Connection(Server(LDAP_HOST),
                        user=LDAP_USER,
                        password=LDAP_PWD,
                        auto_bind=True,
                        read_only=True) as cnxldap:

            cnxldap.search(
                search_base=LDAP_SEARCHBASE,
                search_filter=filter,
                search_scope=SUBTREE,
                attributes = [
                        'SamAccountName',
                        'DistinguishedName',
                        'mail',
                        'whenCreated',
                        'whenChanged',
                        'description',
                        'info',
                        'extensionAttribute15',
                        'ObjectGUID',
                        'ObjectSID',]
            )
    finally:
        pass

    response = cnxldap
    response_json = response.response_to_json()
    result = json.loads(response_json)

    return result


def search_ldap_exists_userid(ldapdb, userid):
    query = "(&(samAccountName=" + userid.upper() + "))"
    ldapuser = exec_ldap_query(ldapdb, query)
    if ldapuser['entries']:
        result = True
    else:
        result = False
    return result


def search_ldap_exists_employeenumber(ldapdb, employeenumber):
    query = "(&(employeenumber=" + employeenumber.upper() + "))"
    ldapuser = exec_ldap_query(ldapdb, query)
    if ldapuser['entries']:
        result = True
    else:
        result = False
    return result


def search_ldap_exists_employeenumberfor(ldapdb, employeenumber):
    query = "(&(employeenumber=" + employeenumber.upper() + "))"
    ldapuser = exec_ldap_query(ldapdb, query)
    if ldapuser['entries']:
        result = ldapuser['entries'][0]['attributes']['sAMAccountName']
    else:
        result = ""
    return result


def search_ldap_by_userid(ldapdb, userid):
    query = "(&(samAccountName=" + userid.upper() + "))"
    ldapuser = exec_ldap_query(ldapdb, query)
    if ldapuser['entries']:
        ldapuser = ldapuser['entries'][0]['attributes']
    else:
        ldapuser = None
    return ldapuser


def search_ldap_by_name(ldapdb, name):
    query = "(&(sn=" + name.upper() + "))"
    ldapuser = exec_ldap_query(ldapdb, query)
    if ldapuser['entries']:
        ldapuser = ldapuser['entries'][0]['attributes']
    else:
        ldapuser = None
    return ldapuser


def search_ldap_by_employeenumber(ldapdb, employeenumber):
    query = "(&(employeenumber=" + employeenumber.upper() + "))"
    ldapuser = exec_ldap_query(ldapdb, query)
    if ldapuser['entries']:
        ldapuser = ldapuser['entries'][0]['attributes']
    else:
        ldapuser = None
    return ldapuser


def search_ldap_group_by_userid(ldapdb, userid):
    # query = "(&(samAccountName=" + userid.upper() + ")(info=IAM-Application))"
    query = "(&(samAccountName=" + userid.upper() + "))"
    ldapuser = exec_ldap_query(ldapdb, query)
    if ldapuser['entries']:
        groups = ldapuser['entries'][0]['attributes']['memberOf']
        # for group in groups:
        #     print(group)
    else:
        groups = None

    return groups


def extract_samaccountname(dn):
    # dn = "CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be"
    samaccountname = dn.split(",")[0].replace('CN=','')
    return samaccountname

def print_ldap_user(user):
    print("\n")
    print(f"sAMAccountName: {user['sAMAccountName']}")
    print(f"cn: {user['cn']}")
    print(f"sn: {user['sn']}")
    print(f"givenName: {user['givenName']}")
    print(f"company: {user['company']}")
    print(f"physicalDeliveryOfficeName: {user['physicalDeliveryOfficeName']}")
    print(f"userPrincipalName: {user['userPrincipalName']}")
    print(f"info: {user['info']}")
    print(f"objectGUID: {user['objectGUID']}")
    print(f"objectSid: {user['objectSid']}")


# def update_attribute_in_groups(dn, attribute_dict):
def update_attribute_in_groups(dn, pinfo, pextensionAttribute15):
    params = init_ldapdb()

    LDAP_HOST = params.get('LDAP_HOST')
    LDAP_USER = params.get('LDAP_USER')
    LDAP_PWD = params.get('LDAP_PWD')

    # define the server
    s = Server(LDAP_HOST, get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

    # define the connection
    c = Connection(s, user=LDAP_USER, password=LDAP_PWD)
    c.bind()

    print(dn)

    # perform the Modify operation
    c.modify(dn,
             {'extensionAttribute15': [(MODIFY_REPLACE, [pextensionAttribute15])],
              'info': [(MODIFY_REPLACE, [pinfo])]})
    print(c.result)

    # close the connection
    c.unbind()

    return c.result


# Main =============================================================================================================
if __name__ == "__main__":

    ldapdb = 'OSIRIS-ALL'
    userid = 'wynchr'
    user_search = '*'
    name = 'Wyns'
    employeenumber = "00045678901"

    while True:
        options = ["exec_ldap_search_paged",
                   "exec_ldap_search_paged_for_groups",
                   "exec_ldap_search_evidian_paged",
                   "exec_ldap_query",
                   "search_ldap_exists_userid",
                   "search_ldap_exists_employeenumber",
                   "search_ldap_by_userid",
                   "search_ldap_by_name",
                   "search_ldap_by_employeenumber",
                   "search_ldap_group_by_userid",
                   "exec_ldap_search_groups",
                   "extract_samaccountname",
                   "update_attribute_in_groups",
                   "Exit"]
        res = utils.let_user_pick("ldap", options)
        if options[res] == "Exit":
            break
        choice = options[res]
        print(choice)

        # ==== exec_ldap_search_paged====
        if choice == "exec_ldap_search_paged":
            query = "(objectClass=user)"
            # query = "(&(employeeID=*)(businessCategory=*)(sAMAccountName=wynchr))"
            print(f"===== ldap_query: {query} =====")
            users = exec_ldap_search_paged('OSIRIS-PROD', query)

            for user in users:
                # print(user['attributes'])
                print(f" {user['attributes']['sAMAccountName']} : {user['attributes']['sn']}, {user['attributes']['givenName']} - {user['attributes']['extensionAttribute10']}")
                # print(f" {user['attributes']['sAMAccountName']} : {user['attributes']['sn']}, {user['attributes']['givenName']}")

            total_entries = len(users)
            print('Total entries retrieved:', total_entries)

        # ==== exec_ldap_search_paged for groups ====
        if choice == "exec_ldap_search_paged_for_groups":
            # query = "(objectClass=user)"
            query = "(&(employeeID=*)(businessCategory=*)(sAMAccountName=wynchr))"
            print(f"===== ldap_query: {query} =====")
            users = exec_ldap_search_paged_for_groups('OSIRIS-PROD', query)
            for user in users:
                # print(user['attributes'])
                print(f" {user['attributes']['sAMAccountName']} : {user['attributes']['memberOf']}")
                print(len(user['attributes']['memberOf']))
                for group in user['attributes']['memberOf']:
                    print(group)

            total_entries = len(users)
            print('Total entries retrieved:', total_entries)

        # ==== exec_ldap_search_groups====
        if choice == "exec_ldap_search_groups":

            # grouptype = "PROD-DISTRIBUTION"
            # grouptype = "PROD-APPLICATION"
            grouptype = "DEV-DISTRIBUTION"
            # grouptype = "DEV-APPLICATION"

            print(f"===== grouptype: {grouptype} =====")

            groups = exec_ldap_search_groups(grouptype)
            # pprint.pprint(groups)

            i = 0
            for group in groups['entries']:
                i += 1
                # print(group['attributes'])
                print(f"\n{i}")
                if "DISTRIBUTION" in grouptype:
                    print("Distribution")
                elif "APPLICATION" in grouptype:
                    print("Security")
                print(f"sAMAccountName: {str(group['attributes']['sAMAccountName'])}")
                print(f"DistinguishedName: {str(group['attributes']['distinguishedName'])}")
                print(f"mail: {str(group['attributes']['mail'])}")
                print(f"whenCreated: {str(group['attributes']['whenCreated'])}")
                print(f"whenChanged: {str(group['attributes']['whenChanged'])}")
                print(f"description: {str(group['attributes']['description'])}")
                print(f"info: {str(group['attributes']['info'])}")
                print(f"extensionAttribute15: {str(group['attributes']['extensionAttribute15'])}")
                print(f"objectGUID: {str(group['attributes']['objectGUID'])}")
                print(f"objectSid: {str(group['attributes']['objectSid'])}")



        # ==== exec_ldap_search_evidian_paged====
        if choice == "exec_ldap_search_evidian_paged":
            ldapsearchbase = "CN=3c793374,OU=IAMIDENTITY,O=iam"
            # Filter = "(objectCategory=user)"
            # Filter = "(&(STPADlogin=wynchr))"
            Filter = "(&(cn=OSIRIS-N6UAK5X))"
            users = exec_ldap_search_evidian_paged(ldapsearchbase, Filter)

            for user in users:
                pprint.pprint(user['attributes'])

            total_entries = len(users)
            print('Total entries retrieved:', total_entries)

        # ==== exec_ldap_query====
        if choice == "exec_ldap_query":
            query = "(&(samAccountName=" + user_search.upper() + "))"
            # query = "(&(employeeID=*)(businessCategory=*))"
            print(f"===== ldap_query: {query} =====")

            users = exec_ldap_query('OSIRIS-PROD', query)
            # pprint.pprint(users)

            i = 0
            for user in users['entries']:
                i += 1
                print_ldap_user(user['attributes'])
            print(f"\nNumbers of entries: {i}")

        # ==== search_ldap_exists_employeenumber ====
        if choice == "search_ldap_exists_employeenumber":
            employeenumber_exists = search_ldap_exists_employeenumber(ldapdb, employeenumber)
            print(f"\nUser {employeenumber.upper()} exists : {employeenumber_exists}")

        # ==== search_ldap_exists_userid ====
        if choice == "search_ldap_exists_userid":
            user_exists = search_ldap_exists_userid(ldapdb, userid)
            print(f"\nUser {userid.upper()} exists : {user_exists}")

        # ==== search_ldap_by_userid====
        if choice == "search_ldap_by_userid":
            ldapuser = search_ldap_by_userid(ldapdb, userid)
            if ldapuser:
                # pprint.pprint(ldapuser)
                print_ldap_user(ldapuser)

        # ==== search_ldap_by_name====
        if choice == "search_ldap_by_name":
            ldapuser = search_ldap_by_name(ldapdb, name)
            if ldapuser:
                # pprint.pprint(ldapuser)
                print_ldap_user(ldapuser)

        # ==== search_ldap_by_employeenumber====
        if choice == "search_ldap_by_employeenumber":
            ldapuser = search_ldap_by_employeenumber(ldapdb, employeenumber)
            if ldapuser:
                # pprint.pprint(ldapuser)
                print_ldap_user(ldapuser)

        # ==== search_ldap_by_userid====
        if choice == "search_ldap_group_by_userid":
            groups = search_ldap_group_by_userid(ldapdb, userid)
            if groups:
                for group in groups:
                    if "OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be" in group:
                        grouptype = "Distribution"
                    elif "OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be" in group:
                        grouptype = "Applications"
                    elif "OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be" in group:
                        grouptype = "Security"
                    else:
                        grouptype = "Other"

                    print(f"{ldapdb} - {grouptype} - {group}")

        # ==== search_ldap_by_userid====
        if choice == "extract_samaccountname":
            dn = "CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be"
            print(extract_samaccountname(dn))

        # ==== update_attribute_in_groups====
        if choice == "update_attribute_in_groups":
            result = update_attribute_in_groups('CN=OSIRIS - MVSL - Medical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=OSIRIS - MVSL - Nursing,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=OSIRIS - MVSL - Paramedical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=Tous les medecins de Brien,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=Tous les medecins de Brugmann,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=Tous les medecins de Horta,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=Tous les medecins de l Huderf,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-DistributionGroup','REFID-DistributionGroup')
            result = update_attribute_in_groups('CN=Tout le PATO de Brien,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-DistributionGroup','REFID-DistributionGroup')
            result = update_attribute_in_groups('CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-DistributionGroup','REFID-DistributionGroup')
            result = update_attribute_in_groups('CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-DistributionGroup','REFID-DistributionGroup')
            result = update_attribute_in_groups('CN=Tout le PATO de l Huderf,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-DistributionGroup','REFID-DistributionGroup')
            result = update_attribute_in_groups('CN=Tout le nursing de Brien,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=Tout le nursing de Horta,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=Tout le nursing de Reine Astrid,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=Tout le nursing de l Huderf,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')
            result = update_attribute_in_groups('CN=Wireless Users,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be','IAM-Application','REFID-Application')

            print(result)


        time.sleep(WAIT)

    # ___EOF___

    # Ex. USERID = wynchr

    # DISTRIBUTION : info=IAM-DistributionGroup
    # --------------------------------------------------------------------------
    # CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be

    # APPLICATIONS : info=IAM-Application
    # --------------------------------------------------------------------------
    # CN=informatique_all,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=Brugmann - SharePoint - Admins,OU=SharePoint,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=Brugmann - MonitorNow - Users,OU=MonitorNow,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - MVSL - Informatique Admin,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Evidian - All Users,OU=Evidian,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Sophos - OTHERS Users,OU=Sophos,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Sophos - IT Users,OU=Sophos,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Office 365 - Licensed TEST Users,OU=Office 365,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Enterprise Architect - Respository,OU=Sparx Enterprise Architect,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Interoperability - Srv Local Admin,OU=Interoperability,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=Osiris - ServiceDesk - IT Interoperability,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Office 365 - Population RH,OU=Office 365,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Lansweeper - Service Desk Agent,OU=Lansweeper,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Lansweeper Test - Service Desk Agent,OU=Lansweeper,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=Osiris - Informatique - Sharepoint Admin,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be

    # SECURITY : OU = Security, OU = Groups, OU = OSIRIS, DC = chu - brugmann, DC = be
    # --------------------------------------------------------------------------
    # CN=Developement,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=DWH Brugmann - RW,OU=ACL,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=Tous les Cadres BRUGMANN,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=IAM - RW,OU=ACL,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Phone Application - USERS,OU=LDAPCleaning,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=DWH IT - RW,OU=ACL,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - FGP - Individual Users,OU=Fine-Grained Password,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=ParamConnect - Managers,OU=ACL,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=ParamConnect - RW,OU=ACL,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=OSIRIS - Team - Solution Factory,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be

    # AUTRES
    # ------
    # CN=Exchange View-Only Administrators,OU=Microsoft Exchange Security Groups,DC=chu-brugmann,DC=be
    # CN=Informatique,OU=IT,OU=Users,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=Informatique - Helpdesk,OU=IT,OU=Users,OU=OSIRIS,DC=chu-brugmann,DC=be
    # CN=Brugmann - Informatique,OU=IT,OU=Users,OU=OSIRIS,DC=chu-brugmann,DC=be
