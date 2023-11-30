import psycopg2


class UsersDB:
    def __init__(self):
        self.__connection()
        # self.__drop_table()
        self.__create_table()

    # Connection with database
    def __connection(self):
        self._conn = psycopg2.connect(user="postgres",
                                      password="admin",
                                      host="localhost",
                                      port="5432",
                                      database="users")
        self._cur = self._conn.cursor()

    # Drop table if exists
    def __drop_table(self):
        self._cur.execute("DROP TABLE IF EXISTS users")
        self._conn.commit()

    def __create_table(self):
        self._cur.execute("""CREATE TABLE IF NOT EXISTS users (
                          id SERIAL PRIMARY KEY,                                     
                          username TEXT, password TEXT, 
                          telephone_number TEXT,
                          remember_me BOOLEAN,
                          uuid TEXT);
                          CREATE TABLE IF NOT EXISTS user_chats(
                          id SERIAL PRIMARY KEY,
                          user_id_1 INTEGER,
                          user_id_2 INTEGER);
                          CREATE TABLE IF NOT EXISTS user_messages(
                          id SERIAL PRIMARY KEY,
                          user_chat_id INTEGER,
                          text TEXT,
                          sender INTEGER);""")
        self._conn.commit()

    def _execute_query(self, query, params=None):
        try:
            self._cur.execute(query, params)
            self._conn.commit()
            return self._cur
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")

    def set_user(self, username: str, password: str, telephone_number: str, remember_me: bool, uuid: str) -> None:
        query = """INSERT INTO users (username, 
                                      password, 
                                      telephone_number, 
                                      remember_me, 
                                      uuid) 
                                      VALUES (%s, %s, %s, %s, %s)"""
        self._execute_query(query, (username, password, telephone_number, remember_me, uuid))

    def find_username(self, username: str) -> tuple:
        query = "SELECT username FROM users WHERE username = %s"
        db_username = self._execute_query(query, (username,))
        return db_username

    def find_telephone_number(self, telephone_number: str) -> tuple:
        query = "SELECT telephone_number FROM users WHERE telephone_number = %s"
        db_telephone_number = self._execute_query(query, (telephone_number,))
        return db_telephone_number

    def find_password(self, username: str) -> tuple:
        query = "SELECT password FROM users WHERE username = %s"
        db_password = self._execute_query(query, (username,))
        return db_password.fetchone()

    def get_remember_me(self, uuid: str) -> tuple:
        query = "SELECT remember_me FROM users WHERE uuid = %s"
        db_remember_me = self._execute_query(query, (uuid,))
        return db_remember_me.fetchone()

    def update_remember_me(self, remember_me: bool, uuid: str) -> None:
        query = "UPDATE users SET remember_me = %s WHERE uuid = %s"
        self._execute_query(query, (remember_me, uuid))