# coding: utf-8
import glob
for fastq in glob.glob('*subsample-1-percent_mm10_chr19_R2.fastq.gz'):
    read_ids = fastq.replace('.fastq.gz', '__read_ids.txt')
    command = f"gzcat {fastq} | bioawk -c fastx ' " + "{ print $name \}" + f' | cut -f 1 -d '_' > {read_ids}"
    get_ipython().system(' $command')
for fastq in glob.glob('*subsample-1-percent_mm10_chr19_R2.fastq.gz'):
    read_ids = fastq.replace('.fastq.gz', '__read_ids.txt')
    command = f"gzcat {fastq} | bioawk -c fastx ' " + "{ print $name \}" + f" | cut -f 1 -d '_' > {read_ids}"
    get_ipython().system(' $command')
    sample_id = fastq.split('__subsample')[0]
    for read in glob.glob(f'{sample_id}*.subsample-10-percent.fastq.gz'):
        print(read)
        
for fastq in glob.glob('*subsample-1-percent_mm10_chr19_R2.fastq.gz'):
    read_ids = fastq.replace('.fastq.gz', '__read_ids.txt')
    command = f"gzcat {fastq} | bioawk -c fastx " + "' { print $name \ }'" + f" | cut -f 1 -d '_' > {read_ids}"
    get_ipython().system(' $command')
    sample_id = fastq.split('__subsample')[0]
    for read in glob.glob(f'{sample_id}*.subsample-10-percent.fastq.gz'):
        print(read)
        read_subsample1 = read.replace('.subsample-10-percent.fastq.gz', '.subsample-1-percent.fastq.gz')
        command = f"rg -z -A 3 --file {read_ids} {read} | rg -v -F '--' - | gzip -c > {read_subsample1}"
        get_ipython().system(' $command')
        
        
for fastq in glob.glob('*subsample-1-percent_mm10_chr19_R2.fastq.gz'):
    read_ids = fastq.replace('.fastq.gz', '__read_ids.txt')
    command = f"gzcat {fastq} | bioawk -c fastx " + "' { print $name }'" + f" | cut -f 1 -d '_' > {read_ids}"
    get_ipython().system(' $command')
    sample_id = fastq.split('__subsample')[0]
    for read in glob.glob(f'{sample_id}*.subsample-10-percent.fastq.gz'):
        print(read)
        read_subsample1 = read.replace('.subsample-10-percent.fastq.gz', '.subsample-1-percent.fastq.gz')
        command = f"rg -z -A 3 --file {read_ids} {read} | rg -v -F '--' - | gzip -c > {read_subsample1}"
        get_ipython().system(' $command')
        
       
