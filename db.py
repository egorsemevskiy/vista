import pymysql

connection = pymysql.connect(host='localhost',
                             user='vista',
                             password='54132817Qw!',
                             db='vista',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


class MysqlConnect:

    def __init__(self):
        self.create_db()

    def create_db(self):
        # Connect to the database
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "CREATE TABLE IF NOT EXISTS todo (id serial primary key, title varchar(255), " \
                      "price varchar(255), link varchar(255), descript varchar(255));"
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
        except Exception as e:
            print(e)

    def add_to_db(self, note):
        try:
            with connection.cursor() as cursor:
                sql = f'INSERT INTO todo (title, price, link, descript) \
                values (\"{note["title"]}\", \"{note["price"]}\",\" {note["link"]}\",\" {note["descript"]}\");'
                print(sql)
                cursor.execute(sql)
                connection.commit()

        except Exception as e:
            print(e)

    def item_to_list(self):
        try:
            with connection.cursor() as cursor:
                sql = f'Select title from todo'
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(rows)
                return rows

        except Exception as e:
            print(e)

        #finally:
        #    connection.close()
