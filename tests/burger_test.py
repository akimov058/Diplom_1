from praktikum.burger import Burger

class TestBurger:
    def test_set_buns(self,mock_buns):
        burger = Burger()
        burger.set_buns(mock_buns)
        assert mock_buns == burger.bun

    def test_add_ingredient(self,mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self,mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients)==0


