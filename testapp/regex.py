import re

line = "Cats are. smarter than dogs.";

matchObj = re.match( r'(.*) are(\.*)', line, re.M|re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(0) :", matchObj.group(0)
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"
    
# line = u'  9.9wanyuan  ' 
line1=u'90.900\u4e07\u5143'
pattern1=r'\d+(\.\d+)*'

price=re.match(pattern1,line1)
print "price", price.group()

#200nian10yueshangpai
line2=u'2010\u5e7410\u6708\u4e0a\u724c'
pattern2=r'(\d+).*'
date=re.match(pattern2,line2,re.U)
print "date:", date.group()
print "year", date.group(1)
#print "month", date.group(2)


