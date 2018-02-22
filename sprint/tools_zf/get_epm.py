def get_epm(bed_in_dir,epm_out_dir,flag,zz_in_dir):
	fi=open(bed_in_dir)
	fo=open(epm_out_dir,'w')
	fread=open(zz_in_dir)
	gene={}
	for line in fi:
		seq=line.replace('\n','').split('\t')
		i=0
		while i< len(seq):
			if flag in seq[i]:
				try:
					gene[seq[i]][0]=gene[seq[i]][0]+int(seq[4].split(':')[0])
					gene[seq[i]][1]=gene[seq[i]][1]+1
					#gene[seq[i]].append(int(seq[2]))
			
				except Exception, e:
					gene[seq[i]]=[int(seq[4].split(':')[0]),1]

			i=i+1
	j=0
	for line in fread:
		j=j+1
	read_count=j

	read_million=float(read_count)/1000000
	
	for one in gene:
		'''
		tmp=1
		last=1
		point=2
		range_dis=0
		while point < len(gene[one]):
			if gene[one][point]-gene[one][last]>1000:
				range_dis=range_dis+tmp
				#last=point
				tmp=1
				
			else:
				tmp=tmp+gene[one][point]-gene[one][last]
				#last=point
			
			last=point
			point=point+1
		range_dis=range_dis+tmp
		'''
		epm=float(gene[one][0])/( read_million     )
		fo.write(one+'\t'+str(epm)+'\t'+str(gene[one][0])+'\t'+str(gene[one][1])+'\n')

	fi.close()
	fo.close()
	fread.close()
