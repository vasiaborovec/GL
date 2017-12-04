import unittest
from valid import valid_admin_user

class TestCase(unittest.TestCase):
    """Tests for `valid.py`."""

    def test_correct_data(self):
        """Test with correct login and password"""
        self.assertTrue(valid_admin_user("vasja.pupkin","passsecret"))

    def test_with_incorrect_data_1(self):
        """Test with correct login and password"""
        self.assertFalse(valid_admin_user("vasfdfja.pufdf","paset"))

    def test_with_incorrect_data_2(self):
        """Test with correct login and incorrect password"""
        self.assertFalse(valid_admin_user("vasja.pupkin","paset"))

    def test_with_incorrect_data_3(self):
        """Test with incorrect login(letter case not correct) and correct password"""
        self.assertFalse(valid_admin_user("vasja.pupkin","passsecret"))

    def test_with_incorrect_data_4(self):
        """Test with correct login and incorrect password (letter case not correct)"""
        self.assertFalse(valid_admin_user("vasja.pupkin","PasSsecRet"))

    def test_with_empty_data(self):
        """Test with empty login and password"""
        self.assertFalse(valid_admin_user("",""))



if __name__ == '__main__':
    unittest.main()