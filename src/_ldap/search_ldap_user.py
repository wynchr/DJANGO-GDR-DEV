"""
====================================================================================================
.DESCRIPTION
    Test LDAP Search

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		30/03/2022  CWY Initial Version

====================================================================================================
"""
# import pprint
from utils import ldap, utils
import time

WAIT = 2

ldapdb = 'OSIRIS-PROD'
userid = 'wynchr'
user_search = 'z*'
name = 'Wyns'

titre = "search ldap users"

while True:
    options = ["exec_ldap_query", "search_ldap_exists_userid", "search_ldap_by_userid", "search_ldap_by_name", "Exit"]
    res = utils.let_user_pick(titre, options)
    if options[res] == "Exit":
        break
    choice = options[res]
    print(choice)

    # ==== exec_ldap_query====
    if choice == "exec_ldap_query":
        query = "(&(samAccountName=" + user_search.upper() + "))"
        # query = "(&(employeeID=*)(businessCategory=*))"
        print(f"===== ldap_query: {query} =====")

        users = ldap.exec_ldap_query('OSIRIS-PROD', query)
        # pprint.pprint(users)

        i = 0
        for user in users['entries']:
            i += 1
            ldap.print_ldap_user(user['attributes'])
        print(f"\nNumbers of entries: {i}")

    # ==== search_ldap_exists_userid ====
    if choice == "search_ldap_exists_userid":
        user_exists = ldap.search_ldap_exists_userid(ldapdb, userid)
        print(f"\nUser {userid.upper()} exists : {user_exists}")

    # ==== search_ldap_by_userid====
    if choice == "search_ldap_by_userid":
        ldapuser = ldap.search_ldap_by_userid(ldapdb, userid)
        if ldapuser:
            # pprint.pprint(ldapuser)
            ldap.print_ldap_user(ldapuser)

    # ==== search_ldap_by_name====
    if choice == "search_ldap_by_name":
        ldapuser = ldap.search_ldap_by_name(ldapdb, name)
        if ldapuser:
            # pprint.pprint(ldapuser)
            ldap.print_ldap_user(ldapuser)

    time.sleep(WAIT)
# ___EOF___
