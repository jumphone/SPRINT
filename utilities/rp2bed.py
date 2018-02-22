import sys
fi=open(sys.argv[1])
fo=open(sys.argv[2],'w')
for line in fi:
	if line[0]!='#':
		seq=line.split('\t')
		fo.write(seq[5]+'\t'+seq[6]+'\t'+seq[7]+'\t'+seq[10]+' | '+seq[11]+' | '+seq[12]+'\tRepeat_region\t'+seq[9]+'\n')





