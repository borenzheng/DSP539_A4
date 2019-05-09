# Usage: $ python sequence.py filename  k
# e.g. $ python sequence.py ./sequence.txt 2

import pandas as pd
import plotnine as p9
import sys

def count_okmers(seq, k):
    """
    Summary line: count observed kmers of size k

    Parameters:
    seq (list): the input sequence
    k (int): a substring of length 

    Return:
    int: the number of observed kmers
    """
    o_kmers = set()
    for i in range(0,len(seq)-k+1):
        o_kmers.add(''.join(seq[i:i+k]))
    return len(o_kmers)


def count_pkmers(seq, k):
    """
    Summary line: count possible kmers of size k

    Parameters:
    seq (list): the input sequence
    k (int): a substring of length 

    Return:
    int: the number of possible kmers
    """
    l = len(seq)
    if l > 4**k:
        p_kmers = 4**k
    else: p_kmers = l - k + 1
    return p_kmers


def frame(k_list, o_list, p_list):
    """
    Summary line: create a pandas data frame containing all possible k 
    and the associated number of observed and expected kmers

    Parameters:
    k_list (list): a list of k values
    o_list (list): a list of observed kmers based on k values list
    p_list (list): a list of possible kmers based on k values list

    Return: data frame  
    """
    kmers_df = pd.DataFrame(
     {'k':k_list,
       'Observed kmers': o_list,
       'Possible kmers': p_list    
     }
    )
    return kmers_df


def plot(kmers_df,o_list,p_list):
    """
    Summary line: produce a graph from the data frame of the proportion of 
    each kmer observed

    Extended description: the x axis is the value of k, 
    the y axis is the proportion of observed kmers which calculated by 
    observed kmers / possible kmers

    Parameters:
    kmers_df: a data frame
    o_list (list): a list of observed kmers based on k values list
    p_list (list): a list of possible kmers based on k values list

    Return: plot
    """ 
    okmers_proportion = [x/y for x, y in zip(o_list, p_list)]
    p = p9.ggplot(data = kmers_df,
             mapping = p9.aes(x = 'k',
                             y = 'okmers_proportion')) + p9.geom_point() + \
    p9.scale_x_continuous(breaks = range(0,30))
    p.draw()


def ling_complex(o_list, p_list): 
    """
    Summary line: calculate linguistic complexity

    Parameters:
    o_list (list): a list of observed kmers based on k values list
    p_list (list): a list of possible kmers based on k values list

    Return: 
    float: the value of linguistic complexity  
    """ 
    complexity = sum(o_list) / sum(p_list)
    return complexity


def output(filename, k):
    """
    Summary line: output the results

    Parameters:
    filename: path to the sequence file
    k (int): a substring of length
    """ 
    file = open(filename,'r')
    data = [list(x.strip()) for x in file.readlines()]
    for i in range(0, len(data)):
        seq = data[i]
        k_list = list(range(1,len(seq)+1))
        o_list = [count_okmers(seq,x) for x in k_list]
        p_list = [count_pkmers(seq,x) for x in k_list]
        kmers_df = frame(k_list, o_list, p_list)
        print('Sequence length:',len(seq),', Observed kmers:', count_okmers(seq, k),
        ', Possible kmers:', count_pkmers(seq, k))
        print('linguistic complexity:', ling_complex(o_list,p_list))
        print(kmers_df)
        #plot(kmers_df,o_list,p_list)
 
 
def main(): 
    """
    filname = "./sequence.txt", path to the sequence file
    k is a substring of length, interger 
    """   
    filename = sys.argv[1]
    k = int(sys.argv[2])
    output(filename, k)

if __name__ == '__main__':
    main()