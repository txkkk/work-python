def unique_elements(*args):
    unique_element = list(set(args))
    return unique_element


def count_arguments(**kwargs):
    user_type = kwargs.get('user_type', 'Student')
    print(f"Number of arguments: {len(kwargs)}")
    print(f"user_type: {user_type}")


def positional_keyword_args(positional1, positional2, positional_or_keyword=None, *, arg4=0, arg5=0, arg6=0):
    pass


def multiply_function(number):
    def inner_function(n):
        return number * n
    return inner_function


def print_square(length, end_mark=None):
    if length <= 0:
        return
    print("*" * length)
    if end_mark is None:
        print_square(length, end_mark)
    else:
        print(end_mark)


if __name__ == '__main__':
    arguments = unique_elements(1, 2, 3, 4, 3, 2, 1)
    print(arguments)

    count_arguments(arg1='value1', arg2='value2', user_type='Teacher')

    square_func = multiply_function(5)
    result = square_func(4)
    print(result)

    print_square(5, end_mark="Done")
