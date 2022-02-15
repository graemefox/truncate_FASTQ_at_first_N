#!/usr/bin/env python3
import gzip
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="The gzip-ed FASTQ file you want to truncate at first instance of an N.")
parser.add_argument("-o", "--output_dir", help="Directory to write the truncated files to - provide full path")
args = parser.parse_args()

output_file=args.output_dir+args.input.split("/")[1]

with gzip.open(output_file, mode='w', compresslevel=9, encoding=None, errors=None, newline=None) as output_file:
    with gzip.open(args.input, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None) as input_file:
        count = 1
        for line in input_file:
            if count == 1:
                output_file.write(line.decode('ascii').encode('utf-8'))
                count=1
            if count == 2:
                nuc_count = 0
                N_switch=0
                for nuc in str(line.decode('ascii')):
                    if not nuc=="N":
                        nuc_count = nuc_count+1
                    if nuc == "N":
                        N_switch = 1
                        first_N=nuc_count
                        break
                if N_switch == 1:
                    output_seq = line.decode('ascii')[:nuc_count]+"\n"
                    output_file.write(output_seq.encode('utf-8'))
                if N_switch == 0:
                    output_file.write(line.decode('ascii').encode('utf-8'))
                count=2
            if count == 3:
                output_file.write(line.decode('ascii').encode('utf-8'))
                count=3
            if count == 4:
                if N_switch == 1:
                    output_qual = line.decode('ascii')[:nuc_count]+"\n"
                    output_file.write(output_qual.encode('utf-8'))
                if N_switch == 0:
                    output_file.write(line.decode('ascii').encode('utf-8'))
                count = 0
            count = count + 1
