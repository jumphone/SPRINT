import subprocess,os,sys
import  sprint 

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
        print ""
        print ""
        print "   Usage:"
        print ""
        print "      sprint_from_bam   [options]  alinged_reads(.bam)   reference_genome(.fa)   output_path   samtools_path"
        print ""
        print "      options:"
        print "         -rp      repeat_file      # Optional, you can download it from http://sprint.software/SPRINT/dbrep/"
        print "         -cd      INT              # The distance cutoff of SNV duplets (default is 200)"
        print "         -csad1   INT              # Regular - [-rp is required] cluster size - Alu - AD >=1 (default is 3)"
        print "         -csad2   INT              # Regular - [-rp is required] cluster size - Alu - AD >=2 (default is 2)"
        print "         -csnar   INT              # Regular - [-rp is required] cluster size - nonAlu Repeat - AD >=1 (default is 5)"
        print "         -csnr    INT              # Regular - [-rp is required] cluster size - nonRepeat - AD >=1 (default is 7)"
        print "         -csrg    INT              # Regular - [without -rp] cluster size - AD >=1 (default is 5)"
        print ""
        print "   Example:"
        print ""
        print "       sprint_from_bam -rp hg19_repeat.txt  aligned_reads.bam  hg19.fa  output  ./samtools-1.2/samtools"
        print ""
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
        if sys.argv[i]=='-1':
            try:
                read1=sys.argv[i+1]
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
    
    
        i += 1
    
    all_argv=[]
    i=1
    while i< len(sys.argv):
        if i not in options:
            all_argv.append(i)
        i=i+1
    
    if len(all_argv)!=4 :
        help_doc()
        exit()
    
    
    refgenome=sys.argv[all_argv[1]]
    output=sys.argv[all_argv[2]]+'/'
    tmp=output+'/tmp/'
    
    bam=sys.argv[all_argv[0]]
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
        print "BAM processing..." 
        subprocess.Popen(samtools+' view  '+bam+' > '+tmp+'/aligned.sam',shell=True).wait()
        sprint.change_sam_read_name(tmp+'/aligned.sam',tmp+'genome_all.sam','read1')
        sprint.sam2zz(tmp+'genome_all.sam',refgenome,tmp+'genome_all.zz')
        sprint.dedup(tmp+'genome_all.zz',tmp+'genome_all.zz.dedup')
        if os.path.exists(tmp+'genome_all.zz'):
                os.remove(tmp+'genome_all.zz')
        print 'identifying SNVs...'


        fi=open(tmp+'/genome_all.sam')
        fo=open(tmp+'/baseq.cutoff','w')
        did=0
        for line in fi: 
            if did==1:
                break
            qua=line.split('\t')[10]
            for i in qua:
                if ord(i)>76:
                    fo.write('89')
                    did=1
                    break
                if ord(i)<60:
                    fo.write('58')
                    did=1
                    break
        fi.close()
        fo.close()









        sprint.zz2snv(tmp+'genome_all.zz.dedup',tmp+'genome_all.zz.dedup.snv',tmp+'baseq.cutoff') 
        subprocess.Popen('cp '+tmp+'/genome_all.zz.dedup.snv '+tmp+'/regular.snv',shell=True).wait()
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
        else:
            sprint.snv_cluster(tmp+'regular.snv',tmp+'regular.res_tmp',cluster_distance,cluster_size_rg) 
            sprint.o2b(tmp+'regular.res_tmp',tmp+'regular.res') 
        try:
            subprocess.Popen('rm -rf '+tmp+'/*.anno.*',shell=True).wait()
        except Exception, e:
            pass
        sprint.get_depth( tmp+'/genome_all.zz.dedup' , tmp+'/regular.res', tmp+'/regular.res.depth')
        subprocess.Popen('echo "#Chrom\tStart(0base)\tEnd(1base)\tType\tSupporting_reads\tStrand\tAD:DP" | cat - '+tmp +'/regular.res.depth   > '+output+'/SPRINT_identified_regular.res',shell=True).wait()
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
    
    
    
    
main()    
    
    
 

