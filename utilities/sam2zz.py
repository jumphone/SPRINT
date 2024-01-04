import re
def sam2zz(sam_in_dir=0,fa_in_dir=0,zz_out_dir=0):


	#-----------------------------------------------------------
	#reading refgenome
	fref=open(fa_in_dir)
	chrom={}
	chrr=''
	line=fref.read()
	line=line.split('>')
	for seq in line:
			if ' ' in seq:
				chrr=seq[0:seq.find(' ')]
			else:
				chrr=seq[0:seq.find('\n')]
			chrom[chrr]=seq[seq.find('\n'):].replace('\n','')

	#0 base

	fref.close()
	#------------------------------------------------------------
	#
	#donee:dolist;lst:donumlist
	def doCG(a):
		donee=[]
		lst=re.findall( '(\d+|\+|-|\*|/)', a )
		for i in a:
			if i == 'I' or i == 'D' or i== 'M' or i=='S' or i=='P' or i=='N' :
				donee.append(i)
		return donee,lst
	#donefunction

	def doneCG(CG,chrr,pos,seq,qseq):#pos is 1 base
		donee,lst=doCG(CG)
		errorsite=''
		intersite=''
		quasite=''
		locsite=''
		pieceloc=''
		refseq=''
		seqseq=''
		refpos=int(pos)-1
		seqpos=0
		step=0
		while step<len(donee):
			if donee[step]=='I':
				seqpos=seqpos+int(lst[step])
			elif donee[step]=='D':
				refpos=refpos+int(lst[step])
			elif donee[step]=='N':
				refpos=refpos+int(lst[step])
			elif donee[step]=='S':
				seqpos=seqpos+int(lst[step])
			elif donee[step]=='M':
				
				refseq=refseq+chrom[chrr][refpos:refpos+int(lst[step])]
				seqseq=seqseq+seq[seqpos:seqpos+int(lst[step])]
				j=refpos
				jj=seqpos
				while j<refpos+int(lst[step]):
					try:
						if chrom[chrr][j].upper() != seq[jj].upper() and chrom[chrr][j].upper() !='N' and seq[jj].upper() != 'N':
							errorsite=errorsite+chrom[chrr][j].upper()+seq[jj].upper()+':'+str(j+1)+';'
							quasite=quasite+','+str(ord(qseq[jj]))
							locsite=locsite+','+str(jj+1)
							pieceloc=pieceloc+','+str( min( jj+1-seqpos,seqpos+int(lst[step])-jj  ) )
							 		
					except Exception, e:
						pass
						#print "error with",chrr,pos,e
					j=j+1
					jj=jj+1
				intersite=intersite+str(refpos+1)+':'+str(refpos+int(lst[step]))+';'
				refpos=refpos+int(lst[step])
				seqpos=seqpos+int(lst[step])
			step=step+1
		refseq=refseq.upper()
		seqseq=seqseq.upper()
		return refseq,seqseq,errorsite,intersite,quasite,locsite,pieceloc
	#------------------------------------------------------------
	###################additional
	'''
	whole={}
	fi=open(sam_in_dir)
	for line in fi:
		seq=line.split('\t')
		if line[0]!='@'and len(seq)>5:
			if seq[0][0]!='@' and seq[2]!='*' and seq[5]!='*':
				name=seq[0].split('_|_')[0]
				
				#tmp = [ seq[4].count(':') ,seq[0] ]
				if name in whole:
				#	if tmp[0] < whole[name][0]:
				#		whole[name]=tmp
					
					whole[name] +=1
				else:
					whole[name]=1
					#whole[name]=tmp
	fi.close()
	'''
	#######################			
	fi=open(sam_in_dir) #sam
	fo=open(zz_out_dir,'w') #zz
	for line in fi:
		seq=line.split('\t')
		if line[0]!='@' and len(seq)>5:
			name=seq[0].split('_|_')[0]
			if seq[0][0]!='@' and seq[2]!='*' and seq[5]!='*' :# and whole[name]<2:
				refseq,seqseq,errorsite,intersite,quasite,locsite,pieceloc=doneCG(seq[5],seq[2],seq[3],seq[9],seq[10])
				quasite=quasite[1:]
				locsite=locsite[1:]
				pieceloc=pieceloc[1:]
				
				if len(intersite[0:-1])==0:
					intersite='*;'
				if len(errorsite[0:-1])==0:
					errorsite='*;'
				if len(quasite)==0:
					quasite='*'
				if len(locsite)==0:
					locsite='*'
				if len(pieceloc)==0:
					pieceloc='*'
				
				if len(bin(int(seq[1])))>=9 and bin(int(seq[1]))[-7]=='1':
					fo.write(seq[2]+'\t'+seq[1]+'\t'+seq[4]+'\t'+intersite[0:-1]+'\t'+errorsite[0:-1]+'\t'+quasite+'\t'+locsite+'\t'+seq[9]+'\t'+seq[0]+'_1'+'\t'+pieceloc+'\n')
				elif len(bin(int(seq[1])))>=10 and bin(int(seq[1]))[-8]=='1':
					fo.write(seq[2]+'\t'+seq[1]+'\t'+seq[4]+'\t'+intersite[0:-1]+'\t'+errorsite[0:-1]+'\t'+quasite+'\t'+locsite+'\t'+seq[9]+'\t'+seq[0]+'_2'+'\t'+pieceloc+'\n')
				else:
					fo.write(seq[2]+'\t'+seq[1]+'\t'+seq[4]+'\t'+intersite[0:-1]+'\t'+errorsite[0:-1]+'\t'+quasite+'\t'+locsite+'\t'+seq[9]+'\t'+seq[0]+'\t'+pieceloc+'\n')
					
	fi.close()	
	fo.close()

