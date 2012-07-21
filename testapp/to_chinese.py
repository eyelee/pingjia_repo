def to_chinese(s):
    if isinstance(s, unicode):
        print s.encode('gb2312')
    else:
        print s.decode('utf-8').encode('gb2312')

s=u'9.8\u4e07\u5143'
     
print to_chinese(s)