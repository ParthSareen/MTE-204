import math as m
'''
f: func to pass in
x_i: initial guess
iter_nums: number of iterations
'''

def fixed(f, x_i, iter_nums):
    ea = 100
    for i in range(0, iter_nums+1):
        print("Iter: {}, | X_i: {:.8f}, | Ea: {:.8f}".format(i, x_i, ea))
        x_i1 = f(x_i)
        ea = abs((x_i1 - x_i)/x_i1)*100
        x_i = x_i1
    return x_i1

def main():
    #function isolated for x
    f = lambda x: (-2*x**3 +11.7*x**2 +5)/17.7
    approx_func = fixed(f, 3, 3)
    print("Solution: ", approx_func)

if __name__ == "__main__":
    main()