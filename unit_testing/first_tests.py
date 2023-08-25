# Unit testing is a way to test individual units of code
# - Typically automated
# - Gain confidence that individual parts of our software are working
# - Key part of refactoring

import unittest

class TestStringOperations(unittest.TestCase):

    def test_length_wesley_is_6(self):
        name = 'Wesley'
        self.assertEqual(len(name), 6)

    def test_x_not_in_string(self):
        sent = "On Earth, gravity gives weight to physical objects"
        is_x_in_sent = 'x' in sent
        self.assertFalse(is_x_in_sent)

if __name__ == '__main__':
    unittest.main()