import math 

def estimate_pi():
    """It returns an estimation of pi"""
    sum = 0
    subsum = 1
    k =0
    while(subsum > 1e-15):
        subsum = (math.factorial(4*k)*(1103 + 26390*k))/(math.factorial(k)**4 * 396**(4*k)) 
        sum += subsum
        k += 1

    pi = 1 / ((2 * math.sqrt(2)/9801) *sum) 
    return pi

if __name__ == '__main__':
    print(estimate_pi())
        
