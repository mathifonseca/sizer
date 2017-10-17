#!flask/bin/python
from flask import Flask, jsonify, request
from random import uniform

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'ok': True}), 200


@app.route('/dimensions', methods=['POST'])
def calculate_dimensions():

    json = request.get_json(silent=True)
    errors = check_params(json)

    if len(errors) > 0:
        response = jsonify(errors)
        response.status_code = 400
        return response

    dimensions = random_dimensions()

    return jsonify(dimensions), 200


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'}), 405


def check_params(json):
    errors = []

    if not json:
        errors.append(error('Incorrect JSON body'))
    else:
        if 'image' not in json:
            errors.append(error('Missing parameter', 'image'))
        elif not decode_image(json['image']):
            errors.append(error('Invalid base64 representation', 'image'))

    return errors


def decode_image(img):
    try:
        img = img.replace('data:image/png;base64,', '')
        img.decode('base64')
        return True
    except:
        return False


def random_dimensions():
    return {
        'height': round(uniform(0, 10), 2),
        'length': round(uniform(0, 20), 2),
        'weight': round(uniform(0, 15), 2)
    }


def error(message, field=None):
    msg = {
        'message': message
    }
    if field:
        msg['field'] = field
    return msg


if __name__ == '__main__':
    app.run(debug=True)
