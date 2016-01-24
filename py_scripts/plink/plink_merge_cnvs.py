#!/usr/bin/env python
#
#
#
#
import argparse


def print_small_association(plink_cnv):
    with open(plink_cnv) as assoc:
        old_p = -1
        no_printed = 0
        no_probes = 0
        for i, line in enumerate(assoc):
            if i != 0:
                line_s = line.strip().split() 
                emp_1 = float(line_s[2])
                if (emp_1 == 1 or old_p != emp_1): 
                    if (no_printed > 0):
                        print chrom,start_pos,end_pos,old_p,emp_2,no_probes
                        no_probes = 0
                        start_pos = line_s[1].split('-')[1]
                    else:
                        start_pos = line_s[1].split('-')[1]
                    no_printed += 1
                chrom = line_s[0]
                end_pos = line_s[1].split('-')[1]
                old_p = emp_1
                emp_2 = float(line_s[3])
                no_probes += 1
def main():
    parser= argparse.ArgumentParser(description="Merges SNPs from PLINK CNV output")
    parser.add_argument("plink_cnv")
    args = parser.parse_args()
    print_small_association(args.plink_cnv)

if __name__=="__main__":
    main()
