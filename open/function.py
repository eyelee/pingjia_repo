import re
import math

def Average(datalist):
    r=0
    for i in datalist:
        r+=i
    result=float(r)/len(datalist)
    if result<10:
        result=round(result,1)
    else:
        result=int(result)
    return result

def Normalprice(price):
    resource_price=re.search('\d+(\.\d+)?',str(price))
    if resource_price is not None:
        friendly_price=float(resource_price.group())
        normal_price=int(friendly_price*10000)
        return normal_price
    else:
        return 
    
def Normdistribution(x,u=0,sigma=0.4):
    x=float(x)/200
    u=float(u)/200
    pai=3.141592653
    e=2.718281828
    index=-pow((x-u),2)/(2*pow(sigma,2))
    result=1/(sigma*math.sqrt(2*pai))*pow(e,index)
    result=180*result
    return result