# Use Bioawk to extract read ids of fasta
bioawk -c fastx '{ print $name }' ncbi_refseq_vertebrate_mammalian_ptprc.fasta > ncbi_refseq_vertebrate_mammalian_ptprc_ids.txt

# Create a header file for the tab-separated output
zcat prot.accession2taxid.gz| head -n 1 > prot.accession2taxid.header.txt

# Find the read ids in the gzipped file, add the heaer
zgrep --fixed-strings -f \
	~/data_lg/czbiohub-reference/ncbi/refseq/releases/refseq-release98-2020-02-06/vertebrate_mammalian/ncbi_refseq_vertebrate_mammalian_ptprc_ids.txt prot.accession2taxid.gz  \
	| cat prot.accession2taxid.header.txt -  \
	| gzip -c - > prot.accession2taxid.vertebrate_mammalian_ptprc.with_header.txt.gz
