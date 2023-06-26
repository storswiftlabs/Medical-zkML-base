from .leo.syntax import LeoTypes


def get_leo_quantized_type(bits: int) -> LeoTypes:
    """
    Gets the Leo integer type for a given number of bits.

    :param bits: The number of bits.
    :return: The Leo integer type.
    """
    assert bits in [8, 16, 32, 64, 128], "bits must be one of 8, 16, 32, 64, 128"

    if bits == 8:
        return LeoTypes.I8
    elif bits == 16:
        return LeoTypes.I16
    elif bits == 32:
        return LeoTypes.I32
    elif bits == 64:
        return LeoTypes.I64
    elif bits == 128:
        return LeoTypes.I128


def quantize(x: float, bits: int) -> str:
    """
    Quantizes a floating point number to a Leo integer type.

    :param x: The floating point number to quantize.
    :param bits: The number of bits to quantize to.
    :return: The quantized number as a string.
    """
    assert bits in [8, 16, 32, 64, 128], "bits must be one of 8, 16, 32, 64, 128"

    mlt = 2 ** (bits // 2 - 1) # Avoid overflow
    value = int(x * mlt)

    if value == mlt:
        value -= 1

    leo_type = get_leo_quantized_type(bits).value
    return f"{value}{leo_type}"


__all__ = [
    "quantize",
    "get_leo_quantized_type"
]
