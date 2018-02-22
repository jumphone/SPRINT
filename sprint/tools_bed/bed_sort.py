def bed_sort(bed_in_dir,bed_out_dir):
	fi=open(bed_in_dir)
	fo=open(bed_out_dir,'w')
	whole=[]
	for line in fi:
		seq=line.split('\t')
		whole.append([seq[0],int(seq[1]),int(seq[2]),line])	
	whole.sort()
	for one in whole:
		fo.write(one[3])
	fi.close()
	fo.close()
