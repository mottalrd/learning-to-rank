import operator, functools

class GreedyOrder:
    def __init__(self, V, preference):
        self.V = list(V)
        self.preference = preference

    def run(self):
        rank = []
        power = self.__compute_power()
        while len(self.V) > 0:
            curr_best = max(power, key=power.get)
            rank.append(curr_best)
            self.V.remove(curr_best)
            power = self.__compute_power()

        return rank

    def __compute_power(self):
        power = {}

        for e1 in self.V:
            outbound = [self.preference(e1, e2) for e2 in self.V]
            inbound = [self.preference(e2, e1) for e2 in self.V]
            power[e1] = functools.reduce(operator.add, outbound) - functools.reduce(operator.add, inbound)

        return power