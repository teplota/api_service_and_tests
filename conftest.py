import pytest
import numpy as np
from mimesis import Person
from config import API_URL, ID_QUANTITY
from api_methods.request import create_user, get_all_users

person = Person('ru')


@pytest.fixture(scope='module')
def start_add_users():
    for i in range(1, ID_QUANTITY + 1):
        create_user(API_URL, {'name': person.first_name(), 'surname': person.surname()})


@pytest.fixture()
def random_user_name_surname_id(start_add_users):
    users = get_all_users(API_URL).json()['users']
    user = np.random.choice(users)
    name = user['name']
    surname = user['surname']
    id_exist = int(user['uri'].split('/')[-1])
    return name, surname, id_exist


@pytest.fixture()
def id_non_exist():
    response = get_all_users(API_URL).json()
    id_non_exist = len(response['users']) + 1
    return id_non_exist
