from unittest import TestCase

from csci_utils.hash.hash import hash_str


class HashTests(TestCase):
    def test_basic(self):
        self.assertEqual(hash_str("world!", salt="hello, ").hex()[:6], "68e656")
