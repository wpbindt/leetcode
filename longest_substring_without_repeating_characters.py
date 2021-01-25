def longest_non_repeating_substring(string: str) -> int:
    """
    O(n^2), can maybe be improved by substring which supports
    faster search, append, and delete (len is easy to keep track of)
    """
    substring = []
    lengths = []
    for c in string:
        try:
            ix = substring.index(c)
            lengths.append(len(substring))
            del substring[:ix+1]
            substring.append(c)
        except ValueError:
            substring.append(c)
    lengths.append(len(substring))
        
    return max(lengths)

