# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from .json_schema import validate_computer
from jsonschema.exceptions import ValidationError


class DesktopBgPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("pc_specs.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute('''
                    CREATE TABLE IF NOT EXISTS specs_tb (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        processor TEXT,
                        gpu TEXT,
                        motherboard TEXT,
                        ram TEXT,
                        UNIQUE(processor, gpu, motherboard, ram)

                    )
                ''')
        self.conn.commit()

    def close_spider(self):
        self.conn.close()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        is_valid, validation_error = validate_computer(dict(item))
        if not is_valid:
            raise ValueError(f"Item validation failed: {validation_error}")

        self.curr.execute("""INSERT OR IGNORE INTO specs_tb (processor, gpu, motherboard, ram)
                                   VALUES (?,?,?,?)""", (

                                item['processor'],
                                item['gpu'],
                                item['motherboard'],
                                item['ram'],
        ))
        self.conn.commit()
