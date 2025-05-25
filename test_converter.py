import pytest
from currency_converter import convert

def test_convert_rub_to_usd():
    result = convert(100, 'RUB', 'USD')
    expected = 100 / 79.753
    print(f"\nDEBUG: {result=:.5f}, expected={expected:.5f}")
    assert pytest.approx(result, rel=1e-3) == expected
