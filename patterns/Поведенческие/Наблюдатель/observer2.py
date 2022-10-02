"""Демонстратор наблюдателя: реализация с интерфейсами."""

from abc import ABC, abstractmethod
from numbers import Real


class Patient(ABC):
    def __init__(self):
        self.__monitors = []

    def add_monitor(self, device):
        self.__monitors.append(device)

    def remove_monitor(self, device):
        self.__monitors.remove(device)

    def update_monitors(self, patient):
        for device in self.__monitors:
            device.update(patient)


class COVIDPatient(Patient):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.__parameters = {
            'температура': 37.0,
            'пульс': 90,
            'сатурация': 95
        }

    def get_value(self, parameter: str):
        if parameter in self.__parameters:
            return self.__parameters[parameter]

    def set_value(self, parameter: str, value: Real):
        if parameter in self.__parameters:
            self.__parameters[parameter] = value
            self.update_monitors(self)



class Monitor(ABC):
    @abstractmethod
    def update(self, subject: Patient):
        pass


class Thermometer(Monitor):
    def update(self, patient: Patient):
        if patient.__class__ is COVIDPatient:
            temperature = patient.get_value('температура')
            if temperature <= 36.4:
                self.emrg_message(f'{patient.name} - {temperature}')
            elif 36.5 <= temperature <= 37.0:
                self.info_message(f'{patient.name} - {temperature}')
            elif 37.1 <= temperature <= 38.3:
                self.warn_message(f'{patient.name} - {temperature}')
            elif 38.4 <= temperature:
                self.emrg_message(f'{patient.name} - {temperature}')

    @staticmethod
    def info_message(text: str):
        print(f'НОРМАЛЬНО: {text}')

    @staticmethod
    def warn_message(text: str):
        print(f'ПРЕДУПРЕЖДЕНИЕ: {text}')

    @staticmethod
    def emrg_message(text: str):
        print(f'КРИТИЧНО: {text}')

