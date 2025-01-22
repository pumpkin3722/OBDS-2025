import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--inputa', dest='inputa', required=True, help="Input file A")
parser.add_argument('-b', '--inputb', dest='inputb', required=True, help="Input file B")
parser.add_argument('-o', '--output', dest='outfile', default='output1.bed', help="Output file (default: output.bed)")
args = parser.parse_args()

with open(args.inputa, 'r') as beda, open(args.inputb, 'r') as bedb, open(args.outfile, 'wt') as opt:
    for line_a in beda:
        result_a = line_a.split("\t")
        chra = result_a[0]
        starta = int(result_a[1])
        enda = int(result_a[2])
        bedb.seek(0)
        for line_b in bedb:
            result_b = line_b.split("\t")
            chrb = result_b[0]
            startb = int(result_b[1])
            endb = int(result_b[2])
            if chra == chrb:
                if startb <= enda and endb >= starta: 
                    intervalstart = max(starta, startb)
                    intervalend = min(enda, endb)
                    opt.write(f"{chra}\t{intervalstart}\t{intervalend}\n")
                    break