import operator, functools

class GreedyOrder:
    def __init__(self, V, preference):
        self.__log("Loading Greedy Order")
        self.V = list(V)
        self.preference = preference

    def run(self):
        rank = []
        power = self.__compute_power()
        while len(self.V) > 0:
            self.__log("To process {} element".format(len(self.V)))
            curr_best = max(power, key=power.get)
            rank.append(curr_best)
            self.V.remove(curr_best)
            power = self.__compute_power()

        self.__log("Done", close=True)
        return rank

    def __compute_power(self):
        self.__log("Compute power")
        power = {}

        for i, e1 in enumerate(self.V):
            self.__log("Compute {} / {}".format(i, len(self.V)))
            outbound = [self.preference(e1, e2) for e2 in self.V]
            inbound = [self.preference(e2, e1) for e2 in self.V]
            power[e1] = functools.reduce(operator.add, outbound) - functools.reduce(operator.add, inbound)

        return power

    def __log(self, message, close=False):
        if not hasattr(self, 'log'):
            self.log = open('greedy_out.txt', 'w')

        self.log.write(message + "\n")
        self.log.flush()

        if close:
            self.log.close()
