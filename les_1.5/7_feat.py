class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = total_mem_slots

    def get_config(self):
        result = [f'Материнская плата: {self.name}',
               f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
               f'Слотов памяти: {self.total_mem_slots}',]
        tmp = 'Память:'
        for i in self.mem_slots:
            tmp += f' {i.name} - {i.volume};'
        result.append(tmp.strip(';'))
        return result


mb = MotherBoard('asus', CPU('amd', 4000), [Memory('kingston', 8), Memory('kingston', 8)])

print(mb.get_config())