import re

splitted = {
    'left': '',
    'right': ''
}
side = ''

with open('task2.fa', 'r') as fasta:
    for line in fasta.readlines():
        if line[0] == '>':
            if re.search("left", line):
                side = 'left'
            elif re.search(r"right", line):
                side = 'right'
        splitted[side] += line

    for entry in splitted.items():
        print(entry[0])
        print(entry[1])
        print('')
        with open('task2-' + entry[0] + '.fasta', 'w') as outfile:
            outfile.write(entry[1])