
def get_depth(zz_in_dir=0,bed_in_dir=0,bed_out_dir=0):

	fread=open(zz_in_dir)# './zz_folder/all.zz')
	fsnv=open(bed_in_dir) #'../bed_folder/try_new.bed') #   Hap_SRR521447.bed')
	fo=open(bed_out_dir,'w')#'./tmp/readspersite_new.zer','w')

	class Read:
		def __init__(self,read):
			
			self.snv=read.split('\t')[4].split(';')
			self.inter=read.split('\t')[3].split(';')
			self.direct=read.split('\t')[1]
		def locisin(self,loc):
			isin=0
			for inter in self.inter:
				inter=inter.split(':')
				if int(loc)<=int(inter[1]) and int(loc)>=int(inter[0]):
					isin =1
					break
			if isin ==0:
				return 0
			elif isin ==1:
				return 1
		def snvisin(self,snv):
			if snv in self.snv:
				return 1
			else:
				return 0
		def getmin(self):
			return int(self.inter[0].split(':')[0])
		def getmax(self):
			return int(self.inter[-1].split(':')[1])


	reads={}
	for line in fread:
		seq=line.split('\t')
		try:
				reads[seq[0]].append(Read(line[0:-1]))
		except Exception,e :
				print seq[0]+' begin'
				reads[seq[0]]=[Read(line[0:-1])]


	top=0
	chrr=''
	for line in fsnv:
		seq=line[0:-1].split('\t')
		deep=0
		altdeep=0
		snv=seq[3]+':'+seq[2]
		if seq[0] != chrr:
			top=0
			chrr=seq[0]
		if top < len(reads[seq[0]]):
			while seq[0]==chrr and top < len(reads[seq[0]]) and reads[seq[0]][top].getmax() < int(seq[2]):
				top=top+1
			point=top
			while seq[0]==chrr and point < len(reads[seq[0]]) and reads[seq[0]][point].getmin() <= int(seq[2]):
				if reads[seq[0]][point].locisin(seq[2]) ==1:
					deep=deep+1
					
				if reads[seq[0]][point].snvisin(snv)==1:
					altdeep=altdeep+1
				
				point=point+1
		fo.write(line[0:-1]+'\t'+str(altdeep)+':'+str(deep)+'\n')
		
	fread.close()
	fsnv.close()
	fo.close()

