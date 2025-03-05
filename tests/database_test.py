from praktikum.database import Database
import pytest

class TestDatabase:
    @pytest.mark.parametrize('result',['black bun','white bun','red bun'])
    def test_available_buns(self,result):
        db = Database()
        buns = db.available_buns()
        buns_list = [bun.get_name() for bun in buns]
        assert result in buns_list, buns_list

