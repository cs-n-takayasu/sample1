import pytest
from src.fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "num, result",
    [(15, "FizzBuzz")],
)
def test_fizzbuzz(num, result):
    """
    関数をパラメータ化して、FizzBuzzを検証
    """
    assert result == fizzbuzz(num)
