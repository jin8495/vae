import torch
from torch import nn

class NAN_Exception(Exception):
    pass

class Hook():
    def __init__(self, name="", backward=False):
        self.name = name
        self.backward = backward
    def __call__(self, module, inputs, outputs):
        try:
            for input in inputs:
                if (torch.isnan(input).any()):
                    print("------------Input  NAN------------")
                    raise NAN_Exception
            for output in outputs:
                if (torch.isnan(output).any()):
                    print("------------Output NAN------------")
                    raise NAN_Exception
                    
        except NAN_Exception as e:
            if (self.backward):
                print("Backward", self.name, module)
            else:
                print("Forward ", self.name, module)

            print("Input")
            for input in inputs:
                print(input.shape)
            print("Output")
            for output in outputs:
                print(output.shape)
                
            assert False
                
