def dedup(in_dir,out_dir):
	old=set()
	fi=open(in_dir)
	fo=open(out_dir,'w')	
	for line in fi:
		seq=line.split('\t')
		if seq[0]+':'+seq[3]+':'+seq[7] not in old:
			fo.write(line)
			old.add(seq[0]+':'+seq[3]+':'+seq[7])
