def longest_non_repeating_substring(string: str) -> int:
    """
    On average this should be linear bc of hash table stuff
    but sets are weird
    """
    substring_set = set()
    lengths = []
    i = 0
    j = 0
    while j < len(string):
        while string[j] in substring_set:
            substring_set -= {string[i]}
            i += 1
        substring_set.add(string[j])
        j += 1
        if j - i > max_len:
            max_len = j - i
        
    return max_len

