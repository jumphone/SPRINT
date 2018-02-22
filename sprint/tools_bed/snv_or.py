def snv_or(bed_in_dir1,bed_in_dir2,bed_out_dir):
    f1=open(bed_in_dir1)
    f2=open(bed_in_dir2)
    fo=open(bed_out_dir,'w')
    whole={}
    for line in f1:
        seq=line.rstrip().split('\t')
        whole[':'.join(seq[0:4])+':'+seq[5]]=int(seq[4])
    for line in f2:
        seq=line.rstrip().split('\t')
        if ':'.join(seq[0:4])+':'+seq[5] in whole:
            whole[':'.join(seq[0:4])+':'+seq[5]] +=int(seq[4])
        else:
            whole[':'.join(seq[0:4])+':'+seq[5]]=int(seq[4])
    lst=[]
    for one in whole:
        seq=one.split(':')
        lst.append([seq[0],int(seq[1]),int(seq[2]),seq[3],str(whole[one]),seq[4]])
    lst.sort()
    for one in lst:
        out=[]
        for i in one:
            out.append(str(i))
        fo.write('\t'.join(out)+'\n')

    f1.close()
    f2.close()
    fo.close()
