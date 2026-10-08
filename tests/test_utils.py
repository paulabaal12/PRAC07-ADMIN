import pytest
from textlib._utils import require_str, strip_accents


def test_require_str_accepts_str():
    require_str("hola", "s") 


@pytest.mark.parametrize("bad", [1, None, 2.5, ["a"]])
def test_require_str_rejects_non_str(bad):
    with pytest.raises(TypeError):
        require_str(bad, "s")


def test_strip_accents():
    assert strip_accents("canción áéíóú") == "cancion aeiou"