def remove(bed_in_dir,bed_out_dir,flag):
	fi=open(bed_in_dir)
	fo=open(bed_out_dir,'w')
	for line in fi:
		if flag not in line:
			fo.write(line)
	fo.close()
	fi.close()

