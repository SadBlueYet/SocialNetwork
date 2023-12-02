from fastapi import FastAPI
from main_model import UserVerification, Data, DB, MessageLoader

app = FastAPI()
db = DB()
verification = UserVerification(db=db)


@app.post("/sign")
def get_data(data: dict):
    data = Data(username=data['username'],
                password=data['password'],
                is_registration=data['is_registration'],
                telephone_number=data['telephone_number'],
                remember_me=data['remember_me'],
                uuid=data['uuid'])

    return verification.verification(data)


@app.get("/remember")
def get_remember_me(data: dict):
    remember_me = verification.get_remember_me_from_db(data['uuid'])
    return {'remember_me': (False,)}


@app.get("/loading_messages")
def get_messages(data: dict):
    a = MessageLoader(db=db).main_method(data['username'], data['password'])
    return a
