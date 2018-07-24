import sys

import gzip
fzz=gzip.open(sys.argv[1], 'r')
fALL_A_to_I=open(sys.argv[2])
fo=open(sys.argv[3],'w')

SNV={}

for line in fzz:
    seq=line.rstrip().split('\t')
    if seq[4] !='*':
        CHR=seq[0]
        THIS_SNV=seq[4].split(';')
        for snv in THIS_SNV:
            sss=snv.split(':')
            LOC=sss[1]
            TYP=sss[0]

            try:
                SNV[CHR+':'+LOC+':'+TYP]+=1
            except Exception as e:
                SNV[CHR+':'+LOC+':'+TYP]=1

for line in fALL_A_to_I:
    seq=line.rstrip().split('\t')
    CHR=seq[0]
    LOC=seq[2]
    TYP=seq[3]
    try:
        output=CHR+'\t'+LOC+'\t'+TYP+'\t'+str(SNV[CHR+':'+LOC+':'+TYP])+'\n'
        fo.write(output)
    except Exception as e:
        pass
