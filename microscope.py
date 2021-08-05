SIMULATOR_IDX = 1

from .simulator.simulator import SimulatorWindow

class Microscope():
    def __init__(self, connector):
        if connector == SIMULATOR_IDX:
            return SimulatorWindow()
        elif self.checkForConnection(connector):



    def checkForConnection(com_port):
        # send on port or all ports and if returns show
    