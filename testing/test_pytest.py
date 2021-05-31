from python.calc import Calc


class TestDemo:
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1, 3)
        print(result)
        assert 3 == result