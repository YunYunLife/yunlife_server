from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import json
from mongoConnect import getCollection, collectionNames
from chatgpt_handler import process_user_input, update_memory


app = Flask(__name__)
CORS(app)

# MongoDB Routes
@app.route('/', methods=['GET'])
def index():
    return "Hello, This is yunlifeserver!"

@app.route('/articles', methods=['GET'])
def get_articles():
    result = getCollection(collectionNames.articles)
    return saveChinese(result)

@app.route('/calendar', methods=['GET'])
def get_calendar():
    result = getCollection(collectionNames.calendar)
    return saveChinese(result)

@app.route('/classrooms', methods=['GET'])
def get_classrooms():
    result = getCollection(collectionNames.classrooms)
    return saveChinese(result)

@app.route('/clubs', methods=['GET'])
def get_clubs():
    result = getCollection(collectionNames.clubs)
    return saveChinese(result)

@app.route('/elearing', methods=['GET'])
def get_elearing_articles():  # 修改函数名称
    result = getCollection(collectionNames.elearing)
    return saveChinese(result)

@app.route('/business_reality', methods=['GET'])
def get_business_reality_articles():  # 修改函数名称
    result = getCollection(collectionNames.business_reality)
    return saveChinese(result)

@app.route('/business_online', methods=['GET'])
def get_business_online_articles():  # 修改函数名称
    result = getCollection(collectionNames.business_online)
    return saveChinese(result)

@app.route('/siliconvalley', methods=['GET'])
def get_siliconvalley_articles():  # 修改函数名称
    result = getCollection(collectionNames.siliconvalley)
    return saveChinese(result)

@app.route('/university_course', methods=['GET'])
def get_university_course_articles():  # 修改函数名称
    result = getCollection(collectionNames.university_course)
    return saveChinese(result)

@app.route('/university_course_list', methods=['GET'])
def get_university_course_list_articles():  # 修改函数名称
    result = getCollection(collectionNames.university_course_list)
    return saveChinese(result)

# Save response in Chinese (UTF-8)
def saveChinese(data):
    response = make_response(json.dumps({'greetings': data}, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

# ChatGPT Endpoint
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get('prompt', '').lower()
    
    # Process user input
    response = process_user_input(user_input)
    
    # Update memory
    update_memory(user_input, response)
    
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
