import sys
def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        exit()
    except ValueError:
        print("Error: Please enter numeric values only.")
        exit()
    return result
    
 
 
    


    
                     