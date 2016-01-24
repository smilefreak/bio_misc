#!/usr/bin/env python
#
# Parses the CNV group summary and mperm and generates a table for presentation
#


import argparse


def print_table(perm,group):
    with open(perm) as p:
        with open(group) as g:
            i = 0
            l_1 = g.readline()
            l_index = [0,2,3]
            l_2 = p.readline()
            while( i < 6 ):
                l_1=l_1.split()
                if ( i != 1):
                    l_2=l_2.split()
                if i == 0:
                    print '\t'.join([l_1[index] for index in l_index]) + '\tP value'
                    l_2 = p.readline()
                elif i == 1:
                    print '\t'.join([l_1[index] for index in l_index])
                else:
                    print '\t'.join([l_1[index] for index in l_index]) + '\t' + l_2[2]
                    l_2 = p.readline()

                l_1 = g.readline()
                i+=1


def main():
    parser = argparse.ArgumentParser(description="Parse PLINK burden to excel")
    parser.add_argument("-p", '--permutation', dest='permutation', required=True)
    parser.add_argument("-g", "--group-summary", dest='group', required=True)
    args = parser.parse_args()
    print_table(args.permutation,args.group)

if __name__ == "__main__":
    main()
