def print_abacus(value):
       #
       ### Add you code here 
       #
    check = value/10000000000
    if check  != 0:
        print 'Number factor is too large'
        return
    if value < 0:
        print 'Choose a positive whole number'
    
    if not float(value).is_integer():
        print 'Enter a whole number'
    
    rows, itr, index = ["|00000*****   |"]*10, 0, 0
   
   # a little too complicated, but fairly straightforward
    while(value>0):
        index = 9 - itr
        rows[index],value,itr = rows[index][:(11-(value%10))]+rows[index][11:14]+rows[index][(11-(value%10)):11]+rows[index][-1],value/10,itr+1
    for row in rows:
        print row
    
    
    #some random code i write when i test, left there for the memories
  #  line = '0'*5) + '*'*5
   # space = '   '
    #end = '|'
#    while(value>0):
 #       index = 10 - value%10 
  #      print end + line[:index] + space + line[index:] + end
   #     value = value/10
    
        
        
    
         
###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|
