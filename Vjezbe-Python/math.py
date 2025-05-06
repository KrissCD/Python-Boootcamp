def kvadrat(x):
    return x * x

def sqrt(x):
    return x ** 0.5

def pi(x):
    return 3.14 

def round_down(x):
    return floor(x)

def round_up(x):
    return ceil(x)

def povrsina(x):
    return pi(x) * x * x

def opseg(x):
    return 2 * pi(x) * x

def power(x, y):
    return x ** y

def hipoteza(x, y):
    return x ** (1/y)

def datetime(x, y):
    from datetime import datetime
    import time
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def os(x, y):
    import os
    return os.getcwd()

def statistics(x):
    import statistics
    return statistics.mean(x), statistics.median(x), statistics.stdev(x)

def random(x):
    import random
    return random.randint(1, x)
