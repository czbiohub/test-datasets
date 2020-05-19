# coding: utf-8
import pandas as pd
df = pd.read_csv("molecule-protein_ksize-27_log2sketchsize-14_trackabundance-true__mini_subset_smallest_bams.csv")
df['bam_github'] = df.bam.str.replace('/home/olga/ibm_lg/kmer-hashing/brawand2011/nfcore-rnaseq/bonobo/single_end/STAR/', 'https://github.com/czbiohub/test-datasets/raw/olgabot/predictorthologs--orthology-featurecounts/testdata/featurecounts/')
df['bam_github'] = df.bam_github.str.replace('/home/olga/ibm_lg/kmer-hashing/brawand2011/nfcore-rnaseq/macaque/single_end/STAR/', 'https://github.com/czbiohub/test-datasets/raw/olgabot/predictorthologs--orthology-featurecounts/testdata/featurecounts/')
df['gtf_github'] = df['gtf'].str.replace(
'/home/olga/ibm_lg/kmer-hashing/brawand2011/gtfs_with_orthology/',
'https://github.com/czbiohub/test-datasets/raw/olgabot/predictorthologs--orthology-featurecounts/testdata/featurecounts/')
df.head()
df['gtf_github'].values
get_ipython().run_line_magic('ls', '')
df['gtf_github'] = df['gtf_github'].str.replace('.gtf', '.diffhash_subset.gtf')
df['gtf_github'].values
df
df.fasta.values
df['fasta_github'] = df['fasta'].str.replace('/home/olga/ibm_lg/kmer-hashing/brawand2011/kmermaid_uniprot_opisthokonta/extract_coding/', 'https://github.com/czbiohub/test-datasets/raw/olgabot/predictorthologs--orthology-featurecounts/testdata/featurecounts/')
df['fasta_github']
df['fasta_github'].values
df.columns
df['sig'].values
df['sig_github'] = df['sig'].str.replace('/home/olga/ibm_lg/kmer-hashing/brawand2011/kmermaid_existing_peptides_uniprot_opisthokonta/sketches_peptide/molecule-protein_ksize-27_log2sketchsize-14_trackabundance-true/',  'https://github.com/czbiohub/test-datasets/raw/olgabot/predictorthologs--orthology-featurecounts/testdata/featurecounts/')
df['sig_github'].values
df.head()
df.columms
df.columns
df.species
samples = df.set_index('sample_id')[['group', 'species', 'bam_github', 'gtf_github', 'fasta_github', 'sig_github']]
samples.head()
samples.values
samples.columns = samples.columns.str.split('_github').str[0]
samples.head()
samples.columns
samples.to_csv('samples_cleaned_for_github.csv')
get_ipython().run_line_magic('save', 'sample_cleaning.py 1-30')
get_ipython().run_line_magic('ll', '')
import glob
for fasta in glob.glob('*fasta'):
    if 'coding_reads' in fasta:
        continue
    fasta2 = fasta.replace('.fasta', '__coding_reads_peptides.fasta')
    get_ipython().system(' mv $fasta $fasta2')
    
get_ipython().run_line_magic('ls', '')
