import subprocess,os,sys
import tmp as sprint

def prepare():
#    import subprocess,sprint,os,sys
    print ''
    print "##############################################################################################"
    print ''
    print "   SPRINT: SNP-free RNA editing Identification Toolkit"
    print ""
    print "   http://sprint.tianlab.cn/SPRINT/"
    print ""
    print "   Please contact 15110700005@fudan.edu.cn when questions arise."
    print ""
    print "##############################################################################################"
    
    def help_doc():
        print ""
        print "   Usage:"
        print ""
        print "      sprint prepare   [options]   reference_genome(.fa)   bwa_path"
        print ""
        print "      options:"
        print "         -t transcript_annotation(.gtf) #Optional"
        print ""
        print "   Example:"
        print ""
        print "      sprint prepare -t hg19.gtf hg19.fa ./bwa-0.7.12/bwa"
        print ""
        print ""
        #print sys.argv[0]
    
        sys.exit(0)
    
    if len(sys.argv)<3:
        help_doc()
    
    
    
    gtf_file=False
    options=[]
    read2=''
    i=1
    while i< len(sys.argv):
        if sys.argv[i]=='-t':
            paired_end=True
            try:
                gtf_file=sys.argv[i+1]
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
    
    
        i += 1
    
    all_argv=[]
    i=1
    while i< len(sys.argv):
        if i not in options:
            all_argv.append(i)
        i +=1
    
    try:
        refgenome=sys.argv[all_argv[0]]
        #gtf_file=sys.argv[2]
        bwa=sys.argv[all_argv[1]]
    
    
    
    
    
        print 'Masking A with G in reference genome...'
        sprint.maskAwithG(refgenome,refgenome+'.mskAG.fa')
        print 'Masking T with C in reference genome...'
        sprint.maskTwithC(refgenome,refgenome+'.mskTC.fa')
       
        if gtf_file != False:
            print 'Assembling transcripts...'
            sprint.transcript_assembler(refgenome,gtf_file,refgenome+'.trans.fa')
            print 'Masking A with G in transcripts...'
            sprint.maskAwithG(refgenome+'.trans.fa',refgenome+'.trans.fa.mskAG.fa')
            print 'Masking T with C in transcripts...'
            sprint.maskTwithC(refgenome+'.trans.fa',refgenome+'.trans.fa.mskTC.fa')
    
    
        print 'Building BWA index...'
        step1=subprocess.Popen(bwa+' index -a bwtsw '+refgenome,shell=True)
        step2=subprocess.Popen(bwa+' index -a bwtsw '+refgenome+'.mskAG.fa',shell=True)
        step3=subprocess.Popen(bwa+' index -a bwtsw '+refgenome+'.mskTC.fa',shell=True)
        if gtf_file !=False:
            step4=subprocess.Popen(bwa+' index -a bwtsw '+refgenome+'.trans.fa',shell=True)
            step5=subprocess.Popen(bwa+' index -a bwtsw '+refgenome+'.trans.fa.mskAG.fa',shell=True)
            step6=subprocess.Popen(bwa+' index -a bwtsw '+refgenome+'.trans.fa.mskTC.fa',shell=True)
            step4.wait()
            step5.wait()
            step6.wait()
        step1.wait()
        step2.wait()
        step3.wait()
        sys.exit(0)    
    except Exception, e:
        print "ERROR!"
        print ""
        print e
        help_doc()
    
    
    
    
    
#if __name__ == "__main__": 
#    prepare()
