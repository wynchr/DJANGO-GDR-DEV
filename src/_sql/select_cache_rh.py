"""
====================================================================================================
.DESCRIPTION
    select data from REFID_IOP_CACHE_RH

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

title = 'REFID_IOP_CACHE_RH'
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
        select * from SA.REFID_IOP_CACHE_RH
        """
        dataset = db.exec_sql('ITDEV', sql)
        print(f"\n{len(dataset)} rows")

    # ==== PPrint Dataset ====
    if choice == "PPrint DATASET":
        pprint.pprint(dataset)

    # ==== Convert DATASET in DICT users ====
    if choice == "Convert DATASET in DICT users":
        users = db.convert_dataset_to_dict(dataset, 'V100_RH_MATRICULE')
        print("Done")

    # ==== PPrint Dataset ====
    if choice == "PPrint DICT users":
        pprint.pprint(users)

    # ==== Print DICT users ====
    if choice == "Print DICT users":
        db.print_dict(users)

    # ==== Print DICT users ====
    if choice == "Print DICT specific user":
        userid = input("Enter Matricule: ")
        userid = userid.upper()
        userid = '0631049' if userid == '' else userid

        print(f"\n--- MATRICULE: {userid} ---")
        pprint.pprint(users[userid])

        print(f"\nV100_RH_MATRICULE: {users[userid]['V100_RH_MATRICULE']}")
        print(f"V100_RH_NOM: {users[userid]['V100_RH_NOM']}")
        print(f"V100_RH_PRENOM: {users[userid]['V100_RH_PRENOM']}")
        print(f"V100_RH_PRENOM: {users[userid]['V100_RH_SEXE']}")
        print(f"V100_RH_DATE_NAISSANCE: {users[userid]['V100_RH_DATE_NAISSANCE'][:10]}")

    time.sleep(WAIT)

