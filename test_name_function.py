### Chapter 11: Testing Your Code

## Testing a Function

# Unit Tests and Test Cases: Passing Case

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py' . """

    def test_first_last_name(self):
        """ Do names like Mickey Mouse work? """

        formatted_name = get_formatted_name('mickey', 'mouse')
        self.assertEqual(formatted_name, 'Mickey Mouse')

    def test_first_middle_last_name(self):
        """ Do names like Mickey Mouse work? """

        formatted_name = get_formatted_name('elmer', 'fudd', 't.')
        self.assertEqual(formatted_name, 'Elmer T. Fudd')


if __name__ == '__main__':
    unittest.main()