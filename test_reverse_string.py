import reverse_string


def test_reverse_string():
    assert reverse_string.reverse_string('kot') == 'tok'
    assert reverse_string.reverse_string('kura') == 'aruk'