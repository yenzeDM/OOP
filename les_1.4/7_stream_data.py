import sys


class StreamData:
    def create(self, fields, lst_value):
        if len(fields) == len(lst_value):
            for i in range(len(lst_value)):
                setattr(self, fields[i], lst_value[i])
            return True
        return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        # считывание списка строк из входного потока
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res
    

sr = StreamReader()
data, result = sr.readlines()

