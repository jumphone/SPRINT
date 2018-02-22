def combine_res(bed_in_dir1,bed_in_dir2,bed_in_dir3,bed_out_dir):
	f1=open(bed_in_dir1)
	f2=open(bed_in_dir2)
	f3=open(bed_in_dir3)
	fo=open(bed_out_dir,'w')
	whole=[]
	for line in f1:
		seq=line.replace('\n','').split('\t')
		whole.append([seq[0],int(seq[2]),seq[3],seq[4],seq[5]])
	for line in f2:
		seq=line.replace('\n','').split('\t')
		whole.append([seq[0],int(seq[2]),seq[3],seq[4],seq[5]])
	for line in f3:
		seq=line.replace('\n','').split('\t')
		whole.append([seq[0],int(seq[2]),seq[3],seq[4],seq[5]])
	whole.sort()
	for one in whole:
		fo.write(one[0]+'\t'+str(one[1]-1)+'\t'+str(one[1])+'\t'+one[2]+'\t'+one[3]+'\t'+one[4]+'\n')
	f1.close()
	f2.close()
	f3.close()
	fo.close()
