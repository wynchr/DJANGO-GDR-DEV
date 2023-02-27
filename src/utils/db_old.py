"""
=======================================================================================================================
.DESCRIPTION
    DB Function for Project

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	12/01/2023  CWY	Initial Version

.COMMENTS
    .
=======================================================================================================================
"""
from pathlib import Path
import pprint
import environ
import oracledb
import time

import utils

WAIT = 2


# ===== init db params =====


def init_db(db):
    # Retrive BASEDIR
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    # print(f"BASE_DIR : {BASE_DIR}")
    # import ENVIRONMENT settings
    env = environ.Env()
    environ.Env.read_env(env_file=str(BASE_DIR / "src" / "GDR" / ".env"))

    params = {}
    if db == 'ITDEV':
        params['DB_DSN'] = env("DB_HOST") + "/" + env("DB_SERVICE_NAME")
        params['DB_ENCODING'] = env("DB_ENCODING")
        params['DB_USER'] = env("DB_USER")
        params['DB_PASSWORD'] = env("DB_PASSWORD")

    if db == 'ITPROD':
        params['DB_DSN'] = env("DB_HOST") + "/" + env("DB_SERVICE_NAME")
        params['DB_ENCODING'] = env("DB_ENCODING")
        params['DB_USER'] = env("DB_USER")
        params['DB_PASSWORD'] = env("DB_PASSWORD")

    return params


# ===== connect to the db =====


def connect_db(db):
    params = init_db(db)

    DB_DSN = params.get('DB_DSN')
    DB_ENCODING = params.get('DB_ENCODING')
    DB_USER = params.get('DB_USER')
    DB_PASSWORD = params.get('DB_PASSWORD')

    # print(f"DB_DSN : {DB_DSN}")
    # print(f"DB_ENCODING : {DB_ENCODING}")
    # print(f"DB_USER : {DB_USER}")
    # print(f"DB_PASSWORD : {DB_PASSWORD}")

    oracledb.init_oracle_client()
    cnxdb = oracledb.connect(dsn=DB_DSN,
                             encoding=DB_ENCODING,
                             user=DB_USER,
                             password=DB_PASSWORD)
    # print(f"cnx : {cnx}")
    return cnxdb


# ===== exec sql =====


def exec_sql(db, sql_query):
    try:
        cnxdb = connect_db(db)
        cursor = cnxdb.cursor()
        cursor.execute(sql_query)
        columns = [col[0] for col in cursor.description]
        dataset = [dict(zip(columns, row)) for row in cursor.fetchall()]
    finally:
        cursor.close()
        cnxdb.close()
    return dataset


# ===== exec UPDATE sql =====


def exec_update_sql(db, sql_query):
    try:
        cnxdb = connect_db(db)
        cursor = cnxdb.cursor()
        cursor.execute(sql_query)
        cnxdb.commit()
    finally:
        cursor.close()
        cnxdb.close()
    return True


# ===== exec DDL sql =====


def exec_ddl_sql(db, sql_query):
    try:
        cnxdb = connect_db(db)
        cursor = cnxdb.cursor()
        cursor.execute(sql_query)
        cnxdb.commit()
    finally:
        cursor.close()
        cnxdb.close()
    return True


def convert_dataset_to_dict(dataset, key):
    dict = {}
    for data in dataset:
        dict[data[key]] = data
    return dict


def print_dict(my_dict):
    for id, info in my_dict.items():
        print("\nKey:", id)
        for key in info:
            print(key + ':', info[key])


# Main =============================================================================================================
if __name__ == "__main__":

    userid = "WYNCHR"

    while True:
        options = ["REFID_IOP_CACHE_AD_OSIRIS", "REFID_IOP_CACHE_EVIDIAN", "Exit"]
        res = utils.let_user_pick("db", options)
        if options[res] == "Exit":
            break
        choice = options[res]
        print(choice)

        # ==== REFID_IOP_CACHE_AD_OSIRIS ====
        if choice == "REFID_IOP_CACHE_AD_OSIRIS":
            sql_query = "select * from SA.REFID_IOP_CACHE_AD_OSIRIS"
            dataset = exec_sql('ITDEV', sql_query)
            users = convert_dataset_to_dict(dataset, 'SAMACCOUNTNAME')
            print_dict(users)
            print(f"\n{len(dataset)} rows")


        # ==== REFID_IOP_CACHE_EVIDIAN ====
        if choice == "REFID_IOP_CACHE_EVIDIAN":
            sql_query = "select * from SA.REF2ID_IOP_CACHE_EVIDIAN"
            dataset = exec_sql('ITDEV', sql_query)
            users = convert_dataset_to_dict(dataset, 'STPADLOGIN')
            print_dict(userid)
            print(f"\n{len(dataset)} rows")

        time.sleep(WAIT)
