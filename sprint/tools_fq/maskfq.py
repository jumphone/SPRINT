def antisense_reverse(read):
	read=read.upper()
	read_change_base=""
	for one in read:
		if one == 'A':
			read_change_base += 'T'
		elif one == 'C':
			read_change_base += 'G'
		elif one == 'G':
			read_change_base += 'C'
		elif one == 'T':
			read_change_base += 'A'
		else:
			read_change_base += 'N'
	read_reverse=read_change_base[::-1]
	return read_reverse


def maskfq(fq_in_dir,mask_from,mask_to):
	mask_from=mask_from.upper()
	mask_to=mask_to.upper()
	fi=open(fq_in_dir)
	fo=open(fq_in_dir[0:-3]+'_'+mask_from+'_to_'+mask_to+'.fq','w')
	line1=fi.readline().replace('\n','')
	line2=fi.readline().upper().replace('\n','')
	line3=fi.readline().replace('\n','')
	line4=fi.readline().replace('\n','')
	while line1 !='':
		if line1[-1]=='1':
			line2=antisense_reverse(line2)
			line4=line4[::-1]
		record="1"
		line2_new=""
		for one in line2.replace('\n',''):
			if one==mask_from:
				record=record+'1'
			else:
				record=record+'0'
		
		fo.write(line1+'_|_'+mask_from+'_to_'+mask_to+'_|_'+str(int(record,2))+'_|_read2'+'\n')
		fo.write(line2.replace(mask_from,mask_to)+'\n')			
		fo.write('+\n')
		fo.write(line4+'\n')
		line1=fi.readline().replace('\n','')
		line2=fi.readline().upper().replace('\n','')
		line3=fi.readline().replace('\n','')
		line4=fi.readline().replace('\n','')
	fi.close()
	fo.close()

