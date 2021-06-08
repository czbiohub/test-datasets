# How the test data was created

## Fastq files

1. Subsample fastq file by 10% with seqtk

```
(base)
 Mon 31 May - 11:11  ~/code/nf-core/test-datasets/testdata   origin ☊ olgabot/sicilian ↑1 28☀ 4‒ 
  seqtk seq -f 0.1 -s 0 MACA_24m_M_BLADDER_59__subsample-10-percent_mm10_chr19_R2.fastq.gz| gzip -c > MACA_24m_M_BLADDER_59__subsample-1-percent_mm10_chr19_R2.fastq.gz
(base)
 Mon 31 May - 11:12  ~/code/nf-core/test-datasets/testdata   origin ☊ olgabot/sicilian ↑1 29☀ 4‒ 
  seqtk seq -f 0.1 -s 0 MACA_24m_M_BLADDER_58__subsample-10-percent_mm10_chr19_R2.fastq.gz| gzip -c > MACA_24m_M_BLADDER_58__subsample-1-percent_mm10_chr19_R2.fastq.gz
 ```

1. Align as usual using nf-sicilian pipeline
1. Download bams from AWS
1. Extract reads aligned to chromosome 19 and save to new file

## Get chromosome 19 reads from bam
### One-liner to create chr19 testdata

```bash
for BAM in $(ls *out.bam); do SORTED=$(echo $BAM | sed s:.bam:.sorted.bam:) ; echo $SORTED ; samtools sort -o $SORTED -O bam -@ 4 $BAM ; samtools index $SORTED ; CHR19=$(echo $SORTED | sed s:.sorted.bam:.sorted.chr19.bam:); samtools view -bh $SORTED chr19 > $CHR19 ; R2=$(echo $BAM | cut -f1 -d '.'| sed s:T1::)_mm10_chr19_R2.fastq.gz ; samtools fastq $CHR19 | gzip -c > $R2 ; echo $R2 ; done
```

### One-liner to create chrM testdata

```bash
for BAM in $(ls *subsample*out.bam); do SORTED=$(echo $BAM | sed s:.bam:.sorted.bam:) ; echo $SORTED ; samtools sort -o $SORTED -O bam -@ 4 $BAM ; samtools index $SORTED ; CHRM=$(echo $SORTED | sed s:.sorted.bam:.sorted.chrM.bam:); samtools view -bh $SORTED chrM > $CHRM ; R2=$(echo $BAM | cut -f1 -d '.')_mm10_chrM_R2.fastq.gz ; samtools fastq $CHRM > $R2 ; echo $R2 ; done
```


## Get R1 paired reads from R2 read ids

### One-liner

```bash
for FASTQ in $(ls *subsample-1-percent_mm10_chr19_R2.fastq.gz) ; do echo $FASTQ ; READ_IDS=$(echo $FASTQ | sed s:.fastq.gz:__read_ids.txt:) ; gzcat $FASTQ | bioawk -c fastx ' { print $name } ' | cut -f 1 -d '_' > $READ_IDS ; SAMPLE_ID=$(echo $FASTQ | sed s:__subsample-1-percent_mm10_chr19_R2.fastq.gz::) ; for READS in $(ls "$SAMPLE_ID*.subsample-10-percent.fastq.gz") ;do echo $READS ; done ; done
```
