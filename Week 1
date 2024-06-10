#Question 1
import math
def calc_f1_score(tp, fp, fn):
    if tp + fp == 0 or tp + fn == 0:
       return 0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if precision + recall == 0:
       return 0
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score

assert round(calc_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
print(round(calc_f1_score(tp=2, fp=4, fn=5), 2))

#Question 2
import math
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

assert is_number(3) == True
assert is_number('-2a') == False
print(is_number(1))
print(is_number('n'))

#Question 4
import math
def calc_sig(x):
    return 1 / (1 + math.exp(-x))

assert round(calc_sig(3), 2) == 0.95
print(round(calc_sig(2), 2))

#Question 5
import math
def calc_elu(x, alpha=0.01):
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x

assert round(calc_elu(1)) == 1
print(round(calc_elu(-1), 2))

#Question 6
import math
def calc_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif act_name == 'relu':
        return max(0, x)
    elif act_name == 'elu':
        return x if x > 0 else (math.exp(x) - 1)
    else:
        raise ValueError("Unknown activation function")

assert calc_activation_func(x=1, act_name='relu') == 1
print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))

#Question 7
import math
def calc_ae(y, y_hat):
    return abs(y - y_hat)

y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))

#Question 8
import math
def calc_se(y, y_hat):
    return (y - y_hat) ** 2

y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))

#Question 9
import math
def approx_cos(x, n):
    cos_approx = 0
    for k in range(n + 1):
        cos_approx += ((-1)**k * x**(2*k)) / math.factorial(2*k)
    return cos_approx

assert round(approx_cos(x=1, n=10), 2) == 0.54
print(round(approx_cos(x=3.14, n=10), 2))

#Question 10
import math
def approx_sin(x, n):
    sin_approx = 0
    for k in range(n + 1):
        sin_approx += ((-1)**k * x**(2*k+1)) / math.factorial(2*k+1)
    return sin_approx

assert round(approx_sin(x=1, n=10), 4) == 0.8415
print(round(approx_sin(x=3.14, n=10), 4))

#Question 11
import math
def approx_sinh(x, n):
    sinh_approx = 0
    for k in range(n + 1):
        sinh_approx += (x**(2*k+1)) / math.factorial(2*k+1)
    return sinh_approx

assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))

#Question 12
import math
def approx_cosh(x, n):
    cosh_approx = 0
    for k in range(n + 1):
        cosh_approx += (x**(2*k)) / math.factorial(2*k)
    return cosh_approx

assert round(approx_cosh(x=1, n=10), 2) == 1.54
print(round(approx_cosh(x=3.14, n=10), 2))
