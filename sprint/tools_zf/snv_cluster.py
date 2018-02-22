def snv_cluster(bed_in_dir=0,bed_out_dir=0,cluster_distance=-1,cluster_size=-1):
	fi=open(bed_in_dir)
	fo=open(bed_out_dir,'w')
	tmp='chr0:0:AA'
	limitdistance=int(cluster_distance)
	limitnum=int(cluster_size)
	lst=[]
	for line in fi:
			seq=line.split('\t')
			tmpseq=tmp.split(':')
			if seq[0]==tmpseq[0] and int(seq[2])-int(tmpseq[1])<=limitdistance and seq[3]==tmpseq[2]:
				lst.append(line)
			else:
				if len(lst)>=limitnum:
						begin=float(lst[0].split('\t')[1])
						end=float(lst[-1].split('\t')[2])
						density=len(lst)/(end-begin)
						for one in lst:
							fo.write(one[0:-1]+'\t'+str(len(lst))+'\t'+str(density)+'\n')
				lst=[]
				lst.append(line)
			tmp=seq[0]+':'+seq[2]+':'+seq[3]
	if len(lst)>=limitnum:
			begin=float(lst[0].split('\t')[1])
			end=float(lst[-1].split('\t')[2])
			density=len(lst)/(end-begin)
			for one in lst:
				fo.write(one[0:-1]+'\t'+str(len(lst))+'\t'+str(density)+'\n')
	fi.close()
	fo.close()
