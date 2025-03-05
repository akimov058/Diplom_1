from unittest.mock import Mock
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
import random
import string

from praktikum.burger import Burger

@pytest.fixture()
def mock_buns():
    mock_buns = Mock()
    mock_buns.name = 'Black Buns'
    mock_buns.price = 49.99
    return mock_buns
@pytest.fixture()
def mock_ingredient():
    letters = string.ascii_lowercase
    mock_ingredient = Mock()
    mock_ingredient.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient.name = ''.join(random.choice(letters) for i in range(10))
    mock_ingredient.price = 19.99
    return mock_ingredient