import sample


def test_total() -> None:
    assert sample.total(iter([3, 4])) == 7
    assert sample.total(iter([])) == 0


def test_total_squares() -> None:
    assert sample.total_squares(iter([3, 4])) == 25
    assert sample.total_squares(iter([])) == 0
