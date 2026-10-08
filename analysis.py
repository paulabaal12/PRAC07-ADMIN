from utils import require_str, strip_accents


def reverse(s):
    """Retorna la cadena en orden inverso."""
    require_str(s, "s")
    return s[::-1]

def count_vowels(s):
    """Retorna el total de vocales (con o sin tilde)."""
    require_str(s, "s")
    return sum(1 for c in strip_accents(s).lower() if c in "aeiou")