## How this test data was created

After downloading whole-genome aligned bams, the data was subset to only mouse chromosome 19 (the smallest chromosome) and all reads were output to a single fastq file, and called R2 because the R2 read for droplet data is the one with sequence that can be aligned.

```bash
for BAM in $(ls *out.bam); do
    SORTED=$(echo $BAM | sed s:.bam:.sorted.bam:)
    echo $SORTED
    samtools sort -o $SORTED -O bam -@ 4 $BAM
    samtools index $SORTED
    CHR19=$(echo $SORTED | sed s:.sorted.bam:.sorted.chr19.bam:)
    samtools view -bh $SORTED chr19 > $CHR19
    R2=$(echo $BAM | cut -f1 -d '.')_mm10_chr19_R2.fastq.gz
    samtools fastq $CHR19 > $R2
    echo $R2
done
```
