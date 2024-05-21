#!/usr/bin/python3


def validUTF8(data):
    """
    Determines if a given data set represents
    a valid UTF-8 encoding.

    Args:
      data (list): data set.

    Returns:
      True if data is a valid UTF-8 encoding, else
      return False.
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0


# Example
data_set1 = [197, 130, 1]
print(validUTF8(data_set1))

data_set2 = [235, 140, 4]
print(validUTF8(data_set2))
