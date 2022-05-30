import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py' """

    def test_first_last_name(self):
        """ Will it work with names like 'Janis Joplin'?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')  # add assertion here

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('dimchek', 'truten', 'vitalich')
        self.assertEqual(formatted_name, 'Dimchek Vitalich Truten')


if __name__ == '__main__':
    unittest.main()
