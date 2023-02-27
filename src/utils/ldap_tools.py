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
from ldap3 import Server, Connection, ALL, SUBTREE, MODIFY_REPLACE, MODIFY_ADD
import json
import time
import utils

from config.config import Config

CUR_DIR = os.path.dirname(__file__)
# config_start = Config(ENV="development")
config_start = Config(ENV="production")

WAIT = 2


# Define Class Ldap Client


class LDAPClient:
    def __init__(self, server, base_dn, username, password, page_size=100):
        self.server = Server(server)
        self.connection = Connection(self.server, user=username, password=password, auto_bind=True)
        self.base_dn = base_dn
        self.page_size = page_size

    def search(self, search_filter, attributes):
        self.connection.search(search_base=self.base_dn,
                               search_filter=search_filter,
                               attributes=attributes,
                               size_limit=1)
        return self.connection.response

    def add(self, dn, attributes):
        self.connection.add(dn, attributes)
        return self.connection.result

    def update(self, dn, attribute, value, operation=MODIFY_REPLACE):
        self.connection.modify(dn, {attribute: [(operation, [value])]})
        return self.connection.result

    def delete(self, dn):
        self.connection.delete(dn)
        return self.connection.result

    # New

    def list(self, search_filter, attributes, size_limit):
        self.connection.search(search_base=self.base_dn,
                               search_filter=search_filter,
                               search_scope=SUBTREE,
                               attributes=attributes,
                               size_limit=size_limit)

        return self.connection.response

    def get_entries(self, search_filter, page_size=100):
        results = []
        cookie = None
        self.connection.bind()
        n = 0
        while True:
            n += 1
            self.connection.search(search_base=self.base_dn,
                                   search_filter=search_filter,
                                   search_scope=0,
                                   # paged_size=self.page_size,
                                   paged_size=page_size,
                                   paged_cookie=cookie)
            results += self.connection.entries
            # print(f"results {n} {results}")
            print(f"results {n} ")
            cookie = self.connection.result.get('paged_cookie', None)
            if cookie is None:
                break
        return results

    # Specific


# Main =============================================================================================================
if __name__ == "__main__":

    ldap_client = LDAPClient(config_start.get_ldap_param()['HOST'],
                             config_start.get_ldap_param()['BASEDN'],
                             config_start.get_ldap_param()['USER'],
                             config_start.get_ldap_param()['PWD'])

    userid = 'wynchr'
    user_search = 'z*'
    name = 'Wyns'

    LDAP_ATTRIBUTES = ['objectGUID',
                       'objectSID',
                       'distinguishedName',
                       'sAMAccountName',
                       'sn',
                       'givenName',
                       'cn',
                       'name',
                       'displayName',
                       'userPrincipalName',
                       'extensionAttribute1',
                       'extensionAttribute2',
                       'extensionAttribute10',
                       'extensionAttribute11',
                       'employeeID',
                       'employeeNumber',
                       'preferredLanguage',
                       'company',
                       'physicalDeliveryOfficeName',
                       'employeeType',
                       'BusinessCategory',
                       'department',
                       'telephoneNumber',
                       'pager',
                       'info',
                       'mail',
                       'homeDirectory',
                       'homeDrive',
                       'msExchWhenMailboxCreated',
                       'whenCreated',
                       'whenchanged',
                       'LastLogon',
                       'LastLogonTimeStamp',
                       'pwdLastSet',
                       'accountExpires',
                       'description',
                       'enabled',
                       'MemberOf']

    while True:
        options = ["Create",
                   "Read",
                   "Update",
                   "Delete",
                   "List",
                   "get_entries",
                   "Exit"]
        res = utils.let_user_pick("ldap", options)
        if options[res] == "Exit":
            break
        choice = options[res]
        print(choice)

        # === Create ===
        if choice == "Create":
            attributes = {
                "objectClass": ["top", "person", "organizationalPerson", "inetOrgPerson"],
                "cn": ["ZZDEV Test"],
                "sn": ["ZZDEV"],
                "sAMAccountName": ["ZZDEVTE"],
                "mail": ["init.zzdev@example.com"]
            }
            result = ldap_client.add("CN=ZZDEV Test,OU=REFID,OU=Users,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", attributes)
            if result["result"] == 0:
                print("Create successful")
            else:
                print("Create failed")

        # === Read ===
        if choice == "Read":
            user = ldap_client.search("(sAMAccountName=ZZDEVIN)",
                                      ["distinguishedName", "sAMAccountName", "cn", "sn", "mail"])
            if user:
                print(user[0]["attributes"])
            else:
                print("User not found")

        # === Update ===
        if choice == "Update":
            # result = ldap_client.update("CN=ZZDEV Init,OU=REFID,OU=Users,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "mail", "johndoe@example.com")
            result = ldap_client.update("CN=ZZDEV Init,OU=REFID,OU=Users,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "mail",
                                        "johndoe2@example.com")
            if result["result"] == 0:
                print("Update successful")
            else:
                print("Update failed")

        # === Delete ===
        if choice == "Delete":
            result = ldap_client.delete("CN=ZZDEV Init,OU=REFID,OU=Users,OU=TESTOSIRIS,DC=chu-brugmann,DC=be")
            if result["result"] == 0:
                print("Delete successful")
            else:
                print("Delete failed")

        # === List ===
        if choice == "List":
            # entries = ldap_client.list("(objectClass=*)", ["dn", "cn", "sn", "mail"], 100)
            # entries = ldap_client.list("(&(employeeID=*)(businessCategory=*))", ["sAMAccountName", "cn", "sn", "mail"], 100)
            entries = ldap_client.list("(&(employeeID=*)(businessCategory=*))", LDAP_ATTRIBUTES, 2000)

            i = 0
            for entry in entries:
                i += 1
                print(entry)
            print(i)

        # === get_entries ===
        if choice == "get_entries":
            entries = ldap_client.get_entries('(objectClass=*)', 100)

            # i = 0
            # for entry in entries:
            #     i += 1
            #     print(f"entry {i} {entry}")
            # print(i)

        time.sleep(WAIT)

    # ___EOF___
