# coding: utf-8
import screed
import glob
import os
option1 = 'protein tyrosine phosphatase, receptor type, c'
option2 = 'receptor-type tyrosine-protein phosphatase c'
option3 = 'PTPRC'
option4 = 'leukocyte common antigen'
options = option1, option2, option3, option4

with open('ncbi_refseq_vertebrate_mammalian_ptprc.fasta', 'w') as f:

    for filename in glob.iglob('*faa.gz'):
        for record in screed.open(filename):
            name = record['name'].lower()
            if any(option in name for option in options):
                f.write(f">{record['name']}\n{record['sequence']}\n")
                
