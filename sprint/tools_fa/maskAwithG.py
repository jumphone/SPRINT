def maskAwithG(fa_in_dir=0,fa_out_dir=0):
    if fa_in_dir==0 or fa_out_dir==0:
        print 'fa_in_dir\tfa_our_dir'
        return 0
    fi=open(fa_in_dir)
    fo=open(fa_out_dir,'w')

    for line in fi:
        if line[0]=='>':
            fo.write(line)
        else:
            fo.write(line.replace('A','G').replace('a','g'))
