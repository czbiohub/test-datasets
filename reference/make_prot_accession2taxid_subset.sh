
DIR=/mnt/ibm_lg/olga/czbiohub-reference/ncbi/refseq/releases/refseq-release98-2020-02-06/vertebrate_mammalian
PTPRC_IDS=$DIR/ncbi_refseq_vertebrate_mammalian_ptprc_ids.txt
PROT_ACCESSION=prot.accession2taxid.gz
HEADER=prot.accession2taxid.header.txt

echo "Extracting PTPRC sequence ids ..."
time bioawk -c fastx '{ print $name }' $DIR/ncbi_refseq_vertebrate_mammalian_ptprc.fasta > $PTPRC_IDS
echo "\tDone!"

echo "Making header for protein accession tsv ..."
time zcat $PROT_ACCESSION | head -n 1 > $HEADER
echo "\tDone!"

echo "Searching for the PTPRC sequence ids in the prot2accession file ..."
time zgrep --fixed-strings \
      -f $PTPRC_IDS $PROT_ACCESSION \
    | cat $HEADER -  \
    | gzip -c - > prot.accession2taxid.vertebrate_mammalian_ptprc.with_header.txt.gz
echo "\tDone!"
