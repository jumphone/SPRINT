#use .bed to annotate .bed
def annotate(bed_in_dir=0,bed_anno_dir=0,bed_out_dir=0):
	if bed_in_dir ==0 or bed_anno_dir ==0 or bed_out_dir ==0:
		print 'Please check the input directory! annotate(bed_in_dir,bed_anno_dir,bed_out_dir)'
		return 'Please check the input directory! annotate(bed_in_dir,bed_anno_dir,bed_out_dir)'
	else:
		fi=open(bed_in_dir) #must by sorted
		fa=open(bed_anno_dir)
		fo=open(bed_out_dir,'w')
		anno={}
		for line in fa:
			seq=line[0:-1].split('\t')
			try:
				anno[seq[0]].append([int(seq[1])+1,int(seq[2]),seq[3],seq[4],seq[5]])	
			except Exception, e:
				anno[seq[0]]=[ [int(seq[1])+1,int(seq[2]),seq[3],seq[4],seq[5]]  ]
		for a in anno:
			anno[a].sort()
		top=0
		point=0
		lastchr=''
		for line in fi:
		
			seq = line.split()
			if len(seq[0]) <=5:
				output=line[0:-1]
				if seq[0]==lastchr:
					1+1
				else:
					top=0
					lastchr=seq[0]
				if seq[0] not in anno:
					anno[seq[0]]=[ [0,0,0,0,0]  ]
				if top<len(anno[seq[0]]):			
					while anno[seq[0]][top][1] < int(seq[2]) :
		
						top=top+1
						if top >= len(anno[seq[0]]):
							break
					point=top
					if point < len(anno[seq[0]]):
						while anno[seq[0]][point][0] <= int(seq[2])     and     anno[seq[0]][point][1] >= int(seq[2]) :
								if anno[seq[0]][point][2]+'\t'+anno[seq[0]][point][3]+'\t'+anno[seq[0]][point][4] not in output:
									output=output+'\t'+anno[seq[0]][point][2]+'\t'+anno[seq[0]][point][3]+'\t'+anno[seq[0]][point][4]
								point=point+1
								if point >= len(anno[seq[0]]):
									break
		
				fo.write(output+'\n')
		fi.close()
		fa.close()
		fo.close()

