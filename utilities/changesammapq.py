import sys
print "\n"
print "python | changeSAMmapQ.py | Input.sam | Output.sam"
print "\n"

fi=open(sys.argv[1])
fo=open(sys.argv[2],'w')
for line in fi:
    seq=line.rstrip().split('\t')
    if len(seq)>10:
        seq[4]='30'
        fo.write('\t'.join(seq)+'\n')

    else:
        fo.write(line)
