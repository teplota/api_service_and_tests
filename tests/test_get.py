import pytest
from pytest_lazyfixture import lazy_fixture
from constants import ID_INVALID
from config import API_URL
from api_methods.request import get_user_by_id, get_all_users


def test_get_all_users(start_add_users):
    response = get_all_users(API_URL)
    assert response.status_code == 200, 'Status code is not 200'
    response_body = response.json()
    assert list(response_body.keys()) == ['users'], 'No "users" in response body'
    assert len(response_body['users']) > 0, 'No users in response body'


def test_get_exist_id(random_user_name_surname_id):
    name, surname, id_exist = random_user_name_surname_id
    response = get_user_by_id(API_URL, id_exist)
    assert response.status_code == 200, 'Status code is not 200'
    assert response.headers['Content-Type'] == "application/json", 'Header is not JSON'
    response_body = response.json()['user']
    assert len(response_body) == 3, 'Wrong user data in response body'
    assert response_body['id'] == id_exist, 'Wrong id in response body'
    assert response_body['name'] == name, 'Wrong name in response body'
    assert response_body['surname'] == surname, 'Wrong surname in response body'


@pytest.mark.parametrize('user_id', [lazy_fixture('id_non_exist'), ID_INVALID, ""],
                         ids=["id_non_exist", "invalid_id", "empty_id"])
def test_get_non_exist_id(start_add_users, user_id):
    response = get_user_by_id(API_URL, user_id)
    assert response.status_code == 404, 'Status code is not 404'
