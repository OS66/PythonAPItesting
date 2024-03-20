import jsonpath
import requests

base_url = 'https://restful-booker.herokuapp.com'


def test_existing_booking():
    test_id = '19'
    response = requests.get(base_url + '/booking/' + test_id)
    assert response.status_code == 200
    print(response.text)


