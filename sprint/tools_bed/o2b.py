def o2b(bed_in,bed_out):
    fi=open(bed_in)
    fo=open(bed_out,'w')
    for line in fi:
        seq=line.rstrip().split('\t')
        #if float(seq[7])<0.2:
        fo.write('\t'.join(seq[0:6])+'\n')
