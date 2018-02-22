import sys
fi=open(sys.argv[1])
fo=open(sys.argv[1]+'.sam','w')
for line in fi:
    seq=line.rstrip().split('\t')
    chrr=seq[0]
    sss=seq[7]
    mapq=seq[2]
    rangee=seq[3].split(';')
    name=seq[8]
    j=1
    for one in rangee:
        start=int(one.split(':')[0])
        end=int(one.split(':')[1])
        lll=end-start+1
        this_sss = sss[0:lll]
        sss=sss[lll:]
        fo.write(name+'_'+str(j)+'\t0\t'+chrr+'\t'+str(start)+'\t'+mapq+'\t'+str(lll)+'M\t*\t0\t0\t'+this_sss+'\t'+'a'*lll+'\n')
        j+=1
    
