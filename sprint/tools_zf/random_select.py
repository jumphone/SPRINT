import random
def random_select(file_in_dir=0,file_out_dir=0,ratio=1):


	fi=open(file_in_dir)
	fo=open(file_out_dir,'w')
	
	for line in fi:
		if random.random()<=ratio:
			fo.write(line)

	fi.close()
	fo.close()

