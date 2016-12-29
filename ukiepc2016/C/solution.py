n = int(raw_input())

REGISTERS = (A, X, Y) = ('A', 'X', 'Y')

def solve(n):
    if n == 0 :
        set_zero(X)
    elif n == 1:
        set_one(X)
    else:
        make_on_stack(n)
        pop_to(X)
    display(X)

def make_on_stack(n, extra_ones=0):
    """Print the instructions to produce the number n on the top of the
    stack.

    Assumes n > 0.
    
    extra_ones: Running total of the number of extra 1's needed on the stack.
    This is for when n doesn't evenly divide by any number > 1. In this case,
    make_on_stack calls itself with n-1, and adds the extra 1 on afterwards.
    """
    if n == 1:
        set_one(X)
        for _ in range(extra_ones + 1):
            push_from(X)
        return

    div = lowest_divisor(n)
    if div == 1:
        make_on_stack(n-1, extra_ones+1)
        add() # add the extra one
        return

    # get n/div, then add it to itself div times to get n
    make_on_stack(n/div, extra_ones)
    pop_to(X)
    for _ in range(div):
        push_from(X)
    for _ in range(div - 1):
        add()

def lowest_divisor(n):
    """Return lowest q > 0 s.t. q divides n"""
    q = 2
    while q*q <= n:
        if n % q == 0:
            return q
        q += 1
    return 1

def set_one(register):
    print "ST " + register

def set_zero(register):
    print "ZE " + register

def push_from(register):
    print "PH " + register

def pop_to(register):
    print "PL " + register

def add():
    print "AD"

def display(register):
    print "DI " + register

solve(n)
