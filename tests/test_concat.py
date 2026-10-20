import pytest
from analysis import concat

@pytest.mark.parametrize("c,b , esperado", [
    ("hola", " Galleta", "hola Galleta" ), 
    ("como", " estas", "como estas"),
    ("password", "123", "password123" ),
    ("", "Hola", "Hola"),
    ("123", "456", "123456")
])

def test_concat_happy_path(c,b, esperado):
    assert concat(c,b)==esperado
    
@pytest.mark.parametrize("c, b", [
    (None, "a"),
    ("a", None), 
    (1234, "a"), 
    ("a", 1234), 
    (["a"], "b"),
    ("b", ["a"]),  
    (True, "a"), 
    ("a", False)
])
def test_concat_invalid_type(c, b):
    with pytest.raises(TypeError):
        concat(c,b)
