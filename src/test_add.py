from operations import add

class TestsAdd():

    def test_add_int(self):
        assert add(1, 2) == 3
        assert add(1, 1) == 2

    def test_add_negative(self):
        assert add(1, -1) == 0
        assert add(-1, -1) == -2
