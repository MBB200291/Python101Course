    def 乘(*args):
        temp = 1
        for i in args:
            temp = temp * i
        return temp

    def 減(*args):
        temp = args[0]
        for i in args[1:]:
            temp -= i
        return temp

    def 加(*args):
        temp = 0
        for i in args:
            temp += i
        return temp

    def 除(*args):
        temp = args[0]
        for i in args[1:]:
            temp = temp / i
        return temp