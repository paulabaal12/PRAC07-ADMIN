import unicodedata

def require_str(value, name):
    if not isinstance(value, str):
        raise TypeError(f"{name} debe ser una cadena de texto")


def strip_accents(s):
    normalized = unicodedata.normalize("NFD", s)
    return "".join(c for c in normalized if not unicodedata.combining(c))