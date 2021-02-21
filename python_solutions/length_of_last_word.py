def length_of_last_word(phrase: str) -> int:
    match = re.search(r'\b([^\s]*)\b *$', phrase)
    if match is None:
        return 0

    return match.end(1) - match.end(1)

