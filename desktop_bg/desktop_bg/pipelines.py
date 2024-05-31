# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class DesktopBgPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("pc_specs.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""CREATE TABLE specs_tb(
                            processor text,
                            gpu text,
                            motherboard text,
                            ram text
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO specs_tb
                             VALUES (?,?,?,?)"""(
                                item['processor'][0],
                                item['gpu'][0],
                                item['motherboard'][0],
                                item['ram'][0],
        ))
        self.conn.commit()
