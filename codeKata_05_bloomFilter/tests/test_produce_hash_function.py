import unittest
import codeKata_05_bloomFilter as bF


class TestProduceHashFunction(unittest.TestCase):
    """
    hashlib.sha224('bork'.encode('utf-8')).hexdigest() produces the string
        '33f8294eed104d7aded64d81d298ad9a2fbebf59176172ec4be65a29'
    """
    def test_produce_hash_function_gets_correct_index(self):
        self.assertEqual(bF.produce_hash_function(0, 1, 'bork'), '3')
        self.assertEqual(bF.produce_hash_function(1, 1, 'bork'), '3')
        self.assertEqual(bF.produce_hash_function(2, 1, 'bork'), 'f')
        self.assertEqual(bF.produce_hash_function(3, 1, 'bork'), '8')
        self.assertEqual(bF.produce_hash_function(4, 1, 'bork'), '2')
        self.assertEqual(bF.produce_hash_function(5, 1, 'bork'), '9')
        self.assertEqual(bF.produce_hash_function(6, 1, 'bork'), '4')

        self.assertEqual(bF.produce_hash_function(0, 5, 'bork'), '33f82')
        self.assertEqual(bF.produce_hash_function(55, 1, 'bork'), '9')
