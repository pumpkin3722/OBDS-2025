import argparse
import gzip


parser = argparse.ArgumentParser()
parser.add_argument('-o', dest='outfile', default='out.bed.gz', help='output file(default out.bed)')
parser.add_argument('-i', '--input', dest='infile', help='Input file name (required)')
parser.add_argument('-p', '--pad', dest='pad', type=int, default=0, help="Specified number of bases to each end of each interval")
parser.add_argument('-f', '--fragments', action='store_true', help="Output fragments instead of individual reads")
args = parser.parse_args()

with open(args.infile, 'r') as sam, gzip.open(args.outfile, 'wt') as bed: 
         for line in sam:
            if not line.startswith("@"):
                result = line.split("\t")
                if result[2][0:3] == 'chr':
                    chrom = result[2]
                    start = int(result[3])-1-args.pad
                    end = start+len(result[9])+args.pad*2
                    name = result[0]
                    score = result[4]
                    bed.write(f'{chrom}\t{start}\t{end}\t{name}\t{score}\n')
                    

