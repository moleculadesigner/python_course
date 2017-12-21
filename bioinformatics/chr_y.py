import re

from utils import *


chrY_url = 'http://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chrY.fa.gz'

fs = get_archive(chrY_url)
fs_header = fs.split('\n')[0][1:]
chrY = ''.join(fs.split('\n')[1:])

complements = {
    'a':'t',
    'g':'c',
    'c':'g',
    't':'a',
    'A':'T',
    'G':'C',
    'C':'G',
    'T':'A',
    'N':'N',
    'n':'n'
    }

re_a = re.compile(r"[aA]")
re_g = re.compile(r"[gG]")
re_c = re.compile(r"[cC]")
re_t = re.compile(r"[tT]")
re_n = re.compile(r"[nN]")
nucleotides = {
    'A': re_a, 
    'G': re_g,
    'C': re_c,
    'T': re_t,
    'N': re_n
}

def main():
    ## 1
    forward_stats = {}
    backward_stats = {}
    print("1. Backward content:\n")
    for base in nucleotides.items():
        num = len(base[1].findall(chrY))
        forward_stats[base[0]] = num
        backward_stats[complements[base[0]]] = num
        print("   {}: {}".format(complements[base[0]], num))

    print("\n   Number of U in transcript: {}".format(backward_stats['T']))
    gcg = 100 * ((forward_stats['G']) + forward_stats['C']) / (forward_stats['G'] + forward_stats['C'] + forward_stats['T'] + forward_stats['A'])
    print("   Global GC content: {0:.2f}%\n".format(gcg))

    ## 2, 3
    seq = chrY[99999:100100]
    seq_reverse = seq[::-1]
    seq_reverse_complement = ''
    ## Reverse complement
    for base in seq_reverse:
        seq_reverse_complement += complements[base]
    print('2, 3. Sequence 100 000 : 100 100 processing\n')
    print(wrap(seq, 'Forward'))
    print(wrap(seq_reverse, 'Reverse'))
    print(wrap(seq_reverse_complement, 'Reverse-complement') + '\n')

    ## 4
    at = len(nucleotides['A'].findall(seq)) + len(nucleotides['T'].findall(seq))
    gc = len(nucleotides['G'].findall(seq)) + len(nucleotides['C'].findall(seq))
    print("4. Local GC content: {0:.2f}%".format(100*gc/(gc + at)))
    


if __name__ == '__main__':
    main()