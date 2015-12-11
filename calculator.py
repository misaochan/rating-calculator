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
        goodcat = float(obj.goodcatlist[i])
        falsepos = float(obj.falseposlist[i])
        manualcat = float(manualcatlist[i])
        result = ((goodcat - falsepos)/3)/manualcat
        print "Score for sample", (i+1), "=", result
        resultsum = resultsum + result
        
    print "Total score =", resultsum

print "Scoring WikiData results..."        
ratingcalc(wikiDataObj)
print "\n"

print "Scoring Method C results..."
ratingcalc(methodCObj)