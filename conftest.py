from unittest.mock import Mock
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.burger import Burger

@pytest.fixture()
def mock_buns():
    mock_buns = Mock()
    mock_buns.name = 'Black Buns'
    mock_buns.price = 49.99
    return mock_buns
@pytest.fixture()
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient.name = 'Cheese'
    mock_ingredient.price = 19.99