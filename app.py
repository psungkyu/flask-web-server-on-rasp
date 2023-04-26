from flask import Flask, request, jsonify
import control_led
from enum import Enum

class LED_PIN(Enum):
    RED = 17
    YELLOW = 27
    GREEN = 22

app = Flask(__name__)

@app.route('/path/to/endpoint', methods=['POST'])
def handle_request():
    # Get the JSON payload from the request
    payload = request.get_json()

    # Extract the similarity score from the payload
    similarity_score = payload['similarity_score']
    name = payload['name']

    # Print the similarity score to the console
    print('Similarity score:', similarity_score)

    if similarity_score > 80:
        print("hello {}!" .format(name))
        control_led.led_dimming(LED_PIN.GREEN.value)
    else:
        print("you are not authorized!")
        control_led.led_dimming(LED_PIN.RED.value)

    # Return a response to the AWS Lambda function
    response_payload = {
        'message': 'Success'
    }
    return jsonify(response_payload)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
