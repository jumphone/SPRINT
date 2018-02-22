

def combine_depth(bed_in_dir=0,bed_out_dir=0):

	fi=open(bed_in_dir)# './zz_folder/all.zz')
	fo=open(bed_out_dir,'w')#'./tmp/readspersite_new.zer','w')
	for line in fi:
		seq=line[:-1].split('\t')
		AD=int(seq[4].split(':')[0])+int(seq[-1].split(':')[0])
		DP=int(seq[4].split(':')[1])+int(seq[-1].split(':')[1])
		
		fo.write(seq[0]+'\t'+seq[1]+'\t'+seq[2]+'\t'+seq[3]+'\t'+str(AD)+':'+str(DP)+'\t'+seq[5]+'\n')
	fi.close()
	fo.close()

