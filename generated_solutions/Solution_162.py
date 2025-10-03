import hashlib
from typing import Optional

def string_to_md5(text: str) -> Optional[str]:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    >>> string_to_md5('') is None
    >>> string_to_md5('Python MD5 example') == '032e5416035848c081831413a24a520f'
    >>> string_to_md5('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'
    """
    if not text:
        return None
    
    # MD5 hash objects require bytes as input.
    # We encode the string to bytes, typically using UTF-8.
    md5_hash = hashlib.md5(text.encode('utf-8'))
    
    # hexdigest() returns the hash as a hexadecimal string.
    return md5_hash.hexdigest()