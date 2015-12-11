class WikiData:
    goodcatlist=  [2,1,1,0,1,0,0,1,0,1]
    falseposlist= [1,0,0,1,0,1,0,3,0,0]
   

class MethodC:
    goodcatlist=  [3,1,1,2,1,1,0,1,1,2]
    falseposlist= [3,0,1,3,0,0,2,5,1,0]

    
manualcatlist=[5,5,3,3,1,1,3,1,2,3]   
wikiDataObj = WikiData()
methodCObj = MethodC()

def ratingcalc(obj):
    resultsum = 0
    for i in range(10):
        goodcat = obj.goodcatlist[i]
        falsepos = obj.falseposlist[i]
        manualcat = manualcatlist[i]
        
        result = ((float(goodcat) - float(falsepos))/3)/float(manualcat)
        print "Sample", (i+1), ":", goodcat, "good categories,", falsepos, "false positives,", manualcat, "manual categories."
        print "Score =", result
        resultsum = resultsum + result
        
    print "Total score =", resultsum

print "WikiData results:"        
ratingcalc(wikiDataObj)
print "\n"

print "Method C results:"
ratingcalc(methodCObj)