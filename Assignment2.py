
x = 1

while(x<=100):
    if(x%2==0):
         print(x,("Fizz"))
         
         if(x%5==0):
             print(x,("Buzz"))
             if(x%3==0 and x%5==0):
                 print(x,("FizzBuzz"))
   
    x+=1
