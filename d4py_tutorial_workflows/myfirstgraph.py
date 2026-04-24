from dispel4py.base import ProducerPE
from dispel4py.base import IterativePE
from dispel4py.workflow_graph import WorkflowGraph


class NumberProducer(ProducerPE):
    def __init__(self, start, limit):
        ProducerPE.__init__(self)
        self.start = start
        self.limit = limit
    def _process(self, inputs):
        for i in range(self.start, self.limit):
            self.write('output', i)

class MyFirstPE(IterativePE):

    def __init__(self, divisor):
        IterativePE.__init__(self)
        self.divisor = divisor

    def _process(self, data):
        if not data % self.divisor == 0:
            return data

producer = NumberProducer(2, 100)
divide = MyFirstPE(3)
graph = WorkflowGraph()
graph.connect(producer, 'output', divide, 'input')
