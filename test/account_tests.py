import unittest
from account import Details


class TestDetailClass(unittest.TestCase):
    def test_accountDetailsExist(self):
        account_id = 'GBCKQLHFUZF36FIJUKUW37YFQG5O5MXT3YB2M7ZGVBORLUZMPIITWHZI'
        self.assertTrue(Details(account_id).get, msg='Test exist failed case failed')

    def test_accountDetailsDoesNotExist(self):
        account_id = 'GBCKQLHFUZF36FIJUKUW37YFQG5O5MXT3YB2M7ZGVBORLUZMPIITWHZ'
        self.assertIsNone(Details(account_id).get, msg='Test case Does not exist failed')

    def test_XLM(self):
        account_id = 'GBCKQLHFUZF36FIJUKUW37YFQG5O5MXT3YB2M7ZGVBORLUZMPIITWHZI'
        self.assertIs(Details(account_id).asset, 'XLM', msg='XLM checking failed')


if __name__ == '__main__':
    unittest.main()
