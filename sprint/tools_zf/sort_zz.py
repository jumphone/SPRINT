def sort_zz(zz_in,zz_out):
    out=[]
    fi=open(zz_in)
    for line in fi:
        seq=line.split('\t')
        out.append([seq[0],int(seq[3].split(':')[0]),int(seq[3].split(':')[-1]),line])
    fi.close()
    fo=open(zz_out, 'w')
    out.sort()
    for one in out:
        fo.write(one[3])
