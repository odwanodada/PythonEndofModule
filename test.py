import unittest
from play import *

class TestLottoTestCase(unittest.TestCase):
    def test_win(self):
        lotto= play()
        assert lotto.win() == True,"return True"




