class CPU:
    """Моделирует работу центрального процессора."""
    @staticmethod
    def cooling():
        print('Запуск кулера центрального процессора')

    @staticmethod
    def read_register(register: str):
        print(f'Чтение регистра {register}')

    @staticmethod
    def execute():
        print('Запуск процессора')


class RAM:
    """Моделирует работу оперативной памяти."""
    @staticmethod
    def load(data: str):
        print(f'Чтение из оперативной памяти блока данных {data}')
        return ''.join(bin(ord(ch))[2:] for ch in data).upper()


class Drive:
    """Моделирует работу носителя данных."""
    @staticmethod
    def read(data: str):
        print(f'Чтение из носителя данных блока данных {data}')
        return ''.join(hex(ord(ch))[2:] for ch in data).upper()


class Computer:
    """Фасад для компонентов компьютера.

    Обеспечивает возможность запуска компьютера.
    """
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.drive = Drive()

    def start(self):
        self.cpu.cooling()
        self.cpu.execute()
        hex_data = self.drive.read('MBR: ...')
        bin_data = self.ram.load(hex_data)
        self.cpu.read_register(bin_data)


pc = Computer()
pc.start()
