def get_res(regular_alu,regular_nalurp,regular_nrp,hyper,output):

    falu=open(regular_alu)
    fnalurp=open(regular_nalurp)
    fnrp=open(regular_nrp)
    fhyper=open(hyper)
    fo_AI=open(output+'_A_to_I_regular.res','w')
    fo_hAI=open(output+'_A_to_I_hyper.res','w')
    fo_CU=open(output+'_C_to_U.res','w')

    for line in falu:
        seq=line.rstrip().split('\t')
        if seq[3]=='AG' or seq[3]=='TC':
            fo_AI.write(line)
    for line in fnalurp:
        seq=line.rstrip().split('\t')
        if seq[3]=='AG' or seq[3]=='TC':
            fo_AI.write(line)
        if seq[3]=='CT' or seq[3]=='GA':
            fo_CU.write(line)
    for line in fnrp:
        seq=line.rstrip().split('\t')
        if seq[3]=='AG' or seq[3]=='TC':
            fo_AI.write(line)
        if seq[3]=='CT' or seq[3]=='GA':
            fo_CU.write(line)
    for line in fhyper:
        seq=line.rstrip().split('\t')
        if seq[3]=='AG' or seq[3]=='TC':
            fo_hAI.write(line)
