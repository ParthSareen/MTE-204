from pprint import pprint
import math as m
def bisection(f,x_lower,x_upper,iterations):
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

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
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> bisection(f,1,2,25)
    1.618033990263939
    >>> f = lambda x: (2*x - 1)*(x - 3)
    >>> bisection(f,0,1,10)
    0.5
    '''
    if f(x_lower)*f(x_upper) >= 0:
        print("Bisection method fails.")
        return None
    x_lower_new = x_lower
    x_upper_new = x_upper
    # setting this to 0 so we can change the variable later; first error is probably wrong
    x_r = 0
    for n in range(1,iterations+1):
        x_r_new = (x_lower_new + x_upper_new)/2.0
        abs_relative_error = abs((x_r_new - x_r)/x_r_new)*100.0
        x_r = x_r_new
        f_m_n = f(x_r)
        
        pprint("Iter: {}, | X_l: {:.8f}, | X_u: {:.8f}, | X_r: {:.8f}, | f(X_l): {:.8f}, | f(X_u): {:.8f}, | f(X_r): {:.8f}, | Ea: {:.8f}".format(n, x_lower_new, x_upper_new, x_r_new, f(x_lower_new), f(x_upper_new), f_m_n, abs_relative_error))
        if f(x_lower_new)*f_m_n < 0:
            x_lower_new = x_lower_new
            x_upper_new = x_r
        elif f(x_upper_new)*f_m_n < 0:
            x_lower_new = x_r
            x_upper_new = x_upper_new
        elif f_m_n == 0:
            print("Found exact solution. Iter: {}".format(n))
            return x_r
        else:
            print("Bisection method fails.")
            return None
    return x_r #(x_lower_new + x_upper_new)/2

def main():
    # Enter function here
    # f = lambda x: x**2 - x - 1
    p = lambda x: ((82.0*9.81/x)*(1.0-m.exp(-2.0*x/41.0)))-36.0
    approx_func = bisection(p,3,5,7)
    print(approx_func)


if __name__ == "__main__":
    main()