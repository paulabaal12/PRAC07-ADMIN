import pytest
from analysis import reverse

@pytest.mark.parametrize("entrada, esperado", [
    ("hola", "aloh"),
    ("Python", "nohtyP"),
    ("", ""),
    ("a", "a"),
])
def test_reverse_happy_path(entrada, esperado):
    assert reverse(entrada) == esperado


@pytest.mark.parametrize("bad", [123, None, ["hola"]])
def test_reverse_invalid_type(bad):
    with pytest.raises(TypeError):
        reverse(bad)