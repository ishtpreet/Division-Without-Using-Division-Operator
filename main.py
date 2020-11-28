def myDivision(divident, divisor):
  #Check for illegal division
  if divisor==0:
    return
  #Check if divident or divisor is negative, then quotient will be also negative
  sign=1
  if(divident<0):
    divident = -1*divident
    sign = -1
  if(divisor<0):
    divisor = -1*divisor
    sign = sign*-1
  quotient = 0
  while(divident>=divisor):
    divident -= divisor 
    quotient += 1
  return sign*quotient

divident = int(input("Enter divident: "))
divisor = int(input("Enter divisor: "))
print("Quotient is "+str(myDivision(divident, divisor)))
