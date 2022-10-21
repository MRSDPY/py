import sqlite3


class CoronaPipeline(object):

    def __init__(self):
        self.con = sqlite3.connect("Corona.db")
        self.cur = self.con.cursor()
        self.create_drop()

    def create_drop(self):
        self.cur.execute("""drop table if exists corona_detail""")
        self.cur.execute("""CREATE TABLE corona_detail(state TEXT,cases INTEGER,recovery INTEGER,death INTEGER)""")

    def process_item(self, item, spider):
        self.insert_data(item)
        return item

    def insert_data(self, item):
        try:
            for s, c, r, d in zip(item['state'], item['case'], item['recovery'], item['death']):
                self.cur.execute("""insert into corona_detail values (?, ?, ?, ?)""", (s, c, r, d))
            self.con.commit()
        except sqlite3.Error as er:
            print("Error during :", er)
