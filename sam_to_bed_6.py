import argparse
import gzip


parser = argparse.ArgumentParser()
parser.add_argument('-o', dest='outfile', default='out.6.bed', help='output file(default out.bed)')
parser.add_argument('-i', '--input', dest='infile', help='Input file name (required)')
parser.add_argument('-p', '--pad', dest='pad', type=int, default=0, help="Specified number of bases to each end of each interval")
parser.add_argument('-f', '--fragments', action='store_true', help="Output fragments instead of individual reads")
args = parser.parse_args()

with open(args.infile, 'r') as sam, open(args.outfile, 'wt') as bed: 
        previous_result = None
        for line in sam:
            if not line.startswith("@"):
                result = line.split("\t")
                if result[2][0:3] == 'chr':                
                    if args.fragments:
                        if previous_result:
                            if previous_result[3] == result[7]:
                                chrom = result[2]
                                start = min(int(result[3]),int(previous_result[3]))-1-args.pad
                                end = start + abs(int(result[8]))+args.pad*2
                                name = result[0]
                                score = result[4]
                                bed.write(f'{chrom}\t{start}\t{end}\t{name}\t{score}\n')
                            elif previous_result[7] == result[3]:
                                chrom = result[2]
                                start = min(int(result[3]),int(previous_result[3]))-1-args.pad
                                end = start + abs(int(result[8]))+args.pad*2
                                name = result[0]
                                score = result[4]
                                bed.write(f'{chrom}\t{start}\t{end}\t{name}\t{score}\n')
                            else:
                                # Write the previous line here
                                chrom = result[2]
                                start = int(result[3])-1-args.pad
                                end = start+len(result[9])+args.pad*2
                                name = result[0]
                                score = result[4]
                                # Store lines in a varible not writting until next line?
                                bed.write(f'{chrom}\t{start}\t{end}\t{name}\t{score}\n')
                            # last line??
                    else:
                        chrom = result[2]
                        start = int(result[3])-1-args.pad
                        end = start+len(result[9])+args.pad*2
                        name = result[0]
                        score = result[4]
                        bed.write(f'{chrom}\t{start}\t{end}\t{name}\t{score}\n')
                previous_result = result    

