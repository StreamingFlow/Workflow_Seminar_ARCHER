from dispel4py.core import GenericPE
from dispel4py.base import IterativePE
from dispel4py.workflow_graph import WorkflowGraph
import os

class SplitLines(GenericPE):
    def __init__(self):
        GenericPE.__init__(self)
        self._add_input("input")
        self._add_output("output")
        
    def _process(self, inputs):
        for line in inputs["input"].splitlines():
            self.write("output", line)

class SplitWords(IterativePE):

    def __init__(self):
        IterativePE.__init__(self)
        
    def _process(self, data):
        for word in data.split(" "):
            self.write("output", (word,1))


class CountWords(GenericPE):
    def __init__(self):
        
        from collections import defaultdict
        GenericPE.__init__(self)
        self._add_input("input", grouping=[0])
        self._add_output("output")
        self.count=defaultdict(int)
        
    def _process(self, inputs):
        word, count = inputs['input']
        self.count[word] += count
    
    def _postprocess(self):
        self.write('output', self.count)

split = SplitLines()
split.name ='split'
words = SplitWords()
count = CountWords()


graph = WorkflowGraph()
graph.connect(split, 'output', words, 'input')
graph.connect(words, 'output', count, 'input')
