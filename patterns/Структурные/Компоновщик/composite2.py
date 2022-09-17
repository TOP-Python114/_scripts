

class Neuron:
    def __init__(self, name: str):
        self.name = name
        self.inputs = []
        self.outputs = []

    def connect_to(self, other: 'Neuron'):
        self.outputs += [other]
        other.inputs += [self]

    def __iter__(self):
        yield self

    def __str__(self):
        return f'<{self.name}>'

    def show_connections(self):
        res = '\tinputs:\n'
        res += '\n'.join(f'\t\t{neur}' for neur in self.inputs)
        res += '\n\toutputs:\n'
        res += '\n'.join(f'\t\t{neur}' for neur in self.outputs)
        return res


class NeuronLayer(list):
    def __init__(self, name: str, count: int = 2):
        super().__init__()
        self.name = name

        for i in range(1, count+1):
            self.append(
                Neuron(f'Слой {self.name} Нейрон {i}')
            )

    def connect_to(self, other):
        if self is other:
            return

        for neuron_out in self:
            for neuron_in in other:
                neuron_out.connect_to(neuron_in)

    def __str__(self):
        res = '\n\n'.join(str(neur) for neur in self)
        return res


n1 = Neuron('Отдельный Нейрон 1')
n2 = Neuron('Отдельный Нейрон 2')

n1.connect_to(n2)

print(n1)
print(n1.show_connections(), end='\n\n')

print(n2)
print(n2.show_connections(), end='\n\n\n')


nl1 = NeuronLayer('Слой_1')
nl1.connect_to(n1)

print(n1)
print(n1.show_connections(), end='\n\n')
