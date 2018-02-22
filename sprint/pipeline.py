#import sprint
def pipeline():
    import re,sys
    from sprint_prepare import prepare as PP
    from sprint_main import main as MA



    def help_doc():


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
        print ""
        print ""
        print '   Usage: '
        print ""
        print '      "sprint prepare" or "sprint pp"   #build mapping index'
        print ""
        print '      "sprint main" or "sprint ma"      #identify RESs'
        print ""
        print ""
        sys.exit(0)

    if len(sys.argv)<2:
        help_doc()

    if sys.argv[1] =='sprint_prepare' or sys.argv[1] =='prepare' or sys.argv[1] =='pp'  :
        sys.argv=sys.argv[1:]
        PP()

    elif sys.argv[1]=='sprint_main' or sys.argv[1]=='main' or sys.argv[1] =='ma':
        sys.argv=sys.argv[1:]
        MA()
    else:
        help_doc()

