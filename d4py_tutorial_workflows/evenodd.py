from dispel4py.base import ProducerPE, IterativePE
from dispel4py.core import GenericPE
from dispel4py.workflow_graph import WorkflowGraph
from dispel4py.core import GenericPE
import random

class NumberProducer(ProducerPE):
    def __init__(self):
        ProducerPE.__init__(self)
        
    def _process(self, inputs):
        result= random.randint(1, 1000)
        return result
        #OR: self.write('output', result)

class Divideby2(IterativePE):
    def __init__(self, compare):
        IterativePE.__init__(self)
        self.compare = compare
    def _process(self, data):
        if data % 2 == self.compare:
            return data
          
class PairProducer(GenericPE):
    def __init__(self):
        GenericPE.__init__(self)
        self._add_input("odd")
        self._add_input("even")
        self._add_output("output")
        self.list_odd=[]
        self.list_even=[]
      
    def _process(self, inputs):
        if "odd" in inputs:
            self.list_odd.append(inputs["odd"])
        if "even" in inputs:
            self.list_even.append(inputs["even"])
       
        while self.list_odd and self.list_even:
            self.write("output", (self.list_odd.pop(0), self.list_even.pop(0)))
    
    def _postprocess(self):
        self.log('We are left behind: odd: %s, even: %s' % (self.list_odd, self.list_even))
        self.list_odd = []
        self.list_even = []

producer = NumberProducer()
filter_even = Divideby2(0)
filter_odd = Divideby2(1)
pair = PairProducer()

graph = WorkflowGraph()
graph.connect(producer, 'output', filter_even, 'input')
graph.connect(producer, 'output', filter_odd, 'input')
graph.connect(filter_even, 'output', pair, 'even')
graph.connect(filter_odd, 'output', pair, 'odd')
