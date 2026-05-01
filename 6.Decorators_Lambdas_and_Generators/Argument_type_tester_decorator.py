def check_arg_types(strings_allowed: bool, numbers_allowed: bool, sequences_allowed: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not strings_allowed and isinstance(arg, str):
                    raise TypeError("Strings not allowed")
                if not numbers_allowed and isinstance(arg, (int, float)):
                    raise TypeError("Numbers not allowed")
                elif not sequences_allowed and isinstance(arg, (list, tuple, dict)):
                    raise TypeError("sequences not allowed")

            func(*args, **kwargs)
        return wrapper
    return decorator

@check_arg_types(strings_allowed=True, numbers_allowed=False, sequences_allowed=True)
def main(*args):
    print ("Working OK")

if __name__ == '__main__':
    main("hello", "test", (1, 2))  # working OK
    main("string", 1)  # raise TypeError