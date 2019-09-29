from flask import Blueprint
from .extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    user_collection = mongo.db.users
    user_collection.insert(
        {   
            "user_id" : "123",
            "first_name" : "John",
            "last_name" : "Doe",
            "gender" : "Male",
            "account" : {
                "user_id" : "12345",
                "mail_id" : "lol@gmail.com",
                "username" : "lol@gmail.com",
                "password" : "thisispassword"
            },
            "notes" : [
                {
                    "title" : "mongo",
                    "created_on" : "12234234",
                    "note" : "This is note"
                },
                {
                    "title" : "oracle",
                    "created_on" : "12234234",
                    "note" : "This is note"
                },
                {
                    "title" : "oracle",
                    "created_on" : "12234234",
                    "note" : "This is note"
                },
                {
                    "title" : "oracle",
                    "created_on" : "12234234",
                    "note" : "This is note"
                }
            ],
            "password_holder" :[
                {
                    "webapp" : "amazon.com",
                    "username" : "abc@gmail.com",
                    "mail_id" : "abc@gmail.com",
                    "password" : "abcde"
                },
                {
                    "webapp" : "amazon.com",
                    "username" : "abc@gmail.com",
                    "mail_id" : "abc@gmail.com",
                    "password" : "abcde"
                },
                {
                    "webapp" : "amazon.com",
                    "username" : "abc@gmail.com",
                    "mail_id" : "abc@gmail.com",
                    "password" : "abcde"
                }
            ]

        }
    )
    return "Success"