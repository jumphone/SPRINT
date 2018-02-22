def cut(fq_in_dir=0,fq_out_dir=0,cutnum=0,name='read1'):
	fi=open(fq_in_dir)
	fo=open(fq_out_dir,'w')
	cutnum=int(cutnum)
	line1=fi.readline()
	line2=fi.readline()
	line3=fi.readline()
	line4=fi.readline()
	idd=1
	while line1 !='':
		CELL_TAG=''
		if "XC:Z:" in line1:
			seq=line1.split('_')
			for one in seq:
				if one[:5]=='XC:Z:':
					CELL_TAG=one		
		if CELL_TAG !='':
			fo.write('@id_'+str(idd)+'_'+CELL_TAG+'_'+name+'\n')
		else:
			fo.write('@id_'+str(idd)+'_'+name+'\n')
		fo.write(line2[cutnum:])
		fo.write(line3)
		fo.write(line4[cutnum:])
		line1=fi.readline()
		line2=fi.readline()
		line3=fi.readline()
		line4=fi.readline()
		idd=idd+1
	fi.close()
	fo.close()	
