import sys
 
teens = [13, 14, 17, 18, 19]

def is_integer(n):
    '''
    function to check if the given value 'n' is integer or not
    
    :param n: value to check
    :type n: int
    :return: True if n is int else False
    :rtype: boolean
    '''
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def calculate_sum(args):
    '''
    function to check and pass values of a,b,c only if they are int 
    else returns the error message
    
    :param args: list of values
    :type args: list
    :return: calculated sum value
    :rtype: int
    '''
    if len(args) < 3 or len(args) > 3:
        return 400, "Exactly 3 numbers are required"
    if not is_integer(args[0]) or not is_integer(args[1]) or not is_integer(args[2]):
        return 400, "All inputs must be numeric"
    return 200, check_teens(int(args[0]), int(args[1]), int(args[2]))

def check_teens(a, b, c):
    '''
    function to check if a,b,c are teens or not and updates their value
    
    :param a: first value
    :type a: int
    :param b: second value 
    :type b: int
    :param c: third value
    :type c: int
    :return: calculated sum value
    :rtype: int
    '''
    if a in teens:
        a = 0
    if b in teens:
        b = 0
    if c in teens:
        c = 0
    return get_sum(a, b, c)

def get_sum(a, b, c):
    '''
    function to calculate sum
    
    :param a: first value
    :type a: int
    :param b: second value 
    :type b: int
    :param c: third value
    :type c: int
    :return: calculated sum
    :rtype: int
    '''
    return a+b+c


if __name__ == "__main__":
    # print('Number of arguments:', len(sys.argv), 'arguments.')
    # print('Argument List:', str(sys.argv))
    
    print(calculate_sum(sys.argv[1:])[1])