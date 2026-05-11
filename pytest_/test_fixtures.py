import pytest

@pytest.fixture
def user_data():
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]

#Test functions to check for a specific user

def test_user_exists(user_data):
    user = {"name": "Alice", "age": 30}

    #check is user in list
    assert user in user_data

def test_average_age(user_data):
    ages = [user["age"] for user in user_data]
    avg_age = sum(ages) / len(ages)
    assert avg_age == 30