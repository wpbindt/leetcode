def longest_palindrome(s: str) -> str:
    ...


assert longest_palindrome('') == ''
assert longest_palindrome('a') == 'a'
assert longest_palindrome('ab') in {'a', 'b'}
assert longest_palindrome('abba') == 'abba'
assert longest_palindrome('babad') in {'bab', 'aba'}
assert longest_palindrome('dabab') in {'bab', 'aba'}
assert longest_palindrome('babads') in {'bab', 'aba'}

