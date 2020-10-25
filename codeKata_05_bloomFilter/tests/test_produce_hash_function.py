import unittest
import codeKata_05_bloomFilter as bF


class TestProduceHashFunction(unittest.TestCase):

    def test_inputs_bork_0_1(self):
        self.assertEqual('a2759bbbc506c841737b4285a457deaa23865660338dd568f9ebadc4f1e1067b',
                         bF.produce_hash_function(0, 64, 'bork'))
        self.assertEqual('a', bF.produce_hash_function(0, 1, 'bork'))

    def test_inputs_bork_1_1(self):
        self.assertEqual('decda4e39f1beb4ab32ee478fe1b429fccb569ac49602737ec7b293db0e39cf0',
                         bF.produce_hash_function(1, 64, 'bork'))
        self.assertEqual('d', bF.produce_hash_function(1, 1, 'bork'))

    def test_inputs_bork_2_1(self):
        self.assertEqual('fb63227dd8b2bd88b17bd7c4bd717a2c4b1937ed8f38a5f989323e975426a33f',
                         bF.produce_hash_function(2, 64, 'bork'))
        self.assertEqual('f', bF.produce_hash_function(2, 1, 'bork'))

    def test_inputs_bork_3_1(self):
        self.assertEqual('eb9470c8a67b62ab9ec2c2c4eda534d5b17f5d4d5e3b152b87c012286768514d',
                         bF.produce_hash_function(3, 64, 'bork'))
        self.assertEqual('e', bF.produce_hash_function(3, 1, 'bork'))

    def test_inputs_bork_4_1(self):
        self.assertEqual('cd3053dc875afd439f8bd21c09c4129261a6e24d8c9d3cc068c53c739e53ac3a',
                         bF.produce_hash_function(4, 64, 'bork'))
        self.assertEqual('c', bF.produce_hash_function(4, 1, 'bork'))

    def test_inputs_bork_5_1(self):
        self.assertEqual('0685f0f6f3920fea47a8bebc58e095677f08f49600c3e8aa131c09dd2a395f56',
                         bF.produce_hash_function(5, 64, 'bork'))
        self.assertEqual('0', bF.produce_hash_function(5, 1, 'bork'))

    def test_inputs_bork_6_1(self):
        self.assertEqual('1f3cd989d0843b96f68dc43102a3142d71d591b5b2bb3c571913862cd1e5848e',
                         bF.produce_hash_function(6, 64, 'bork'))
        self.assertEqual('1', bF.produce_hash_function(6, 1, 'bork'))

    def test_inputs_bork_0_5(self):
        self.assertEqual('a2759', bF.produce_hash_function(0, 5, 'bork'))

    def test_inputs_bork_0_64(self):
        self.assertEqual(64, len('a2759bbbc506c841737b4285a457deaa23865660338dd568f9ebadc4f1e1067b'))
        self.assertEqual(64, len(bF.produce_hash_function(0, 64, 'bork')))

    def test_inputs_bork_0_64(self):
        self.assertEqual('a2759bbbc506c841737b4285a457deaa23865660338dd568f9ebadc4f1e1067b',
                         bF.produce_hash_function(0, 65, 'bork'))
        self.assertEqual(64, len(bF.produce_hash_function(0, 65, 'bork')))
        # this will work fine for bloom filters that need an m value of less than 16^64


if __name__ == '__main__':
    unittest.main()
