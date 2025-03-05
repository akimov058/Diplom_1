from unittest.mock import Mock
import pytest
from praktikum.burger import Burger

@pytest.fixture()
def mock_buns():
    mock_buns = Mock()
    mock_buns.name = 'Black Buns'
    mock_buns.price = 49.99
    return mock_buns