import copy
import re
from functools import reduce

#solved
small_input = "1 + 2 * 3 + 4 * 5 + 6"
#solved
small_input = "2 * 3 + (4 * 5)"
#solved
small_input = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
#
small_input = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"


def get_operator(_c):
    if _c == '+':
        return lambda a, b: a + b
    elif _c == '*':
        return lambda a, b: a * b


def sol_basic(_input):
    prev = []
    for c in _input:
        if bool(re.search("\d+", c)):
            prev.append(int(c))
            if len(prev) >= 2:
                prev = [reduce(f, prev)]
        elif bool(re.search("[*+]", c)):
            f = get_operator(c)
    return prev


def find_first_right_bracket(_input):
    i = 0
    expr = "[)]"
    while not bool(re.search(expr, _input[i])):
        i += 1

    if bool(re.search(expr, _input[i])):
        return i
    else:
        raise Exception("Didn't find a right bracket")


def find_matching_parenthesis_in_string(_input):
    left_brackets = []
    sols = []
    for i, c in enumerate(_input):
        if c == '(':
            left_brackets.append(i)
        elif c == ')':
            sols.append((left_brackets.pop(), i))
        else:
            pass
        return sols


def sol(_input):
    re_digit_without_left_bracket = "(?<!\()\d+"
    if type(_input) == str:
        _input = _input.split(" ")
    prev = []
    i = 0
    while i < len(_input):
        c = _input[i]
        if bool(re.search(re_digit_without_left_bracket, c)):
            prev.append(int(c))
            if len(prev) >= 2:
                prev = [reduce(f, prev)]
            i += 1
        elif bool(re.search("[*+]", c)):
            f = get_operator(c)
            i += 1
        elif bool(re.search("[(]", c)):
            print(c[0])
            #local_ind = re.search("[)]", _input[i:]).start()
            local_ind = find_first_right_bracket(_input[i:])
            global_ind = i + local_ind
            #new_exprs = _input[(i+1):global_ind]
            new_exprs = [c[1:], *_input[(i+1):global_ind], _input[global_ind][:-1]]
            sub_sol = sol(new_exprs)
            new_input = copy.deepcopy(_input)
            del new_input[i:(global_ind+1)]
            new_input = [*_input[:i], str(sub_sol), *_input[global_ind+1:]]
            _input = new_input
    value = prev[0]
    return value

#print(sol_basic(basic_input))
print(sol(small_input))
#print(find_first_right_bracket(small_input.split()))