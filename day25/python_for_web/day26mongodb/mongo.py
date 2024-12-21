# from flask import Flask, render_template, jsonify
# import os
# import pymongo


# MONGODB_URI = 'mongodb+srv://ashuu:385358@30daysofpython.v6xbp.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfpython'

# # # Connect to MongoDB
# try:
#     client = pymongo.MongoClient(MONGODB_URI)
#     db = client.thirty_days_of_python
#     print("MongoDB connection successful")
# except Exception as e:
#     print("Failed to connect to MongoDB:", e)

# # Insert students
# students = [
#     {'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34},
#     {'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28},
#     {'name': 'ashuu', 'country': 'somali', 'city': 'mog', 'age': 22},
# ]
# try:
#     for student in students:
#         db.students.insert_one(student)
#     print("Data insertion successful")
# except Exception as e:
#     print("Data insertion failed:", e)

# # Flask application
# app = Flask(__name__)

# @app.route('/students', methods=['GET'])
# def get_students():
#     try:
#         students = list(db.students.find())
#         for student in students:
#             student['_id'] = str(student['_id'])  # Convert ObjectId to string
#         return jsonify(students), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
from flask import Flask, jsonify
import os
import pymongo
from bson import ObjectId


MONGODB_URI = 'mongodb+srv://ashuu:385358@30daysofpython.v6xbp.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfpython'

client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

#fnde_one 
# student = db.students.find_one()
# print(student)
# student = db.students.find_one({'_id':ObjectId('6765c8104dd83a75cd64bd47')})
# print(student)
# find(): returns all the occurrence from a collection if we don't pass a query object. The object is pymongo.cursor object.

# students = db.students.find()

# We can specify which fields to return by passing second object in the find({}, {}). 0 means not include and 1 means include but we can not mix 0 and 1, except for _id.

# students = db.students.find({}, {"_id":0, "name":1,"country":1})

#Find with Query
# query = {
#     "country": "somali",
# }

#Find query with modifier
# query = {"age": {"$gt":30}}
# students = db.students.find(query)
#Limiting documents

# db.students.find().limit(3)
# for student in students:
#     print(student)
#Find with sort

# students = db.students.find().sort('name')
# for student in students:
#     print(student)


# students = db.students.find().sort('name',-1)
# for student in students:
#     print(student)

# students = db.students.find().sort('age')
# for student in students:
#     print(student)

# students = db.students.find().sort('age',-1)
# for student in students:
#     print(student)
    
    
    #Update with query
# query = {'age':250}
# new_value = {'$set':{'age':38}}

# db.students.update_one(query, new_value)
# # lets check the result if the age is modified
# for student in db.students.find():
#     print(student)
    
    #Delete 
query = {'name':'David'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)
#Drop a collection
#db.students.drop()
app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)