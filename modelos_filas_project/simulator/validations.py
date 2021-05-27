def validateLambda(l, s, miu):
    if l < (s * miu): return True
    else: return False

def validateServer(s):
    if s > 1: return True
    else: return False

def validateNegatives(numbers):
    for num in numbers:
        if num < 0: return False
    return True