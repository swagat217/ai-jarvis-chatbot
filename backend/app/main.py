# import os
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from fastapi import FastAPI
# from fastapi.responses import JSONResponse

# # Load environment variables from .env
# load_dotenv()
# MONGODB_URI = os.getenv("MONGODB_URI")

# # Connect to the database
# client = MongoClient(MONGODB_URI)
# db = client["jarvisdb"]  # Use your database name

# # Define the users collection
# users_col = db["users"]

# app = FastAPI()

# @app.get("/users")
# def get_users():
#     users = list(users_col.find({}, {"_id": 0}))  # Exclude the MongoDB _id field
#     return JSONResponse(content=users)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}
