
#poly_limit=10

def poly_check(seq,poly_limit):
	if 'A'*poly_limit not in seq and 'T'*poly_limit not in seq and 'G'*poly_limit not in seq and 'C'*poly_limit not in seq:
		return True
	else:
		return False
				
def var_check(change_from, change_to, seq,var_limit):
	ALL=['A','T','C','G']
	tmp=[]
	for one in ALL:
		if one !=change_from.upper() and one !=change_to.upper():
			tmp.append(one)
	flag=1
	for one in tmp:
		if seq.count(one) < var_limit/(float(len(tmp))+2):
			flag=0
	if flag==1:
		return True
	else:
		return False
	
def reverse_base(base):
	base=base.upper()
	if base=='A':
		return 'T'
	elif base=='C':
		return 'G'
	elif base=='G':
		return 'C'
	elif base=='T':
		return 'A'
	else:
		return 'N'		
def recover_sam(sam_in_dir,sam_out_dir, var_limit=20,poly_limit=10,rm_multi=0):

	fi=open(sam_in_dir)
	fo=open(sam_out_dir,'w')
	for line in fi:
		seq=line.split('\t')
		if line[0]=='@':
			fo.write(line)
		elif seq[1]=='4' and seq[2]=='*':
			break
		elif seq[1]!='4' and len(seq)>=9:
			seq=line.split('\t')
			seq[9]=seq[9].upper()
			seq[1]=int(seq[1])
			if len(bin(seq[1]))>=7:
				if bin(seq[1])[-3]!='1':
					if bin(seq[1])[-5]=='1':
						seq[1]='16'
					else:
						seq[1]='0'
			seq[1]=str(seq[1])
			record=bin(int(seq[0].split('_|_')[2]))[3:]
			change_from=seq[0].split('_|_')[1].split('_')[0]
			change_to=seq[0].split('_|_')[1].split('_')[2]
			
			
			if len(bin(int(seq[1]))) > 5 and bin(int(seq[1]))[-5]=='1':   #seq[1]=='16':
				change_from=reverse_base(change_from)
				change_to=reverse_base(change_to)
				record=record[::-1]
			else:
				record=record
			changed_read=seq[9]
			i=0
			recovered_read=''
			while i<len(seq[9]):
				if record[i]=='1' and seq[9][i]==change_to:
					recovered_read += change_from
				elif record[i]=='1' and seq[9][i]!=change_to:
					#print "recover error in "+seq[0]
					recovered_read += 'N'
				else:
					recovered_read += seq[9][i]
				i=i+1
			seq[9]=recovered_read
			#fo.write(seq[0])
			#if len(record)==len(seq[9]) and 'I' not in seq[5] and 'D' not in seq[5] and len(record)-changed_read.count(change_to) > 25 and poly_check(seq[9],poly_limit):
			if len(record)==len(seq[9]) and len(record)-changed_read.count(change_to) > var_limit and poly_check(seq[9],poly_limit): #and var_check(change_from,change_to,seq[9],var_limit):
				if (rm_multi==1 and "XA:Z:" not in line) or rm_multi==0:
					fo.write(seq[0])
					j=1
					while j<len(seq):
			
						fo.write('\t'+seq[j])
						j=j+1
			
			#		1+1
	fo.close()
	fi.close()

