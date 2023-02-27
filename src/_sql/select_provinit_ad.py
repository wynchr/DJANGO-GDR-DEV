"""
====================================================================================================
.DESCRIPTION
    select data from REFID_IOP_PROVINIT_AD

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		19/01/2023  CWY Initial Version

====================================================================================================
"""
import pprint
import time
from utils import utils, db

WAIT = 2

title = 'REFID_IOP_PROVINIT_AD'
while True:
    options = ["Create DATASET",
               "PPrint DATASET",
               "Convert DATASET in DICT users",
               "PPrint DICT users",
               "Print DICT users",
               "Print DICT specific user",
               "Exit"]
    res = utils.let_user_pick(title, options)
    if options[res] == "Exit":
        break
    choice = options[res]
    print(f"\n{choice}")

    # ==== Create DATASET ====
    if choice == "Create DATASET":
        sql = """
        select * from SA.REFID_IOP_PROVINIT_AD
        """
        dataset = db.exec_sql('ITDEV', sql)
        print(f"\n{len(dataset)} rows")

    # ==== PPrint Dataset ====
    if choice == "PPrint DATASET":
        pprint.pprint(dataset)

    # ==== Convert DATASET in DICT users ====
    if choice == "Convert DATASET in DICT users":
        users = db.convert_dataset_to_dict(dataset, 'SAMACCOUNTNAME')
        print("Done")

    # ==== PPrint Dataset ====
    if choice == "Print Dataset":
        pprint.pprint(users)

    # ==== Print DICT users ====
    if choice == "Print DICT users":
        db.print_dict(users)

    # ==== Print DICT users ====
    if choice == "Print DICT specific user":
        userid = input("Enter UserId: ")
        userid = userid.upper()
        userid = 'WYNCHR' if userid == '' else userid

        print(f"\n--- USERID: {userid} ---")
        pprint.pprint(users[userid])

        print(f"\nSAMACCOUNTNAME:{users[userid]['SAMACCOUNTNAME']}")
        print(f"SN: {users[userid]['SN']}")
        print(f"GIVENNAME: {users[userid]['GIVENNAME']}")
        print(f"GENDER:{users[userid]['GENDER']}")
        print(f"BIRTHDATE:{users[userid]['BIRTHDATE'][:10]}")

    time.sleep(WAIT)
