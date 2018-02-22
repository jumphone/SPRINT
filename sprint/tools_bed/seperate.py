def seperate(bed_in_dir,flag_out_dir,rp_out_dir,nonrp_out_dir,flag):
	fi=open(bed_in_dir)
	fo_flag=open(flag_out_dir,'w')
	fo_rp=open(rp_out_dir,'w')
	fo_nonrp=open(nonrp_out_dir,'w')
	for line in fi:
		if 'Simple_repeat' in line or 'Low_complexity' in line:
			next
		elif flag in line:
			fo_flag.write(line)
		elif 'Repeat_region' in line:
			fo_rp.write(line)
		else:
			fo_nonrp.write(line)
	fi.close()
	fo_flag.close()
	fo_rp.close()
	fo_nonrp.close()
