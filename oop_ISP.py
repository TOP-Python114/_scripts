# Interface Segregation Principle — Принцип Разделения Интерфейсов

from abc import ABC, abstractmethod


# нарушает ISP:
#   объединяет в себе методы, которые не обязательно используются совместно
class MultiFunctionMachine(ABC):
    """Interface for printing, scanning and fax transmitting."""
    @abstractmethod
    def print(self, document):
        pass
    @abstractmethod
    def scan(self, document):
        pass
    @abstractmethod
    def fax(self, document):
        pass

# здесь всё в порядке
class MultiFunctionDevice(MultiFunctionMachine):
    """Device that can print, scan and make fax transmissions."""
    def print(self, document):
        """It prints"""
        pass
    def scan(self, document):
        """It scans"""
        pass
    def fax(self, document):
        """It calls for fax"""
        pass
    
# следствие нарушения ISP
class Printer(MultiFunctionMachine):
    """Old device that can only print."""
    def print(self, document):
        """It prints"""
        pass
    # мы вынуждены реализовывать не нужные в данном классе методы
    def scan(self, document):
        """Not implmented!"""
        raise NotImplementedError
    # все эти предупреждения не являются гарантией неиспользования методов
    def fax(self, document):
        """Not implmented!"""
        raise NotImplementedError

p1 = Printer()
# мы видим методы, которые не могут быть использованы
print([el for el in dir(p1) if not el.startswith('__')], end='\n\n')



# корректная реализация разделённых интерфейсов
class PrinterInterface(ABC):
    @abstractmethod
    def print(self, document):
        pass

class ScannerInterface(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class FaxInterface(ABC):
    @abstractmethod
    def fax(self, document):
        pass


# устройства
class OldPrinter(PrinterInterface):
    """Device for printing"""
    def print(self, document):
        """It prints"""
        pass

class Xerox(PrinterInterface, ScannerInterface):
    """Photocopying machine"""
    def print(self, document):
        """It prints"""
        pass
    def scan(self, document):
        """It scans"""
        pass

class FaxPhone(FaxInterface):
    """Fax implementation"""
    def fax(self, document):
        """It calls for fax"""
        pass

class Woonderwaffle(PrinterInterface, ScannerInterface, FaxInterface):
    """AllInOne"""
    def print(self, document):
        """It prints"""
        pass
    def scan(self, document):
        """It scans"""
        pass
    def fax(self, document):
        """It calls for fax"""
        pass


devices = [OldPrinter(),
           Xerox(),
           FaxPhone(),
           Woonderwaffle()]
# мы видим только те методы, которые могут быть использованы
for dev in devices:
    print(dev.__class__.__name__, end=': ')
    print([el for el in dir(dev) if not el.startswith('__')])
