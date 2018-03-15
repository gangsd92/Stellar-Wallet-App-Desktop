import unittest
from transaction import Build

ANONYMOUS = 'GBCKQLHFUZF36FIJUKUW37YFQG5O5MXT3YB2M7ZGVBORLUZMPIITW'
ALICE_SEED = 'SAKM5BVR5OK75VAC4YCUXD4YLPIJEV7WIUY6WJUXNZF6LCJ3CGYD6WU2'
BOB = 'GAATZTOYFZSLGKM6BUTXNWMIWUETMEK74VBJNEPRGB5WW3ELVTKBWNGN'


class TestTransactionClass(unittest.TestCase):

    def test_transaction(self):
        self.assertTrue(Build(ALICE_SEED, BOB, 20).send())

    def test_invalid_account(self):
        self.assertFalse(Build(ALICE_SEED, ANONYMOUS, 20).send())


if __name__ == "__main__":
    unittest.main()
