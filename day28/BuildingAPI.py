# # GET        Used for object retrieval
# # POST       Used for object creation and object actions
# # PUT        Used for object update
# # DELETE     Used for object deletion

# # from flask import Flask,  Response
# # import json
# # import pymongo
# # import os

# # app = Flask(__name__)
# # @app.route('/api/v1/students', methods=['GET'])
# # def students ():
# #     student_list = [
# #         {
# #             'name':'Asabeneh',
# #             'country':'Finland',
# #             'city':'Helsinki',
# #             'skills':['HTML', 'CSS','JavaScript','Python']
# #         },
# #         {
# #             'name':'David',
# #             'country':'UK',
# #             'city':'London',
# #             'skills':['Python','MongoDB']
# #         },
# #         {
# #             'name':'Ashuu',
# #             'country':'somali',
# #             'city':'mog',
# #             'skills':['Java','C#']
# #         }
# #     ]
# #     return Response(json.dumps(student_list), mimetype='application/json')

# # if __name__ == '__main__':
# #     # for deployment
# #     # to make it work for both production and development
# #     port = int(os.environ.get("PORT", 5000))
# #     app.run(debug=True, host='0.0.0.0', port=port)

# from flask import Flask,  Response
# import json
# from bson.objectid import ObjectId
# import os
# import json
# from bson.json_util import dumps
# import pymongo
# from datetime import datetime
# app = Flask(__name__)

# # MONGODB_URI = 'mongodb+srv://ashuu:385358@30daysofpython.v6xbp.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfpython'
# # client = pymongo.MongoClient(MONGODB_URI, tls=True, tlsAllowInvalidCertificates=True, serverSelectionTimeoutMS=5000)  # Set a shorter timeout for testing
# # db = client['thirty_days_of_python']  # accessing the database

# # @app.route('/api/v1.0/students', methods=['GET'])
# # def get_students():
# #     students = list(db.students.find({}, {'_id': 0}))  # Exclude the '_id' field from the result
# #     return Response(json.dumps(students), mimetype='application/json')

# # if __name__ == '__main__':
# #     # for deployment
# #     # to make it work for both production and development
# #     port = int(os.environ.get("PORT", 5000))
# #     app.run(debug=True, host='0.0.0.0', port=port)


# app = Flask(__name__)

# MONGODB_URI = 'mongodb+srv://ashuu:385358@30daysofpython.v6xbp.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfpython'
# client = pymongo.MongoClient(MONGODB_URI, tls=True, tlsAllowInvalidCertificates=True, serverSelectionTimeoutMS=5000)
# db = client['thirty_days_of_python']

# @app.route('/api/v1.0/students', methods=['GET'])
# def get_students():
#     students = list(db.students.find({}, {'_id': 0}))  # Exclude the '_id' field from the result
#     return Response(json.dumps(students), mimetype='application/json')

# @app.route('/api/v1.0/students/<id>', methods=['GET'])
# def get_single_student(id):
#     student = db.students.find_one({'_id': ObjectId(id)})
#     return Response(dumps(student), mimetype='application/json')

# @app.route('/api/v1.0/students', methods=['POST'])
# def create_student():
#     name = request.form['name']
#     country = request.form['country']
#     city = request.form['city']
#     skills = request.form['skills'].split(', ')
#     bio = request.form['bio']
#     birthyear = request.form['birthyear']
#     created_at = datetime.now()
#     student = {
#         'name': name,
#         'country': country,
#         'city': city,
#         'birthyear': birthyear,
#         'skills': skills,
#         'bio': bio,
#         'created_at': created_at
#     }
#     db.students.insert_one(student)
#     return jsonify({'message': 'Student created successfully'}), 201

# @app.route('/api/v1.0/students/<id>', methods=['PUT'])
# def update_student(id):
#     name = request.form['name']
#     country = request.form['country']
#     city = request.form['city']
#     skills = request.form['skills'].split(', ')
#     bio = request.form['bio']
#     birthyear = request.form['birthyear']
#     updated_at = datetime.now()
#     student = {
#         'name': name,
#         'country': country,
#         'city': city,
#         'birthyear': birthyear,
#         'skills': skills,
#         'bio': bio,
#         'updated_at': updated_at
#     }
#     db.students.update_one({'_id': ObjectId(id)}, {'$set': student})
#     return jsonify({'message': 'Student updated successfully'}), 200

# if __name__ == '__main__':
#     # for deployment
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
    
# #update

# # @app.route('/api/v1.0/students', methods = ['GET'])
# # def students ():

# #     return Response(json.dumps(student), mimetype='application/json')
# # @app.route('/api/v1.0/students/<id>', methods = ['GET'])
# # def single_student (id):
# #     student = db.students.find({'_id':ObjectId(id)})
# #     return Response(dumps(student), mimetype='application/json')
# # @app.route('/api/v1.0/students', methods = ['POST'])
# # def create_student ():
# #     name = request.form['name']
# #     country = request.form['country']
# #     city = request.form['city']
# #     skills = request.form['skills'].split(', ')
# #     bio = request.form['bio']
# #     birthyear = request.form['birthyear']
# #     created_at = datetime.now()
# #     student = {
# #         'name': name,
# #         'country': country,
# #         'city': city,
# #         'birthyear': birthyear,
# #         'skills': skills,
# #         'bio': bio,
# #         'created_at': created_at

# #     }
# #     db.students.insert_one(student)
# #     return
# # @app.route('/api/v1.0/students/<id>', methods = ['PUT']) # this decorator create the home route
# # def update_student (id):
# #     query = {"_id":ObjectId(id)}
# #     name = request.form['name']
# #     country = request.form['country']
# #     city = request.form['city']
# #     skills = request.form['skills'].split(', ')
# #     bio = request.form['bio']
# #     birthyear = request.form['birthyear']
# #     created_at = datetime.now()
# #     student = {
# #         'name': name,
# #         'country': country,
# #         'city': city,
# #         'birthyear': birthyear,
# #         'skills': skills,
# #         'bio': bio,
# #         'created_at': created_at

# #     }
# #     db.students.update_one(query, student)
# #     # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
# #     return
# # def update_student (id):
# # if __name__ == '__main__':
# #     # for deployment
# #     # to make it work for both production and development
# #     port = int(os.environ.get("PORT", 5000))
# #     app.run(debug=True, host='0.0.0.0', port=port)
    
# #     #delete
    
# # @app.route('/api/v1.0/students', methods = ['GET'])
# # def students ():

# #     return Response(json.dumps(student), mimetype='application/json')
# # @app.route('/api/v1.0/students/<id>', methods = ['GET'])
# # def single_student (id):
# #     student = db.students.find({'_id':ObjectId(id)})
# #     return Response(dumps(student), mimetype='application/json')
# # @app.route('/api/v1.0/students', methods = ['POST'])
# # def create_student ():
# #     name = request.form['name']
# #     country = request.form['country']
# #     city = request.form['city']
# #     skills = request.form['skills'].split(', ')
# #     bio = request.form['bio']
# #     birthyear = request.form['birthyear']
# #     created_at = datetime.now()
# #     student = {
# #         'name': name,
# #         'country': country,
# #         'city': city,
# #         'birthyear': birthyear,
# #         'skills': skills,
# #         'bio': bio,
# #         'created_at': created_at

# #     }
# #     db.students.insert_one(student)
# #     return
# # @app.route('/api/v1.0/students/<id>', methods = ['PUT']) # this decorator create the home route
# # def update_student (id):
# #     query = {"_id":ObjectId(id)}
# #     name = request.form['name']
# #     country = request.form['country']
# #     city = request.form['city']
# #     skills = request.form['skills'].split(', ')
# #     bio = request.form['bio']
# #     birthyear = request.form['birthyear']
# #     created_at = datetime.now()
# #     student = {
# #         'name': name,
# #         'country': country,
# #         'city': city,
# #         'birthyear': birthyear,
# #         'skills': skills,
# #         'bio': bio,
# #         'created_at': created_at

# #     }
# #     db.students.update_one(query, student)
# #     # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
# #     return
# # @app.route('/api/v1.0/students/<id>', methods = ['PUT']) # this decorator create the home route
# # def update_student (id):
# #     query = {"_id":ObjectId(id)}
# #     name = request.form['name']
# #     country = request.form['country']
# #     city = request.form['city']
# #     skills = request.form['skills'].split(', ')
# #     bio = request.form['bio']
# #     birthyear = request.form['birthyear']
# #     created_at = datetime.now()
# #     student = {
# #         'name': name,
# #         'country': country,
# #         'city': city,
# #         'birthyear': birthyear,
# #         'skills': skills,
# #         'bio': bio,
# #         'created_at': created_at

# #     }
# #     db.students.update_one(query, student)
# #     # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
# #     return ;
# # @app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
# # def delete_student (id):
# #     db.students.delete_one({"_id":ObjectId(id)})
# #     return
# # if __name__ == '__main__':
# #     # for deployment
# #     # to make it work for both production and development
# #     port = int(os.environ.get("PORT", 5000))
# #     app.run(debug=True, host='0.0.0.0', port=port)