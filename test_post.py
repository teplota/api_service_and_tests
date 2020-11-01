import pytest
from mimesis import Person
from .constants import NAME_LONG, SURNAME_LONG
from .config import API_URL
from .api_methods.request import create_user

person = Person('ru')


@pytest.mark.parametrize('name', [person.name(), NAME_LONG], ids=["random_name", "long_name"])
@pytest.mark.parametrize('surname', [person.surname(), SURNAME_LONG], ids=["random_surname", "long_surname"])
def test_create_user_name_surname(name, surname):
    response = create_user(API_URL, {'name': name, 'surname': surname})
    assert response.status_code == 201, 'Status code is not 201'
    assert response.headers['Content-Type'] == "application/json", 'Header is not JSON'
    response_body = response.json()
    assert len(response_body['user']) == 3, 'Wrong user data in response body'
    response_body_user = response_body['user']
    assert response_body_user['name'] == name, 'Wrong name in response body'
    assert response_body_user['surname'] == surname, 'Wrong surname in response body'


@pytest.mark.parametrize('params', [{}, {'name': person.name()}, {'surname': person.surname()}, ''],
                         ids=["empty_params", "name_only", "surname_only", 'empty_request_body'])
def test_create_user_without_mandatory_params(params):
    response = create_user(API_URL, params)
    assert response.status_code == 400, 'Status code is not 400'


@pytest.mark.xfail(reason='Validation is not implemented in the service yet')
@pytest.mark.parametrize('name', [1, None, True, False, -1])
def test_create_user_with_bad_name(name):
    response = create_user(API_URL, {'name': name, 'surname': person.surname()})
    assert response.status_code == 400, 'Status code is not 400'


@pytest.mark.xfail(reason='Validation is not implemented in the service yet')
@pytest.mark.parametrize('surname', [1, None, True, False, -1])
def test_create_user_with_bad_surname(surname):
    response = create_user(API_URL, {'name': person.name(), 'surname': surname})
    assert response.status_code == 400, 'Status code is not 400'
