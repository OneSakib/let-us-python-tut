import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time-start_time
        print(f"Finished {func.__name__!r} in runtime {runtime:0.8f} secs")
        return value

    return wrapper


@timer
def product(num):
    fact = 1
    for i in range(num):
        fact = fact*i+1
    return fact

@timer
def product_and_sum(num):
    p = 1
    for i in range(num):
        p = p*i+1
    s = 0
    for i in range(num):
        s = s+i+1
    return (p, s)


print("Factorail: ", product(4))
print(product_and_sum(10))
