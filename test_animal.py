import animal


def test_animal_total_number():
    d = animal.Dog('Azor', 'Hysky')
    assert animal.Animal.total_number_of_animal == 1


