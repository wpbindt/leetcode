from collections import Counter
from string import ascii_lowercase
from typing import Hashable


def serialize_to_sorted(string: str) -> str:
    """worst case O(k log(k))"""
    return ''.join(sorted(string))

def serialize_to_counter(
    string: str
) -> typing.Tuple[typing.Tuple[str, int]]:
    """
    Immutable counter, so technically O(k).
    For our range this turns out slower than
    the other serialization.
    Maybe there's a better way to get a
    hashable counter.
    """
    counter = Counter(string)
    return tuple(
        (char, counter.get(char, 0))
        for char in ascii_lowercase
    )

def group_anagrams(
    strs: List[str], 
    serialize: typing.Callable[[str], typing.Hashable]
) -> List[List[str]]:
    """
    avgerage time nk log(k) or nk solution, 
    depending on the chosen serialization
    k length of string, n length of list
    """
    groups = {}
    for string in strs:
        group = serialize(string)
        if group in groups:
            groups[group].append(string)
        else:
            group[group] = [string]

    return list(groups.values())

