
def composeMap(fun1, fun2, l):
    """
    Returns a new list r where each element in r is fun2(fun1(i)) for the
    corresponding element i in l
    :param fun1: function
    :param fun2: function
    :param l: list
    :return: list
    """
    new_list = [0] * len(l)
    index = 0
    #go through the list given
    for x in l:
        #apply fun1 first then fun2 with the output of fun1
        output = fun1(x)
        new_list[index] = fun2(output)
        index = index + 1
    
    return new_list
    pass


def tripleMap(fun, l):
    """
    Returns a new list r where each element in r is fun(fun((fun(i))) for the
    corresponding element i in l
    :param fun: function
    :param l: list
    :return: list
    """
    #double
    output_double = composeMap(fun, fun, l)
    #go through the list outputted above
    new_list = [0] * len(l)
    index = 0
    for x in output_double:
        new_list[index] = fun(x)
        index = index + 1

    return new_list
    pass


def compose(fun1, fun2):
    """
    Returns a new function f. f should take a single input i, and return
    fun1(fun2(i))
    :param fun1: function
    :param fun2: function
    :return: function
    """
    def retfun(i):
        #calls fun2 then fun1
        return fun1(fun2(i))
        pass
    return retfun


def repeater(fun, num_repeats):
    """
    Returns a new function f. f should take a single input i, and return
    fun applied to i num_repeats times. In other words, if num_repeats is 1, f
    should return fun(i). If num_repeats is 2, f should return fun(fun(i)). If
    num_repeats is 0, f should return i.
    :param fun: function
    :param num_repeats: int
    :return: function
    """
    def retfun(x):
        output = fun(x)
        for i in range(num_repeats): #repeat num times
            output = fun(output)
        return output
    return retfun


if __name__ == '__main__':
    def test1(x):
        return x * 2
    
    def test2(x):
        return x - 3
        
    data = [2, 5, -10, -7, -7, -3, -1, 9, 8, -6]

    print(composeMap(test1, test2, data))
    print(composeMap(test2, test1, data))
    print(tripleMap(test1, data))
    
    f1 = compose(test1, test2)
    
    print(f1(4))
    
    print(list(map(f1, data)))
    
    f2 = compose(test2, test1)

    print(f2(4))

    print(list(map(f2, data)))
    
    z = repeater(test1, 0)
    once = repeater(test1, 1)
    twice = repeater(test1, 2)
    thrice = repeater(test1, 3)
    
    print("repeat 0 times: {}".format(z(5)))
    print("repeat 1 time: {}".format(once(5)))
    print("repeat 2 times: {}".format(twice(5)))
    print("repeat 3 times: {}".format(thrice(5)))

