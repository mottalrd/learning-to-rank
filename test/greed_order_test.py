import init_tests
import pytest
from greedy_order import *


class TestGreedyOrder:

    @pytest.fixture
    def v(self):
        return [5, 2, 3, 1, 8, 13]

    @pytest.fixture
    def preference(self):
        return lambda e1, e2: e1 - e2 if e1 - e2 > 0 else 0

    @pytest.fixture
    def subject(self, v, preference):
        return GreedyOrder(v, preference)

    def test_hello(self, subject):
        assert subject.run() == [13, 8, 5, 3, 2, 1]
