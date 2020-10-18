import math as m

def fixed(f, x_i, iter_nums) -> float:
'''
f: func to pass in
x_i: initial guess
iter_nums: number of iterations
'''
    for i in range(0, iter_nums):
        x_i1 = f(x_i)
        ea = abs((x_i1 - x_i)/x_i)*100
        print("Iter: {}, X_i: {}, X_i+1: {} Ea: {}".format((i+1), x_i, x_i1, ea))
        x_i = x_i1
    return x_i1

def main():
    f = lambda x: (-2*x**3 +11.7*x**2 +5)/17.7
    approx_func = fixed(f, 3, 3)
    print("Solution: ", approx_func)

if __name__ == "__main__":
    main()