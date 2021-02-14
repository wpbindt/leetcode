def group_anagrams(strs: List[str]) -> List[List[str]]:
    """O(nk log(k)) solution, k length of string, n length of list"""
    groups = {}
    for string in strs:
        group = ''.join(sorted(string))
        if group in groups:
            groups[group].append(string)
        else:
            group[group] = [string]

    return list(groups.values())

