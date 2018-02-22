def hyper_or(bed_in_dir1,bed_in_dir2,bed_out_dir):
	f1=open(bed_in_dir1)
	f2=open(bed_in_dir2)
	fo=open(bed_out_dir,'w')
	whole=[]
	for line in f1:
		seq=line.replace('\n','').split('\t')
		whole.append([seq[0],int(seq[2]),seq[3],seq[-1],seq[5]])
	for line in f2:
		seq=line.replace('\n','').split('\t')
		whole.append([seq[0],int(seq[2]),seq[3],seq[-1],seq[5]])
	whole.sort()
	old=set()
	for one in whole:
		if one[0]+':'+str(one[1]) not in old:
			fo.write(one[0]+'\t'+str(one[1]-1)+'\t'+str(one[1])+'\t'+one[2]+'\t'+one[3]+'\t'+one[4]+'\n')
			old.add(one[0]+':'+str(one[1]))
	f1.close()
	f2.close()
	fo.close()
