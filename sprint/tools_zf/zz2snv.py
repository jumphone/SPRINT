def zz2snv(zz_in_dir=0,bed_out_dir=0,baseq_cutoff_dir=0):


	fi=open(zz_in_dir)
	fo=open(bed_out_dir,'w')

	fqua=open(baseq_cutoff_dir)
	limitbasequa=int(fqua.readline().replace('\n',''))
	fqua.close()
	limitad=1#2
	limitloc=5
	limitmpqua=20
	allsnv={}
	for line in fi:
		truesnv=[]
		seq=line[0:-1].split('\t')
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
			while i < len(basequa):
				baseqlst.append(int(basequa[i]))
				if int(basequa[i]) >= limitbasequa  and  int(loc[i]) > limitloc  :

					truesnv.append([mismatch[i],seq[1],seq[8]])
					
				i=i+1
			
			if len(baseqlst)>0 and sum(baseqlst)/float(len(baseqlst)) >= limitbasequa:
				for snv in truesnv:
					try:
						allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][0]=allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][0]+1
						if (len(bin(int(seq[1]))) > 5 and bin(int(seq[1]))[-5]=='1' and snv[2][-1] == '1' ) or ((len(bin(int(seq[1]))) < 5 or bin(int(seq[1]))[-5]=='0') and snv[2][-1] == '2' ):
							allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][1]=allsnv[seq[0]+'\t'+snv[0].split(':')[0]+'\t'+snv[0].split(':')[1]][1]+1
						elif (len(bin(int(seq[1]))) > 5 and bin(int(seq[1]))[-5]=='1' and snv[2][-1] == '2' ) or ((len(bin(int(seq[1]))) < 5 or bin(int(seq[1]))[-5]=='0')  and snv[2][-1] == '1' ):
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

