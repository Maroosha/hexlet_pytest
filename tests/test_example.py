from hexlet_pytest.example import reverse

def test_reverse():
    print('I am here!!')
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''
