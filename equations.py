# -*- coding: utf-8 -*-
# coding = utf-8
# a func that's check what the sign of the result 
# if the base is negative and the power is float
# * check if difine under the power if not return 0
# * the func dosen't work on fraq  that's is presantion is infity digit

def negativeIfInfinit(y, x):
    #print(y, x)
    t = x
    t = str(t)
    integer = t.split('.')[0]
    t = t.split('.')[1]
    print(integer, t)
    den = power(10, len(t))
    t = int(t) + int(integer)*den
    #print(int(t), '/', den) 
   
    i = min(t, den)
    while i > 0:
        if t%i == 0 and den%i == 0:
            t = t/i
            den = den/i
            
        i = i - 1
    
    
    print(t, '/', den) 

    if t%2 == 0:
        return False
    
    neg = 1
    if den%2 == 1:
        neg = -1
    
    return XtimesY(XtimesY(abs(y), 1/t), den) * neg
   

def negative(x):
    
    t = x
    t = str(t)
    t = t.split('.')[1]
    den = power(10, len(t))
    t = int(t)
    #print(int(t), '/', den) 
    neg_numer = 1
    neg_int = 1
    if int(x) == x:
        if x%2 == 0:
            return 1
        
        return -1
    
    i = t
    while i > 0:
        if t%i == 0 and den%i == 0:
            t = t/i
            den = den/i
            
        i = i - 1
    
    
    #print(t, '/', den) 

    if den%2 == 0:
        return False
    
    if int(x)%2 == 1:
        neg_int = -1
    
    if int(t)%2  == 1:
        neg_numer = -1
    
    
    return neg_int * neg_numer
 
def XtimesY(x, y):
    try:
        if x == 0:
            return 0
        
        if x < 0 and len(str(y)) >= 18 and y!= 0 and  len(str(1/y)) != 18:
            y = 1/y
            return negativeIfInfinit(x, y)
            
        neg = 1
        
        if x < 0 and y != int(y):
            neg = negative(y)
    
        if neg == False:
            return 0
        
        elif x < 0 and y%2 == 1:
            neg = -1
            
        x = abs(x)
        t = y * Ln(x) 
        t = exponent(t)

    
        if 1/y == int(1/y) and x < 0:
            return(sqrt(1/y, x))
        return t*neg
    
    except:
        return 0

def sqrt(x, y):
    try:
        if y == 0:
            return 0
        
        if y <= 0 and x%2 == 0:
           return 0
        
        return XtimesY(y, 1/x)
    
    except:
        return 0
    
def calculate(x):
    #print(exponent(x), XtimesY(7, x), XtimesY(x, -1), sqrt(x, x))
    return round(exponent(x) * XtimesY(7, x) * XtimesY(x, -1) * sqrt(x, x), 6)


def Ln(x):  
    try:    
        y = 0
        y1 = y + 2 * ((x - exponent(y)) / (x + exponent(y)))
        #i = 0
        epsilon = 0.0001
        
        if x < 0:
            return 0
        
        
        while abs(y-y1) > epsilon:
            y = y + 2 * ((x - exponent(y)) / (x + exponent(y)))
            y1 = y + 2 * ((x - exponent(y)) / (x + exponent(y)))
        
        return y1
    
    except:
        return 0
    

def exponent(x):
    i = 0
    exp = 0
    
    while i < 100:
        t = power(x, i) / factorial(i)   
        exp = exp + t
        i = i + 1 
    
    return exp

def power(x, y):
    
    if x == 0:
        return 0
    
    if y == 0:
        return 1
        
    i = 0
    t = 1
    
    while i < y:
        t = t*x
        i = i + 1
        
    
    return t
        
def factorial(x):
    t = 1
    i = 1
    while i <= x:
        t = t * i
        i = i + 1
    
    return t

def abs(x):
    if x < 0:
        x = -x
    
    return x

#print(XtimesY(-2.2, -2))
#print(calculate(-1))
#print(Ln(1.5))
#print(sqrt(2.5, 4))
#print(sqrt(7, -exponent(1)))
#print(exponent(2.5))
#print(len(str(1/7)))
#print(XtimesY(-exponent(1), 1/7))
#print(sqrt(6, -sqrt(2, 2)))
#print(exponent(-5))
#print(factorial(4))
