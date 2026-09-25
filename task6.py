def find_digit(n):
    length=1      
    count=9      
    start=1           
    while n>length*count:
        n -=length*count  
        length +=1       
        count *=10    
        start *=10     
        
    number=start+(n - 1)//length
    
    digit_index=(n - 1)%length
    
    return int(str(number)[digit_index])

print(find_digit(10))  
print(find_digit(15))  
print(find_digit(123123123123)) 
