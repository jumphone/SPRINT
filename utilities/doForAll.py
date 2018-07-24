import subprocess
import multiprocessing
import os

ALL_A_to_I='ALL_A_to_I.res.sorted.uniq.bed'

def Work(sprint_out_dir,a):
    subprocess.Popen('python getA2I.py 0 '+sprint_out_dir+' '+sprint_out_dir+'/A_to_I.res',shell=True).wait()
    if os.path.exists(sprint_out_dir+'/all_combined.zz.sorted.bam')==False:

            subprocess.Popen('python zz2sam.py '+sprint_out_dir+'/all_combined.zz.sorted ',shell=True).wait()
            subprocess.Popen('cat SAMheader.txt '+sprint_out_dir+'/all_combined.zz.sorted.sam > '+sprint_out_dir+'/all_combined.zz.sorted.sam.header',shell=True).wait()
            subprocess.Popen('samtools view -bS '+sprint_out_dir+'/all_combined.zz.sorted.sam.header > '+sprint_out_dir+'/all_combined.zz.bam',shell=True).wait()
            subprocess.Popen('samtools sort '+sprint_out_dir+'/all_combined.zz.bam -f '+sprint_out_dir+'/all_combined.zz.sorted.bam',shell=True ).wait()

            subprocess.Popen('rm -rf '+sprint_out_dir+'/all_combined.zz.sorted.sam',shell=True).wait()
            subprocess.Popen('rm -rf '+sprint_out_dir+'/all_combined.zz.sorted.sam.header',shell=True).wait()
            subprocess.Popen('rm -rf '+sprint_out_dir+'/all_combined.zz.bam',shell=True).wait()
            subprocess.Popen('samtools stats '+sprint_out_dir+'/all_combined.zz.sorted.bam > '+sprint_out_dir+'/all_combined.zz.sorted.bam.stats',shell=True).wait()
    
    subprocess.Popen('samtools depth -b '+ALL_A_to_I+' '+sprint_out_dir+'/all_combined.zz.sorted.bam'+' > '+sprint_out_dir+'/ALL_A_to_I.depth ',shell=True).wait()
    subprocess.Popen('python  getAlt.py '+sprint_out_dir+'/all_combined.zz.sorted  '+ALL_A_to_I+' '+sprint_out_dir+'/ALL_A_to_I.alt ',shell=True).wait()
 
    #subprocess.Popen('python combineAltDep.py '+sprint_out_dir, shell=True).wait()
    #subprocess.Popen('python statGENE.py '+sprint_out_dir, shell=True).wait()
    
  
fa=open('lst.txt')
fa.readline()
PROC_LIMIT=4
jobs=[]
i=1



for line in fa:
    print i;i+=1
    seq=line.rstrip().split('\t')
    sprint_out_dir=seq[0]+'.fastq_sprint'
    print sprint_out_dir

    if 1==1:
        p=multiprocessing.Process(target=Work, args=(sprint_out_dir,1))
        p.start()
        jobs.append(p)
        if len(jobs)>=PROC_LIMIT:
            for p in jobs:
                p.join()
            jobs=[]
for p in jobs:
    p.join()

    
