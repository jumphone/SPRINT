def umsam2fq(sam_in_dir,fq_out_dir):

	fi=open(sam_in_dir)
	fo=open(fq_out_dir,'w')
	for line in fi:
		seq=line.rstrip().split('\t')
		if line[0] !='@' and len(bin(int(seq[1])))>=5 and bin(int(seq[1]))[-3]=='1':
			if len(bin(int(seq[1])))>=9 and bin(int(seq[1]))[-7]=='1':
				seq[0]=seq[0][0:-2]+'_1'
			elif len(bin(int(seq[1])))>=10 and bin(int(seq[1]))[-8]=='1':
				seq[0]=seq[0][0:-2]+'_2'
			elif line[-1]=='1':
				seq[0]=seq[0][0:-2]+'_1'
			elif line[-1]=='2':
				seq[0]=seq[0][0:-2]+'_2'
 			fo.write('@'+seq[0]+'\n'+seq[9]+'\n+\n'+seq[10]+'\n')
	fo.close()
	fi.close()

