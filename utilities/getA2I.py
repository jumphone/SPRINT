import sys
print '''
$1: INT, 1 for strand-specific sequencing data. 
$2: OUTPUT_DIR of SPRINT
$3: OUTPUT_PATH of A-to-G RESs
'''

ss=int(sys.argv[1])
hyper=sys.argv[2]+'/SPRINT_identified_hyper.res'
regular=sys.argv[2]+'/SPRINT_identified_regular.res'
fo=open(sys.argv[3],'w')

output=[]
r=set()
fi=open(regular)
fi.readline()
for line in fi:
    seq=line.rstrip().split('\t')
    if ss==1 and ((seq[3]=='AG' and seq[5]=='+') or (seq[3]=='TC' and seq[5]=='-')):
        output.append([seq[0],int(seq[2]),line.rstrip(),'regular'])   
    elif ss==0 and (seq[3]=='AG' or seq[3]=='TC'):
        output.append([seq[0],int(seq[2]),line.rstrip(),'regular'])   
    r.add(seq[0]+'|'+seq[2]+'|'+seq[3]) 

fi.close()
h=set()
fi=open(hyper)
fi.readline()
for line in fi:
    seq=line.rstrip().split('\t')
    if ((seq[3]=='AG' and seq[5]=='+') or (seq[3]=='TC' and seq[5]=='-')):
        output.append([seq[0],int(seq[2]),line.rstrip(),'hyper'])    
    h.add(seq[0]+'|'+seq[2]+'|'+seq[3]) 
fi.close()

over = r & h


output.sort()
old=set()
for one in output:
    seq=one[2].split('\t')
    if seq[0]+'|'+seq[2]+'|'+seq[3] not in old:
        old.add(seq[0]+'|'+seq[2]+'|'+seq[3])

        if seq[0]+'|'+seq[2]+'|'+seq[3] in over:
            out='\t'.join(seq[0:4])+'\t'+'regular_and_hyper\t'+seq[5]+'\t'+seq[6]+'\n'
            fo.write(out)
        
        else:
            out='\t'.join(seq[0:4])+'\t'+one[3]+'\t'+seq[5]+'\t'+seq[6]+'\n'
            fo.write(out)


