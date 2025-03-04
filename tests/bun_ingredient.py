from praktikum.ingredient import Ingredient
from data.data import Data

class TestIngredient:
    def test_get_price_ingredient(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE,Data.INGREDIENT_NAME,Data.INGREDIENT_PRICE)
        assert ingredient.get_price() == Data.INGREDIENT_PRICE

