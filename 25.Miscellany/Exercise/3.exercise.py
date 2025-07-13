from typing import Optional, Callable, Union


def repeat(_func: Optional[Callable] = None, *, times: int = 1):
    def decorator(func):
        def wrapper(*agrs, **kwargs):
            result = None
            for _ in range(times):
                result = func(*agrs, **kwargs)
            return result
        return wrapper
    if _func is not None:
        return decorator(_func)
    return decorator


@repeat(times=5)
def greet(name):
    print(f"Hello, {name}")


greet("Sakib")
