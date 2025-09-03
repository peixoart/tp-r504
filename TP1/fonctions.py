def puissance(a,b):	
  
    if not type(a) is int :
        raise TypeError("Only integers are allowed for a")
    if not type(b) is int :
        raise TypeError("Only integers are allowed for b")
    if a == 0 and b < 0:
        raise ValueError("0 cannot be raised to a negative power")
    
    return a ** b