class SingletonFive:
    _instance = None
    _count = 0

    def __new__(cls, *args, **kwargs):
        if cls._count < 5:
            cls._count += 1
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return cls._instance
        
    def __init__(self, name):
        self.name = name
        
obj = [SingletonFive(str(n)) for n in range(10)]
for i in obj:
    print(i)