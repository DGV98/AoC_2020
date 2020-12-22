import sys
import os

class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []
    
    def addNode(self, bag):
        self.children.append(bag)
    