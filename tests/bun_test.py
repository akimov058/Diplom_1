from praktikum.bun import Bun
import pytest
from data.data import Data

class TestBun:
    def test_get_name_bun(self):
        bun = Bun(Data.BUN_NAME,Data.BUN_PRICE)
        assert bun.get_name() == Data.BUN_NAME