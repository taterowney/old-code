
import sympy
import numpy




class commodity:
    def __init__(self, essential=False, consumption=0):
        self.consumption_rate = consumption
        self.is_essential=essential
        self.subscribers = []
    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)
    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)
    def update(self):
        for s in self.subscribers:
            self.revoke(s, 1)
    def revoke(self, target, amount):
        target.resources[self]-=amount

class agent:
    def __init__(self, starting_resources, exchanges, name = "autoassign"):
        self.name = name
        self.subscribed_commodities = []
        self.resources = {}
        self.satisfaction = 0
        for c in commodities:
            self.resources[c]=starting_resources[c]
            c.add_subscriber(self)
            self.subscribed_commodities.append(c)
    def sample_bid_iteration(self):
        for r in self.resources:
            if self.resources[r] > 0:
                for e in dict(sorted(resources.items(), key=lambda item: item[1])):
                    if
    def update(self):
        for r in self.resources:
            if self.resources[r] > 0 and r.is_essential=True:
                self.end()
    def end(self):
        for c in self.subscribed_commodities:
            c.remove_subscriber(self)
        print(str(self.name)+" has dropped out!")
