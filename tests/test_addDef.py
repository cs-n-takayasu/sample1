import pytest
from src.addDef import addDef


@pytest.mark.parametrize(
    "num1, num2, result",
    [(0, 1, 1)],
)
def test_addDef(num1, num2, result):
    """
    関数をパラメータ化して、addDefを検証
    """
    assert result == addDef(num1, num2)
    # assert 2 == addDef(num1, num2)
