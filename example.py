'''i= 0
while(i<10):
    print(i)
    i+=1'''

def fun1():
    var1=12
    var2=3
    var3=var1*var2
    print(var3)
fun1()
    
def fun2(var1,var2):
    var3=var1+var2
    print(var3)
fun2(20,10)

def fun3():
    var1=12
    var2=4
    var3=var1/var2
    return var3
var4=fun3()
print(var4)

def fun4(var1,var2):
    var3=var1/var2
    return var3
var4=fun4(20,3)
print(var4)
