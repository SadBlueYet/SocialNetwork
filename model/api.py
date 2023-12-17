from fastapi import FastAPI
from verification import UserVerification, Data
from message_loader import MessageLoader, SetMessage

app = FastAPI()

verification = UserVerification()


@app.post("/sign")
def get_data(data: dict):
    data = Data(username=data.get('username'),
                password=data.get('password'),
                is_registration=data.get('is_registration'),
                telephone_number=data.get('telephone_number'),
                remember_me=data.get('remember_me'),
                uuid=data.get('uuid'))

    return verification.verification(data)


@app.get("/loading_messages")
def get_messages(data: dict):
    loader = MessageLoader()
    response = loader.main_method(data.get('username'), data.get('password'))
    return response


@app.get("/get_username")
def get_username(data: dict):
    username = verification.get_username(data.get("user_id"))
    if username is None:
        return {"username": None}
    return {"username": username[0]}


@app.post("/set_message")
def set_message(data: dict):
    message = SetMessage(text=data.get("text"), getter_id=data.get("getter_id"), sender_id=data.get("sender_id"))
    return message.set_message()


@app.get("/check_user")
def check_user(data: dict):
    user_id = verification.check_user_data(data.get("username"), data.get("password"))
    if user_id is None:
        return {"id": None}
    return {"id": user_id[0]}


@app.get("/get_id_by_username")
def get_id_by_login(data: dict):
    loader = MessageLoader()
    user_id = loader.get_user_id(data.get("username"))
    if user_id:
        return {"user_id": user_id[0]}
    return {"user_id": None}
