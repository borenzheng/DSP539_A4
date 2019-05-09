# Usage: $ pytest test.py

from sequence import *

# Define a function to test count_okmers
def test_count_okmers():
    seq = ['A','T','T','T','G','G','A','T','T']
    k = 2
    obs = count_okmers(seq, k)
    exp = 5
    assert obs == exp

# Define a function to test count_pkmers
def test_count_pkmers():
    seq = ['A','T','T','T','G','G','A','T','T']
    k = 2
    obs = count_pkmers(seq, k)
    exp = 8
    assert obs == exp

# Define a function to test ling_complex
def test_ling_complex():
    seq = ['A','T','T','T','G','G','A','T','T']
    k = 2
    k_list = list(range(1,len(seq)+1))
    o_list = [count_okmers(seq,x) for x in k_list]
    p_list = [count_pkmers(seq,x) for x in k_list]
    obs = ling_complex(o_list, p_list)
    exp = 0.875
    assert obs == exp

