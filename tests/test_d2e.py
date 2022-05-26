"""Test d2e."""
# pylint: disable=broad-except
from de2en.d2e import d2e


def test_d2e():
    """Test d2e."""
    assert "making" in d2e("machen").lower()

    assert "test" == d2e("test").lower()
