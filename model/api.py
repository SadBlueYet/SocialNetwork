from fastapi import FastAPI
from verification import UserVerification, get_remember_me_from_db

app = FastAPI()


@app.post("/sign")
def get_data(data: dict):
    verification = UserVerification(username=data['username'],
                                    password=data['password'],
                                    is_registration=data['is_registration'],
                                    telephone_number=data['telephone_number'],
                                    remember_me=data['remember_me'],
                                    uuid=data['uuid'])
    return verification.verification()


@app.post("/remember")
def get_remember_me(data: dict):
    remember_me = get_remember_me_from_db(data['uuid'])
    return {'remember_me': remember_me}
