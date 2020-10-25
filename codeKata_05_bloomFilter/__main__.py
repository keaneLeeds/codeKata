import hashlib
import random
import string
import numpy as np
import nltk
from nltk.corpus import words
from functools import partial
import argparse


A = ''
n: int = 0
m: int = 0
k: int = 0
v: np.ndarray = []
H = []


def import_nltk_corpus_words() -> None:
    """Imports the words corpus from nltk

    the words corpus from nltk is 234377 unique english words
    """

    nltk.download('words', quiet=True)


def produce_hash_function(prefix: int, length: int, text: str) -> str:
    """Returns a hash string large enough to cover size m

    Produces a hexadecimal digest from a sha256 hash of the input string,
    prefixed with the value of argument prefix, and slices the desired
    number of characters from it
    """

    return hashlib.sha3_256(f'{prefix}{text}'.encode('utf-8')).hexdigest()[:length]


def create_hashes():
    """Creates a list of hash functions that only need a text argument

    the hash functions set the prefix and length arguments of the produce_hash_function function
    """

    return [partial(produce_hash_function, prefix, (m // 16) + 1) for prefix in range(k)]


def fill_bloom_filter() -> None:
    """Creates the bloom filter

    for each a ∈ A the bits in positions v[h_1(a)], v[h_2(a)],..., v[h_k(a)] are set to 1
    """

    for a in A:
        for h in range(k):
            v[int(H[h](a), 16) % m] = 1  # test this, I think the mod is wrong


def default_words_test() -> None:
    """A small set of words to use as a sanity test for the bloom filter"""
    print(f'f: {already_exists_in_bloom_filter("f")}')
    print(f'zed: {already_exists_in_bloom_filter("zed")}')
    print(f'wonderful: {already_exists_in_bloom_filter("wonderful")}')
    print(f'random: {already_exists_in_bloom_filter("wonderful")}')
    print(f'indubitably: {already_exists_in_bloom_filter("indubitably")}')


def random_words_test(number_of_tests: int) -> None:
    """Random, 5-character words to use to check the false drop frequency"""
    for _ in range(number_of_tests):
        random_word = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        print(f'{random_word}: {already_exists_in_bloom_filter(random_word)}')


def already_exists_in_bloom_filter(entry: str) -> bool:
    """Checks if entry already exists in the bloom filter"""

    hashes = np.array([v[int(H[h](entry), 16) % m] for h in range(k)])
    return np.all(hashes == 1)


def characterize_bloom_filter() -> None:
    raise NotImplemented('Not implemented yet')


def get_args() -> argparse.Namespace:
    """Parses commandline arguments"""
    parser = argparse.ArgumentParser(
        prog='bloomFilter',
        description='Create a bloom filter, or characterize the bloom filter')
    parser.add_argument(
        '-A',
        default='',
        type=str,
        dest='A',
        help='a file, or list of words to add to the bloom filter')
    parser.add_argument(
        '-m',
        default=0,
        type=int,
        dest='m',
        help='the size of the hash output')
    parser.add_argument(
        '-k',
        default=4,
        type=int,
        dest='k',
        help='the number of independent hash functions')
    parser.add_argument(
        '-t', '--tests',
        default=10,
        type=int,
        dest='number_of_tests',
        help='the number of 5 character tests to run')
    parser.add_argument(
        '--runTests',
        default=True,
        type=bool,
        dest='run_tests',
        help='run the 5 characters test')
    parser.add_argument(
        '--defaultTests',
        default=False,
        type=bool,
        dest='default_tests',
        help='run the default word tests or not')
    parser.add_argument(
        '--characterize',
        action='store_true',
        help='Characterize the bloom filter with respect to false drops')
    return parser.parse_args()


def set_bloom_filter_values() -> None:
    """Sets the values that characterize a given bloom filter"""
    global A, n, m, v, k, H

    if args.A == '':
        import_nltk_corpus_words()
        # remove duplicates based on capitalization and convert back to a list
        A = list(set(i.lower() for i in words.words()))
        # sort the list alphabetically
        A.sort()
    elif args.A.endswith('.txt'):
        file = open(args.A, 'r')
        A = file.read()
        file.close()
    else:
        raise ValueError(f'Unsupported document type: {args.A}')

    n = len(A)

    if args.m == 0:
        m = n*4
    else:
        m = args.m

    v = np.zeros(m)
    k = args.k
    H = create_hashes()


if __name__ == '__main__':
    """Implementation of a bloom filter
    
    For set A = {a_1, a_2, ..., a_n}
    create a vector v of size m, initialized to 0
    create k independent hash functions h_1,h_2,...,h_k, with range 1..m
    for each a ∈ A the bits in positions h_1(a),h_2(a),...,h_k(a) are set to 1
    
    to check if an input is already in the bloom filter, check the array locations for zeros.
    """

    args = get_args()
    set_bloom_filter_values()

    fill_bloom_filter()

    if args.default_tests:
        default_words_test()

    if args.run_tests:
        random_words_test(args.number_of_tests)

    if args.characterize:
        characterize_bloom_filter()

    print('Done')
