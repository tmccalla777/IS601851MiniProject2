import math
from decimal import Decimal
import statistics


def mean(a, b):
    a = int(a)
    b = int(b)
    c = ( a + b ) / 2
    return c


def median(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.median([a, b, c])
    return d


def mode(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.mode([a, b, c])
    return d


def stdev(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.stdev([a, b, c])
    return Decimal(d).quantize(Decimal('.001'))


def variance(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.variance([a, b, c])
    return Decimal(d).quantize(Decimal('.001'))


def zscore(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.stdev([a, b, c])
    e = ( a + b + c) / 3
    f = (a - e)/ d
    return Decimal(f).quantize(Decimal('.001'))


def standardized_score(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.stdev([a, b, c])
    e = ( a + b + c) / 3
    f = (a - e)/ d
    return Decimal(f).quantize(Decimal('.001'))


def population_correlation_coefficient(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.stdev([a, b, c])
    e = ( a + b + c) / 3
    f = ((a - e)/ d +(b - e)/ d +(c - e)/ d)/ 3
    return Decimal(f).quantize(Decimal('.001'))


def confidence_interval(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.stdev([a, b, c])
    e = ( a + b + c) / 3
    f = ((a - e)/ d +(b - e)/ d +(c - e)/ d)/ 3
    return Decimal(f).quantize(Decimal('.001'))

'''


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = b * a
    return c


def division(a, b):
    a = float(a)
    b = float(b)
    c = b / a
    return Decimal(c).quantize(Decimal('.000000001'))


def square(a):
    a = int(a)
    c = a * a
    return c


def square_root(a):
    a = int(a)
    c = math.sqrt(a)
    return Decimal(c).quantize(Decimal('.000001'))
'''


class Calculator:
    result = 0

    def __init__(self):
        pass

    def mean(self, a, b):
        self.result = mean(a, b)
        return self.result

    def median(self, a, b, c):
        self.result = median(a, b, c)
        return self.result

    def mode(self, a, b, c):
        self.result = mode(a, b, c)
        return self.result

    def stdev(self, a, b, c):
        self.result = stdev(a, b, c)
        return self.result

    def variance(self, a, b, c):
        self.result = variance(a, b, c)
        return self.result

    def zscore(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result

    def standardized_score(self, a, b, c):
        self.result = standardized_score(a, b, c)
        return self.result

    def population_correlation_coefficient(self, a, b, c):
        self.result = population_correlation_coefficient(a, b, c)
        return self.result

    def confidence_interval(self, a, b, c):
        self.result = confidence_interval(a, b, c)
        return self.result

    '''
    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result
    '''