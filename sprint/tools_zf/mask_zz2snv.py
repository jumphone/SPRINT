#[bwa_aln] 17bp reads: max_diff = 2
#[bwa_aln] 38bp reads: max_diff = 3
#[bwa_aln] 64bp reads: max_diff = 4
#[bwa_aln] 93bp reads: max_diff = 5
#[bwa_aln] 124bp reads: max_diff = 6
#[bwa_aln] 157bp reads: max_diff = 7
#[bwa_aln] 190bp reads: max_diff = 8
#[bwa_aln] 225bp reads: max_diff = 9



def mismatch_num(seqlen):
	if seqlen < 17:
		return 1
	elif seqlen <38:
		return 2
	elif seqlen <64:
		return 3
	elif seqlen <93:
		return 4
	elif seqlen <124:
		return 5
	elif seqlen <157:
		return 6
	elif seqlen <190:
		return 7
	elif seqlen <225:
		return 8
	else:
		return 9




def mask_zz2snv(zz_in_dir=0,bed_out_dir=0,baseq_cutoff_dir=0):

	
	fi=open(zz_in_dir)
	fo=open(bed_out_dir,'w')

	fqua=open(baseq_cutoff_dir)
	limitbasequa=int(fqua.readline().replace('\n',''))
	fqua.close()
	limitad=1
	limitloc=5
	limitmpqua=0
	allsnv={}
	for line in fi:
		truesnv=[]
		seq=line.rstrip().split('\t')
		mismatch=seq[4].split(';')
		basequa=seq[5].split(',')
		loc=seq[9].split(',') #fragment-loc
		mpqua=int(seq[2])
		####################################################################
 		#change the sam flag 'seq[1]' when you didn't use "bwa -aln" as mapper
		seq[1]=int(seq[1])
		if len(bin(seq[1]))>=7:
			if bin(seq[1])[-3]!='1':
				if bin(seq[1])[-5]=='1':
					seq[1]='16'
				else:
					seq[1]='0'
		elif len(bin(seq[1]))>=5:
			if bin(seq[1])[-3]!='1':
				seq[1]='0'
					 		
		else: 
			seq[1]='0'
		#####################################################################
	
		
		
		if basequa[0]!='*' and mpqua >= limitmpqua and mpqua < 200:
			i=0
			baseqlst=[]
			mistype={}
			while i < len(basequa):
				baseqlst.append(int(basequa[i]))
				try:
					mistype[mismatch[i].split(':')[0]] += 1
				except Exception , e:
					mistype[mismatch[i].split(':')[0]] = 1
				if int(basequa[i]) >= limitbasequa  and  int(loc[i]) > limitloc  :

					truesnv.append([mismatch[i],seq[1],seq[8]])
					
				i=i+1

			#fflag=1
			#masktype_tmp=seq[8].split('_|_')[1].split('_to_')
			#masktype=masktype_tmp[0]+masktype_tmp[1]
			miss=[]
			for mis in mistype:
				miss.append(mistype[mis])
			miss.sort()
			if len(miss)>=2:
				missnum=sum(miss[:-1])
			else:
				missnum=0
			


			
			if len(baseqlst)>0 and sum(baseqlst)/float(len(baseqlst)) >= limitbasequa: #and missnum <= mismatch_num(len(seq[7])):
				for snv in truesnv:
					try:
						allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][0]=allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][0]+1
						if (len(bin(int(seq[1]))) > 5 and bin(int(seq[1]))[-5]=='1' and snv[2][-1] == '1' ) or ((len(bin(int(seq[1]))) < 5 or bin(int(seq[1]))[-5]=='0') and snv[2][-1] == '2' ):
							allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][1]=allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][1]+1
						elif (len(bin(int(seq[1]))) > 5 and bin(int(seq[1]))[-5]=='1' and snv[2][-1] == '2' ) or ((len(bin(int(seq[1]))) < 5 or bin(int(seq[1]))[-5]=='0') and snv[2][-1] == '1' ):
							allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][2]=allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][2]+1
					except Exception, e:
						if (len(bin(int(seq[1]))) > 5 and bin(int(seq[1]))[-5]=='1' and snv[2][-1] == '1' ) or ((len(bin(int(seq[1]))) < 5 or bin(int(seq[1]))[-5]=='0') and snv[2][-1] == '2' ):
							allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]]=[1,1,0]
						elif (len(bin(int(seq[1]))) > 5 and bin(int(seq[1]))[-5]=='1' and snv[2][-1] == '2' ) or ((len(bin(int(seq[1]))) < 5 or bin(int(seq[1]))[-5]=='0') and snv[2][-1] == '1' ):
							allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]]=[1,0,1]

	snv_bed=[]
	for snv in allsnv:
		seq=snv.split('\t')
		if allsnv[snv][0]>=limitad:
				if allsnv[snv][1] > allsnv[snv][2]: 
					snv_bed.append([seq[0],int(seq[2]),seq[1],'+',allsnv[snv][0]])
				elif allsnv[snv][2] > allsnv[snv][1]:
					snv_bed.append([seq[0],int(seq[2]),seq[1],'-',allsnv[snv][0]])
				else:
					snv_bed.append([seq[0],int(seq[2]),seq[1],'.',allsnv[snv][0]])

	snv_bed.sort()
	for one in snv_bed:
		fo.write(one[0]+'\t'+str(one[1]-1)+'\t'+str(one[1])+'\t'+one[2]+'\t'+str(one[4])+'\t'+one[3]+'\n')
	fi.close()
	fo.close()

