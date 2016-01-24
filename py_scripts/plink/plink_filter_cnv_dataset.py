#!/usr/bin/env python
#
#
# @author James Boocock
# @date 14 December 2015
# 
# Filters PLINK CNV file by a criteria given by user.

import argparse

class inputRange(object):
    """
        Represents an input range for analysis.
    """
    def __init__(self,range_string):
        range_string = range_string.split('-')
        self.start = int(range_string[0])
        self.end = int(range_string[1])


    def __str__(self):
        print(self.start + "-" + self.end)

def filter_cnvs(cnv_input, dup_range, del_range):
    """
        Process plink CNV file and filters it by criteria specified by user.

        CNV Input is in the following format ( tab-delimited )
        FID     IID     CHR     BP1     BP2     TYPE    SCORE   SITES
    """
    dup_range = inputRange(dup_range)
    del_range = inputRange(del_range)
    with open(cnv_input) as cnvs:
        for i, line in enumerate(cnvs):
            line = line.strip()
            if i == 0:
                print line
            else:
                l_s = line.split("\t")
                size = int(l_s[4]) - int(l_s[3])
                # 0,1 deletion >3 duplication
                type_cnv = int(l_s[5])
                if type_cnv < 2:
                    if size > del_range.start and size < del_range.end:
                        print line
                elif type_cnv > 2:
                    if size > dup_range.start and size < dup_range.end:
                        print line

def main():
    parser = argparse.ArgumentParser(description="Filter PLINK CNV for options missing from plink")
    parser.add_argument("--dup-length", dest="dup_range",required=True,
                        help="Range in bases of duplications be kept format=0-20000")
    parser.add_argument("--del-length", dest="del_range", required=True,
                        help="Range in bases of deletions to be kept format=0-20000")
    parser.add_argument("cnv_input", help="Plink CNV input")
    args = parser.parse_args()
    filter_cnvs(args.cnv_input, args.dup_range, args.del_range)

if __name__ == "__main__":
    main()
