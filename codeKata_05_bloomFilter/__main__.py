import hashlib
import random
import string
import numpy as np
import nltk
from nltk.corpus import words
from functools import partial


def produce_hash_function(prefix: int, length: int, text: str):
    """Returns a hash string large enough to cover size m

    Produces a hexadecimal digest from a sha256 hash of the input string,
    prefixed with the value of argument prefix, and slices the desired
    number of characters from it
    """
    return hashlib.sha3_256(f'{prefix}text'.encode('utf-8')).hexdigest()[:length]


def already_exists_in_bloom_filter(entry):
    """Checks if entry already exists in the bloom filter"""
    hashes = np.array([v[int(H[h](entry), 16) % m] for h in range(k)])
    return np.all(hashes == 1)


if __name__ == '__main__':
    """
    For set A = {a_1, a_2, ..., a_n}
    create a vector v of size m, initialized to 0
    create k independent hash functions h_1,h_2,...,h_k, with range 1..m
    for each a ∈ A the bits in positions h_1(a),h_2(a),...,h_k(a) are set to 1
    
    to check if an input is already in the bloom filter, check the array locations for zeros.
    """
    nltk.download('words', quiet=True)
    A = words.words()
    n = len(A)
    m = n*4
    v = np.zeros(m)
    k = 4
    H = [partial(produce_hash_function, h, (m // 10) + 1) for h in range(k)]

    for a in A:
        for h in range(k):
            v[int(H[h](a), 16) % m] = 1

    print(f'f: {already_exists_in_bloom_filter("f")}')
    print(f'zed: {already_exists_in_bloom_filter("zed")}')
    print(f'wonderful: {already_exists_in_bloom_filter("wonderful")}')
    print(f'random: {already_exists_in_bloom_filter("wonderful")}')
    print(f'indubitably: {already_exists_in_bloom_filter("indubitably")}')

    for _ in range(10):
        random_word = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        print(f'{random_word}: {already_exists_in_bloom_filter(random_word)}')

    print('Done')
