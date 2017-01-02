n_bean_types = int(raw_input())
beans_required = [int(x) for x in raw_input().split()]
n_farm_stocks = int(raw_input())
farm_stocks = []
for _ in range(n_farm_stocks):
    # bean types are given 1-indexed; take 1 to make them 0-indexed:
    farm_stocks.append([int(x) - 1 for x in raw_input().split()[1:]])

max_cows_needed = 0

def solve(beans_required, farm_stocks, combo_len=0, combo=None,
        cows_needed=sum(beans_required)):
    """Update the global variable max_cows_needed to be the number of cows Jack
    needs to be 100% certain he can get all the beans he wants.

    This function recursively generates combinations of numbers. Each combo
    represents a scenario, where combo[i] is the type of bean that Jack got
    from farmer i (assuming the worst case where each farmer gives only one
    of the types of bean they have).

    Args:
      beans_required: A list of the number of each type of bean Jack needs.
      farm_stocks: A list of each farms' bean stocks. The stock of a farm is
        a list of the types of beans they have. E.g. [0, 3] means this farm
        stocks the first and fourth type of bean.
      combo_len: The length of the combination generated so far. Once combo_len
        equals the number of farmers, that means the combination is completed.
      combo: List storing the current combination. Only the first combo_len
        values are valid at any given time.
      cows_needed: A running total of the cows needed so far. As the combo is
        generated this number may go down, as each farmer supplies Jack with
        beans.
    """

    if combo is None:
        combo = [None] * len(farm_stocks)
        
    global max_cows_needed
    if cows_needed < max_cows_needed:
        return

    if combo_len == len(farm_stocks):
        max_cows_needed = max(cows_needed, max_cows_needed)
        return
    
    # try to see if we can pick a bean from this farmer that won't decrease the
    # number of cows needed
    for bean in farm_stocks[combo_len]:
        if beans_required[bean] == 0 or bean in combo[:combo_len]:
            combo[combo_len] = bean
            solve(beans_required, farm_stocks, combo_len + 1, combo,
                    cows_needed)
            return

    # otherwise branch the search and try every possibility
    for bean in farm_stocks[combo_len]:
        combo[combo_len] = bean
        new_cows_needed = cows_needed - beans_required[bean]
        solve(beans_required, farm_stocks, combo_len + 1, combo,
                new_cows_needed)

solve(beans_required, farm_stocks)
print max_cows_needed
