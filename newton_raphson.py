import math as m


def newton(f,Df,x0,epsilon,max_iter):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f,Df,1,1e-8,10)
    Found solution after 5 iterations.
    1.618033988749989
    '''
    xn = x0
    error = 100
    for n in range(0,max_iter+1):
        fxn = f(xn)
        Dfxn = Df(xn)
        print("i: {}, | xi: {:.8f}, | f: {:.8f}, | f': {:.8f}, | Ea: {:.8f}".format(n, xn, fxn, Dfxn, error))
        if error < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        x_i = xn
        xn = xn - fxn/Dfxn
        
        error = 100.0*abs((xn-x_i)/xn)
        
    print("At n = {}, result is: ".format(max_iter))
    return x_i


def main():
    # p = lambda x: x**3 - x**2 - 1    -> func
    # Dp = lambda x: 3*x**2 - 2*x      -> and its derivative
    p = lambda x: 0.7 - 6*m.exp(-0.04*x)
    Dp = lambda x: 6*0.04*m.exp(-0.04*x)
    approx = newton(p,Dp,4,0.002,20)
    print("Solution: ", approx)


if __name__ == "__main__":
    main()