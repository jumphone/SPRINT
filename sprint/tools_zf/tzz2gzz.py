def tzz2gzz(trans_loc_file_in , transcript_zz_in , genome_zz_out):

    fa=open(trans_loc_file_in)
    l1=fa.readline()
    l2=fa.readline()
    TRANS={}
    while l1 !='':
        trans=l1[1:].rstrip()
        seq=l2.split(';')[:-1]
        TRANS[trans]=seq
        l1=fa.readline()
        l2=fa.readline()

    fa.close()

    def loc_t2g(tCHR,tLOC):
        gCHR=tCHR.split('_|_')[1]
        seq=TRANS[tCHR]
        tLOC=int(tLOC)
        flag=1
        tmp=0
        i=0
        while i<len(seq) and flag==1:
            end=int(seq[i].split(',')[1])
            start=int(seq[i].split(',')[0])
            tmp +=  end-start+1
            if tmp >= tLOC :
                flag=0
            i += 1
        j=i-1
        dis2end  = tmp-tLOC
        gLOC = int(seq[j].split(',')[1]) - dis2end
        return gLOC

    def range_t2g(tCHR,tstart,tend):
        gCHR=tCHR.split('_|_')[1]
        tstart=int(tstart)
        tend=int(tend)
        tloc = [tstart+i for i in range(tend-tstart+1)]
        gloc = []
        for one in tloc:
             gloc.append(loc_t2g(tCHR,one))
        i=1
        record=[gloc[0]]
        out=[]
        while i < len(gloc):
            if abs(gloc[i]-gloc[i-1])> 1:
                out.append(str(record[0])+':'+str(record[-1]))
                record=[gloc[i]]
            else:
                record.append(gloc[i])
            i+=1
        out.append(str(record[0])+':'+str(record[-1]))
        return out

    fi=open(transcript_zz_in)
    fo=open(genome_zz_out,'w')
    for line in fi:
        seq=line.split('\t')
        tCHR = seq[0]
        gCHR=tCHR.split('_|_')[1]
        if seq[4]!='*':
            snv=seq[4].split(';')
            gsnv=[]
            for one in snv:
                out=loc_t2g(tCHR,one.split(':')[1])
                gsnv.append(one.split(':')[0]+':'+str(out))
            seq[4]=';'.join(gsnv)

        trange = seq[3].split(';')
        grange=[]
        for one in trange:
            new_one = range_t2g(tCHR, one.split(':')[0],one.split(':')[1])
            grange += new_one
        seq[3] = ';'.join(grange)
        seq[0]=gCHR
        fo.write('\t'.join(seq))






