import csv
import sys
import string

# "number","title","acronym","sme","impactavg","teamavg","impactavg2","teamavg2","fiwareavg","total","smecountry","leadercountry","leadertitle","leadergender","leadername","leadermail","teamcountry2","teamcountry3","teamcountry4","teamcountry5","teamint","teamsize","agribusiness","smartcity","cleantech","otherdomain"

include_fields = ["number","title","acronym","sme","impactavg","teamavg","fiwareavg","total","smecountry","leadercountry","leadergender","teamint","teamsize","agribusiness","smartcity","cleantech"]

force_yn_fields = ["agribusiness","smartcity","cleantech"]

def force_float(a) :
    try :
        return float(a)
    except Exception, e:
        return 0


def force_int(a) :
    try :
        return int(a)
    except Exception, e:
        return 0

def force_yn(a) :
    a=string.upper(a)
    if a in ["Y","N"] :
        return a
    else :
        return "N"

test_record= lambda a : (a["total"] != "") and (force_float(a["total"])>=21)

def transform(ins,outs) :
    for r in ins :
        if test_record(r) : 
            for k in r.keys() :
                if k not in include_fields :
                    del r[k]
            for k in force_yn_fields :
                r[k]=force_yn(r[k])
            outs.writerow(r)



if __name__=="__main__" :
    if "-h" in sys.argv :
        print "transforms csv STDIN -> STDOUT. No further parameters"
    else :
        ins=csv.DictReader(sys.stdin)
        sys.stdout.write("%s\n" % ",".join(include_fields))
        outs=csv.DictWriter(sys.stdout,include_fields)
        transform(ins,outs)


        

