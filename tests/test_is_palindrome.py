import pytest
from analysis import is_palindrome


@pytest.mark.parametrize("entrada", [
    "reconocer",
    "Anita lava la tina",
    "A man, a plan, a canal: Panama",
    "",
])
def test_is_palindrome_true(entrada):
    assert is_palindrome(entrada) is True


@pytest.mark.parametrize("entrada", ["hola", "palindromo"])
def test_is_palindrome_false(entrada):
    assert is_palindrome(entrada) is False


@pytest.mark.parametrize("bad", [12321, None, ["a", "a"]])
def test_is_palindrome_invalid_type(bad):
    with pytest.raises(TypeError):
        is_palindrome(bad)