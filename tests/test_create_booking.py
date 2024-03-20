import pytest
import requests
import json
import jsonpath

base_url = "https://restful-booker.herokuapp.com"


@pytest.fixture()
def get_auth_token():
    payload_auth = {
        "username": "admin",
        "password": "password123"
    }
    headers = {
        "Content-Type": "application/json",
    }
    get_token = requests.post((base_url + "/auth"), json=payload_auth, headers=headers)
    global token
    token = get_token.text
    print(token)


def test_create_booking(get_auth_token):
    file = open('/Users/buba/Projects/pytest_projects/resful_booker/jsons/create_booking.json', 'r')
    json_input = file.read()
    body_json = json.loads(json_input)
    create_booking = requests.post((base_url + '/booking'), json=body_json)
    assert create_booking.status_code == 200
    print(create_booking.content)
    response = json.loads(create_booking.content)
    booking_id = jsonpath.jsonpath(response, 'bookingid')
    assert booking_id[0] > 0
    print(booking_id)


# print(answer.text)
# print(payload_json)
