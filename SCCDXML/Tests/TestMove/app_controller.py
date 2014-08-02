# Statechart compiler by Glenn De Jonghe
#
# Date:   Tue Jul 22 15:08:05 2014

# Model author: Simon Van Mierlo
# Model name:   Test Application
# Model description:
"""
    Handling the simple example, drawing some stuff on the canvas.
"""

from python_runtime.statecharts_core import ObjectManagerBase, Event, InstanceWrapper, RuntimeClassBase, Association


class Main(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_state_1 = 1
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(Main, self).__init__()
        # User defined attributes
        self.test = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
    
    def start(self):
        super(Main, self).start()
        self.enter_Root_state_1()
    
    #The actual constructor
    def __init__(self, controller, test):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.test = test
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_state_1(self):
        self.current_state[self.Root].append(self.Root_state_1)
    
    def exit_Root_state_1(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_state_1:
                catched = self.transition_Root_state_1(event)
        return catched
    
    def transition_Root_state_1(self, event) :
        catched = False
        enableds = []
        if event.name == "right-click" and event.getPort() == "input" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_state_1. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_state_1()
                self.test.create_rectangle()
                self.enter_Root_state_1()
            catched = True
        
        return catched
    
    # Execute transitions
    def transition(self, event = Event("")):
        self.state_changed = self.transition_Root(event)
    # inState method for statechart
    def inState(self, nodes):
        for actives in self.current_state.itervalues():
            nodes = [node for node in nodes if node not in actives]
            if not nodes :
                return True
        return False
    
class ObjectManager (ObjectManagerBase):
    def __init__(self, controller):
        super(ObjectManager, self).__init__(controller)
    
    def instantiate(self, class_name, construct_params):
        associations = []
        if class_name == "Main" :
            instance =  Main(self.controller, *construct_params)
        if instance:
            return InstanceWrapper(instance, associations)
        else :
            return None

from python_runtime.statecharts_core import GameLoopControllerBase
class Controller(GameLoopControllerBase):
    def __init__(self, test, keep_running = True):
        super(Controller, self).__init__(ObjectManager(self), keep_running)
        self.addInputPort("input")
        self.object_manager.createInstance("Main", [test])
        
def main():
    controller = Controller()
    controller.start()

if __name__ == "__main__":
    main()
