#!/usr/bin/python3
""" Define function """


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
     boxes(list of lists of int): a list of lists.

    Returns:
     True if all bowes can be opened, False otherwise.
    """
    if not boxes:
        return True

    unlocked = [False] * len(boxes)
    unlocked[0] = True
    queue = [0]

    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
    return all(unlocked)


if __name__ == "__main__":
    boxes = [[0], [1], [2], []]
    print(canUnlockAll(boxes))
