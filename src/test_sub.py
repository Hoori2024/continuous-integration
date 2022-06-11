from operations import sub

class TestsSub():

    def test_sub(self):
        assert sub(1, 1) == 0
        assert sub (4, 5) == -1

    def test_sub_int(self):
        assert sub(1, 2) == -1
        assert sub(1, 1) == 0

    def test_sub_negative(self):
        assert sub(1, -1) == 2
        assert sub(-1, -1) == 0
