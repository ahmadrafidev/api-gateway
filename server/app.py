from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL API eksternal
DOG_IMAGE_API = "https://dog.ceo/api/breeds/image/random"
JOKE_API = "https://official-joke-api.appspot.com/random_joke"
AGE_API = "https://api.agify.io"
GENDER_API = "https://api.genderize.io"
NATIONALITY_API = "https://api.nationalize.io"
ACTIVITY_API = "https://www.boredapi.com/api/activity"

@app.post('/api/person')
def person_info():
    data = request.get_json()
    name = data.get('name')
    role = data.get('role')
    response_data = {'name': name, 'image': get_dog_image()}

    if role == 'guest':
        response_data.update({
            'age': get_age(name),
            'gender': get_gender(name),
            'nationality': get_nationality(name)
        })
    elif role == 'friend':
        response_data.update({
            'quote': get_joke(),
            'hobby': get_activity()
        })
    elif role == 'inspector':
        response_data.update({
            'age': get_age(name),
            'gender': get_gender(name),
            'nationality': get_nationality(name),
            'quote': get_joke(),
            'hobby': get_activity()
        })

    return jsonify(response_data)

def get_dog_image():
    response = requests.get(DOG_IMAGE_API)
    return response.json().get('message', '-')

def get_joke():
    response = requests.get(JOKE_API)
    joke_data = response.json()
    return f"{joke_data.get('setup', '-')}: {joke_data.get('punchline', '-')}"

def get_age(name):
    response = requests.get(f"{AGE_API}?name={name}")
    return response.json().get('age', '-')

def get_gender(name):
    response = requests.get(f"{GENDER_API}?name={name}")
    gender_data = response.json()
    return gender_data.get('gender', '-') if 'gender' in gender_data else '-'

def get_nationality(name):
    response = requests.get(f"{NATIONALITY_API}?name={name}")
    country_data = response.json()
    return country_data.get('country', [{}])[0].get('country_id', '-')

def get_activity():
    response = requests.get(ACTIVITY_API)
    return response.json().get('activity', '-')

if __name__ == "__main__":
    app.run(debug=True)
    