import utils

class fastq():
    __quality = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    def __init__(self, content = None):
        self.content = content

    def check(self):
        """
        Returns True if sequence and quality strings are not split.
        """
        i = 1
        integrity = True
        for line in self.content.split('\n'):
            if i % 4 == 1: 
                integrity = integrity and (line[0] == '@')
            elif i % 4 == 3:
                integrity = integrity and (line[0] == '+')
            elif i % 4 == 0:
                for c in line:
                    integrity = integrity and (c in self.__quality)
            i+=1
        return integrity

    def to_fasta(self):
        if not self.check():
            print("Invalid .fastq")
            return
        seqs = {}
        fasta = ''
        i = 1
        
        for line in self.content.split('\n'):
            if i % 4 == 1:
                header = line[1:]
                if not (header in seqs.keys()):
                    seqs[header] = ''
            if i%4 == 2:
                seqs[header] += line[:-1]
            i += 1

        for key in seqs.keys():
            fasta += utils.wrap(seqs[key], key) + '\n'
        
        return fasta
        

def main():
    with open('example.fastq', 'r') as ex:
        fq = fastq(ex.read())

    if not fq.check():
        return 0

    print(fq.to_fasta())

if __name__ == '__main__':
    main()

