# Statechart compiler by Glenn De Jonghe
#
# Date:   Mon Jul 21 10:46:34 2014

# Model author: Glenn De Jonghe
# Model name:   AI Tank
# Model description:
"""
    Handling the npc tank.
"""

from python_runtime.statecharts_core import ObjectManagerBase, Event, InstanceWrapper, RuntimeClassBase, Association
from AIMap import AIMap
import math
from mymath import D1, D45, D360


class Main(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_creation = 1
    Root_error = 2
    Root_creation_state_1 = 3
    Root_creation_state_2 = 4
    Root_creation_state_3 = 5
    Root_creation_state_4 = 6
    Root_creation_state_5 = 7
    Root_creation_state_6 = 8
    Root_creation_state_7 = 9
    Root_creation_state_8 = 10
    Root_creation_state_9 = 11
    Root_creation_state_10 = 12
    Root_creation_state_11 = 13
    Root_creation_state_12 = 14
    Root_creation_state_13 = 15
    Root_creation_state_14 = 16
    Root_creation_state_15 = 17
    Root_creation_state_16 = 18
    Root_creation_state_17 = 19
    Root_creation_state_18 = 20
    Root_creation_state_19 = 21
    Root_creation_state_20 = 22
    Root_creation_state_21 = 23
    Root_creation_end = 24
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(Main, self).__init__()
        # User defined attributes
        self.tank = None
        self.map = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_creation] = []
    
    def start(self):
        super(Main, self).start()
        self.enterDefault_Root_creation()
    
    #The actual constructor
    def __init__(self, controller, tank):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
        self.map = AIMap(tank.field.level)
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_creation(self):
        self.current_state[self.Root].append(self.Root_creation)
    
    def exit_Root_creation(self):
        if self.Root_creation_state_1 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_1()
        if self.Root_creation_state_2 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_2()
        if self.Root_creation_state_3 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_3()
        if self.Root_creation_state_4 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_4()
        if self.Root_creation_state_5 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_5()
        if self.Root_creation_state_6 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_6()
        if self.Root_creation_state_7 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_7()
        if self.Root_creation_state_8 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_8()
        if self.Root_creation_state_9 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_9()
        if self.Root_creation_state_10 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_10()
        if self.Root_creation_state_11 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_11()
        if self.Root_creation_state_12 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_12()
        if self.Root_creation_state_13 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_13()
        if self.Root_creation_state_14 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_14()
        if self.Root_creation_state_15 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_15()
        if self.Root_creation_state_16 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_16()
        if self.Root_creation_state_17 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_17()
        if self.Root_creation_state_18 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_18()
        if self.Root_creation_state_19 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_19()
        if self.Root_creation_state_20 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_20()
        if self.Root_creation_state_21 in self.current_state[self.Root_creation] :
            self.exit_Root_creation_state_21()
        if self.Root_creation_end in self.current_state[self.Root_creation] :
            self.exit_Root_creation_end()
        self.current_state[self.Root] = []
    
    def enter_Root_error(self):
        self.current_state[self.Root].append(self.Root_error)
    
    def exit_Root_error(self):
        self.current_state[self.Root] = []
    
    def enter_Root_creation_state_1(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_1)
    
    def exit_Root_creation_state_1(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_2(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_2)
    
    def exit_Root_creation_state_2(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_3(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_3)
    
    def exit_Root_creation_state_3(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_4(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_4)
    
    def exit_Root_creation_state_4(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_5(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_5)
    
    def exit_Root_creation_state_5(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_6(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_6)
    
    def exit_Root_creation_state_6(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_7(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_7)
    
    def exit_Root_creation_state_7(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_8(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_8)
    
    def exit_Root_creation_state_8(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_9(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_9)
    
    def exit_Root_creation_state_9(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_10(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_10)
    
    def exit_Root_creation_state_10(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_11(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_11)
    
    def exit_Root_creation_state_11(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_12(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_12)
    
    def exit_Root_creation_state_12(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_13(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_13)
    
    def exit_Root_creation_state_13(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_14(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_14)
    
    def exit_Root_creation_state_14(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_15(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_15)
    
    def exit_Root_creation_state_15(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_16(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_16)
    
    def exit_Root_creation_state_16(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_17(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_17)
    
    def exit_Root_creation_state_17(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_18(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_18)
    
    def exit_Root_creation_state_18(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_19(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_19)
    
    def exit_Root_creation_state_19(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_20(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_20)
    
    def exit_Root_creation_state_20(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_state_21(self):
        self.current_state[self.Root_creation].append(self.Root_creation_state_21)
    
    def exit_Root_creation_state_21(self):
        self.current_state[self.Root_creation] = []
    
    def enter_Root_creation_end(self):
        self.current_state[self.Root_creation].append(self.Root_creation_end)
    
    def exit_Root_creation_end(self):
        self.current_state[self.Root_creation] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_creation(self):
        self.enter_Root_creation()
        self.enter_Root_creation_state_1()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_error:
                catched = self.transition_Root_error(event)
            elif self.current_state[self.Root][0] == self.Root_creation:
                catched = self.transition_Root_creation(event)
        return catched
    
    def transition_Root_error(self, event) :
        catched = False
        return catched
    
    def transition_Root_creation(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_creation_error" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "instance_association_error" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation()
                print "Instance creation error!"
                self.enter_Root_error()
            elif enabled == 2 :
                self.exit_Root_creation()
                print "Instance association error!"
                self.enter_Root_error()
            catched = True
        
        if not catched :
            if self.current_state[self.Root_creation][0] == self.Root_creation_state_1:
                catched = self.transition_Root_creation_state_1(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_2:
                catched = self.transition_Root_creation_state_2(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_3:
                catched = self.transition_Root_creation_state_3(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_4:
                catched = self.transition_Root_creation_state_4(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_5:
                catched = self.transition_Root_creation_state_5(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_6:
                catched = self.transition_Root_creation_state_6(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_7:
                catched = self.transition_Root_creation_state_7(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_8:
                catched = self.transition_Root_creation_state_8(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_9:
                catched = self.transition_Root_creation_state_9(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_10:
                catched = self.transition_Root_creation_state_10(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_11:
                catched = self.transition_Root_creation_state_11(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_12:
                catched = self.transition_Root_creation_state_12(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_13:
                catched = self.transition_Root_creation_state_13(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_14:
                catched = self.transition_Root_creation_state_14(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_15:
                catched = self.transition_Root_creation_state_15(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_16:
                catched = self.transition_Root_creation_state_16(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_17:
                catched = self.transition_Root_creation_state_17(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_18:
                catched = self.transition_Root_creation_state_18(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_19:
                catched = self.transition_Root_creation_state_19(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_20:
                catched = self.transition_Root_creation_state_20(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_state_21:
                catched = self.transition_Root_creation_state_21(event)
            elif self.current_state[self.Root_creation][0] == self.Root_creation_end:
                catched = self.transition_Root_creation_end(event)
        return catched
    
    def transition_Root_creation_state_1(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_1. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_1()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'turret_control',self.tank]))
                self.enter_Root_creation_state_2()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_2(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_2. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_2()
                self.enter_Root_creation_state_3()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_3(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_3. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_3()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'motor_control',self.tank]))
                self.enter_Root_creation_state_4()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_4(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_4. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_4()
                self.enter_Root_creation_state_5()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_5(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_5. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_5()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'turret_steering',self.tank]))
                self.enter_Root_creation_state_6()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_6(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_6. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_6()
                self.enter_Root_creation_state_7()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_7(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_7. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_7()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'steering',self.tank,self.map]))
                self.enter_Root_creation_state_8()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_8(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_8. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_8()
                self.enter_Root_creation_state_9()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_9(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_9. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_9()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'path_finder',self.tank,self.map]))
                self.enter_Root_creation_state_10()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_10(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_10. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_10()
                self.enter_Root_creation_state_11()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_11(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_11. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_11()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'attack_planner']))
                self.enter_Root_creation_state_12()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_12(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_12. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_12()
                self.enter_Root_creation_state_13()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_13(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_13. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_13()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'explore_planner',self.tank,self.map]))
                self.enter_Root_creation_state_14()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_14(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_14. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_14()
                self.enter_Root_creation_state_15()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_15(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_15. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_15()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'pilot_strategy']))
                self.enter_Root_creation_state_16()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_16(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_16. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_16()
                self.enter_Root_creation_state_17()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_17(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_17. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_17()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'enemy_tracker']))
                self.enter_Root_creation_state_18()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_18(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_18. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_18()
                self.enter_Root_creation_state_19()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_19(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_19. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_19()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'radar',self.tank]))
                self.enter_Root_creation_state_20()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_20(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_20. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_20()
                self.enter_Root_creation_state_21()
            catched = True
        
        return catched
    
    def transition_Root_creation_state_21(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_creation_state_21. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_creation_state_21()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'turret_control']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'motor_control']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'turret_control','turret_steering/turret_control']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'attack_planner','turret_steering/attack_planner']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'turret_steering']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'motor_control','steering/motor_control']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'path_finder','steering/path_finder']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'steering']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'steering','path_finder/steering']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'path_finder']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'turret_steering','attack_planner/turret_steering']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'turret_control','attack_planner/turret_control']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'path_finder','attack_planner/path_finder']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'attack_planner']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'path_finder','explore_planner/path_finder']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'explore_planner']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'explore_planner','pilot_strategy/explore_planner']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'attack_planner','pilot_strategy/attack_planner']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'pilot_strategy']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'pilot_strategy','enemy_tracker/pilot_strategy']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'attack_planner','enemy_tracker/attack_planner']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'enemy_tracker']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'pilot_strategy','radar/pilot_strategy']))
                self.object_manager.addEvent(Event("associate_instance", parameters = [self, 'enemy_tracker','radar/enemy_tracker']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'radar']))
                self.enter_Root_creation_end()
            catched = True
        
        return catched
    
    def transition_Root_creation_end(self, event) :
        catched = False
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
    

class Radar(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_no_enemy = 1
    Root_enemy_in_sight = 2
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(Radar, self).__init__()
        # User defined attributes
        self.tank = None
        self.range = 2000
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
    
    def start(self):
        super(Radar, self).start()
        self.enter_Root_no_enemy()
    
    #The actual constructor
    def __init__(self, controller, tank):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
    
    # User defined method
    def isEnemyVisible(self):
        sighted_list = self.tank.field.getSightedEnemies(self.tank, self.range)
        if len(sighted_list) > 0 :
            return True
        return False
        
    # User defined method
    def getEnemyPos(self):
        sighted_list = self.tank.field.getSightedEnemies(self.tank, self.range)
        if len(sighted_list) > 0 :
            sighted_list.sort(key=lambda x: x[1])
            return sighted_list[0][0]
        else :
            return (-1,-1)
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_no_enemy(self):
        self.current_state[self.Root].append(self.Root_no_enemy)
    
    def exit_Root_no_enemy(self):
        self.current_state[self.Root] = []
    
    def enter_Root_enemy_in_sight(self):
        self.current_state[self.Root].append(self.Root_enemy_in_sight)
    
    def exit_Root_enemy_in_sight(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_no_enemy:
                catched = self.transition_Root_no_enemy(event)
            elif self.current_state[self.Root][0] == self.Root_enemy_in_sight:
                catched = self.transition_Root_enemy_in_sight(event)
        return catched
    
    def transition_Root_no_enemy(self, event) :
        catched = False
        enableds = []
        if self.isEnemyVisible() :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_no_enemy. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_no_enemy()
                send_event = Event("enemy_sighted", parameters = [self.getEnemyPos()])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "enemy_tracker" , send_event]))
                send_event = Event("enemy_sighted", parameters = [self.getEnemyPos()])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "pilot_strategy" , send_event]))
                self.enter_Root_enemy_in_sight()
            catched = True
        
        return catched
    
    def transition_Root_enemy_in_sight(self, event) :
        catched = False
        enableds = []
        if not self.isEnemyVisible() :
            enableds.append(1)
        
        if event.name == "update" and event.getPort() == "engine" :
            if self.isEnemyVisible() :
                enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_enemy_in_sight. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_enemy_in_sight()
                send_event = Event("enemy_out_of_sight", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "enemy_tracker" , send_event]))
                self.enter_Root_no_enemy()
            elif enabled == 2 :
                self.exit_Root_enemy_in_sight()
                send_event = Event("enemy_pos", parameters = [self.getEnemyPos()])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "enemy_tracker" , send_event]))
                self.enter_Root_enemy_in_sight()
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
    

class EnemyTracker(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_no_enemy = 1
    Root_enemy_pos_known = 2
    Root_enemy_pos_unsure = 3
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(EnemyTracker, self).__init__()
        # User defined attributes
        self.enemy_pos = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
    
    def start(self):
        super(EnemyTracker, self).start()
        self.enter_Root_no_enemy()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
    
    # User defined method
    def hasEnemyMoved(self, new_position):
        return new_position != self.enemy_pos
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_no_enemy(self):
        self.current_state[self.Root].append(self.Root_no_enemy)
    
    def exit_Root_no_enemy(self):
        self.current_state[self.Root] = []
    
    def enter_Root_enemy_pos_known(self):
        self.current_state[self.Root].append(self.Root_enemy_pos_known)
    
    def exit_Root_enemy_pos_known(self):
        self.current_state[self.Root] = []
    
    def enter_Root_enemy_pos_unsure(self):
        self.current_state[self.Root].append(self.Root_enemy_pos_unsure)
    
    def exit_Root_enemy_pos_unsure(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_no_enemy:
                catched = self.transition_Root_no_enemy(event)
            elif self.current_state[self.Root][0] == self.Root_enemy_pos_known:
                catched = self.transition_Root_enemy_pos_known(event)
            elif self.current_state[self.Root][0] == self.Root_enemy_pos_unsure:
                catched = self.transition_Root_enemy_pos_unsure(event)
        return catched
    
    def transition_Root_no_enemy(self, event) :
        catched = False
        enableds = []
        if event.name == "enemy_sighted" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_no_enemy. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                enemy_position = parameters[0]
                self.exit_Root_no_enemy()
                self.enemy_pos = enemy_position
                self.enter_Root_enemy_pos_known()
            catched = True
        
        return catched
    
    def transition_Root_enemy_pos_known(self, event) :
        catched = False
        enableds = []
        if event.name == "enemy_pos" and event.getPort() == "" :
            parameters = event.getParameters()
            position = parameters[0]
            if self.hasEnemyMoved(position) :
                enableds.append(1)
        
        if event.name == "enemy_out_of_sight" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_enemy_pos_known. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                position = parameters[0]
                self.exit_Root_enemy_pos_known()
                self.enemy_pos = position
                send_event = Event("enemy_pos_changed", parameters = [self.enemy_pos])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "attack_planner" , send_event]))
                self.enter_Root_enemy_pos_known()
            elif enabled == 2 :
                self.exit_Root_enemy_pos_known()
                send_event = Event("enemy_out_of_sight", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "attack_planner" , send_event]))
                self.enter_Root_enemy_pos_unsure()
            catched = True
        
        return catched
    
    def transition_Root_enemy_pos_unsure(self, event) :
        catched = False
        enableds = []
        if event.name == "destination_reached" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "enemy_sighted" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_enemy_pos_unsure. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_enemy_pos_unsure()
                send_event = Event("enemy_lost", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "pilot_strategy" , send_event]))
                print "raise enemy_lost"
                self.enter_Root_no_enemy()
            elif enabled == 2 :
                parameters = event.getParameters()
                position = parameters[0]
                self.exit_Root_enemy_pos_unsure()
                self.enemy_pos = position
                self.enter_Root_enemy_pos_known()
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
    

class PilotStrategy(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_exploring = 1
    Root_attacking = 2
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(PilotStrategy, self).__init__()
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
    
    def start(self):
        super(PilotStrategy, self).start()
        self.enter_Root_exploring()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_exploring(self):
        send_event = Event("explore", parameters = [])
        self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "explore_planner" , send_event]))
        self.current_state[self.Root].append(self.Root_exploring)
    
    def exit_Root_exploring(self):
        send_event = Event("stop_exploring", parameters = [])
        self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "explore_planner" , send_event]))
        self.current_state[self.Root] = []
    
    def enter_Root_attacking(self):
        self.current_state[self.Root].append(self.Root_attacking)
    
    def exit_Root_attacking(self):
        send_event = Event("stop_attacking", parameters = [])
        self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "attack_planner" , send_event]))
        print "raise stop_attacking"
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_exploring:
                catched = self.transition_Root_exploring(event)
            elif self.current_state[self.Root][0] == self.Root_attacking:
                catched = self.transition_Root_attacking(event)
        return catched
    
    def transition_Root_exploring(self, event) :
        catched = False
        enableds = []
        if event.name == "enemy_sighted" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_exploring. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                position = parameters[0]
                self.exit_Root_exploring()
                send_event = Event("attack", parameters = [position])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "attack_planner" , send_event]))
                self.enter_Root_attacking()
            catched = True
        
        return catched
    
    def transition_Root_attacking(self, event) :
        catched = False
        enableds = []
        if event.name == "enemy_lost" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_attacking. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_attacking()
                print "received enemy lost"
                self.enter_Root_exploring()
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
    

class ExplorePlanner(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_exploring = 1
    Root_idle = 2
    Root_exploring_no_destination = 3
    Root_exploring_destination_set = 4
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(ExplorePlanner, self).__init__()
        # User defined attributes
        self.map = None
        self.tank = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_exploring] = []
    
    def start(self):
        super(ExplorePlanner, self).start()
        self.enter_Root_idle()
    
    #The actual constructor
    def __init__(self, controller, tank, aimap):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
        self.map = aimap
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_exploring(self):
        self.current_state[self.Root].append(self.Root_exploring)
    
    def exit_Root_exploring(self):
        if self.Root_exploring_no_destination in self.current_state[self.Root_exploring] :
            self.exit_Root_exploring_no_destination()
        if self.Root_exploring_destination_set in self.current_state[self.Root_exploring] :
            self.exit_Root_exploring_destination_set()
        self.current_state[self.Root] = []
    
    def enter_Root_idle(self):
        self.current_state[self.Root].append(self.Root_idle)
    
    def exit_Root_idle(self):
        self.current_state[self.Root] = []
    
    def enter_Root_exploring_no_destination(self):
        self.current_state[self.Root_exploring].append(self.Root_exploring_no_destination)
    
    def exit_Root_exploring_no_destination(self):
        self.current_state[self.Root_exploring] = []
    
    def enter_Root_exploring_destination_set(self):
        self.current_state[self.Root_exploring].append(self.Root_exploring_destination_set)
    
    def exit_Root_exploring_destination_set(self):
        self.current_state[self.Root_exploring] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_exploring(self):
        self.enter_Root_exploring()
        self.enter_Root_exploring_no_destination()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_idle:
                catched = self.transition_Root_idle(event)
            elif self.current_state[self.Root][0] == self.Root_exploring:
                catched = self.transition_Root_exploring(event)
        return catched
    
    def transition_Root_idle(self, event) :
        catched = False
        enableds = []
        if event.name == "explore" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_idle. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_idle()
                self.enterDefault_Root_exploring()
            catched = True
        
        return catched
    
    def transition_Root_exploring(self, event) :
        catched = False
        enableds = []
        if event.name == "stop_exploring" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_exploring. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_exploring()
                print "stop_exploring received"
                self.enter_Root_idle()
            catched = True
        
        if not catched :
            if self.current_state[self.Root_exploring][0] == self.Root_exploring_no_destination:
                catched = self.transition_Root_exploring_no_destination(event)
            elif self.current_state[self.Root_exploring][0] == self.Root_exploring_destination_set:
                catched = self.transition_Root_exploring_destination_set(event)
        return catched
    
    def transition_Root_exploring_no_destination(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_exploring_no_destination. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_exploring_no_destination()
                send_event = Event("new_destination", parameters = [self.map.getNewExplore(self.tank.getPosition(),self.tank.getAngle())])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "path_finder" , send_event]))
                self.enter_Root_exploring_destination_set()
            catched = True
        
        return catched
    
    def transition_Root_exploring_destination_set(self, event) :
        catched = False
        enableds = []
        if event.name == "destination_reached" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_exploring_destination_set. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_exploring_destination_set()
                self.enter_Root_exploring_no_destination()
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
    

class AttackPlanner(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_action = 1
    Root_action_movement = 2
    Root_action_shooting = 3
    Root_idle = 4
    Root_action_movement_following = 5
    Root_action_shooting_loaded = 6
    Root_action_shooting_reloading = 7
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(AttackPlanner, self).__init__()
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        self.timers = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_action] = []
        self.current_state[self.Root_action_movement] = []
        self.current_state[self.Root_action_shooting] = []
    
    def start(self):
        super(AttackPlanner, self).start()
        self.enter_Root_idle()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_action(self):
        self.current_state[self.Root].append(self.Root_action)
    
    def exit_Root_action(self):
        self.exit_Root_action_movement()
        self.exit_Root_action_shooting()
        self.current_state[self.Root] = []
    
    def enter_Root_action_movement(self):
        self.current_state[self.Root_action].append(self.Root_action_movement)
    
    def exit_Root_action_movement(self):
        if self.Root_action_movement_following in self.current_state[self.Root_action_movement] :
            self.exit_Root_action_movement_following()
        self.current_state[self.Root_action] = []
    
    def enter_Root_action_shooting(self):
        self.current_state[self.Root_action].append(self.Root_action_shooting)
    
    def exit_Root_action_shooting(self):
        if self.Root_action_shooting_loaded in self.current_state[self.Root_action_shooting] :
            self.exit_Root_action_shooting_loaded()
        if self.Root_action_shooting_reloading in self.current_state[self.Root_action_shooting] :
            self.exit_Root_action_shooting_reloading()
        self.current_state[self.Root_action] = []
    
    def enter_Root_idle(self):
        self.current_state[self.Root].append(self.Root_idle)
    
    def exit_Root_idle(self):
        self.current_state[self.Root] = []
    
    def enter_Root_action_movement_following(self):
        self.current_state[self.Root_action_movement].append(self.Root_action_movement_following)
    
    def exit_Root_action_movement_following(self):
        self.current_state[self.Root_action_movement] = []
    
    def enter_Root_action_shooting_loaded(self):
        self.current_state[self.Root_action_shooting].append(self.Root_action_shooting_loaded)
    
    def exit_Root_action_shooting_loaded(self):
        self.current_state[self.Root_action_shooting] = []
    
    def enter_Root_action_shooting_reloading(self):
        self.timers[0] = 0.5
        self.current_state[self.Root_action_shooting].append(self.Root_action_shooting_reloading)
    
    def exit_Root_action_shooting_reloading(self):
        self.timers.pop(0, None)
        self.current_state[self.Root_action_shooting] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_action(self):
        self.enter_Root_action()
        self.enterDefault_Root_action_movement()
        self.enterDefault_Root_action_shooting()
    
    def enterDefault_Root_action_movement(self):
        self.enter_Root_action_movement()
        self.enter_Root_action_movement_following()
    
    def enterDefault_Root_action_shooting(self):
        self.enter_Root_action_shooting()
        self.enter_Root_action_shooting_loaded()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_idle:
                catched = self.transition_Root_idle(event)
            elif self.current_state[self.Root][0] == self.Root_action:
                catched = self.transition_Root_action(event)
        return catched
    
    def transition_Root_idle(self, event) :
        catched = False
        enableds = []
        if event.name == "attack" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_idle. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                enemy_pos = parameters[0]
                self.exit_Root_idle()
                print "received attack"
                send_event = Event("new_destination", parameters = [enemy_pos])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "path_finder" , send_event]))
                send_event = Event("aim_at", parameters = [enemy_pos])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "turret_steering" , send_event]))
                self.enterDefault_Root_action()
            catched = True
        
        return catched
    
    def transition_Root_action(self, event) :
        catched = False
        enableds = []
        if event.name == "stop_attacking" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_action. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_action()
                print "received stop attack"
                send_event = Event("stop_aiming", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "turret_steering" , send_event]))
                self.enter_Root_idle()
            catched = True
        
        if not catched :
            catched = self.transition_Root_action_movement(event) or catched
            catched = self.transition_Root_action_shooting(event) or catched
        return catched
    
    def transition_Root_action_movement(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_action_movement][0] == self.Root_action_movement_following:
                catched = self.transition_Root_action_movement_following(event)
        return catched
    
    def transition_Root_action_movement_following(self, event) :
        catched = False
        enableds = []
        if event.name == "enemy_pos_changed" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "enemy_out_of_sight" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_action_movement_following. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                enemy_pos = parameters[0]
                self.exit_Root_action_movement_following()
                send_event = Event("new_destination", parameters = [enemy_pos])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "path_finder" , send_event]))
                send_event = Event("aim_at", parameters = [enemy_pos])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "turret_steering" , send_event]))
                self.enter_Root_action_movement_following()
            elif enabled == 2 :
                self.exit_Root_action_movement_following()
                send_event = Event("stop_aiming", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "turret_steering" , send_event]))
                self.enter_Root_action_movement_following()
            catched = True
        
        return catched
    
    def transition_Root_action_shooting(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_action_shooting][0] == self.Root_action_shooting_loaded:
                catched = self.transition_Root_action_shooting_loaded(event)
            elif self.current_state[self.Root_action_shooting][0] == self.Root_action_shooting_reloading:
                catched = self.transition_Root_action_shooting_reloading(event)
        return catched
    
    def transition_Root_action_shooting_loaded(self, event) :
        catched = False
        enableds = []
        if event.name == "ready_to_shoot" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_action_shooting_loaded. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_action_shooting_loaded()
                send_event = Event("shoot", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "turret_control" , send_event]))
                print "raise shoot"
                self.enter_Root_action_shooting_reloading()
            catched = True
        
        return catched
    
    def transition_Root_action_shooting_reloading(self, event) :
        catched = False
        enableds = []
        if event.name == "_0after" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_action_shooting_reloading. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_action_shooting_reloading()
                self.enter_Root_action_shooting_loaded()
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
    

class PathFinder(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_idle = 1
    Root_check_points = 2
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(PathFinder, self).__init__()
        # User defined attributes
        self.waypoints = []
        self.destination = (-1,-1)
        self.map = None
        self.tank = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
    
    def start(self):
        super(PathFinder, self).start()
        self.enter_Root_idle()
    
    #The actual constructor
    def __init__(self, controller, tank, aimap):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
        self.map = aimap
    
    # User defined method
    def calculatePath(self):
        return self.map.calculatePath(self.tank.getPosition(), self.destination)
        
    # User defined method
    def requiresNewPath(self, new_destination):
        return self.map.calculateCell(self.destination) != self.map.calculateCell(new_destination)
        
    # User defined method
    def morePoints(self):
        return len(self.waypoints) > 0
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_idle(self):
        self.current_state[self.Root].append(self.Root_idle)
    
    def exit_Root_idle(self):
        self.current_state[self.Root] = []
    
    def enter_Root_check_points(self):
        self.current_state[self.Root].append(self.Root_check_points)
    
    def exit_Root_check_points(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_idle:
                catched = self.transition_Root_idle(event)
            elif self.current_state[self.Root][0] == self.Root_check_points:
                catched = self.transition_Root_check_points(event)
        return catched
    
    def transition_Root_idle(self, event) :
        catched = False
        enableds = []
        if event.name == "waypoint_reached" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "new_destination" and event.getPort() == "" :
            parameters = event.getParameters()
            destination = parameters[0]
            if self.requiresNewPath(destination) :
                enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_idle. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_idle()
                self.enter_Root_check_points()
            elif enabled == 2 :
                parameters = event.getParameters()
                destination = parameters[0]
                self.exit_Root_idle()
                self.destination = destination
                self.waypoints = self.calculatePath()
                self.enter_Root_check_points()
            catched = True
        
        return catched
    
    def transition_Root_check_points(self, event) :
        catched = False
        enableds = []
        if self.morePoints() :
            enableds.append(1)
        
        if not self.morePoints() :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_check_points. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_check_points()
                next_waypoint = self.waypoints.pop(0)
                send_event = Event("new_waypoint", parameters = [next_waypoint])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "steering" , send_event]))
                self.enter_Root_idle()
            elif enabled == 2 :
                self.exit_Root_check_points()
                send_event = Event("destination_reached", parameters = [])
                self.object_manager.addEvent(Event("broad_cast", parameters = [send_event]))
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
    

class Steering(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_steering = 1
    Root_idle = 2
    Root_steering_forward_backward = 3
    Root_steering_left_right = 4
    Root_steering_wait = 5
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(Steering, self).__init__()
        # User defined attributes
        self.dest_waypoint = (-1,-1)
        self.dest_cell = (-1,-1)
        self.reaction_time = 0.05
        self.tank = None
        self.map = None
        self.margin = 0.2
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        self.timers = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_steering] = []
    
    def start(self):
        super(Steering, self).start()
        self.enter_Root_idle()
    
    #The actual constructor
    def __init__(self, controller, tank, aimap):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
        self.map = aimap
    
    # User defined method
    def pointReached(self):
        cell = self.map.calculateCell((self.tank.x, self.tank.y))
        return cell == self.dest_cell
        
    # User defined method
    def pointAhead(self):
        goal_angle = self.tank.angleToDest(self.dest_waypoint)
        diff = math.fabs(self.tank.angle - goal_angle)
        if diff <= (D45) :
            #self.tank.moveSpeed = int(math.ceil(((D45 - diff) / D45) * self.maxMoveSpeed))
            return True
        elif diff >= (D360 - D45) :
            #self.tank.moveSpeed = int(math.ceil(((diff - (D360 - D45)) / D45) * self.maxMoveSpeed))
            return True
        return False
        
    # User defined method
    def pointBehind(self):
        goal_angle = self.tank.angleToDest(self.dest_waypoint)
        diff = math.fabs(self.tank.angle - goal_angle)
        if diff <= (D45) or diff >= (D360 - D45) :
            return False
        return True
        
    # User defined method
    def pointRight(self):
        goal_angle = self.tank.angleToDest(self.dest_waypoint)
        diff = (self.tank.angle - goal_angle) % D360
        if diff >= self.margin and diff <= math.pi:
            return True
        return False
        
    # User defined method
    def pointLeft(self):
        goal_angle = self.tank.angleToDest(self.dest_waypoint)
        diff = (goal_angle - self.tank.angle) % D360
        if diff >= self.margin and diff <= math.pi:
            return True
        return False
        
    # User defined method
    def pointStraight(self):
        goal_angle = self.tank.angleToDest(self.dest_waypoint)
        diff = math.fabs(self.tank.angle - goal_angle)
        if diff < self.margin or diff > (D360- self.margin) :
            return True
        return False
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_steering(self):
        self.current_state[self.Root].append(self.Root_steering)
    
    def exit_Root_steering(self):
        if self.Root_steering_forward_backward in self.current_state[self.Root_steering] :
            self.exit_Root_steering_forward_backward()
        if self.Root_steering_left_right in self.current_state[self.Root_steering] :
            self.exit_Root_steering_left_right()
        if self.Root_steering_wait in self.current_state[self.Root_steering] :
            self.exit_Root_steering_wait()
        self.current_state[self.Root] = []
    
    def enter_Root_idle(self):
        self.current_state[self.Root].append(self.Root_idle)
    
    def exit_Root_idle(self):
        self.current_state[self.Root] = []
    
    def enter_Root_steering_forward_backward(self):
        self.current_state[self.Root_steering].append(self.Root_steering_forward_backward)
    
    def exit_Root_steering_forward_backward(self):
        self.current_state[self.Root_steering] = []
    
    def enter_Root_steering_left_right(self):
        self.current_state[self.Root_steering].append(self.Root_steering_left_right)
    
    def exit_Root_steering_left_right(self):
        self.current_state[self.Root_steering] = []
    
    def enter_Root_steering_wait(self):
        self.timers[0] = self.reaction_time
        self.current_state[self.Root_steering].append(self.Root_steering_wait)
    
    def exit_Root_steering_wait(self):
        self.timers.pop(0, None)
        self.current_state[self.Root_steering] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_steering(self):
        self.enter_Root_steering()
        self.enter_Root_steering_forward_backward()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_idle:
                catched = self.transition_Root_idle(event)
            elif self.current_state[self.Root][0] == self.Root_steering:
                catched = self.transition_Root_steering(event)
        return catched
    
    def transition_Root_idle(self, event) :
        catched = False
        enableds = []
        if event.name == "new_waypoint" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_idle. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                dest_waypoint = parameters[0]
                self.exit_Root_idle()
                self.dest_waypoint = dest_waypoint
                self.dest_cell = self.map.calculateCell(dest_waypoint)
                self.enterDefault_Root_steering()
            catched = True
        
        return catched
    
    def transition_Root_steering(self, event) :
        catched = False
        enableds = []
        if self.pointReached() :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_steering. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_steering()
                send_event = Event("waypoint_reached", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "path_finder" , send_event]))
                self.enter_Root_idle()
            catched = True
        
        if not catched :
            if self.current_state[self.Root_steering][0] == self.Root_steering_forward_backward:
                catched = self.transition_Root_steering_forward_backward(event)
            elif self.current_state[self.Root_steering][0] == self.Root_steering_left_right:
                catched = self.transition_Root_steering_left_right(event)
            elif self.current_state[self.Root_steering][0] == self.Root_steering_wait:
                catched = self.transition_Root_steering_wait(event)
        return catched
    
    def transition_Root_steering_forward_backward(self, event) :
        catched = False
        enableds = []
        if self.pointAhead() :
            enableds.append(1)
        
        if self.pointBehind() :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_steering_forward_backward. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_steering_forward_backward()
                send_event = Event("forward", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "motor_control" , send_event]))
                self.enter_Root_steering_left_right()
            elif enabled == 2 :
                self.exit_Root_steering_forward_backward()
                send_event = Event("stop", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "motor_control" , send_event]))
                self.enter_Root_steering_left_right()
            catched = True
        
        return catched
    
    def transition_Root_steering_left_right(self, event) :
        catched = False
        enableds = []
        if self.pointStraight() :
            enableds.append(1)
        
        if self.pointLeft() :
            enableds.append(2)
        
        if self.pointRight() :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_steering_left_right. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_steering_left_right()
                send_event = Event("stop_turning", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "motor_control" , send_event]))
                self.enter_Root_steering_wait()
            elif enabled == 2 :
                self.exit_Root_steering_left_right()
                send_event = Event("turn_left", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "motor_control" , send_event]))
                self.enter_Root_steering_wait()
            elif enabled == 3 :
                self.exit_Root_steering_left_right()
                send_event = Event("turn_right", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "motor_control" , send_event]))
                self.enter_Root_steering_wait()
            catched = True
        
        return catched
    
    def transition_Root_steering_wait(self, event) :
        catched = False
        enableds = []
        if event.name == "_0after" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_steering_wait. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_steering_wait()
                self.enter_Root_steering_forward_backward()
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
    

class TurretSteering(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_aiming = 1
    Root_idle = 2
    Root_aiming_adjust = 3
    Root_aiming_wait = 4
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(TurretSteering, self).__init__()
        # User defined attributes
        self.reaction_time = 0.05
        self.tank = None
        self.margin = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        self.timers = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_aiming] = []
    
    def start(self):
        super(TurretSteering, self).start()
        self.enter_Root_idle()
    
    #The actual constructor
    def __init__(self, controller, tank):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
        self.margin = tank.cannonSpeed * D1
    
    # User defined method
    def pointRight(self):
        goal_angle = self.tank.angleToDest(self.target)
        diff = (self.tank.cannonAngle - goal_angle) % D360
        if diff >= self.margin and diff <= math.pi:
            return True
        return False
        
    # User defined method
    def pointLeft(self):
        goal_angle = self.tank.angleToDest(self.target)
        diff = (goal_angle - self.tank.cannonAngle) % D360
        if diff >= self.margin and diff <= math.pi:
            return True
        return False
        
    # User defined method
    def pointCorrect(self):
        goal_angle = self.tank.angleToDest(self.target)
        diff = math.fabs(goal_angle - self.tank.cannonAngle)
        if diff < self.margin or diff > (D360- self.margin):
            return True
        return False
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_aiming(self):
        self.current_state[self.Root].append(self.Root_aiming)
    
    def exit_Root_aiming(self):
        if self.Root_aiming_adjust in self.current_state[self.Root_aiming] :
            self.exit_Root_aiming_adjust()
        if self.Root_aiming_wait in self.current_state[self.Root_aiming] :
            self.exit_Root_aiming_wait()
        self.current_state[self.Root] = []
    
    def enter_Root_idle(self):
        self.current_state[self.Root].append(self.Root_idle)
    
    def exit_Root_idle(self):
        self.current_state[self.Root] = []
    
    def enter_Root_aiming_adjust(self):
        self.current_state[self.Root_aiming].append(self.Root_aiming_adjust)
    
    def exit_Root_aiming_adjust(self):
        self.current_state[self.Root_aiming] = []
    
    def enter_Root_aiming_wait(self):
        self.timers[0] = self.reaction_time
        self.current_state[self.Root_aiming].append(self.Root_aiming_wait)
    
    def exit_Root_aiming_wait(self):
        self.timers.pop(0, None)
        self.current_state[self.Root_aiming] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_aiming(self):
        self.enter_Root_aiming()
        self.enter_Root_aiming_adjust()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_idle:
                catched = self.transition_Root_idle(event)
            elif self.current_state[self.Root][0] == self.Root_aiming:
                catched = self.transition_Root_aiming(event)
        return catched
    
    def transition_Root_idle(self, event) :
        catched = False
        enableds = []
        if event.name == "aim_at" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_idle. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                target = parameters[0]
                self.exit_Root_idle()
                self.target = target
                self.enterDefault_Root_aiming()
            catched = True
        
        return catched
    
    def transition_Root_aiming(self, event) :
        catched = False
        enableds = []
        if event.name == "stop_aiming" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "aim_at" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_aiming. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_aiming()
                send_event = Event("stop_turning", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "turret_control" , send_event]))
                self.enter_Root_idle()
            elif enabled == 2 :
                parameters = event.getParameters()
                target = parameters[0]
                self.exit_Root_aiming()
                self.target = target
                self.enterDefault_Root_aiming()
            catched = True
        
        if not catched :
            if self.current_state[self.Root_aiming][0] == self.Root_aiming_adjust:
                catched = self.transition_Root_aiming_adjust(event)
            elif self.current_state[self.Root_aiming][0] == self.Root_aiming_wait:
                catched = self.transition_Root_aiming_wait(event)
        return catched
    
    def transition_Root_aiming_adjust(self, event) :
        catched = False
        enableds = []
        if self.pointRight() :
            enableds.append(1)
        
        if self.pointLeft() :
            enableds.append(2)
        
        if self.pointCorrect() :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_aiming_adjust. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_aiming_adjust()
                send_event = Event("turn_right", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "turret_control" , send_event]))
                self.enter_Root_aiming_wait()
            elif enabled == 2 :
                self.exit_Root_aiming_adjust()
                send_event = Event("turn_left", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "turret_control" , send_event]))
                self.enter_Root_aiming_wait()
            elif enabled == 3 :
                self.exit_Root_aiming_adjust()
                send_event = Event("stop_turning", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "turret_control" , send_event]))
                send_event = Event("ready_to_shoot", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, "attack_planner" , send_event]))
                self.enter_Root_aiming_wait()
            catched = True
        
        return catched
    
    def transition_Root_aiming_wait(self, event) :
        catched = False
        enableds = []
        if event.name == "_0after" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_aiming_wait. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_aiming_wait()
                self.enter_Root_aiming_adjust()
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
    

class MotorControl(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_control = 1
    Root_control_left_right = 2
    Root_control_forward_backward = 3
    Root_control_left_right_stop = 4
    Root_control_left_right_going_forward = 5
    Root_control_left_right_going_backward = 6
    Root_control_forward_backward_straight = 7
    Root_control_forward_backward_turning_left = 8
    Root_control_forward_backward_turning_right = 9
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(MotorControl, self).__init__()
        # User defined attributes
        self.tank = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_control] = []
        self.current_state[self.Root_control_left_right] = []
        self.current_state[self.Root_control_forward_backward] = []
    
    def start(self):
        super(MotorControl, self).start()
        self.enterDefault_Root_control()
    
    #The actual constructor
    def __init__(self, controller, tank):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_control(self):
        self.current_state[self.Root].append(self.Root_control)
    
    def exit_Root_control(self):
        self.exit_Root_control_left_right()
        self.exit_Root_control_forward_backward()
        self.current_state[self.Root] = []
    
    def enter_Root_control_left_right(self):
        self.current_state[self.Root_control].append(self.Root_control_left_right)
    
    def exit_Root_control_left_right(self):
        if self.Root_control_left_right_stop in self.current_state[self.Root_control_left_right] :
            self.exit_Root_control_left_right_stop()
        if self.Root_control_left_right_going_forward in self.current_state[self.Root_control_left_right] :
            self.exit_Root_control_left_right_going_forward()
        if self.Root_control_left_right_going_backward in self.current_state[self.Root_control_left_right] :
            self.exit_Root_control_left_right_going_backward()
        self.current_state[self.Root_control] = []
    
    def enter_Root_control_forward_backward(self):
        self.current_state[self.Root_control].append(self.Root_control_forward_backward)
    
    def exit_Root_control_forward_backward(self):
        if self.Root_control_forward_backward_straight in self.current_state[self.Root_control_forward_backward] :
            self.exit_Root_control_forward_backward_straight()
        if self.Root_control_forward_backward_turning_left in self.current_state[self.Root_control_forward_backward] :
            self.exit_Root_control_forward_backward_turning_left()
        if self.Root_control_forward_backward_turning_right in self.current_state[self.Root_control_forward_backward] :
            self.exit_Root_control_forward_backward_turning_right()
        self.current_state[self.Root_control] = []
    
    def enter_Root_control_left_right_stop(self):
        self.current_state[self.Root_control_left_right].append(self.Root_control_left_right_stop)
    
    def exit_Root_control_left_right_stop(self):
        self.current_state[self.Root_control_left_right] = []
    
    def enter_Root_control_left_right_going_forward(self):
        self.current_state[self.Root_control_left_right].append(self.Root_control_left_right_going_forward)
    
    def exit_Root_control_left_right_going_forward(self):
        self.current_state[self.Root_control_left_right] = []
    
    def enter_Root_control_left_right_going_backward(self):
        self.current_state[self.Root_control_left_right].append(self.Root_control_left_right_going_backward)
    
    def exit_Root_control_left_right_going_backward(self):
        self.current_state[self.Root_control_left_right] = []
    
    def enter_Root_control_forward_backward_straight(self):
        self.current_state[self.Root_control_forward_backward].append(self.Root_control_forward_backward_straight)
    
    def exit_Root_control_forward_backward_straight(self):
        self.current_state[self.Root_control_forward_backward] = []
    
    def enter_Root_control_forward_backward_turning_left(self):
        self.current_state[self.Root_control_forward_backward].append(self.Root_control_forward_backward_turning_left)
    
    def exit_Root_control_forward_backward_turning_left(self):
        self.current_state[self.Root_control_forward_backward] = []
    
    def enter_Root_control_forward_backward_turning_right(self):
        self.current_state[self.Root_control_forward_backward].append(self.Root_control_forward_backward_turning_right)
    
    def exit_Root_control_forward_backward_turning_right(self):
        self.current_state[self.Root_control_forward_backward] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_control(self):
        self.enter_Root_control()
        self.enterDefault_Root_control_left_right()
        self.enterDefault_Root_control_forward_backward()
    
    def enterDefault_Root_control_left_right(self):
        self.enter_Root_control_left_right()
        self.enter_Root_control_left_right_stop()
    
    def enterDefault_Root_control_forward_backward(self):
        self.enter_Root_control_forward_backward()
        self.enter_Root_control_forward_backward_straight()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_control:
                catched = self.transition_Root_control(event)
        return catched
    
    def transition_Root_control(self, event) :
        catched = False
        if not catched :
            catched = self.transition_Root_control_left_right(event) or catched
            catched = self.transition_Root_control_forward_backward(event) or catched
        return catched
    
    def transition_Root_control_left_right(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_control_left_right][0] == self.Root_control_left_right_stop:
                catched = self.transition_Root_control_left_right_stop(event)
            elif self.current_state[self.Root_control_left_right][0] == self.Root_control_left_right_going_forward:
                catched = self.transition_Root_control_left_right_going_forward(event)
            elif self.current_state[self.Root_control_left_right][0] == self.Root_control_left_right_going_backward:
                catched = self.transition_Root_control_left_right_going_backward(event)
        return catched
    
    def transition_Root_control_left_right_stop(self, event) :
        catched = False
        enableds = []
        if event.name == "forward" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "backward" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_control_left_right_stop. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_control_left_right_stop()
                self.enter_Root_control_left_right_going_forward()
            elif enabled == 2 :
                self.exit_Root_control_left_right_stop()
                self.enter_Root_control_left_right_going_backward()
            catched = True
        
        return catched
    
    def transition_Root_control_left_right_going_forward(self, event) :
        catched = False
        enableds = []
        if event.name == "stop" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "backward" and event.getPort() == "" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_control_left_right_going_forward. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_control_left_right_going_forward()
                self.enter_Root_control_left_right_stop()
            elif enabled == 2 :
                self.exit_Root_control_left_right_going_forward()
                self.enter_Root_control_left_right_going_backward()
            elif enabled == 3 :
                self.exit_Root_control_left_right_going_forward()
                self.tank.moveUp()
                self.enter_Root_control_left_right_going_forward()
            catched = True
        
        return catched
    
    def transition_Root_control_left_right_going_backward(self, event) :
        catched = False
        enableds = []
        if event.name == "stop" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "forward" and event.getPort() == "" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_control_left_right_going_backward. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_control_left_right_going_backward()
                self.enter_Root_control_left_right_stop()
            elif enabled == 2 :
                self.exit_Root_control_left_right_going_backward()
                self.enter_Root_control_left_right_going_forward()
            elif enabled == 3 :
                self.exit_Root_control_left_right_going_backward()
                self.tank.moveDown()
                self.enter_Root_control_left_right_going_backward()
            catched = True
        
        return catched
    
    def transition_Root_control_forward_backward(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_control_forward_backward][0] == self.Root_control_forward_backward_straight:
                catched = self.transition_Root_control_forward_backward_straight(event)
            elif self.current_state[self.Root_control_forward_backward][0] == self.Root_control_forward_backward_turning_left:
                catched = self.transition_Root_control_forward_backward_turning_left(event)
            elif self.current_state[self.Root_control_forward_backward][0] == self.Root_control_forward_backward_turning_right:
                catched = self.transition_Root_control_forward_backward_turning_right(event)
        return catched
    
    def transition_Root_control_forward_backward_straight(self, event) :
        catched = False
        enableds = []
        if event.name == "turn_right" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "turn_left" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_control_forward_backward_straight. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_control_forward_backward_straight()
                self.enter_Root_control_forward_backward_turning_right()
            elif enabled == 2 :
                self.exit_Root_control_forward_backward_straight()
                self.enter_Root_control_forward_backward_turning_left()
            catched = True
        
        return catched
    
    def transition_Root_control_forward_backward_turning_left(self, event) :
        catched = False
        enableds = []
        if event.name == "stop_turning" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "turn_right" and event.getPort() == "" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_control_forward_backward_turning_left. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_control_forward_backward_turning_left()
                self.enter_Root_control_forward_backward_straight()
            elif enabled == 2 :
                self.exit_Root_control_forward_backward_turning_left()
                self.enter_Root_control_forward_backward_turning_right()
            elif enabled == 3 :
                self.exit_Root_control_forward_backward_turning_left()
                self.tank.turnLeft()
                self.enter_Root_control_forward_backward_turning_left()
            catched = True
        
        return catched
    
    def transition_Root_control_forward_backward_turning_right(self, event) :
        catched = False
        enableds = []
        if event.name == "stop_turning" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "turn_left" and event.getPort() == "" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_control_forward_backward_turning_right. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_control_forward_backward_turning_right()
                self.enter_Root_control_forward_backward_straight()
            elif enabled == 2 :
                self.exit_Root_control_forward_backward_turning_right()
                self.enter_Root_control_forward_backward_turning_left()
            elif enabled == 3 :
                self.exit_Root_control_forward_backward_turning_right()
                self.tank.turnRight()
                self.enter_Root_control_forward_backward_turning_right()
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
    

class TurretControl(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_turret = 1
    Root_turret_rotation = 2
    Root_turret_shooting = 3
    Root_turret_rotation_none = 4
    Root_turret_rotation_turning_left = 5
    Root_turret_rotation_turning_right = 6
    Root_turret_shooting_polling = 7
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(TurretControl, self).__init__()
        # User defined attributes
        self.tank = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_turret] = []
        self.current_state[self.Root_turret_rotation] = []
        self.current_state[self.Root_turret_shooting] = []
    
    def start(self):
        super(TurretControl, self).start()
        self.enterDefault_Root_turret()
    
    #The actual constructor
    def __init__(self, controller, tank):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_turret(self):
        self.current_state[self.Root].append(self.Root_turret)
    
    def exit_Root_turret(self):
        self.exit_Root_turret_rotation()
        self.exit_Root_turret_shooting()
        self.current_state[self.Root] = []
    
    def enter_Root_turret_rotation(self):
        self.current_state[self.Root_turret].append(self.Root_turret_rotation)
    
    def exit_Root_turret_rotation(self):
        if self.Root_turret_rotation_none in self.current_state[self.Root_turret_rotation] :
            self.exit_Root_turret_rotation_none()
        if self.Root_turret_rotation_turning_left in self.current_state[self.Root_turret_rotation] :
            self.exit_Root_turret_rotation_turning_left()
        if self.Root_turret_rotation_turning_right in self.current_state[self.Root_turret_rotation] :
            self.exit_Root_turret_rotation_turning_right()
        self.current_state[self.Root_turret] = []
    
    def enter_Root_turret_shooting(self):
        self.current_state[self.Root_turret].append(self.Root_turret_shooting)
    
    def exit_Root_turret_shooting(self):
        if self.Root_turret_shooting_polling in self.current_state[self.Root_turret_shooting] :
            self.exit_Root_turret_shooting_polling()
        self.current_state[self.Root_turret] = []
    
    def enter_Root_turret_rotation_none(self):
        self.current_state[self.Root_turret_rotation].append(self.Root_turret_rotation_none)
    
    def exit_Root_turret_rotation_none(self):
        self.current_state[self.Root_turret_rotation] = []
    
    def enter_Root_turret_rotation_turning_left(self):
        self.current_state[self.Root_turret_rotation].append(self.Root_turret_rotation_turning_left)
    
    def exit_Root_turret_rotation_turning_left(self):
        self.current_state[self.Root_turret_rotation] = []
    
    def enter_Root_turret_rotation_turning_right(self):
        self.current_state[self.Root_turret_rotation].append(self.Root_turret_rotation_turning_right)
    
    def exit_Root_turret_rotation_turning_right(self):
        self.current_state[self.Root_turret_rotation] = []
    
    def enter_Root_turret_shooting_polling(self):
        self.current_state[self.Root_turret_shooting].append(self.Root_turret_shooting_polling)
    
    def exit_Root_turret_shooting_polling(self):
        self.current_state[self.Root_turret_shooting] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_turret(self):
        self.enter_Root_turret()
        self.enterDefault_Root_turret_rotation()
        self.enterDefault_Root_turret_shooting()
    
    def enterDefault_Root_turret_rotation(self):
        self.enter_Root_turret_rotation()
        self.enter_Root_turret_rotation_none()
    
    def enterDefault_Root_turret_shooting(self):
        self.enter_Root_turret_shooting()
        self.enter_Root_turret_shooting_polling()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_turret:
                catched = self.transition_Root_turret(event)
        return catched
    
    def transition_Root_turret(self, event) :
        catched = False
        if not catched :
            catched = self.transition_Root_turret_rotation(event) or catched
            catched = self.transition_Root_turret_shooting(event) or catched
        return catched
    
    def transition_Root_turret_rotation(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_turret_rotation][0] == self.Root_turret_rotation_none:
                catched = self.transition_Root_turret_rotation_none(event)
            elif self.current_state[self.Root_turret_rotation][0] == self.Root_turret_rotation_turning_left:
                catched = self.transition_Root_turret_rotation_turning_left(event)
            elif self.current_state[self.Root_turret_rotation][0] == self.Root_turret_rotation_turning_right:
                catched = self.transition_Root_turret_rotation_turning_right(event)
        return catched
    
    def transition_Root_turret_rotation_none(self, event) :
        catched = False
        enableds = []
        if event.name == "turn_right" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "turn_left" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_turret_rotation_none. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_turret_rotation_none()
                self.enter_Root_turret_rotation_turning_right()
            elif enabled == 2 :
                self.exit_Root_turret_rotation_none()
                self.enter_Root_turret_rotation_turning_left()
            catched = True
        
        return catched
    
    def transition_Root_turret_rotation_turning_left(self, event) :
        catched = False
        enableds = []
        if event.name == "stop_turning" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "turn_right" and event.getPort() == "" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_turret_rotation_turning_left. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_turret_rotation_turning_left()
                self.enter_Root_turret_rotation_none()
            elif enabled == 2 :
                self.exit_Root_turret_rotation_turning_left()
                self.enter_Root_turret_rotation_turning_right()
            elif enabled == 3 :
                self.exit_Root_turret_rotation_turning_left()
                self.tank.turnCannonLeft()
                self.enter_Root_turret_rotation_turning_left()
            catched = True
        
        return catched
    
    def transition_Root_turret_rotation_turning_right(self, event) :
        catched = False
        enableds = []
        if event.name == "stop_turning" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "turn_left" and event.getPort() == "" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_turret_rotation_turning_right. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_turret_rotation_turning_right()
                self.enter_Root_turret_rotation_none()
            elif enabled == 2 :
                self.exit_Root_turret_rotation_turning_right()
                self.enter_Root_turret_rotation_turning_left()
            elif enabled == 3 :
                self.exit_Root_turret_rotation_turning_right()
                self.tank.turnCannonRight()
                self.enter_Root_turret_rotation_turning_right()
            catched = True
        
        return catched
    
    def transition_Root_turret_shooting(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_turret_shooting][0] == self.Root_turret_shooting_polling:
                catched = self.transition_Root_turret_shooting_polling(event)
        return catched
    
    def transition_Root_turret_shooting_polling(self, event) :
        catched = False
        enableds = []
        if event.name == "shoot" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_turret_shooting_polling. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_turret_shooting_polling()
                self.tank.shoot()
                self.enter_Root_turret_shooting_polling()
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
            associations.append(Association("radar", "Radar", 1, 1))
            associations.append(Association("enemy_tracker", "EnemyTracker", 1, 1))
            associations.append(Association("pilot_strategy", "PilotStrategy", 1, 1))
            associations.append(Association("explore_planner", "ExplorePlanner", 1, 1))
            associations.append(Association("attack_planner", "AttackPlanner", 1, 1))
            associations.append(Association("path_finder", "PathFinder", 1, 1))
            associations.append(Association("steering", "Steering", 1, 1))
            associations.append(Association("turret_steering", "TurretSteering", 1, 1))
            associations.append(Association("motor_control", "MotorControl", 1, 1))
            associations.append(Association("turret_control", "TurretControl", 1, 1))
        elif class_name == "Radar" :
            instance =  Radar(self.controller, *construct_params)
            associations.append(Association("enemy_tracker", "EnemyTracker", 1, 1))
            associations.append(Association("pilot_strategy", "PilotStrategy", 1, 1))
        elif class_name == "EnemyTracker" :
            instance =  EnemyTracker(self.controller, *construct_params)
            associations.append(Association("pilot_strategy", "PilotStrategy", 1, 1))
            associations.append(Association("attack_planner", "AttackPlanner", 1, 1))
        elif class_name == "PilotStrategy" :
            instance =  PilotStrategy(self.controller, *construct_params)
            associations.append(Association("explore_planner", "ExplorePlanner", 1, 1))
            associations.append(Association("attack_planner", "AttackPlanner", 1, 1))
        elif class_name == "ExplorePlanner" :
            instance =  ExplorePlanner(self.controller, *construct_params)
            associations.append(Association("path_finder", "PathFinder", 1, 1))
        elif class_name == "AttackPlanner" :
            instance =  AttackPlanner(self.controller, *construct_params)
            associations.append(Association("turret_steering", "TurretSteering", 1, 1))
            associations.append(Association("path_finder", "PathFinder", 1, 1))
            associations.append(Association("turret_control", "TurretControl", 1, 1))
        elif class_name == "PathFinder" :
            instance =  PathFinder(self.controller, *construct_params)
            associations.append(Association("steering", "Steering", 1, 1))
        elif class_name == "Steering" :
            instance =  Steering(self.controller, *construct_params)
            associations.append(Association("motor_control", "MotorControl", 1, 1))
            associations.append(Association("path_finder", "PathFinder", 1, 1))
        elif class_name == "TurretSteering" :
            instance =  TurretSteering(self.controller, *construct_params)
            associations.append(Association("turret_control", "TurretControl", 1, 1))
            associations.append(Association("attack_planner", "AttackPlanner", 1, 1))
        elif class_name == "MotorControl" :
            instance =  MotorControl(self.controller, *construct_params)
        elif class_name == "TurretControl" :
            instance =  TurretControl(self.controller, *construct_params)
        if instance:
            return InstanceWrapper(instance, associations)
        else :
            return None

from python_runtime.statecharts_core import GameLoopControllerBase
class Controller(GameLoopControllerBase):
    def __init__(self, tank, keep_running = True):
        super(Controller, self).__init__(ObjectManager(self), keep_running)
        self.addInputPort("engine")
        self.object_manager.createInstance("Main", [tank])
        
def main():
    controller = Controller()
    controller.start()

if __name__ == "__main__":
    main()
