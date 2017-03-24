n, a, b = [int(x) for x in raw_input().split()]
msg = raw_input()

offset = a**b

AB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shift(c, offset):
    if c == ' ':
        return ' '
    return AB[(AB.index(c) - offset) % len(AB)]

new_msg = ''.join([shift(c, offset) for c in msg])
print new_msg
