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
import os
import pprint
import time
import oracledb
import utils
import ldap

from config.config import Config


CUR_DIR = os.path.dirname(__file__)
# config_start = Config(ENV="development")
config_start = Config()

WAIT = 2


class OracleConnexion():

    def __init__(self, DB):
        self.server_address = config_start.get_database_param(DB)['HOST']
        self.service_name = config_start.get_database_param(DB)['SERVICE']
        self.oracle_instant_client = config_start.get_client_path(DB)
        self.user_name = config_start.get_database_param(DB)['CREDENTIAL']['USERNAME']
        self.password = config_start.get_database_param(DB)['CREDENTIAL']['PASSWORD']
        oracledb.init_oracle_client(lib_dir=self.oracle_instant_client)
        self.connection = oracledb.connect(user=self.user_name, password=self.password,
                                           dsn=self.server_address + ":" + "1521" + "/" + self.service_name)

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, connection):
        self._connection = connection

    def exec_ddl_sql(self, sql_query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_query)
            self.connection.commit()
            result = True
        except Exception as e:
            print(f"message: An internal error occurred : {e}")
            result = False
        finally:
            cursor.close()
        return result

    def insert(self, query, data):
        with  self.connection.cursor() as curs:
            curs.execute(query, data)

    def fetch_data_from_db(self, query):
        result = dict()
        with  self.connection.cursor() as curs:
            curs.execute(query)
            num_fields = len(curs.description)
            # field_names = [i[0] for i in curs.description]
            # list of table columns
            column_names = list(map(lambda x: x.lower(), [d[0] for d in curs.description]))
            # list of data items
            rows = curs.fetchall()

            # return rows
            result = [dict(zip(column_names, row)) for row in rows]
            return result

    def prepare_statement_insert(self, table_name, dict_data):
        valueslist = list(dict_data.values())
        fields = ""
        for x in list(dict_data.keys()):
            fields += str(x) + ","
        fields = fields.rstrip(fields[-1])

        fields = fields.replace("#", "")
        preparefield = ""
        for x in list(dict_data.keys()):
            preparefield += ":" + str(x) + ","
        preparefield = preparefield.rstrip(preparefield[-1])
        sql = f"""insert into {table_name}({fields}) values({preparefield})"""

        return {"sql": sql, "valuelist": valueslist}


# Main =============================================================================================================
if __name__ == "__main__":
    oracle_IT = OracleConnexion('DB-IT')
    oracle_RH = OracleConnexion('DB-RH')

    userid = "WYNCHR"

    while True:
        options = ["REFID_IOP_PROV_AD",
                   "EVIDIAN.ARNO_CONTACTS",
                   "REFID_IOP_CACHE_AD_OSIRIS",
                   "REFID_IOP_CACHE_EVIDIAN",
                   "UPDATE PROV GROUPS",
                   "Exit"]
        res = utils.let_user_pick("db", options)
        if options[res] == "Exit":
            break
        choice = options[res]
        print(choice)
        # ========================

        if choice == "REFID_IOP_PROV_AD":
            sql_query = "select * from SA.REFID_IOP_PROV_AD"
            dataset = oracle_IT.fetch_data_from_db(sql_query)
            pprint.pprint(dataset)

        if choice == "EVIDIAN.ARNO_CONTACTS":
            sql_query = "SELECT * FROM EVIDIAN.ARNO_CONTACTS WHERE v100_rh_nom = 'WYNS'"
            dataset = oracle_RH.fetch_data_from_db(sql_query)
            pprint.pprint(dataset)

        if choice == "REFID_IOP_CACHE_AD_OSIRIS":
            sql_query = "select * from SA.REFID_IOP_CACHE_AD_OSIRIS"
            dataset = oracle_IT.fetch_data_from_db(sql_query)
            pprint.pprint(dataset)
            # users = utils.convert_dataset_to_dict(dataset, 'SAMACCOUNTNAME')
            # utils.print_dict(users)
            # print(f"\n{len(dataset)} rows")

        if choice == "REFID_IOP_CACHE_EVIDIAN":
            sql_query = "select * from SA.REFID_IOP_CACHE_EVIDIAN"
            dataset = oracle_IT.fetch_data_from_db(sql_query)
            pprint.pprint(dataset)
            # users = utils.convert_dataset_to_dict(dataset, 'STPADLOGIN')
            # utils.print_dict(userid)
            # print(f"\n{len(dataset)} rows")

        if choice == "UPDATE PROV GROUPS":
            dn = "CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be"
            samaccountname = ldap.extract_samaccountname(dn)
            sql_query = f"""
                UPDATE SA.REFID_IOP_PROV_AD SET GROUPS = '{samaccountname}'
                WHERE SAMACCOUNTNAME = 'ZZDEVIN'
                """
            result = oracle_IT.exec_ddl_sql(sql_query)



        time.sleep(WAIT)
