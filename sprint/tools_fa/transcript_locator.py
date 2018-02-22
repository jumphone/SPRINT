def transcript_locator(fbed_in_dir=0,ftransloc_in_dir=0,fbed_out_dir=0):
    if fbed_in_dir==0 or ftransloc_in_dir==0:
        print 'fbed_in_dir\tftransloc_in_dir\tfbed_out_dir'
        return 0

    ftransloc=open(ftransloc_in_dir)
    fi=open(fbed_in_dir)
    fo=open(fbed_out_dir,'w')


    transcript={}
    whole=ftransloc.read().split('>')[1:]
    for one in whole:
        line=one.split('\n')
        transcript[line[0]]=line[1]
        #print line[0]


    for line in fi:
        seq=line.rstrip().split('\t')
        #print seq[0]
        if seq[0] in transcript:
            transcript_id=seq[0]
            chrr=transcript_id.split('_|_')[1]
            trans_loc=int(seq[2])
            loc=[]
            bande=transcript[seq[0]].split(';')[:-1]
            for one in bande:
                be=one.split(',')
                begin=int(be[0])
                end=int(be[1])
                tmp = [begin]*(end-begin+1)
                i=0
                while i< len(tmp):
                    tmp[i] = tmp[i]+i
                    i +=1
                loc += tmp
            ref_loc=loc[trans_loc-1]
            fo.write(chrr+'\t'+str(ref_loc-1)+'\t'+str(ref_loc)+'\t'+'\t'.join(seq[3:])+'\n')#'\t'+chrom[chrr][ref_loc-1]+':'+chrom_t[transcript_id][trans_loc-1]+'\n')

    






