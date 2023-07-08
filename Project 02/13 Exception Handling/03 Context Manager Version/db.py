import sqlite3

class SQLite:
    def __init__(self, file="application.db"):
        self.file = file
        
    def __enter__(self):
        self.con = sqlite3.connect(self.file)
        return self.con.cursor()

    def __exit__(self, type, value, traceback):
        self.con.close()


class NotFoundError(Exception):
    pass


class NotAuthorizedError(Exception):
    pass


def blog_lst_to_json(item):
    return {
        'id': item[0],
        'published-date': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
    }


def fetch_blogs():
    try:
        with SQLite() as cur:  # Don't forget to call
            cur.execute('SELECT * FROM blogs where public=1')
            result = list(map(blog_lst_to_json, cur.fetchall()))
            return result
    
    except Exception as e:
        print(e)
        return "No Blogs Exist!"


def fetch_blog(id: str):
    try:
        with SQLite() as cur:
            cur.execute(f"SELECT * FROM blogs where id='{id}'")
            result = cur.fetchone()

            if result is None:
                raise NotFoundError(f'Unable to find blog with id {id}')
            
            data = blog_lst_to_json(result)
            if not data['public']:
                raise NotAuthorizedError(f'You are not allowed to access blog with id {id}')

            return data
    
    except sqlite3.OperationalError as e:
        print(e)
        raise NotFoundError(f'Unable to find blog with id {id}')

