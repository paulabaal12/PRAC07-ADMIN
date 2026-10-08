from utils import require_str


def reverse(s):
    """Retorna la cadena en orden inverso."""
    require_str(s, "s")
    return s[::-1]