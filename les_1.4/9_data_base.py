import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for i in data:
            result = {}
            tmp = i.split(' ')
            for j in range(0, 4):
                result[self.FIELDS[j]] = tmp[j]
            self.lst_data.append(result)

    def select(self, a, b):
        return self.lst_data[a:b+1]

db = DataBase()
db.insert(lst_in)
print(db.select(0, 4))