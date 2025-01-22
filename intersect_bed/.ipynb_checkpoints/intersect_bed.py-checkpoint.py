import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--inputa', dest='inputa', required=True, help="Input file A")
parser.add_argument('-b', '--inputb', dest='inputb', required=True, help="Input file B")
parser.add_argument('-o', '--output', dest='outfile', default='output.bed', help="Output file (default: output.bed)")
args = parser.parse_args()

with open(args.inputa, 'r') as beda,open(args.inputb, 'r') as bedb, open(args.outfile, 'wt') as opt:
    la=[]
    lb=[]
    for line in beda:
        result = line.split("\t")
        chra=result[0]
        starta=int(result[1])
        enda=int(result[2])
        la.append((chra, starta, enda))
        
    for line in bedb:
        result = line.split("\t")
        chrb=result[0]
        startb=int(result[1])
        endb=int(result[2])
        lb.append((chrb, startb, endb))
    
    for inta in la:
        for intb in lb:
            if inta[0] == intb[0]:
                if intb[1] <= inta[2] and intb[2]>=inta[1]:
                    intervalstart=max(inta[1],intb[1])
                    intervalend=min(inta[2],intb[2])
                    opt.write(f"{inta[0]}\t{intervalstart}\t{intervalend}\n")
                    break