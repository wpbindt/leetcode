def longest_palindrome(s: str) -> str:
    max_palindrome = ''
    for ix, c in enumerate(s):
        palindrome = c
        left = ix - 1
        right = ix + 1
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                palindrome = s[left] + palindrome + s[right]
                left -= 1
                right += 1
            else:
                break

        max_palindrome = max(
            max_palindrome,
            palindrome,
            key=len
        )
    
    for ix in range(len(s) - 1):
        palindrome = ''
        left = ix
        right = ix + 1
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                palindrome = s[left] + palindrome + s[right]
                left -= 1
                right += 1
            else:
                break

        max_palindrome = max(
            max_palindrome,
            palindrome,
            key=len
        )

    return max_palindrome


assert longest_palindrome('') == ''
assert longest_palindrome('a') == 'a'
assert longest_palindrome('baaaaa') == 'aaaaa'
assert longest_palindrome('ab') in {'a', 'b'}
assert longest_palindrome('abba') == 'abba'
assert longest_palindrome('babad') in {'bab', 'aba'}
assert longest_palindrome('dabab') in {'bab', 'aba'}
assert longest_palindrome('babads') in {'bab', 'aba'}

