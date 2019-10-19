import palindrom


def test_is_palindrome():
    assert palindrom.is_palindrome('ala')
    assert palindrom.is_palindrome('oko')
    assert not palindrom.is_palindrome('as')