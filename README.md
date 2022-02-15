# truncate_FASTQ_at_first_N
Python script to truncate the reads in a gzip-ed FASTQ file at the first instance of an 'N' in the sequence.

The script has two required parameters: -i and -o.

-i is the compressed (fq.gz) input FASTQ format file that you want to truncate.

-o is the output directory where you would like the truncated FASTQ file to be written.

Example:

./truncate_at_first_N.py -i input_file.fastq.gz -o output_dir/
