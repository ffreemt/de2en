"""Test de2en."""
# pylint: disable=broad-except
from de2en import de2en


def test_de2en():
    """Test de2en."""
    assert "making" in "".join(de2en("machen"))

    assert "test" in " ".join(de2en("test"))

    res = de2en(["Dies is ein Test".split()])
    assert len(res[0].split()) >= 20
