import my_class


def test_dog_initialization():
    d = my_class.Dog('Azor')
    assert d.name == 'Azor'


def test_dog_speak():
    d = my_class.Dog('Azor')
    assert d.speak() == 'hau hau. Jestem Azor.'
