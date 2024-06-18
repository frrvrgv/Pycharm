import area
class TestArea:
    def test_circle(self):
        assert area.circle(14) == 615.44
        assert area.circle(-14) == 615.44

    def test_square(self):
        assert area.square(5) == 25
        assert area.square(4) == 16

    def test_rectangle(self):
        assert area.rectangle(4,6) == 24
        assert area.rectangle(6,9) == 54

    def test_parallelogram(self):
        assert area.parallelogram(5,8) == 40
        assert area.parallelogram(4,10) == 40

    def test_triangle(self):
        assert area.triangle(8,9) == 36
        assert area.triangle(2,3) == 3

    def test_fact(self):
        assert area.fact(2) == 2
        assert area.fact(4) == 24
