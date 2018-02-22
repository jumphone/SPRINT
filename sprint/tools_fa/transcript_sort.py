def transcript_sort(fbed_in_dir=0,fbed_out_dir=0):

    fi=open(fbed_in_dir)
    fo=open(fbed_out_dir,'w')

    whole={}
    for line in fi:
        seq=line.rstrip().split('\t')
        try:
            whole[seq[0]+':'+seq[2]+':'+seq[3]+':'+seq[5]] += int(seq[4])
        except Exception,e:
            whole[seq[0]+':'+seq[2]+':'+seq[3]+':'+seq[5]] = int(seq[4])

    tmp=[]
    for one in whole:
        seq=one.split(':')
        dep=str(whole[one])
        tmp.append([seq[0],int(seq[1]),seq[2],dep,seq[3]])
    tmp.sort()
    for one in tmp:
       fo.write(one[0]+'\t'+str(one[1]-1)+'\t'+str(one[1])+'\t'+one[2]+'\t'+one[3]+'\t'+one[4]+'\n')





