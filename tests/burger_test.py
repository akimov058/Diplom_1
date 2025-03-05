from praktikum.burger import Burger

class TestBurger:
    def test_set_buns(self,mock_buns):
        burger = Burger()
        burger.set_buns()
        assert mock_buns == burger.bun

