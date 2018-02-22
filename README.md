# SPRINT

Tips:
________________________

1. Edited reads can be extracted from "tmp/all_combined.zz".

all_combined.zz :

| Chr | SAM_Flag | MapQ | Loc | SNV | BaseQ | Read-loc | Seq | Read-name | Fragment-loc |

Users can use zz2sam.py to convert 'tmp/all_combined.zz' into BAM format (Download: zz2sam.zip, python2.7): 

Step 1:  Please move to the output-directory of SPRINT, and download zz2sam.zip;

Step 2: "unzip zz2sam.zip";

Step 3: "python zz2sam.py tmp/all_combined.zz";

Step 4: "samtools view -H tmp/genome/all.bam > SAMheader.txt";

Step 5: "cat SAMheader.txt tmp/all_combined.zz.sam > all_combined.zz.sam.header";

Step 6: "samtools view -bS all_combined.zz.sam.header > all_combined.zz.bam";

Step 7: "samtools sort all_combined.zz.bam -f all_combined.zz.sorted.bam".

________________________

2. Get A-to-I RESs from the ouput directory of SPRINT.

Users can use getA2I.py to extract A-to-I RESs from the output of SPRINT (version>=0.1.7)

python   |  getA2I.py   |  0 (1 for strand-specific data)   |  SPRINT_OUT   |   A_to_I_OUT

________________________

3. About "Supporting reads" and "AD":

For a given RES,

Supporting reads (regular-RES): mapped high-quality reads (MQ>=20 AND BASEQ >=25 AND fragment-loc >5);
Supporting reads (hyper-RES): remapped high-quality reads (BASEQ >=25 AND fragment-loc >5 AND Poly(N) <10 AND n(C)+n(T)<20);
AD (all RES): mapped reads (without the restriction of quality) + remapped reads (without the restriction of quality).
________________________

4. Change RepeatMasker File (rmsk) into BED file (used by SPRINT):

Step 1:  Users can get RepeatMasker file from UCSC Table Browser (http://genome.ucsc.edu/cgi-bin/hgTables).



Step 2: python  | rp2bed.py  |  hg38.rmsk  |  hg38_repeat.bed

________________________

5. About A-to-I (A-to-G) rate:

For strand-specific data, “AG +” and "TC -"  are all thought to be A-to-G (A-to-I editing). 
For non-strand-specific data, there are two ways to estimate the A-to-G rate:
a. "AG +/-" + "TC +/-". Disadvantages: overestimate the A-to-G rate
b. assign the strand of sites by using GENE annotations (e.g. ENSEMBL, REFSEQ, GENCODE, etc.) , and then: "AG +" + "TC -".  Disadvantages: gene region only, underestimate the A-to-G rate (the opposite strand may also have transcript )
________________________
