"""Демонстратор шаблона Команды: каждая команда в своём классе."""
from abc import ABC, abstractmethod
from datetime import datetime


class InvokerError(Exception):
    pass

class CommandNotRegisteredError(InvokerError):
    def __init__(self, name: str):
        super().__init__(f"command '{name}' is not registered")

class EmptyHistoryError(InvokerError):
    def __init__(self):
        super().__init__('no command has been executed yet')


class Light:
    """Адресат для команд."""
    @staticmethod
    def turn_on():
        print('Лампа включена')

    @staticmethod
    def turn_off():
        print('Лампа выключена')


class Switch:
    """Инициатор команд."""
    def __init__(self):
        self._commands: dict[str, 'ICommand'] = {}
        self._history: list[tuple[datetime, str]] = []

    def register(self, command_name: str, command: 'ICommand'):
        self._commands[command_name] = command

    def execute(self, command_name: str):
        if command_name in self._commands:
            self._commands[command_name].execute()
            self._history.append(
                (datetime.now(), command_name)
            )
        else:
            raise CommandNotRegisteredError(command_name)

    def show_history(self, newest_first: bool = False):
        for timestamp, command_name in self._history[::(1, -1)[newest_first]]:
            print(f'{timestamp:%H:%M:%S}'
                  f' — {self.__class__.__name__}'
                  f' — {command_name.upper()}')

    def replay_last(self):
        if self._history:
            command_name = self._history[-1][1]
            self.execute(command_name)
        else:
            raise EmptyHistoryError


class ICommand(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class SwitchOnCommand(ICommand):
    def execute(self):
        self.receiver.turn_on()


class SwitchOffCommand(ICommand):
    def execute(self):
        self.receiver.turn_off()



torcher = Light()

smart_switch = Switch()
smart_switch.register('ON', SwitchOnCommand(torcher))
smart_switch.register('OFF', SwitchOffCommand(torcher))

smart_switch.execute('ON')
smart_switch.execute('OFF')

smart_switch.show_history()

smart_switch.replay_last()

smart_switch.show_history(True)
