class Calc:

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def multi(self,*args):
        result = 1
        for i in args:
            result *= i
        return result

    def divide(self, a , b):
        try:
            return a / b

        except ZeroDivisionError:
            return 'inf'