#!/usr/bin/env python
#
# Looks for NS within a sequence.
#


import argparse
import pyfasta
import logging 
logger = logging.getLogger(__name__)
def get_position_of_ns(args):
    fasta_input = args.fasta_input
    fasta = pyfasta.Fasta(fasta_input)
    key = fasta.keys()
    sequence = fasta[key[0]]
    for i, base, in enumerate(sequence):
        if base == "N":
            logger.info("Position: {0}".format(i + 1))

def remove_n_near(args):
    fasta_input = args.fasta_input
    fasta = pyfasta.Fasta(fasta_input)
    n_to_remove = int(args.position_to_remove)
    n_to_remove -= 1
    keys = fasta.keys()
    for key in keys:
        print ">" + key
        logging.info("Processing {0}".format(key))
        no_matches_in_fasta = 0 
        sequence = fasta[key]
        for i in range(n_to_remove - 10, n_to_remove + 10):
                if (sequence[i] == "N"):
                    no_matches_in_fasta += 1
                    logging.info("got match #{0}".format(no_matches_in_fasta))
                    sequence = sequence[:i] + sequence[(i+1):]
        logger.info("Number of N matches in 20 bp window nearby = {0}".format(no_matches_in_fasta)) 
        print sequence 

def main():
    parser = argparse.ArgumentParser(description="Print positions of Ns in a fasta sequence")
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("fasta_input", help="Fast input to print out Ns from")
    parent_parser.add_argument('-l','--log-file',  dest="log_file", help="Log fil output", default="n_outputs.txt")
    subparsers = parser.add_subparsers(title="subcommands",
                                       description="valid subcommands",
                                       help="Additional help")
    npos = subparsers.add_parser('npos', parents=[parent_parser])
    npos.set_defaults(func=get_position_of_ns)
    nrm = subparsers.add_parser('nrm', parents=[parent_parser])
    nrm.set_defaults(func=remove_n_near)
    nrm.add_argument('-p', '--position', dest="position_to_remove", help="Position to remove", required=True)
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s %(message)s',
                   filemode='w', filename=args.log_file, level=logging.INFO)
    args.func(args)

if __name__ == "__main__":
    main()
