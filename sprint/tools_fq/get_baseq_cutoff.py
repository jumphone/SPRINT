
def get_baseq_cutoff(fq_in_dir=0,cutoff_out_dir=0):
	fi=open(fq_in_dir)
	fo=open(cutoff_out_dir,'w')
	line1=fi.readline()
	line2=fi.readline()
	line3=fi.readline()
	line4=fi.readline()
	did=0
	while line1 !='':
		if did==1:
			break
		qua=line4[0:-1]
		for i in qua:
			if ord(i) > 76:
				fo.write('89') #64+25
				did=1
				break
			if ord(i) < 60:
				fo.write('58') #33+25
				did=1
				break

		line1=fi.readline()
		line2=fi.readline()
		line3=fi.readline()
		line4=fi.readline()
	fi.close()
	fo.close()	
