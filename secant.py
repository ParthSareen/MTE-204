from pprint import pprint
import math as m

def secant(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    m_N : number
        The x intercept of the secant line on the the Nth interval
            m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
        for some intercept m_n then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iterations, the secant method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f,1,2,5)
    1.6180257510729614
    '''
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
        
    a_n = a
    b_n = b
    abs_relative_error = 100
    
    for n in range(0,N+1):
        m_n = b_n - f(b_n)*(b_n - a_n)/(f(b_n) - f(a_n))


        pprint("i: {}, | x_i-1: {:.8f}, | f(x_i-1): {:.8f}, | x_i: {:.8f}, | f(x_i): {:.8f}, | x_i+1: {:.8f}, | Ea: {:.8f}".format(n, a_n, f(a_n), b_n, f(b_n), m_n, abs_relative_error))
        
        abs_relative_error = abs((m_n - b_n)/m_n)*100
        
        f_m_n = f(m_n)
                
        a_n = b_n
        b_n = m_n
            
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))


def main():
    f = lambda x: 2*x**3 - 11.7*x**2 + 17.7*x - 5
    approx = secant(f,3,4,3)
    print(approx)
    print("Solution: ", approx)


if __name__ == "__main__":
    main()