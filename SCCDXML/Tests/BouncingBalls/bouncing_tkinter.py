# Statechart compiler by Glenn De Jonghe
#
# Date:   Thu Jul 31 16:54:14 2014

# Model author: Simon Van Mierlo
# Model name:   Bouncing Balls - Tkinter Version 
# Model description:
"""
    Tkinter frame with bouncing balls in it.
"""

from python_runtime.statecharts_core import ObjectManagerBase, Event, InstanceWrapper, RuntimeClassBase, Association
import time
import random
import Tkinter as tk
from mvk_widget import MvKWidget


class MainApp(tk.Tk, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_running = 1
    Root_running_root = 2
    Root_running_root_main_behaviour = 3
    Root_running_root_cd_behaviour = 4
    Root_running_root_main_behaviour_initializing = 5
    Root_running_root_main_behaviour_running = 6
    Root_running_root_cd_behaviour_waiting = 7
    Root_running_root_cd_behaviour_creating = 8
    Root_running_root_cd_behaviour_check_nr_of_fields = 9
    Root_running_stopped = 10
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_running] = []
        self.current_state[self.Root_running_root] = []
        self.current_state[self.Root_running_root_main_behaviour] = []
        self.current_state[self.Root_running_root_cd_behaviour] = []
    
    def start(self):
        super(MainApp, self).start()
        self.enterDefault_Root_running()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        tk.Tk.__init__(self)
        self.fixed_update_time = 20
        self.update_self()
        self.withdraw()
        self.nr_of_fields = 0
    
    # User defined method
    def update_self(self):
        self.controller.update(self.fixed_update_time / 1000.0)
        self.schedule_time = time.time()
        self.scheduled_update_id = self.after(self.fixed_update_time, self.update_self)
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_running(self):
        self.current_state[self.Root].append(self.Root_running)
    
    def exit_Root_running(self):
        if self.Root_running_root in self.current_state[self.Root_running] :
            self.exit_Root_running_root()
        if self.Root_running_stopped in self.current_state[self.Root_running] :
            self.exit_Root_running_stopped()
        self.current_state[self.Root] = []
    
    def enter_Root_running_root(self):
        self.current_state[self.Root_running].append(self.Root_running_root)
    
    def exit_Root_running_root(self):
        self.exit_Root_running_root_main_behaviour()
        self.exit_Root_running_root_cd_behaviour()
        self.current_state[self.Root_running] = []
    
    def enter_Root_running_root_main_behaviour(self):
        self.current_state[self.Root_running_root].append(self.Root_running_root_main_behaviour)
    
    def exit_Root_running_root_main_behaviour(self):
        if self.Root_running_root_main_behaviour_initializing in self.current_state[self.Root_running_root_main_behaviour] :
            self.exit_Root_running_root_main_behaviour_initializing()
        if self.Root_running_root_main_behaviour_running in self.current_state[self.Root_running_root_main_behaviour] :
            self.exit_Root_running_root_main_behaviour_running()
        self.current_state[self.Root_running_root] = []
    
    def enter_Root_running_root_cd_behaviour(self):
        self.current_state[self.Root_running_root].append(self.Root_running_root_cd_behaviour)
    
    def exit_Root_running_root_cd_behaviour(self):
        if self.Root_running_root_cd_behaviour_waiting in self.current_state[self.Root_running_root_cd_behaviour] :
            self.exit_Root_running_root_cd_behaviour_waiting()
        if self.Root_running_root_cd_behaviour_creating in self.current_state[self.Root_running_root_cd_behaviour] :
            self.exit_Root_running_root_cd_behaviour_creating()
        if self.Root_running_root_cd_behaviour_check_nr_of_fields in self.current_state[self.Root_running_root_cd_behaviour] :
            self.exit_Root_running_root_cd_behaviour_check_nr_of_fields()
        self.current_state[self.Root_running_root] = []
    
    def enter_Root_running_root_main_behaviour_initializing(self):
        self.current_state[self.Root_running_root_main_behaviour].append(self.Root_running_root_main_behaviour_initializing)
    
    def exit_Root_running_root_main_behaviour_initializing(self):
        self.current_state[self.Root_running_root_main_behaviour] = []
    
    def enter_Root_running_root_main_behaviour_running(self):
        self.current_state[self.Root_running_root_main_behaviour].append(self.Root_running_root_main_behaviour_running)
    
    def exit_Root_running_root_main_behaviour_running(self):
        self.current_state[self.Root_running_root_main_behaviour] = []
    
    def enter_Root_running_root_cd_behaviour_waiting(self):
        self.current_state[self.Root_running_root_cd_behaviour].append(self.Root_running_root_cd_behaviour_waiting)
    
    def exit_Root_running_root_cd_behaviour_waiting(self):
        self.current_state[self.Root_running_root_cd_behaviour] = []
    
    def enter_Root_running_root_cd_behaviour_creating(self):
        self.current_state[self.Root_running_root_cd_behaviour].append(self.Root_running_root_cd_behaviour_creating)
    
    def exit_Root_running_root_cd_behaviour_creating(self):
        self.current_state[self.Root_running_root_cd_behaviour] = []
    
    def enter_Root_running_root_cd_behaviour_check_nr_of_fields(self):
        self.current_state[self.Root_running_root_cd_behaviour].append(self.Root_running_root_cd_behaviour_check_nr_of_fields)
    
    def exit_Root_running_root_cd_behaviour_check_nr_of_fields(self):
        self.current_state[self.Root_running_root_cd_behaviour] = []
    
    def enter_Root_running_stopped(self):
        self.current_state[self.Root_running].append(self.Root_running_stopped)
    
    def exit_Root_running_stopped(self):
        self.current_state[self.Root_running] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_running(self):
        self.enter_Root_running()
        self.enterDefault_Root_running_root()
    
    def enterDefault_Root_running_root(self):
        self.enter_Root_running_root()
        self.enterDefault_Root_running_root_main_behaviour()
        self.enterDefault_Root_running_root_cd_behaviour()
    
    def enterDefault_Root_running_root_main_behaviour(self):
        self.enter_Root_running_root_main_behaviour()
        self.enter_Root_running_root_main_behaviour_initializing()
    
    def enterDefault_Root_running_root_cd_behaviour(self):
        self.enter_Root_running_root_cd_behaviour()
        self.enter_Root_running_root_cd_behaviour_waiting()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_running:
                catched = self.transition_Root_running(event)
        return catched
    
    def transition_Root_running(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_running][0] == self.Root_running_root:
                catched = self.transition_Root_running_root(event)
            elif self.current_state[self.Root_running][0] == self.Root_running_stopped:
                catched = self.transition_Root_running_stopped(event)
        return catched
    
    def transition_Root_running_root(self, event) :
        catched = False
        if not catched :
            catched = self.transition_Root_running_root_main_behaviour(event) or catched
            catched = self.transition_Root_running_root_cd_behaviour(event) or catched
        return catched
    
    def transition_Root_running_root_main_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_running_root_main_behaviour][0] == self.Root_running_root_main_behaviour_initializing:
                catched = self.transition_Root_running_root_main_behaviour_initializing(event)
            elif self.current_state[self.Root_running_root_main_behaviour][0] == self.Root_running_root_main_behaviour_running:
                catched = self.transition_Root_running_root_main_behaviour_running(event)
        return catched
    
    def transition_Root_running_root_main_behaviour_initializing(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_running_root_main_behaviour_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_running_root_main_behaviour_initializing()
                self.addEvent(Event("create_field", parameters = []))
                self.enter_Root_running_root_main_behaviour_running()
            catched = True
        
        return catched
    
    def transition_Root_running_root_main_behaviour_running(self, event) :
        catched = False
        enableds = []
        if event.name == "button_pressed" and event.getPort() == "" :
            parameters = event.getParameters()
            event_name = parameters[0]
            if event_name == "create_new_field" :
                enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_running_root_main_behaviour_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                event_name = parameters[0]
                self.exit_Root_running_root_main_behaviour_running()
                self.addEvent(Event("create_field", parameters = []))
                self.enter_Root_running_root_main_behaviour_running()
            catched = True
        
        return catched
    
    def transition_Root_running_root_cd_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_running_root_cd_behaviour][0] == self.Root_running_root_cd_behaviour_waiting:
                catched = self.transition_Root_running_root_cd_behaviour_waiting(event)
            elif self.current_state[self.Root_running_root_cd_behaviour][0] == self.Root_running_root_cd_behaviour_creating:
                catched = self.transition_Root_running_root_cd_behaviour_creating(event)
            elif self.current_state[self.Root_running_root_cd_behaviour][0] == self.Root_running_root_cd_behaviour_check_nr_of_fields:
                catched = self.transition_Root_running_root_cd_behaviour_check_nr_of_fields(event)
        return catched
    
    def transition_Root_running_root_cd_behaviour_waiting(self, event) :
        catched = False
        enableds = []
        if event.name == "create_field" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "delete_field" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_running_root_cd_behaviour_waiting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_running_root_cd_behaviour_waiting()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "fields"]))
                self.enter_Root_running_root_cd_behaviour_creating()
            elif enabled == 2 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_running_root_cd_behaviour_waiting()
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, association_name]))
                self.nr_of_fields -= 1
                self.enter_Root_running_root_cd_behaviour_check_nr_of_fields()
            catched = True
        
        return catched
    
    def transition_Root_running_root_cd_behaviour_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_running_root_cd_behaviour_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_running_root_cd_behaviour_creating()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.nr_of_fields += 1
                self.enter_Root_running_root_cd_behaviour_waiting()
            catched = True
        
        return catched
    
    def transition_Root_running_root_cd_behaviour_check_nr_of_fields(self, event) :
        catched = False
        enableds = []
        if self.nr_of_fields == 0 :
            enableds.append(1)
        
        if self.nr_of_fields != 0 :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_running_root_cd_behaviour_check_nr_of_fields. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_running_root()
                self.destroy()
                self.enter_Root_running_stopped()
            elif enabled == 2 :
                self.exit_Root_running_root_cd_behaviour_check_nr_of_fields()
                self.enter_Root_running_root_cd_behaviour_waiting()
            catched = True
        
        return catched
    
    def transition_Root_running_stopped(self, event) :
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
    

class Field(MvKWidget, tk.Toplevel, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_root = 1
    Root_root_running = 2
    Root_root_running_main_behaviour = 3
    Root_root_running_deleting_behaviour = 4
    Root_root_running_child_behaviour = 5
    Root_root_waiting = 6
    Root_root_initializing = 7
    Root_root_creating = 8
    Root_root_packing = 9
    Root_root_running_main_behaviour_running = 10
    Root_root_running_main_behaviour_creating = 11
    Root_root_running_deleting_behaviour_running = 12
    Root_root_running_child_behaviour_listening = 13
    Root_root_deleting = 14
    Root_root_deleted = 15
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        self.timers = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_root] = []
        self.current_state[self.Root_root_running] = []
        self.current_state[self.Root_root_running_main_behaviour] = []
        self.current_state[self.Root_root_running_deleting_behaviour] = []
        self.current_state[self.Root_root_running_child_behaviour] = []
    
    def start(self):
        super(Field, self).start()
        self.enterDefault_Root_root()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        tk.Toplevel.__init__(self)
        self.title('BouncingBalls')
        
        CANVAS_SIZE_TUPLE = (0, 0, self.winfo_screenwidth() * 2, self.winfo_screenheight() * 2)
        self.c = tk.Canvas(self, relief=tk.RIDGE, scrollregion=CANVAS_SIZE_TUPLE)
        
        MvKWidget.__init__(self, self.controller, self.c)
    
    # User defined destructor
    def __del__(self):
        self.destroy()
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_root(self):
        self.current_state[self.Root].append(self.Root_root)
    
    def exit_Root_root(self):
        if self.Root_root_waiting in self.current_state[self.Root_root] :
            self.exit_Root_root_waiting()
        if self.Root_root_initializing in self.current_state[self.Root_root] :
            self.exit_Root_root_initializing()
        if self.Root_root_creating in self.current_state[self.Root_root] :
            self.exit_Root_root_creating()
        if self.Root_root_packing in self.current_state[self.Root_root] :
            self.exit_Root_root_packing()
        if self.Root_root_running in self.current_state[self.Root_root] :
            self.exit_Root_root_running()
        if self.Root_root_deleting in self.current_state[self.Root_root] :
            self.exit_Root_root_deleting()
        if self.Root_root_deleted in self.current_state[self.Root_root] :
            self.exit_Root_root_deleted()
        self.current_state[self.Root] = []
    
    def enter_Root_root_running(self):
        self.current_state[self.Root_root].append(self.Root_root_running)
    
    def exit_Root_root_running(self):
        self.exit_Root_root_running_main_behaviour()
        self.exit_Root_root_running_deleting_behaviour()
        self.exit_Root_root_running_child_behaviour()
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_running_main_behaviour(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_main_behaviour)
    
    def exit_Root_root_running_main_behaviour(self):
        if self.Root_root_running_main_behaviour_running in self.current_state[self.Root_root_running_main_behaviour] :
            self.exit_Root_root_running_main_behaviour_running()
        if self.Root_root_running_main_behaviour_creating in self.current_state[self.Root_root_running_main_behaviour] :
            self.exit_Root_root_running_main_behaviour_creating()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_running_deleting_behaviour(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_deleting_behaviour)
    
    def exit_Root_root_running_deleting_behaviour(self):
        if self.Root_root_running_deleting_behaviour_running in self.current_state[self.Root_root_running_deleting_behaviour] :
            self.exit_Root_root_running_deleting_behaviour_running()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_running_child_behaviour(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_child_behaviour)
    
    def exit_Root_root_running_child_behaviour(self):
        if self.Root_root_running_child_behaviour_listening in self.current_state[self.Root_root_running_child_behaviour] :
            self.exit_Root_root_running_child_behaviour_listening()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_waiting(self):
        self.current_state[self.Root_root].append(self.Root_root_waiting)
    
    def exit_Root_root_waiting(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_initializing(self):
        self.current_state[self.Root_root].append(self.Root_root_initializing)
    
    def exit_Root_root_initializing(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_creating(self):
        self.current_state[self.Root_root].append(self.Root_root_creating)
    
    def exit_Root_root_creating(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_packing(self):
        self.current_state[self.Root_root].append(self.Root_root_packing)
    
    def exit_Root_root_packing(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_running_main_behaviour_running(self):
        self.current_state[self.Root_root_running_main_behaviour].append(self.Root_root_running_main_behaviour_running)
    
    def exit_Root_root_running_main_behaviour_running(self):
        self.current_state[self.Root_root_running_main_behaviour] = []
    
    def enter_Root_root_running_main_behaviour_creating(self):
        self.current_state[self.Root_root_running_main_behaviour].append(self.Root_root_running_main_behaviour_creating)
    
    def exit_Root_root_running_main_behaviour_creating(self):
        self.current_state[self.Root_root_running_main_behaviour] = []
    
    def enter_Root_root_running_deleting_behaviour_running(self):
        self.current_state[self.Root_root_running_deleting_behaviour].append(self.Root_root_running_deleting_behaviour_running)
    
    def exit_Root_root_running_deleting_behaviour_running(self):
        self.current_state[self.Root_root_running_deleting_behaviour] = []
    
    def enter_Root_root_running_child_behaviour_listening(self):
        self.current_state[self.Root_root_running_child_behaviour].append(self.Root_root_running_child_behaviour_listening)
    
    def exit_Root_root_running_child_behaviour_listening(self):
        self.current_state[self.Root_root_running_child_behaviour] = []
    
    def enter_Root_root_deleting(self):
        self.timers[0] = 0.05
        self.current_state[self.Root_root].append(self.Root_root_deleting)
    
    def exit_Root_root_deleting(self):
        self.timers.pop(0, None)
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_deleted(self):
        self.current_state[self.Root_root].append(self.Root_root_deleted)
    
    def exit_Root_root_deleted(self):
        self.current_state[self.Root_root] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_root(self):
        self.enter_Root_root()
        self.enter_Root_root_waiting()
    
    def enterDefault_Root_root_running(self):
        self.enter_Root_root_running()
        self.enterDefault_Root_root_running_main_behaviour()
        self.enterDefault_Root_root_running_deleting_behaviour()
        self.enterDefault_Root_root_running_child_behaviour()
    
    def enterDefault_Root_root_running_main_behaviour(self):
        self.enter_Root_root_running_main_behaviour()
        self.enter_Root_root_running_main_behaviour_running()
    
    def enterDefault_Root_root_running_deleting_behaviour(self):
        self.enter_Root_root_running_deleting_behaviour()
        self.enter_Root_root_running_deleting_behaviour_running()
    
    def enterDefault_Root_root_running_child_behaviour(self):
        self.enter_Root_root_running_child_behaviour()
        self.enter_Root_root_running_child_behaviour_listening()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_root:
                catched = self.transition_Root_root(event)
        return catched
    
    def transition_Root_root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root][0] == self.Root_root_waiting:
                catched = self.transition_Root_root_waiting(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_initializing:
                catched = self.transition_Root_root_initializing(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_creating:
                catched = self.transition_Root_root_creating(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_packing:
                catched = self.transition_Root_root_packing(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_running:
                catched = self.transition_Root_root_running(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_deleting:
                catched = self.transition_Root_root_deleting(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_deleted:
                catched = self.transition_Root_root_deleted(event)
        return catched
    
    def transition_Root_root_waiting(self, event) :
        catched = False
        enableds = []
        if event.name == "set_association_name" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_waiting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_waiting()
                self.association_name = association_name
                self.enter_Root_root_initializing()
            catched = True
        
        return catched
    
    def transition_Root_root_initializing(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_initializing()
                print 'blaaat'
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "buttons",self,'create_new_field','Spawn New Window']))
                self.enter_Root_root_creating()
            catched = True
        
        return catched
    
    def transition_Root_root_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_creating()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                self.enter_Root_root_packing()
            catched = True
        
        return catched
    
    def transition_Root_root_packing(self, event) :
        catched = False
        enableds = []
        if event.name == "button_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_packing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                button = parameters[0]
                self.exit_Root_root_packing()
                button.pack(expand=False, fill=tk.X, side=tk.TOP)
                self.c.focus_force()
                self.c.pack(expand=True, fill=tk.BOTH)
                self.enterDefault_Root_root_running()
            catched = True
        
        return catched
    
    def transition_Root_root_running(self, event) :
        catched = False
        enableds = []
        if event.name == "window-close" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_root_running()
                send_event = Event("delete_self", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'balls' , send_event]))
                self.enter_Root_root_deleting()
            catched = True
        
        if not catched :
            catched = self.transition_Root_root_running_main_behaviour(event) or catched
            catched = self.transition_Root_root_running_deleting_behaviour(event) or catched
            catched = self.transition_Root_root_running_child_behaviour(event) or catched
        return catched
    
    def transition_Root_root_running_main_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_main_behaviour][0] == self.Root_root_running_main_behaviour_running:
                catched = self.transition_Root_root_running_main_behaviour_running(event)
            elif self.current_state[self.Root_root_running_main_behaviour][0] == self.Root_root_running_main_behaviour_creating:
                catched = self.transition_Root_root_running_main_behaviour_creating(event)
        return catched
    
    def transition_Root_root_running_main_behaviour_running(self, event) :
        catched = False
        enableds = []
        if event.name == "right-click" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_root_running_main_behaviour_running()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "balls",self.c,self.last_x,self.last_y]))
                self.enter_Root_root_running_main_behaviour_creating()
            catched = True
        
        return catched
    
    def transition_Root_root_running_main_behaviour_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_main_behaviour_creating()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_root_running_main_behaviour_running()
            catched = True
        
        return catched
    
    def transition_Root_root_running_deleting_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_deleting_behaviour][0] == self.Root_root_running_deleting_behaviour_running:
                catched = self.transition_Root_root_running_deleting_behaviour_running(event)
        return catched
    
    def transition_Root_root_running_deleting_behaviour_running(self, event) :
        catched = False
        enableds = []
        if event.name == "delete_ball" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_deleting_behaviour_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_deleting_behaviour_running()
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, association_name]))
                self.enter_Root_root_running_deleting_behaviour_running()
            catched = True
        
        return catched
    
    def transition_Root_root_running_child_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_child_behaviour][0] == self.Root_root_running_child_behaviour_listening:
                catched = self.transition_Root_root_running_child_behaviour_listening(event)
        return catched
    
    def transition_Root_root_running_child_behaviour_listening(self, event) :
        catched = False
        enableds = []
        if event.name == "button_pressed" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_child_behaviour_listening. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                event_name = parameters[0]
                self.exit_Root_root_running_child_behaviour_listening()
                send_event = Event("button_pressed", parameters = [event_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_running_child_behaviour_listening()
            catched = True
        
        return catched
    
    def transition_Root_root_deleting(self, event) :
        catched = False
        enableds = []
        if event.name == "_0after" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_deleting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_deleting()
                send_event = Event("delete_field", parameters = [self.association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_deleted()
            catched = True
        
        return catched
    
    def transition_Root_root_deleted(self, event) :
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
    

class Button(tk.Button, MvKWidget, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_initializing = 1
    Root_running = 2
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
    
    def start(self):
        super(Button, self).start()
        self.enter_Root_initializing()
    
    #The actual constructor
    def __init__(self, controller, parent, event_name, button_text):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        tk.Button.__init__(self, parent, text=button_text)
        MvKWidget.__init__(self, self.controller)
        self.event_name = event_name
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_initializing(self):
        self.current_state[self.Root].append(self.Root_initializing)
    
    def exit_Root_initializing(self):
        self.current_state[self.Root] = []
    
    def enter_Root_running(self):
        self.current_state[self.Root].append(self.Root_running)
    
    def exit_Root_running(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_initializing:
                catched = self.transition_Root_initializing(event)
            elif self.current_state[self.Root][0] == self.Root_running:
                catched = self.transition_Root_running(event)
        return catched
    
    def transition_Root_initializing(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_initializing()
                send_event = Event("button_created", parameters = [self])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_running()
            catched = True
        
        return catched
    
    def transition_Root_running(self, event) :
        catched = False
        enableds = []
        if event.name == "left-click" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_running()
                send_event = Event("button_pressed", parameters = [self.event_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_running()
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
    

class Ball(MvKWidget, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_main_behaviour = 1
    Root_main_behaviour_initializing = 2
    Root_main_behaviour_bouncing = 3
    Root_main_behaviour_dragging = 4
    Root_main_behaviour_selected = 5
    Root_deleted = 6
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        # User defined attributes
        self.canvas = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        self.timers = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_main_behaviour] = []
    
    def start(self):
        super(Ball, self).start()
        self.enterDefault_Root_main_behaviour()
    
    #The actual constructor
    def __init__(self, controller, canvas, x, y):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.canvas = canvas
        self.r = 15.0
        self.smooth = 0.4 # value between 0 and 1
        self.vel = {'x': random.random() * 2.0 - 1.0, 'y': random.random() * 2.0 - 1.0}
        self.id = self.canvas.create_oval(x, y, x + (self.r * 2), y + (self.r * 2), fill="black")
        MvKWidget.__init__(self, self.controller, self.canvas, self.id)
    
    # User defined destructor
    def __del__(self):
        self.canvas.delete(self.id)
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_main_behaviour(self):
        self.current_state[self.Root].append(self.Root_main_behaviour)
    
    def exit_Root_main_behaviour(self):
        if self.Root_main_behaviour_initializing in self.current_state[self.Root_main_behaviour] :
            self.exit_Root_main_behaviour_initializing()
        if self.Root_main_behaviour_bouncing in self.current_state[self.Root_main_behaviour] :
            self.exit_Root_main_behaviour_bouncing()
        if self.Root_main_behaviour_dragging in self.current_state[self.Root_main_behaviour] :
            self.exit_Root_main_behaviour_dragging()
        if self.Root_main_behaviour_selected in self.current_state[self.Root_main_behaviour] :
            self.exit_Root_main_behaviour_selected()
        self.current_state[self.Root] = []
    
    def enter_Root_main_behaviour_initializing(self):
        self.current_state[self.Root_main_behaviour].append(self.Root_main_behaviour_initializing)
    
    def exit_Root_main_behaviour_initializing(self):
        self.current_state[self.Root_main_behaviour] = []
    
    def enter_Root_main_behaviour_bouncing(self):
        self.timers[0] = 0.01
        self.current_state[self.Root_main_behaviour].append(self.Root_main_behaviour_bouncing)
    
    def exit_Root_main_behaviour_bouncing(self):
        self.timers.pop(0, None)
        self.current_state[self.Root_main_behaviour] = []
    
    def enter_Root_main_behaviour_dragging(self):
        self.current_state[self.Root_main_behaviour].append(self.Root_main_behaviour_dragging)
    
    def exit_Root_main_behaviour_dragging(self):
        self.current_state[self.Root_main_behaviour] = []
    
    def enter_Root_main_behaviour_selected(self):
        self.current_state[self.Root_main_behaviour].append(self.Root_main_behaviour_selected)
    
    def exit_Root_main_behaviour_selected(self):
        self.current_state[self.Root_main_behaviour] = []
    
    def enter_Root_deleted(self):
        self.current_state[self.Root].append(self.Root_deleted)
    
    def exit_Root_deleted(self):
        self.current_state[self.Root] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_main_behaviour(self):
        self.enter_Root_main_behaviour()
        self.enter_Root_main_behaviour_initializing()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_main_behaviour:
                catched = self.transition_Root_main_behaviour(event)
            elif self.current_state[self.Root][0] == self.Root_deleted:
                catched = self.transition_Root_deleted(event)
        return catched
    
    def transition_Root_main_behaviour(self, event) :
        catched = False
        enableds = []
        if event.name == "delete_self" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_main_behaviour. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_main_behaviour()
                send_event = Event("delete_ball", parameters = [self.association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_deleted()
            catched = True
        
        if not catched :
            if self.current_state[self.Root_main_behaviour][0] == self.Root_main_behaviour_initializing:
                catched = self.transition_Root_main_behaviour_initializing(event)
            elif self.current_state[self.Root_main_behaviour][0] == self.Root_main_behaviour_bouncing:
                catched = self.transition_Root_main_behaviour_bouncing(event)
            elif self.current_state[self.Root_main_behaviour][0] == self.Root_main_behaviour_dragging:
                catched = self.transition_Root_main_behaviour_dragging(event)
            elif self.current_state[self.Root_main_behaviour][0] == self.Root_main_behaviour_selected:
                catched = self.transition_Root_main_behaviour_selected(event)
        return catched
    
    def transition_Root_main_behaviour_initializing(self, event) :
        catched = False
        enableds = []
        if event.name == "set_association_name" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_main_behaviour_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_main_behaviour_initializing()
                self.association_name = association_name
                self.enter_Root_main_behaviour_bouncing()
            catched = True
        
        return catched
    
    def transition_Root_main_behaviour_bouncing(self, event) :
        catched = False
        enableds = []
        if event.name == "_0after" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "left-click" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_main_behaviour_bouncing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_main_behaviour_bouncing()
                pos = self.canvas.coords(self.id)
                x = self.canvas.canvasx(pos[0])
                y = self.canvas.canvasy(pos[1])
                if x <= 0 or x + (self.r * 2) >= self.canvas.canvasx(self.canvas.winfo_width()):
                	self.vel['x'] = -self.vel['x']
                if y <= 0 or y + (self.r * 2) >= self.canvas.canvasy(self.canvas.winfo_height()):
                	self.vel['y'] = -self.vel['y']
                self.canvas.move(self.id, self.vel['x'], self.vel['y']);
                self.enter_Root_main_behaviour_bouncing()
            elif enabled == 2 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_main_behaviour_bouncing()
                self.canvas.itemconfig(self.id, fill="yellow")
                self.enter_Root_main_behaviour_selected()
            catched = True
        
        return catched
    
    def transition_Root_main_behaviour_dragging(self, event) :
        catched = False
        enableds = []
        if event.name == "motion" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "left-release" and event.getPort() == "input" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_main_behaviour_dragging. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_main_behaviour_dragging()
                coords = self.canvas.coords(self.id)
                dx = self.canvas.canvasx(self.last_x) - self.canvas.canvasx(coords[0])
                dy = self.canvas.canvasx(self.last_y) - self.canvas.canvasy(coords[1])
                
                self.canvas.move(self.id, dx, dy);
                
                # keep ball within boundaries
                coords = self.canvas.coords(self.id)
                x = self.canvas.canvasx(coords[0])
                y = self.canvas.canvasy(coords[1])
                if x - self.r <= 0:
                	x = 1;
                elif x + self.r >= self.canvas.winfo_width():
                	x = self.canvas.winfo_width() - (2 * self.r) - 1
                if y - self.r <= 0:
                	y = 1
                elif y + self.r >= self.canvas.winfo_height():
                	y = self.canvas.winfo_height() - (2 * self.r) - 1;
                self.canvas.coords(self.id, x, y, x + (self.r * 2), y + (self.r * 2));
                self.vel = {
                	'x': (1 - self.smooth) * dx + self.smooth * self.vel['x'],
                	'y': (1 - self.smooth) * dy + self.smooth * self.vel['y']
                }
                self.enter_Root_main_behaviour_dragging()
            elif enabled == 2 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_main_behaviour_dragging()
                self.canvas.itemconfig(self.id, fill="red")
                self.enter_Root_main_behaviour_bouncing()
            catched = True
        
        return catched
    
    def transition_Root_main_behaviour_selected(self, event) :
        catched = False
        enableds = []
        if event.name == "left-click" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(1)
        
        if event.name == "delete" and event.getPort() == "input" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_main_behaviour_selected. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_main_behaviour_selected()
                self.enter_Root_main_behaviour_dragging()
            elif enabled == 2 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_main_behaviour_selected()
                self.addEvent(Event("delete_self", parameters = []))
                self.enter_Root_main_behaviour_selected()
            catched = True
        
        return catched
    
    def transition_Root_deleted(self, event) :
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
    
class ObjectManager (ObjectManagerBase):
    def __init__(self, controller):
        super(ObjectManager, self).__init__(controller)
    
    def instantiate(self, class_name, construct_params):
        associations = []
        if class_name == "MainApp" :
            instance =  MainApp(self.controller, *construct_params)
            associations.append(Association("fields", "Field", 0, -1))
        elif class_name == "Field" :
            instance =  Field(self.controller, *construct_params)
            associations.append(Association("balls", "Ball", 0, -1))
            associations.append(Association("buttons", "Button", 0, -1))
            associations.append(Association("parent", "MainApp", 1, 1))
        elif class_name == "Button" :
            instance =  Button(self.controller, *construct_params)
            associations.append(Association("parent", "Field", 1, 1))
        elif class_name == "Ball" :
            instance =  Ball(self.controller, *construct_params)
            associations.append(Association("parent", "Field", 1, 1))
        if instance:
            return InstanceWrapper(instance, associations)
        else :
            return None

from python_runtime.statecharts_core import GameLoopControllerBase
class Controller(GameLoopControllerBase):
    def __init__(self, keep_running = True):
        super(Controller, self).__init__(ObjectManager(self), keep_running)
        self.addInputPort("input")
        self.object_manager.createInstance("MainApp", [])
        
def main():
    controller = Controller()
    controller.start()

if __name__ == "__main__":
    main()
