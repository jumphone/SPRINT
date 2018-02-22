def transcript_assembler(fref_in_dir=0, fgtf_in_dir=0, ftrans_out_dir=0):
    if fref_in_dir==0 or fgtf_in_dir==0:
        print 'fref_in_dir\tfgtf_in_dir\tftrans_out_dir'
        return 0








    fref=open(fref_in_dir)
    chrom={}
    chrr=''
    line=fref.read()
    line=line.split('>')
    for seq in line:
        if ' ' in seq:
            chrr=seq[0:seq.find(' ')]
        else:
            chrr=seq[0:seq.find('\n')]
        chrom[chrr]=seq[seq.find('\n'):].replace('\n','').upper()
    fref.close()





    #def antisense_reverse(read):
    #        read=read.upper()
    #        read_change_base=""   
    #        for one in read:
    #                if one == 'A':
    #                        read_change_base += 'T'
    #                elif one == 'C':
    #                        read_change_base += 'G'
    #                elif one == 'G':
    #                        read_change_base += 'C'
    #                elif one == 'T':
    #                        read_change_base += 'A'
    #                else:  
    #                        read_change_base += 'N'
    #        read_reverse=read_change_base[::-1]
    #        return read_reverse





    fgtf=open(fgtf_in_dir)
    transcript={}
    trc=[]

    for line in fgtf:
        if '#' != line[0]:
            seq=line.rstrip().split('\t')
            if seq[0] in chrom and seq[2]=='exon' and 'transcript_id ' in seq[8] and int(seq[4]) <= len(chrom[seq[0]]):
                chrr=seq[0]
                begin=int(seq[3])
                end=int(seq[4])
                transcript_id = seq[8].split('transcript_id ')[1].split(';')[0].replace('"','')
                strand = seq[6]
                if transcript_id not in transcript:
                    trc.append(transcript_id)
                    transcript[transcript_id] = [chrr,strand,[begin,end]]
                else:
                    transcript[transcript_id].append([begin,end])
    
    
    fgtf.close()

    for transcript_id in transcript:
        tmp=transcript[transcript_id][2:]
        tmp.sort()
        transcript[transcript_id][2:]=tmp
        #if transcript[transcript_id][1]=='-':
        #    transcript[transcript_id][2:]=transcript[transcript_id][2:][::-1]

    ftrans=open(ftrans_out_dir,'w')
    ftransloc=open(ftrans_out_dir+'.loc','w')


    for transcript_id in trc:
        trans_name='>'+transcript_id+'_|_'+transcript[transcript_id][0]+'_|_'+transcript[transcript_id][1]+'\n'
        chrr=transcript[transcript_id][0]
        strand=transcript[transcript_id][1]
        loc=transcript[transcript_id][2:]
        trans_seq=''
        ftransloc.write(trans_name)
        for one in loc:
            ftransloc.write(str(one[0])+','+str(one[1])+';')
            trans_seq += chrom[chrr][one[0]-1:one[1]]
        ftransloc.write('\n')
        ftrans.write(trans_name)
        i=0
        while i < len(trans_seq):
            ftrans.write(trans_seq[i])
            i += 1
            if i%50==0:
                ftrans.write('\n')
        if i%50!=0:
            ftrans.write('\n')















