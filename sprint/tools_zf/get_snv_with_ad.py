def get_snv_with_ad(snv_in_dir=0,snv_out_dir=0,flag=0):


	fi=open(snv_in_dir)
	fo=open(snv_out_dir,'w')
	
	for line in fi:
		seq=line.split('\t')
		try:
			if int(seq[4])>=int(flag):
				fo.write(line)
		except Exception, e:
			print seq[0]+'\t'+seq[2]+"\twithout\tAD flag\n"		



	fi.close()
	fo.close()

