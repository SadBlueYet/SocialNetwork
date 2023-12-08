import psycopg2


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class UsersDB(metaclass=MetaSingleton):
    __conn = None

    def __init__(self):
        self.__connection()
        self.__create_table()

    # Connection with database
    def __connection(self):
        self._conn = psycopg2.connect(user="postgres",
                                      password="admin",
                                      host="localhost",
                                      port="5432",
                                      database="users")
        self._cur = self._conn.cursor()

    def disconnect(self):
        self._cur.close()

    def __create_table(self):
        self._cur.execute("""CREATE TABLE IF NOT EXISTS users (
                          id SERIAL PRIMARY KEY,                                     
                          username VARCHAR(255) NOT NULL,
                          password TEXT NOT NULL,
                          telephone_number VARCHAR(20),
                          remember_me BOOLEAN,
                          uuid TEXT,
                          UNIQUE(username),
                          UNIQUE(telephone_number));
                          CREATE TABLE IF NOT EXISTS user_chats(
                          id SERIAL PRIMARY KEY,
                          user_id_1 INTEGER REFERENCES users(id) ON DELETE CASCADE,
                          user_id_2 INTEGER REFERENCES users(id) ON DELETE CASCADE,
                          UNIQUE(user_id_1, user_id_2));
                          CREATE TABLE IF NOT EXISTS user_messages(
                          id SERIAL PRIMARY KEY,
                          chat_id INTEGER REFERENCES user_chats(id) ON DELETE CASCADE,
                          body TEXT,
                          sender_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                          getter_id INTEGER REFERENCES users(id) ON DELETE CASCADE);""")
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
        return self._execute_query(query, (username,)).fetchone()

    def get_telephone_number(self, telephone_number: str) -> tuple:
        query = "SELECT telephone_number FROM users WHERE telephone_number = %s"
        return self._execute_query(query, (telephone_number,)).fetchone()

    def get_password(self, username: str) -> tuple:
        query = "SELECT password FROM users WHERE username = %s"
        return self._execute_query(query, (username,)).fetchone()

    def get_username(self, user_id: int) -> tuple:
        query = "SELECT username FROM users WHERE id = %s"
        return self._execute_query(query, (user_id,)).fetchone()

    def get_remember_me(self, uuid: str) -> tuple:
        query = "SELECT remember_me FROM users WHERE uuid = %s"
        return self._execute_query(query, (uuid,)).fetchone()

    def update_remember_me(self, remember_me: bool, uuid: str) -> None:
        query = "UPDATE users SET remember_me = %s WHERE uuid = %s"
        self._execute_query(query, (remember_me, uuid))

    def get_users_chat(self, user_id_1: int, user_id_2: int):
        query = "SELECT id FROM user_chats WHERE user_id_1 = %s AND user_id_2 = %s OR user_id_1 = %s AND user_id_2 = %s"
        params = (user_id_1, user_id_2, user_id_2, user_id_1)
        return self._execute_query(query, params).fetchone()

    def get_all_messages(self, user_chat_id: int):
        query = """SELECT body, sender_id, getter_id, id FROM user_messages WHERE chat_id = %s"""
        return self._execute_query(query, (user_chat_id,)).fetchall()

    def get_user_interlocutors(self, user_id: int) -> list:
        query = "SELECT user_id_1, user_id_2 FROM user_chats WHERE user_id_1 = %s OR user_id_2 = %s"
        params = (user_id, user_id)
        interlocutors = self._execute_query(query, params)
        data = interlocutors.fetchall()
        return [other_user_id for pair in data for other_user_id in pair if other_user_id != user_id]

    def get_user_id(self, username: str) -> tuple:
        query = "SELECT id FROM users WHERE username = %s"
        return self._execute_query(query, (username,)).fetchone()

    def set_chat(self, user_id_1: int, user_id_2: int) -> None:
        query = """INSERT INTO user_chats (user_id_1, user_id_2)  
                   SELECT %s, %s 
                   WHERE NOT EXISTS (
                        SELECT 1 
                        FROM user_chats 
                        WHERE (user_id_1 = %s AND user_id_2 = %s) 
                           OR (user_id_1 = %s AND user_id_2 = %s));"""
        params = (user_id_1, user_id_2, user_id_1, user_id_2, user_id_2, user_id_1)
        self._execute_query(query, params)

    def set_message(self, chat_id: int, text: str, sender_id: int, getter_id: int) -> None:
        query = "INSERT INTO user_messages (chat_id, body, sender_id, getter_id) VALUES (%s, %s, %s, %s)"
        self._execute_query(query, (chat_id, text, sender_id, getter_id))
