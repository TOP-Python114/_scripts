from collections.abc import Iterable


class Connectable(Iterable):
    def connect_to(self, other):
        if self is other:
            return
        for neuron_out in self:
            for neuron_in in other:
                neuron_out.outputs.append(neuron_in)
                neuron_in.inputs.append(neuron_out)


class Neuron(Connectable):
    def __init__(self, name: str):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __iter__(self):
        yield self

    def __str__(self):
        return f'<{self.name}>\n' + self.__connections()

    def __connections(self):
        res = '\tinputs:\n'
        res += '\n'.join(f'\t\t{neur.name}' for neur in self.inputs)
        res += '\n\toutputs:\n'
        res += '\n'.join(f'\t\t{neur.name}' for neur in self.outputs)
        return res


class NeuronLayer(list, Connectable):
    def __init__(self, name: str, count: int = 2):
        super().__init__()
        self.name = name

        for i in range(1, count+1):
            self.append(
                Neuron(f'{self.name} Нейрон {i}')
            )

    def __str__(self):
        return '\n\n'.join(str(neur) for neur in self)


n1 = Neuron('Отдельный Нейрон 1')
n2 = Neuron('Отдельный Нейрон 2')
n2.connect_to(n1)

print(n1, end='\n\n')
print(n2, end='\n\n\n\n')


nl1 = NeuronLayer('Слой_1')
nl2 = NeuronLayer('Слой_2', 3)

nl2.connect_to(nl1)

print(nl1, end='\n\n')
print(nl2, end='\n\n\n')

