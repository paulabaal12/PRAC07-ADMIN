import pytest
from analysis import to_upper


@pytest.mark.parametrize("entrada, esperado", [
    ("hola", "HOLA"), 
    ("adios", "ADIOS"),
    ("galleta", "GALLETA"),
])

def test_to_upper_happy_path(entrada, esperado):
    assert to_upper(entrada) ==esperado

@pytest.mark.parametrize("bad", [None, True, False, 123, ["a"]])
def test_to_upper_invalid_type(bad):
    with pytest.raises(TypeError):
        to_upper(bad)