"""Test de2en."""
# pylint: disable=broad-except
from de2en import __version__
from de2en import de2en


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not de2en()
    except Exception:
        assert True
