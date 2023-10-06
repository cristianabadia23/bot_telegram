import sqlite3


def create_connection():
    conn = sqlite3.connect('web_watching.db')
    return conn, conn.cursor()


def create_table(conn, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS web_watching (
            link TEXT PRIMARY KEY,
            title TEXT,
            cine TEXT,
            open_vacancy BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()


def insert_web_watching(conn, cursor, link, title, cine, open_vacancy):
    try:
        if len(read_web_by_link_watching(cursor, link)) == 0:
            cursor.execute('INSERT INTO web_watching (link, title, cine,open_vacancy) VALUES (?, ?, ?, ?)',
                           (link, title, cine, open_vacancy))
            conn.commit()
            conn.close()
        else:
            print("registro preExistente")
    except:
        print("registro preExiste")


def read_web_watching(conn, cursor):
    cursor.execute('SELECT * FROM web_watching')
    result = cursor.fetchall()
    conn.close()
    return result


def read_web_watching(conn, cursor):
    cursor.execute('SELECT link,title FROM web_watching')
    result = cursor.fetchall()
    conn.close()
    return result


def read_web_by_name_watching(conn, cursor, title):
    cursor.execute('SELECT * FROM web_watching WHERE title=?', (title,))
    result = cursor.fetchall()
    conn.close()
    return result


def read_web_by_link_watching(cursor, link):
    cursor.execute('SELECT * FROM web_watching WHERE link=?', (link,))
    result = cursor.fetchall()
    return result


def read_web_by_link_watching(cursor, cine):
    cursor.execute('SELECT * FROM web_watching WHERE cine=?', (cine,))
    result = cursor.fetchall()
    return result


def update_web_watching(conn, cursor, link, open_vacancy):
    cursor.execute('UPDATE web_watching SET open_vacancy=? WHERE link=?', (open_vacancy, link))
    conn.commit()


def delete_web_watching(conn, cursor, link):
    cursor.execute('DELETE FROM web_watching WHERE link=?', (link,))
    conn.commit()
    conn.close()
