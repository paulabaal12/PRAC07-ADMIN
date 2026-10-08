import pytest
from analysis import count_vowels


@pytest.mark.parametrize("entrada, esperado", [
    ("Hola Mundo", 4),
    ("AEIOU", 5),
    ("Murciélago", 5),
    ("xyz", 0),
    ("", 0),
])
def test_count_vowels_happy_path(entrada, esperado):
    assert count_vowels(entrada) == esperado


@pytest.mark.parametrize("bad", [None, 42, ["a"]])
def test_count_vowels_invalid_type(bad):
    with pytest.raises(TypeError):
        count_vowels(bad)