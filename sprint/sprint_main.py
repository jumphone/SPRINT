import subprocess,os,sys
import tmp as sprint

def main(): 
    #import subprocess,os,sys
    
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
        print "   Attention:"
        print ""
        print "      Before using 'sprint main', please use 'sprint prepare' to build mapping index."
        print ""
        print "   Usage:"
        print ""
        print "      sprint main   [options]   reference_genome(.fa)   output_path   bwa_path   samtools_path"
        print ""
        print "      options:"
        print "         -1       read1(.fq)       # Required !!!"
        print "         -2       read2(.fq)       # Optional"
        print "         -rp      repeat_file      # Optional, you can download it from http://sprint.software/SPRINT/dbrep/"
        print "         -ss      INT              # when input is strand-specific sequencing data, please clarify the direction of read1. [0 for antisense; 1 for sense] (default is 0)"
        #print "         -b       INT             # the format of read file [0: fq, 1: bam] (default is 0)"
        print "         -c       INT              # Remove the fist INT bp of each read (default is 0)"
        print "         -p       INT              # Mapping CPU (default is 1)"
        print "         -cd      INT              # The distance cutoff of SNV duplets (default is 200)"
        print "         -csad1   INT              # Regular - [-rp is required] cluster size - Alu - AD >=1 (default is 3)"
        print "         -csad2   INT              # Regular - [-rp is required] cluster size - Alu - AD >=2 (default is 2)"
        print "         -csnar   INT              # Regular - [-rp is required] cluster size - nonAlu Repeat - AD >=1 (default is 5)"
        print "         -csnr    INT              # Regular - [-rp is required] cluster size - nonRepeat - AD >=1 (default is 7)"
        print "         -csrg    INT              # Regular - [without -rp] cluster size - AD >=1 (default is 5)"
        print "         -csahp   INT              # Hyper - [-rp is required] cluster size - Alu - AD >=1 (default is 5)"
        print "         -csnarhp INT              # Hyper - [-rp is required] cluster size - nonAlu Repeat - AD >=1 (default is 5)"
        print "         -csnrhp  INT              # Hyper - [-rp is required] cluster size - nonRepeat - AD >=1 (default is 5)"
        print "         -cshp    INT              # Hyper - [without -rp] cluster size - AD >=1 (default is 5)"
        print ""
        print "   Example:"
        print ""
        print "       sprint main -rp hg19_repeat.txt -c 6 -p 6 -1 read1.fq -2 read2.fq hg19.fa output ./bwa-0.7.12/bwa ./samtools-1.2/samtools"
        print ""
        print "       Notes: Default protocol of strand-specific RNA-seq is dUTP (read1: '-'; read2: '+')"
        print ""
        #print sys.argv[0]
        
        sys.exit(0)
    
    
    if len(sys.argv)<2:
        #print sys.argv[0]
        help_doc()
    
    
    
    read_format=0
    cutbp=0
    cluster_distance=200
    cluster_size_alu_ad1 = 3
    cluster_size_alu_ad2 = 2
    cluster_size_nalurp = 5
    cluster_size_nrp = 7
    cluster_size_rg = 5
    cluster_size_hp = 5
    cluster_size_alu_hp = 5
    cluster_size_nalurp_hp = 5
    cluster_size_nrp_hp = 5
    strand_specify=0


    mapcpu = 1
    var_limit=20
    poly_limit=10
    rm_multi=0
    
    paired_end=False
    repeat=False
    options=[]
    read2=''
    read1=''
    #print sys.argv
    i=1
    while i< len(sys.argv):
        #if sys.argv[i]=='-b':
        #    try:
        #        read_format=int(sys.argv[i+1])
        #        options.append(i)
        #        options.append(i+1)
        #    except Exception, e:
        #        print 'options error!'
        #        help_doc()
        if sys.argv[i]=='-1':
            try:
                read1=sys.argv[i+1]
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
        elif sys.argv[i]=='-2':
            paired_end=True
            try:
                read2=sys.argv[i+1]
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-rp':
            try:
                repeat=sys.argv[i+1]
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-ss':
            try:
                strand_specify=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-c':
            try:
                cutbp=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-p':
            try:
                mapcpu=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-cd':
            try:
                cluster_distance=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-csad1':
            try:
                cluster_size_alu_ad1=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-csad2':
            try:
                cluster_size_alu_ad2=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-csnar':
            try:
                cluster_size_nalurp=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-csnr':
            try:
                cluster_size_nrp=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-csrg':
            try:
                cluster_size_rg=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-cshp':
            try:
                cluster_size_hp=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-csahp':
            try:
                cluster_size_alu_hp=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-csnarhp':
            try:
                cluster_size_nalurp_hp=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
        elif sys.argv[i]=='-csnrhp':
            try:
                cluster_size_nrp_hp=int(sys.argv[i+1])
                options.append(i)
                options.append(i+1)
            except Exception, e:
                print 'options error!'
                help_doc()
                exit()
    
    
        i += 1
    
    all_argv=[]
    i=1
    while i< len(sys.argv):
        if i not in options:
            all_argv.append(i)
        i=i+1
    
    if len(all_argv)!=4 or read1=='':
        help_doc()
        exit()
    
    
    refgenome=sys.argv[all_argv[0]]
    output=sys.argv[all_argv[1]]+'/'
    tmp=output+'/tmp/'

    bwa=sys.argv[all_argv[2]]
    samtools=sys.argv[all_argv[3]]
    
    if os.path.exists(output)==False:
            os.mkdir(output)
    if os.path.exists(tmp)==False:
            os.mkdir(tmp)
    
    frc=open(tmp+'PARAMETER.txt','w')
    frc.write(sys.argv[0])
    for one in sys.argv[1:]:
        frc.write('   '+one)
    frc.write('\n')
    frc.close()
    
    
    
    def fq2sam(TAG,paired_end,read1,read2,tmp,refgenome,bwa,samtools,mapcpu, read_format):
        if paired_end==True:
            mapcpu=max([int(int(mapcpu)/2.0),1])
        ori_tmp=tmp
        tmp=tmp+'/'+TAG+'/'
        if os.path.exists(tmp)==False:
            os.mkdir(tmp)
        
        step1_1=subprocess.Popen(bwa+' aln -t '+str(mapcpu)+' '+refgenome+' '+read1+' > '+tmp+'read1.sai',shell=True)
        if paired_end==True:
            step1_2=subprocess.Popen(bwa+' aln  -t '+str(mapcpu)+' '+refgenome+' '+read2+' > '+tmp+'read2.sai',shell=True)

        step1_1.wait()
        if paired_end==True:
            step1_2.wait()
        step1_3=subprocess.Popen(bwa+' samse -n4 '+refgenome+' '+tmp+'read1.sai '+read1+' > '+tmp+'name_read1.sam',shell=True)
        if paired_end==True:
            step1_4=subprocess.Popen(bwa+' samse -n4 '+refgenome+' '+tmp+'read2.sai '+read2+' > '+tmp+'name_read2.sam',shell=True)
        step1_3.wait()
        if paired_end==True:
            step1_4.wait()
        if os.path.exists(tmp+'name_read1.sam'):
            if os.path.exists(tmp+'read1.sai'):
                    os.remove(tmp+'read1.sai')
            if os.path.exists(ori_tmp+'cut_read1.fastq'):
                    os.remove(ori_tmp+'cut_read1.fastq')
        if os.path.exists(tmp+'name_read2.sam'):
            if os.path.exists(tmp+'read2.sai'):
                    os.remove(tmp+'read2.sai')
            if os.path.exists(ori_tmp+'cut_read2.fastq'):
                    os.remove(ori_tmp+'cut_read2.fastq')
    
        step1_7=subprocess.Popen(samtools+' view -bS '+tmp+'name_read1.sam >'+tmp+'name_read1.bam',shell=True)
        if paired_end==True:
            step1_8=subprocess.Popen(samtools+' view -bS '+tmp+'name_read2.sam >'+tmp+'name_read2.bam',shell=True)
        step1_7.wait()
        if paired_end==True:
            step1_8.wait()
        if paired_end==True:
            step1_9=subprocess.Popen(samtools+' sort '+tmp+'name_read1.bam '+tmp+'name_read1_sorted',shell=True)
            step1_10=subprocess.Popen(samtools+' sort '+tmp+'name_read2.bam '+tmp+'name_read2_sorted',shell=True)
            step1_9.wait()
            step1_10.wait()
            step1_11=subprocess.Popen(samtools+' merge -f '+tmp+'all.bam '+tmp+'name_read1_sorted.bam '+tmp+'name_read2_sorted.bam',shell=True)
            step1_11.wait()
            if os.path.exists(tmp+'all.bam'):
                    if os.path.exists(tmp+'name_read1.sam'):
                            os.remove(tmp+'name_read1.sam')
                    if os.path.exists(tmp+'name_read1.bam'):
                            os.remove(tmp+'name_read1.bam')
                    if os.path.exists(tmp+'name_read1_sorted.bam'):
                            os.remove(tmp+'name_read1_sorted.bam')
                    if os.path.exists(tmp+'name_read2.sam'):
                            os.remove(tmp+'name_read2.sam')
                    if os.path.exists(tmp+'name_read2.bam'):
                            os.remove(tmp+'name_read2.bam')
                    if os.path.exists(tmp+'name_read2_sorted.bam'):
                            os.remove(tmp+'name_read2_sorted.bam')
    
        else:
            step1_9=subprocess.Popen(samtools+' sort '+tmp+'name_read1.bam '+tmp+'all',shell=True)
            step1_9.wait()
            if os.path.exists(tmp+'all.bam'):
                    if os.path.exists(tmp+'name_read1.sam'):
                            os.remove(tmp+'name_read1.sam')
                    if os.path.exists(tmp+'name_read1.bam'):
                            os.remove(tmp+'name_read1.bam')
        step2_2=subprocess.Popen(samtools+' view -h -o '+tmp+'all.sam '+tmp+'all.bam',shell=True)
        step2_2.wait()
        subprocess.Popen('cp '+tmp+'./all.sam '+ori_tmp+'/'+TAG+'_all.sam',shell=True).wait()
        if os.path.exists(tmp+'all.sam'):
            os.remove(tmp+'all.sam')
    
    
      
    
    
    
    
    #try:
    if 1==1: 

        print 'preprocessing...'
        if read_format !=0:
            subprocess.Popen(samtools+' view -h -o '+tmp+'read1.sam '+read1,shell=True).wait()
            sprint.sam2fq(tmp+'read1.sam', tmp+'read1.fq')
            read1=tmp+'read1.fq'
            sprint.cut(read1,tmp+'cut_read1.fastq',cutbp,'read1')
            if paired_end==True:
                subprocess.Popen(samtools+' view -h -o '+tmp+'read2.sam '+read2,shell=True).wait()
                sprint.sam2fq(tmp+'read2.sam', tmp+'read2.fq')
                read2=tmp+'read2.fq'
                sprint.cut(read2,tmp+'cut_read2.fastq',cutbp,'read2')             
        else:
            if strand_specify==0:
                sprint.cut(read1,tmp+'cut_read1.fastq',cutbp,'read1')
                if paired_end==True:
                    sprint.cut(read2,tmp+'cut_read2.fastq',cutbp,'read2')
            else:
                sprint.cut(read1,tmp+'cut_read1.fastq',cutbp,'read2')
                if paired_end==True:
                    sprint.cut(read2,tmp+'cut_read2.fastq',cutbp,'read1')


        sprint.get_baseq_cutoff(read1,tmp+'baseq.cutoff')
                    
        print 'mapping...'
    
        TAG='genome'
        fq2sam(TAG,paired_end,tmp+'cut_read1.fastq',tmp+'cut_read2.fastq',tmp,refgenome,bwa,samtools,mapcpu,read_format)
    
        subprocess.Popen(samtools+' view -f4 '+tmp+'/'+TAG+'/all.bam > '+tmp+'/'+TAG+'_unmapped.sam',shell=True).wait()
        sprint.umsam2fq(tmp+'/'+TAG+'_unmapped.sam',tmp+'/'+TAG+'_unmapped.fq')
     
        if os.path.exists(refgenome+'.trans.fa'):
            TAG='transcript'
            fq2sam(TAG,False,tmp+'/genome_unmapped.fq',read2,tmp,refgenome+'.trans.fa',bwa,samtools,mapcpu,read_format)
    
            subprocess.Popen(samtools+' view -f4 '+tmp+'/'+TAG+'/all.bam > '+tmp+'/'+TAG+'_unmapped.sam',shell=True).wait()
            sprint.umsam2fq(tmp+'/'+TAG+'_unmapped.sam',tmp+'/regular_unmapped.fq')    
            sprint.maskfq(tmp+'/regular_unmapped.fq','A','G')
        else:
            sprint.umsam2fq(tmp+'/'+TAG+'_unmapped.sam',tmp+'/regular_unmapped.fq')
            sprint.maskfq(tmp+'/regular_unmapped.fq','A','G')
    
    
        TAG='genome_mskAG'
        fq2sam(TAG,False,tmp+'/regular_unmapped_A_to_G.fq',read2,tmp,refgenome+'.mskAG.fa',bwa,samtools,mapcpu,read_format)
    
        subprocess.Popen(samtools+' view -f4 '+tmp+'/'+TAG+'/all.bam > '+tmp+'/'+TAG+'_unmapped.sam',shell=True).wait()
        sprint.umsam2fq(tmp+'/'+TAG+'_unmapped.sam',tmp+'/'+TAG+'_unmapped.fq')    
    
        TAG='genome_mskTC'
        fq2sam(TAG,False,tmp+'/regular_unmapped_A_to_G.fq',read2,tmp,refgenome+'.mskTC.fa',bwa,samtools,mapcpu,read_format)
    
        subprocess.Popen(samtools+' view -f4 '+tmp+'/'+TAG+'/all.bam > '+tmp+'/'+TAG+'_unmapped.sam',shell=True).wait()
        sprint.umsam2fq(tmp+'/'+TAG+'_unmapped.sam',tmp+'/'+TAG+'_unmapped.fq')    
        
        
        if os.path.exists(refgenome+'.trans.fa'):
            TAG='transcript_mskAG'
            fq2sam(TAG,False,tmp+'/genome_mskAG_unmapped.fq',read2,tmp,refgenome+'.trans.fa.mskAG.fa',bwa,samtools,mapcpu,read_format)
    
            TAG='transcript_mskTC'
            fq2sam(TAG,False,tmp+'/genome_mskTC_unmapped.fq',read2,tmp,refgenome+'.trans.fa.mskTC.fa',bwa,samtools,mapcpu,read_format)
    
        if os.path.exists(tmp+'genome_mskAG_unmapped.sam'):
                    if os.path.exists(tmp+'cut_read1.fastq'):
                            os.remove(tmp+'cut_read1.fastq')
                    if os.path.exists(tmp+'cut_read2.fastq'):
                            os.remove(tmp+'cut_read2.fastq')
                    if os.path.exists(tmp+'genome_mskAG_unmapped.fq'):
                            os.remove(tmp+'genome_mskAG_unmapped.fq')
                    if os.path.exists(tmp+'genome_mskAG_unmapped.sam'):
                            os.remove(tmp+'genome_mskAG_unmapped.sam')
                    if os.path.exists(tmp+'genome_mskTC_unmapped.fq'):
                            os.remove(tmp+'genome_mskTC_unmapped.fq')
                    if os.path.exists(tmp+'genome_mskTC_unmapped.sam'):
                            os.remove(tmp+'genome_mskTC_unmapped.sam')
                    if os.path.exists(tmp+'genome_unmapped.fq'):
                            os.remove(tmp+'genome_unmapped.fq')
                    if os.path.exists(tmp+'genome_unmapped.sam'):
                            os.remove(tmp+'genome_unmapped.sam')
                    if os.path.exists(tmp+'transcript_unmapped_A_to_G.fq'):
                            os.remove(tmp+'transcript_unmapped_A_to_G.fq')
                    if os.path.exists(tmp+'transcript_unmapped.fq'):
                            os.remove(tmp+'transcript_unmapped.fq')
                    if os.path.exists(tmp+'transcript_unmapped.sam'):
                            os.remove(tmp+'transcript_unmapped.sam')
                    if os.path.exists(tmp+'regular_unmapped.fq'):
                            os.remove(tmp+'regular_unmapped.fq')
                    if os.path.exists(tmp+'regular_unmapped_A_to_G.fq'):
                            os.remove(tmp+'regular_unmapped_A_to_G.fq')
                            
        
        if os.path.exists(refgenome+'.trans.fa'):
            sprint.recover_sam(tmp+'transcript_mskAG_all.sam',tmp+'transcript_mskAG_all.sam.rcv', var_limit, poly_limit, rm_multi)
            sprint.sam2zz(tmp+'transcript_mskAG_all.sam.rcv',refgenome+'.trans.fa',tmp+'transcript_mskAG_all.zz')
            sprint.recover_sam(tmp+'transcript_mskTC_all.sam',tmp+'transcript_mskTC_all.sam.rcv', var_limit, poly_limit, rm_multi)
            sprint.sam2zz(tmp+'transcript_mskTC_all.sam.rcv',refgenome+'.trans.fa',tmp+'transcript_mskTC_all.zz')
            sprint.sam2zz(tmp+'transcript_all.sam',refgenome+'.trans.fa',tmp+'transcript_all.zz')
            
            if os.path.exists(tmp+'transcript_mskAG_all.sam.rcv'):
                os.remove(tmp+'transcript_mskAG_all.sam.rcv')
            if os.path.exists(tmp+'transcript_mskAG_all.sam'):
                os.remove(tmp+'transcript_mskAG_all.sam')
            if os.path.exists(tmp+'transcript_mskTC_all.sam.rcv'):
                os.remove(tmp+'transcript_mskTC_all.sam.rcv')
            if os.path.exists(tmp+'transcript_mskTC_all.sam'):
                os.remove(tmp+'transcript_mskTC_all.sam')
            if os.path.exists(tmp+'transcript_all.sam'):
                os.remove(tmp+'transcript_all.sam')

    
        sprint.recover_sam(tmp+'genome_mskAG_all.sam',tmp+'genome_mskAG_all.sam.rcv', var_limit, poly_limit, rm_multi)
        sprint.sam2zz(tmp+'genome_mskAG_all.sam.rcv',refgenome,tmp+'genome_mskAG_all.zz')
        sprint.recover_sam(tmp+'genome_mskTC_all.sam',tmp+'genome_mskTC_all.sam.rcv', var_limit, poly_limit, rm_multi)
        sprint.sam2zz(tmp+'genome_mskTC_all.sam.rcv',refgenome,tmp+'genome_mskTC_all.zz')
        sprint.sam2zz(tmp+'genome_all.sam',refgenome,tmp+'genome_all.zz')

        if os.path.exists(tmp+'genome_mskAG_all.sam.rcv'):
                os.remove(tmp+'genome_mskAG_all.sam.rcv')
        if os.path.exists(tmp+'genome_mskAG_all.sam'):
                os.remove(tmp+'genome_mskAG_all.sam')
        if os.path.exists(tmp+'genome_mskTC_all.sam.rcv'):
                os.remove(tmp+'genome_mskTC_all.sam.rcv')
        if os.path.exists(tmp+'genome_mskTC_all.sam'):
                os.remove(tmp+'genome_mskTC_all.sam')
        if os.path.exists(tmp+'genome_all.sam'):
                os.remove(tmp+'genome_all.sam')
                
        
        if os.path.exists(refgenome+'.trans.fa'):
            sprint.dedup(tmp+'transcript_mskAG_all.zz',tmp+'transcript_mskAG_all.zz.dedup')
            sprint.dedup(tmp+'transcript_mskTC_all.zz',tmp+'transcript_mskTC_all.zz.dedup') 
            sprint.dedup(tmp+'transcript_all.zz',tmp+'transcript_all.zz.dedup') 
    
        sprint.dedup(tmp+'genome_mskAG_all.zz',tmp+'genome_mskAG_all.zz.dedup') 
        sprint.dedup(tmp+'genome_mskTC_all.zz',tmp+'genome_mskTC_all.zz.dedup') 
        sprint.dedup(tmp+'genome_all.zz',tmp+'genome_all.zz.dedup')
         
        if os.path.exists(tmp+'transcript_mskAG_all.zz'):
                os.remove(tmp+'transcript_mskAG_all.zz')
        if os.path.exists(tmp+'transcript_mskTC_all.zz'):
                os.remove(tmp+'transcript_mskTC_all.zz')
        if os.path.exists(tmp+'transcript_all.zz'):
                os.remove(tmp+'transcript_all.zz')
        if os.path.exists(tmp+'genome_mskAG_all.zz'):
                os.remove(tmp+'genome_mskAG_all.zz')
        if os.path.exists(tmp+'genome_mskTC_all.zz'):
                os.remove(tmp+'genome_mskTC_all.zz')
        if os.path.exists(tmp+'genome_all.zz'):
                os.remove(tmp+'genome_all.zz')

        print 'identifying SNVs...'
   
        if os.path.exists(refgenome+'.trans.fa'):
            sprint.mask_zz2snv(tmp+'transcript_mskAG_all.zz.dedup',tmp+'transcript_mskAG_all.zz.dedup.snv',tmp+'baseq.cutoff') 
            sprint.mask_zz2snv(tmp+'transcript_mskTC_all.zz.dedup',tmp+'transcript_mskTC_all.zz.dedup.snv',tmp+'baseq.cutoff') 
            sprint.mask_zz2snv(tmp+'transcript_all.zz.dedup',tmp+'transcript_all.zz.dedup.snv',tmp+'baseq.cutoff')

            sprint.tzz2gzz(refgenome+'.trans.fa.loc', tmp+'transcript_mskAG_all.zz.dedup', tmp+'transcript_mskAG_all.zz.dedup.genome.zz')
            sprint.tzz2gzz(refgenome+'.trans.fa.loc', tmp+'transcript_mskTC_all.zz.dedup', tmp+'transcript_mskTC_all.zz.dedup.genome.zz')
            sprint.tzz2gzz(refgenome+'.trans.fa.loc', tmp+'transcript_all.zz.dedup', tmp+'transcript_all.zz.dedup.genome.zz')
             
    
        sprint.mask_zz2snv(tmp+'genome_mskAG_all.zz.dedup',tmp+'genome_mskAG_all.zz.dedup.snv',tmp+'baseq.cutoff') 
        sprint.mask_zz2snv(tmp+'genome_mskTC_all.zz.dedup',tmp+'genome_mskTC_all.zz.dedup.snv',tmp+'baseq.cutoff') 
        sprint.mask_zz2snv(tmp+'genome_all.zz.dedup',tmp+'genome_all.zz.dedup.snv',tmp+'baseq.cutoff') 
        

        if os.path.exists(refgenome+'.trans.fa'):
            subprocess.Popen('cat '+tmp+'/genome_mskAG_all.zz.dedup '+tmp+'/genome_mskTC_all.zz.dedup '+tmp+'/genome_all.zz.dedup '+tmp+'/transcript_mskAG_all.zz.dedup.genome.zz '+tmp+'/transcript_mskTC_all.zz.dedup.genome.zz '+tmp+'/transcript_all.zz.dedup.genome.zz '+' > '+tmp+'/all_combined.zz',shell=True).wait()
            sprint.sort_zz(tmp+'/all_combined.zz', tmp+'/all_combined.zz.sorted')
        else: 
            subprocess.Popen('cat '+tmp+'/genome_mskAG_all.zz.dedup '+tmp+'/genome_mskTC_all.zz.dedup '+tmp+'/genome_all.zz.dedup '+' > '+tmp+'/all_combined.zz',shell=True).wait()
            sprint.sort_zz(tmp+'/all_combined.zz', tmp+'/all_combined.zz.sorted')
        
     
        if os.path.exists(refgenome+'.trans.fa'):
            sprint.transcript_locator(tmp+'transcript_mskAG_all.zz.dedup.snv',refgenome+'.trans.fa.loc', tmp+'transcript_mskAG_all.zz.dedup.snv.genome.snv')
            sprint.transcript_locator(tmp+'transcript_mskTC_all.zz.dedup.snv',refgenome+'.trans.fa.loc', tmp+'transcript_mskTC_all.zz.dedup.snv.genome.snv')
            sprint.transcript_locator(tmp+'transcript_all.zz.dedup.snv',refgenome+'.trans.fa.loc', tmp+'transcript_all.zz.dedup.snv.genome.snv')

            sprint.transcript_sort(tmp+'transcript_all.zz.dedup.snv.genome.snv',tmp+'transcript_all.zz.dedup.snv.genome.snv.sort')
            sprint.transcript_sort(tmp+'transcript_mskTC_all.zz.dedup.snv.genome.snv',tmp+'transcript_mskTC_all.zz.dedup.snv.genome.snv.sort')
            sprint.transcript_sort(tmp+'transcript_mskAG_all.zz.dedup.snv.genome.snv',tmp+'transcript_mskAG_all.zz.dedup.snv.genome.snv.sort')

            sprint.snv_or(tmp+'transcript_all.zz.dedup.snv.genome.snv.sort',tmp+'genome_all.zz.dedup.snv',tmp+'regular.snv')
            sprint.snv_or(tmp+'transcript_mskTC_all.zz.dedup.snv.genome.snv.sort',tmp+'genome_mskTC_all.zz.dedup.snv', tmp+'hyper_mskTC.snv')
            sprint.snv_or(tmp+'transcript_mskAG_all.zz.dedup.snv.genome.snv.sort',tmp+'genome_mskAG_all.zz.dedup.snv', tmp+'hyper_mskAG.snv')


        else:
            subprocess.Popen('cp '+tmp+'/genome_all.zz.dedup.snv '+tmp+'/regular.snv',shell=True).wait()
            subprocess.Popen('cp '+tmp+'/genome_mskTC_all.zz.dedup.snv '+tmp+'/hyper_mskTC.snv',shell=True).wait()
            subprocess.Popen('cp '+tmp+'/genome_mskAG_all.zz.dedup.snv '+tmp+'/hyper_mskAG.snv',shell=True).wait()
        
        


        print 'identifying RESs...'

        if repeat !=False:

            sprint.annotate(tmp+'regular.snv',repeat,tmp+'regular.snv.anno')    
            sprint.seperate(tmp+'regular.snv.anno',tmp+'regular.snv.anno.alu',tmp+'regular.snv.anno.nalurp',tmp+'regular.snv.anno.nrp','Alu')
            sprint.get_snv_with_ad(tmp+'regular.snv.anno.alu',tmp+'regular.snv.anno.alu.ad2',2)
            sprint.snv_cluster(tmp+'regular.snv.anno.alu',tmp+'regular_alu.res.ad1', cluster_distance, cluster_size_alu_ad1)
            sprint.snv_cluster(tmp+'regular.snv.anno.alu.ad2',tmp+'regular_alu.res.ad2', cluster_distance, cluster_size_alu_ad2)
            sprint.bed_or(tmp+'regular_alu.res.ad1',tmp+'regular_alu.res.ad2',tmp+'regular_alu.res')
            sprint.snv_cluster(tmp+'regular.snv.anno.nalurp',tmp+'regular_nalurp.res', cluster_distance, cluster_size_nalurp)
            sprint.snv_cluster(tmp+'regular.snv.anno.nrp',tmp+'regular_nrp.res', cluster_distance, cluster_size_nrp)
            sprint.combine_res(tmp+'regular_alu.res',tmp+'regular_nalurp.res',tmp+'regular_nrp.res',tmp+'regular_split.res')
            cluster_size_regular_max=max([cluster_size_alu_ad1,cluster_size_alu_ad2,cluster_size_nalurp,cluster_size_nrp])
            sprint.combine_res(tmp+'regular.snv.anno.alu',tmp+'regular.snv.anno.nalurp',tmp+'regular.snv.anno.nrp',tmp+'regular.snv.anno.rmsrp')
            sprint.snv_cluster(tmp+'regular.snv.anno.rmsrp',tmp+'regular_overall.res', cluster_distance, cluster_size_regular_max)
            sprint.res_or(tmp+'regular_split.res',tmp+'regular_overall.res',tmp+'regular.res')
    

            sprint.annotate(tmp+'hyper_mskTC.snv',repeat,tmp+'hyper_mskTC.snv.anno')    
            sprint.seperate(tmp+'hyper_mskTC.snv.anno',tmp+'hyper_mskTC.snv.anno.alu',tmp+'hyper_mskTC.snv.anno.nalurp',tmp+'hyper_mskTC.snv.anno.nrp','Alu')
            sprint.snv_cluster(tmp+'hyper_mskTC.snv.anno.alu',tmp+'hyper_mskTC_alu.res', cluster_distance, cluster_size_alu_hp)
            sprint.snv_cluster(tmp+'hyper_mskTC.snv.anno.nalurp',tmp+'hyper_mskTC_nalurp.res', cluster_distance, cluster_size_nalurp_hp)
            sprint.snv_cluster(tmp+'hyper_mskTC.snv.anno.nrp',tmp+'hyper_mskTC_nrp.res', cluster_distance, cluster_size_nrp_hp)
            sprint.combine_res(tmp+'hyper_mskTC_alu.res',tmp+'hyper_mskTC_nalurp.res',tmp+'hyper_mskTC_nrp.res',tmp+'hyper_mskTC_split.res')            
            cluster_size_hyper_max=max([cluster_size_alu_hp,cluster_size_nalurp_hp,cluster_size_nrp_hp])
            sprint.combine_res(tmp+'hyper_mskTC.snv.anno.alu',tmp+'hyper_mskTC.snv.anno.nalurp',tmp+'hyper_mskTC.snv.anno.nrp',tmp+'hyper_mskTC.snv.anno.rmsrp')
            sprint.snv_cluster(tmp+'hyper_mskTC.snv.anno.rmsrp',tmp+'hyper_mskTC_overall.res', cluster_distance, cluster_size_hyper_max)
            sprint.res_or(tmp+'hyper_mskTC_split.res',tmp+'hyper_mskTC_overall.res',tmp+'hyper_mskTC.res')


            sprint.annotate(tmp+'hyper_mskAG.snv',repeat,tmp+'hyper_mskAG.snv.anno')    
            sprint.seperate(tmp+'hyper_mskAG.snv.anno',tmp+'hyper_mskAG.snv.anno.alu',tmp+'hyper_mskAG.snv.anno.nalurp',tmp+'hyper_mskAG.snv.anno.nrp','Alu')
            sprint.snv_cluster(tmp+'hyper_mskAG.snv.anno.alu',tmp+'hyper_mskAG_alu.res', cluster_distance, cluster_size_alu_hp)
            sprint.snv_cluster(tmp+'hyper_mskAG.snv.anno.nalurp',tmp+'hyper_mskAG_nalurp.res', cluster_distance, cluster_size_nalurp_hp)
            sprint.snv_cluster(tmp+'hyper_mskAG.snv.anno.nrp',tmp+'hyper_mskAG_nrp.res', cluster_distance, cluster_size_nrp_hp)
            sprint.combine_res(tmp+'hyper_mskAG_alu.res',tmp+'hyper_mskAG_nalurp.res',tmp+'hyper_mskAG_nrp.res',tmp+'hyper_mskAG_split.res')            
            cluster_size_hyper_max=max([cluster_size_alu_hp,cluster_size_nalurp_hp,cluster_size_nrp_hp])
            sprint.combine_res(tmp+'hyper_mskAG.snv.anno.alu',tmp+'hyper_mskAG.snv.anno.nalurp',tmp+'hyper_mskAG.snv.anno.nrp',tmp+'hyper_mskAG.snv.anno.rmsrp')
            sprint.snv_cluster(tmp+'hyper_mskAG.snv.anno.rmsrp',tmp+'hyper_mskAG_overall.res', cluster_distance, cluster_size_hyper_max)
            sprint.res_or(tmp+'hyper_mskAG_split.res',tmp+'hyper_mskAG_overall.res',tmp+'hyper_mskAG.res')

            sprint.snv_or(tmp+'hyper_mskTC.res',tmp+'hyper_mskAG.res',tmp+'hyper.res')


            
    
     
        else:
            sprint.snv_cluster(tmp+'regular.snv',tmp+'regular.res_tmp',cluster_distance,cluster_size_rg) 
            sprint.o2b(tmp+'regular.res_tmp',tmp+'regular.res') 

            sprint.snv_cluster(tmp+'hyper_mskTC.snv',tmp+'hyper_mskTC.res',cluster_distance,cluster_size_hp)
            sprint.snv_cluster(tmp+'hyper_mskAG.snv',tmp+'hyper_mskAG.res',cluster_distance,cluster_size_hp)
            sprint.snv_or(tmp+'hyper_mskTC.res',tmp+'hyper_mskAG.res',tmp+'hyper.res')

        try:
            subprocess.Popen('rm -rf '+tmp+'/*.anno.*',shell=True).wait()
        except Exception, e:
            pass

        '''
        if repeat !=False:
            sprint.get_res(tmp+'regular_alu.res',tmp+'regular_nalurp.res',tmp+'regular_nrp.res',  tmp+'hyper.res',  tmp+'SPRINT_identified')
            sprint.bed_sort(tmp+'SPRINT_identified_A_to_I_regular.res',tmp+'SPRINT_identified_A_to_I_regular.res_sort')
            sprint.bed_sort(tmp+'SPRINT_identified_A_to_I_hyper.res',tmp+'SPRINT_identified_A_to_I_hyper.res_sort')
            sprint.bed_sort(tmp+'SPRINT_identified_C_to_U.res',tmp+'SPRINT_identified_C_to_U.res_sort')
        
            sprint.o2b(tmp+'SPRINT_identified_A_to_I_regular.res_sort',output+'SPRINT_identified_A_to_I_regular.res')
            sprint.o2b(tmp+'SPRINT_identified_A_to_I_hyper.res_sort',output+'SPRINT_identified_A_to_I_hyper.res')
            sprint.o2b(tmp+'SPRINT_identified_C_to_U.res_sort',output+'SPRINT_identified_C_to_U.res')
        
            sprint.snv_or(tmp+'SPRINT_identified_A_to_I_hyper.res',tmp+'SPRINT_identified_A_to_I_regular.res',output+'SPRINT_identified_A_to_I_all.res') 
        '''

       # subprocess.Popen('cp '+tmp+'/regular.res '+output+'/SPRINT_identified_regular.res',shell=True).wait()
        sprint.get_depth( tmp+'/all_combined.zz.sorted' , tmp+'/regular.res', tmp+'/regular.res.depth')
        subprocess.Popen('echo "#Chrom\tStart(0base)\tEnd(1base)\tType\tSupporting_reads\tStrand\tAD:DP" | cat - '+tmp +'/regular.res.depth   > '+output+'/SPRINT_identified_regular.res',shell=True).wait()
       # subprocess.Popen('cp '+tmp+'/hyper.res '+output+'/SPRINT_identified_hyper.res',shell=True).wait()
        sprint.get_depth( tmp+'/all_combined.zz.sorted' , tmp+'/hyper.res', tmp+'/hyper.res.depth')
        subprocess.Popen('echo "#Chrom\tStart(0base)\tEnd(1base)\tType\tSupporting_reads\tStrand\tAD:DP" | cat - '+tmp +'/hyper.res.depth   > '+output+'/SPRINT_identified_hyper.res',shell=True).wait()
        subprocess.Popen('cp '+tmp+'/PARAMETER.txt '+output+'/PARAMETER.txt',shell=True).wait()

        #subprocess.Popen('grep "AG" '+tmp+'/hyper.res | grep "+"  > '+tmp+'/hyper_AG+.res',shell=True).wait()
        #subprocess.Popen('grep "TC" '+tmp+'/hyper.res | grep "-"  > '+tmp+'/hyper_TC-.res',shell=True).wait()
        #sprint.snv_or(tmp+'/hyper_AG+.res',tmp+'/hyper_TC-.res',tmp+'/hyper_AG.res') 
        #sprint.snv_or(tmp+'/regular.res',tmp+'/hyper_AG.res',tmp+'/all.res') 
        sprint.snv_or(tmp+'/regular.res',tmp+'/hyper.res',tmp+'/all.res') 
        sprint.get_depth( tmp+'/all_combined.zz.sorted' , tmp+'/all.res', tmp+'/all.res.depth')
        subprocess.Popen('echo "#Chrom\tStart(0base)\tEnd(1base)\tType\tSupporting_reads\tStrand\tAD:DP" | cat - '+tmp +'/all.res.depth   > '+output+'/SPRINT_identified_all.res',shell=True).wait()
        print 'finished !'
        sys.exit(0)
    try:
        pass
    except Exception,e:
        print ''
        print 'ERROR!'
        print ''
        print e
        print ''
        help_doc()
    
    
    
    
    
    
    
 
#if __name__=='__main__':   
#    main()

