# Statechart compiler by Glenn De Jonghe
#
# Date:   Sun Jul 27 22:25:01 2014

# Model author: Simon Van Mierlo
# Model name:   Instance Controller
# Model description:
"""
    Moving instances around.
"""

from python_runtime.statecharts_core import ObjectManagerBase, Event, InstanceWrapper, RuntimeClassBase, Association


class Main(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_idle = 1
    Root_selected = 2
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        # User defined attributes
        self.node = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
    
    def start(self):
        super(Main, self).start()
        self.enter_Root_idle()
    
    #The actual constructor
    def __init__(self, controller, node):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.node = node
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_idle(self):
        self.current_state[self.Root].append(self.Root_idle)
    
    def exit_Root_idle(self):
        self.current_state[self.Root] = []
    
    def enter_Root_selected(self):
        self.current_state[self.Root].append(self.Root_selected)
    
    def exit_Root_selected(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_idle:
                catched = self.transition_Root_idle(event)
            elif self.current_state[self.Root][0] == self.Root_selected:
                catched = self.transition_Root_selected(event)
        return catched
    
    def transition_Root_idle(self, event) :
        catched = False
        enableds = []
        if event.name == "left-click" and event.getPort() == "input" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_idle. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_idle()
                self.node.highlight()
                self.enter_Root_selected()
            catched = True
        
        return catched
    
    def transition_Root_selected(self, event) :
        catched = False
        enableds = []
        if event.name == "drag" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "left-release" and event.getPort() == "input" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_selected. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_selected()
                self.node.move()
                self.enter_Root_selected()
            elif enabled == 2 :
                self.exit_Root_selected()
                self.node.unhighlight()
                self.enter_Root_idle()
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
    def __init__(self, node, keep_running = True):
        super(Controller, self).__init__(ObjectManager(self), keep_running)
        self.addInputPort("input")
        self.object_manager.createInstance("Main", [node])
        
def main():
    controller = Controller()
    controller.start()

if __name__ == "__main__":
    main()
