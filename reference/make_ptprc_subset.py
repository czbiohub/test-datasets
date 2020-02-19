# coding: utf-8
import screed
import glob
import os
option1 = 'protein tyrosine phosphatase, receptor type, C'
option2 = 'receptor-type tyrosine-protein phosphatase C'
with open('ncbi_refseq_vertebrate_mammalian_ptprc.fasta', 'w') as f:

    for filename in glob.iglob('*faa.gz'):
        for record in screed.open(filename):
            if option2 in record['name'] or option1 in record['name']:
                f.write(f">{record['name']}\n{record['sequence']}\n")
                
