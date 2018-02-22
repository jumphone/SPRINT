
def change_sam_read_name(sam_in_dir=0,sam_out_dir=0,name='read1'):
	fi=open(sam_in_dir)
	fo=open(sam_out_dir,'w')
	name=name
	idd=1
	for line in fi:
		if line[0] !='@':
			seq=line.split('\t')
			fo.write('id_'+str(idd)+'_'+name+line.replace(seq[0],''))
			idd=idd+1
		else:
			fo.write(line)
	fo.close()
	fi.close()
