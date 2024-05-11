import unittest


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):
    def setUp(self):
        self.formatted_name = formatted_name('', '')

    def test_full_name_formatted_name(self):
        self.assertEqual(formatted_name('john', 'doe'), 'John Doe')

    def test_first_middle_last_name(self):
        self.assertEqual(formatted_name('jane', 'smith', 'lee'), 'Jane Lee Smith')

    def test_only_first_name(self):
        with self.assertRaises(TypeError):
            self.formatted_name('john')