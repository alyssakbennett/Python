"""
Adler-32 is a checksum algorithm which was invented by Mark Adler in 1995.
Compared to a cyclic redundancy check of the same length, it trades reliability for
speed (preferring the latter).
Adler-32 is more reliable than Fletcher-16, and slightly less reliable than
Fletcher-32.[2]

source: https://en.wikipedia.org/wiki/Adler-32
"""

MOD_ADLER = 65521


def adler32(plain_text: str | bytes) -> int:
    """
    Function implements adler-32 hash.
    Adler-32 is defined over bytes, so text is encoded as UTF-8 first; this
    keeps the result equal to zlib.adler32 for non-ASCII input too.

    >>> adler32('Algorithms')
    363791387

    >>> adler32('go adler em all')
    708642122

    >>> adler32('€100')
    196018850

    >>> adler32(b'Wikipedia')
    300286872

    >>> adler32(42)
    Traceback (most recent call last):
        ...
    TypeError: adler32() expects str or bytes, not int
    """
    match plain_text:
        case str():
            data = plain_text.encode("utf-8")
        case bytes():
            data = plain_text
        case _:
            msg = f"adler32() expects str or bytes, not {type(plain_text).__name__}"
            raise TypeError(msg)

    a = 1
    b = 0
    for byte in data:
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
