import sqlite3
from unittest import result
class db_manager:
    def __init__(self) -> None:
        Db_name='url.db'
        conn = sqlite3.connect(Db_name)
        print(f'连接数据库{Db_name}成功')
        self.db=conn
        self.cursor=conn.cursor()

    def creat_table(self,name):
        sql=f"""CREATE TABLE {name}(
            SourceUrl varchar(20),
            Suffix varchar(10000)
        )
        """
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()

    def add_data_to_db(self,name,url,s_url):
        sql = f"""
        INSERT INTO {name} VALUES('{url}','{s_url}')
        """
        self.cursor.execute(sql)
        self.db.commit()
        return True

    def serch_data(self,name,suffix):
        sql = f'''
            SELECT * FROM {name} WHERE Suffix = '{suffix}';
            '''
        result = None
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()[0]
        except:
            pass
        return result

    def del_data(self,name,suffix):
        sql = f'''
             DELETE FROM {name} WHERE Suffix = '{suffix}'
             '''
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            return False
        return True
    
    def serch_all(self,name):
        sql = f'''
            SELECT * FROM {name};
            '''
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result