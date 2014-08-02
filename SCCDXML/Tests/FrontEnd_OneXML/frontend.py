# Statechart compiler by Glenn De Jonghe
#
# Date:   Sun Aug 03 01:22:46 2014

# Model author: Simon Van Mierlo
# Model name:   MvK Frontend
# Model description:
"""
    Tkinter frontend for the Modelverse.
"""

from python_runtime.statecharts_core import ObjectManagerBase, Event, InstanceWrapper, RuntimeClassBase, Association
import time
import Tkinter as tk
from util_classes import *

import urllib
import urllib2
import sys

from mvk.impl.python.util.jsonserializer import MvKEncoder
from mvk.impl.client.jsondeserializer import MvKDecoder
import mvk.impl.client.object as client_object

from mvk.impl.python.datavalue import LocationValue, StringValue, MappingValue, IntegerValue
from mvk.impl.python.datatype import *
from mvk.impl.python.constants import CreateConstants

host = "localhost"
port = "8000"


class MvKFrontend(tk.Tk, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_root = 1
    Root_root_running = 2
    Root_root_running_main_behaviour = 3
    Root_root_running_cd_behaviour = 4
    Root_root_running_listening_client = 5
    Root_root_running_main_behaviour_initializing = 6
    Root_root_running_main_behaviour_creating_client = 7
    Root_root_running_main_behaviour_initializing_windows = 8
    Root_root_running_main_behaviour_creating_main_window = 9
    Root_root_running_main_behaviour_running = 10
    Root_root_running_cd_behaviour_waiting = 11
    Root_root_running_cd_behaviour_creating = 12
    Root_root_running_cd_behaviour_starting = 13
    Root_root_running_cd_behaviour_check_nr_of_windows = 14
    Root_root_running_listening_client_listening_client = 15
    Root_root_stopped = 16
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_root] = []
        self.current_state[self.Root_root_running] = []
        self.current_state[self.Root_root_running_main_behaviour] = []
        self.current_state[self.Root_root_running_cd_behaviour] = []
        self.current_state[self.Root_root_running_listening_client] = []
    
    def start(self):
        super(MvKFrontend, self).start()
        self.enterDefault_Root_root()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        tk.Tk.__init__(self)
        self.fixed_update_time = 20
        self.update_self()
        self.withdraw()
        self.nr_of_windows = 0
    
    # User defined method
    def update_self(self):
        self.controller.update(self.fixed_update_time / 1000.0)
        self.schedule_time = time.time()
        self.scheduled_update_id = self.after(self.fixed_update_time, self.update_self)
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_root(self):
        self.current_state[self.Root].append(self.Root_root)
    
    def exit_Root_root(self):
        if self.Root_root_running in self.current_state[self.Root_root] :
            self.exit_Root_root_running()
        if self.Root_root_stopped in self.current_state[self.Root_root] :
            self.exit_Root_root_stopped()
        self.current_state[self.Root] = []
    
    def enter_Root_root_running(self):
        self.current_state[self.Root_root].append(self.Root_root_running)
    
    def exit_Root_root_running(self):
        self.exit_Root_root_running_main_behaviour()
        self.exit_Root_root_running_cd_behaviour()
        self.exit_Root_root_running_listening_client()
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_running_main_behaviour(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_main_behaviour)
    
    def exit_Root_root_running_main_behaviour(self):
        if self.Root_root_running_main_behaviour_initializing in self.current_state[self.Root_root_running_main_behaviour] :
            self.exit_Root_root_running_main_behaviour_initializing()
        if self.Root_root_running_main_behaviour_creating_client in self.current_state[self.Root_root_running_main_behaviour] :
            self.exit_Root_root_running_main_behaviour_creating_client()
        if self.Root_root_running_main_behaviour_initializing_windows in self.current_state[self.Root_root_running_main_behaviour] :
            self.exit_Root_root_running_main_behaviour_initializing_windows()
        if self.Root_root_running_main_behaviour_creating_main_window in self.current_state[self.Root_root_running_main_behaviour] :
            self.exit_Root_root_running_main_behaviour_creating_main_window()
        if self.Root_root_running_main_behaviour_running in self.current_state[self.Root_root_running_main_behaviour] :
            self.exit_Root_root_running_main_behaviour_running()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_running_cd_behaviour(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_cd_behaviour)
    
    def exit_Root_root_running_cd_behaviour(self):
        if self.Root_root_running_cd_behaviour_waiting in self.current_state[self.Root_root_running_cd_behaviour] :
            self.exit_Root_root_running_cd_behaviour_waiting()
        if self.Root_root_running_cd_behaviour_creating in self.current_state[self.Root_root_running_cd_behaviour] :
            self.exit_Root_root_running_cd_behaviour_creating()
        if self.Root_root_running_cd_behaviour_starting in self.current_state[self.Root_root_running_cd_behaviour] :
            self.exit_Root_root_running_cd_behaviour_starting()
        if self.Root_root_running_cd_behaviour_check_nr_of_windows in self.current_state[self.Root_root_running_cd_behaviour] :
            self.exit_Root_root_running_cd_behaviour_check_nr_of_windows()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_running_listening_client(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_listening_client)
    
    def exit_Root_root_running_listening_client(self):
        if self.Root_root_running_listening_client_listening_client in self.current_state[self.Root_root_running_listening_client] :
            self.exit_Root_root_running_listening_client_listening_client()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_running_main_behaviour_initializing(self):
        self.current_state[self.Root_root_running_main_behaviour].append(self.Root_root_running_main_behaviour_initializing)
    
    def exit_Root_root_running_main_behaviour_initializing(self):
        self.current_state[self.Root_root_running_main_behaviour] = []
    
    def enter_Root_root_running_main_behaviour_creating_client(self):
        self.current_state[self.Root_root_running_main_behaviour].append(self.Root_root_running_main_behaviour_creating_client)
    
    def exit_Root_root_running_main_behaviour_creating_client(self):
        self.current_state[self.Root_root_running_main_behaviour] = []
    
    def enter_Root_root_running_main_behaviour_initializing_windows(self):
        self.current_state[self.Root_root_running_main_behaviour].append(self.Root_root_running_main_behaviour_initializing_windows)
    
    def exit_Root_root_running_main_behaviour_initializing_windows(self):
        self.current_state[self.Root_root_running_main_behaviour] = []
    
    def enter_Root_root_running_main_behaviour_creating_main_window(self):
        self.current_state[self.Root_root_running_main_behaviour].append(self.Root_root_running_main_behaviour_creating_main_window)
    
    def exit_Root_root_running_main_behaviour_creating_main_window(self):
        self.current_state[self.Root_root_running_main_behaviour] = []
    
    def enter_Root_root_running_main_behaviour_running(self):
        self.current_state[self.Root_root_running_main_behaviour].append(self.Root_root_running_main_behaviour_running)
    
    def exit_Root_root_running_main_behaviour_running(self):
        self.current_state[self.Root_root_running_main_behaviour] = []
    
    def enter_Root_root_running_cd_behaviour_waiting(self):
        self.current_state[self.Root_root_running_cd_behaviour].append(self.Root_root_running_cd_behaviour_waiting)
    
    def exit_Root_root_running_cd_behaviour_waiting(self):
        self.current_state[self.Root_root_running_cd_behaviour] = []
    
    def enter_Root_root_running_cd_behaviour_creating(self):
        self.current_state[self.Root_root_running_cd_behaviour].append(self.Root_root_running_cd_behaviour_creating)
    
    def exit_Root_root_running_cd_behaviour_creating(self):
        self.current_state[self.Root_root_running_cd_behaviour] = []
    
    def enter_Root_root_running_cd_behaviour_starting(self):
        self.current_state[self.Root_root_running_cd_behaviour].append(self.Root_root_running_cd_behaviour_starting)
    
    def exit_Root_root_running_cd_behaviour_starting(self):
        self.current_state[self.Root_root_running_cd_behaviour] = []
    
    def enter_Root_root_running_cd_behaviour_check_nr_of_windows(self):
        self.current_state[self.Root_root_running_cd_behaviour].append(self.Root_root_running_cd_behaviour_check_nr_of_windows)
    
    def exit_Root_root_running_cd_behaviour_check_nr_of_windows(self):
        self.current_state[self.Root_root_running_cd_behaviour] = []
    
    def enter_Root_root_running_listening_client_listening_client(self):
        self.current_state[self.Root_root_running_listening_client].append(self.Root_root_running_listening_client_listening_client)
    
    def exit_Root_root_running_listening_client_listening_client(self):
        self.current_state[self.Root_root_running_listening_client] = []
    
    def enter_Root_root_stopped(self):
        self.current_state[self.Root_root].append(self.Root_root_stopped)
    
    def exit_Root_root_stopped(self):
        self.current_state[self.Root_root] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_root(self):
        self.enter_Root_root()
        self.enterDefault_Root_root_running()
    
    def enterDefault_Root_root_running(self):
        self.enter_Root_root_running()
        self.enterDefault_Root_root_running_main_behaviour()
        self.enterDefault_Root_root_running_cd_behaviour()
        self.enterDefault_Root_root_running_listening_client()
    
    def enterDefault_Root_root_running_main_behaviour(self):
        self.enter_Root_root_running_main_behaviour()
        self.enter_Root_root_running_main_behaviour_initializing()
    
    def enterDefault_Root_root_running_cd_behaviour(self):
        self.enter_Root_root_running_cd_behaviour()
        self.enter_Root_root_running_cd_behaviour_waiting()
    
    def enterDefault_Root_root_running_listening_client(self):
        self.enter_Root_root_running_listening_client()
        self.enter_Root_root_running_listening_client_listening_client()
    
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
            if self.current_state[self.Root_root][0] == self.Root_root_running:
                catched = self.transition_Root_root_running(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_stopped:
                catched = self.transition_Root_root_stopped(event)
        return catched
    
    def transition_Root_root_running(self, event) :
        catched = False
        enableds = []
        if event.name == "stop" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_running()
                self.destroy()
                self.enter_Root_root_stopped()
            catched = True
        
        if not catched :
            catched = self.transition_Root_root_running_main_behaviour(event) or catched
            catched = self.transition_Root_root_running_cd_behaviour(event) or catched
            catched = self.transition_Root_root_running_listening_client(event) or catched
        return catched
    
    def transition_Root_root_running_main_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_main_behaviour][0] == self.Root_root_running_main_behaviour_initializing:
                catched = self.transition_Root_root_running_main_behaviour_initializing(event)
            elif self.current_state[self.Root_root_running_main_behaviour][0] == self.Root_root_running_main_behaviour_creating_client:
                catched = self.transition_Root_root_running_main_behaviour_creating_client(event)
            elif self.current_state[self.Root_root_running_main_behaviour][0] == self.Root_root_running_main_behaviour_initializing_windows:
                catched = self.transition_Root_root_running_main_behaviour_initializing_windows(event)
            elif self.current_state[self.Root_root_running_main_behaviour][0] == self.Root_root_running_main_behaviour_creating_main_window:
                catched = self.transition_Root_root_running_main_behaviour_creating_main_window(event)
            elif self.current_state[self.Root_root_running_main_behaviour][0] == self.Root_root_running_main_behaviour_running:
                catched = self.transition_Root_root_running_main_behaviour_running(event)
        return catched
    
    def transition_Root_root_running_main_behaviour_initializing(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_running_main_behaviour_initializing()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "client","MvKClient"]))
                self.enter_Root_root_running_main_behaviour_creating_client()
            catched = True
        
        return catched
    
    def transition_Root_root_running_main_behaviour_creating_client(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_creating_client. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_main_behaviour_creating_client()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                self.enter_Root_root_running_main_behaviour_initializing_windows()
            catched = True
        
        return catched
    
    def transition_Root_root_running_main_behaviour_initializing_windows(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_initializing_windows. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_running_main_behaviour_initializing_windows()
                self.addEvent(Event("create_window", parameters = [{'class_name': 'ModelEditor', 'constructor_parameters': {}}]))
                self.enter_Root_root_running_main_behaviour_creating_main_window()
            catched = True
        
        return catched
    
    def transition_Root_root_running_main_behaviour_creating_main_window(self, event) :
        catched = False
        enableds = []
        if event.name == "window_started" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_creating_main_window. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_main_behaviour_creating_main_window()
                send_event = Event("create_toolbar", parameters = [{'class_name': 'MainToolbar', 'constructor_parameters': {}}])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_root_running_main_behaviour_running()
            catched = True
        
        return catched
    
    def transition_Root_root_running_main_behaviour_running(self, event) :
        catched = False
        enableds = []
        if event.name == "button_pressed" and event.getPort() == "" :
            parameters = event.getParameters()
            event_parameters = parameters[0]
            if event_parameters["event_name"] == "create_window" :
                enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_running_main_behaviour_running()
                self.addEvent(Event("create_window", parameters = [event_parameters]))
                self.enter_Root_root_running_main_behaviour_running()
            catched = True
        
        return catched
    
    def transition_Root_root_running_cd_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_cd_behaviour][0] == self.Root_root_running_cd_behaviour_waiting:
                catched = self.transition_Root_root_running_cd_behaviour_waiting(event)
            elif self.current_state[self.Root_root_running_cd_behaviour][0] == self.Root_root_running_cd_behaviour_creating:
                catched = self.transition_Root_root_running_cd_behaviour_creating(event)
            elif self.current_state[self.Root_root_running_cd_behaviour][0] == self.Root_root_running_cd_behaviour_starting:
                catched = self.transition_Root_root_running_cd_behaviour_starting(event)
            elif self.current_state[self.Root_root_running_cd_behaviour][0] == self.Root_root_running_cd_behaviour_check_nr_of_windows:
                catched = self.transition_Root_root_running_cd_behaviour_check_nr_of_windows(event)
        return catched
    
    def transition_Root_root_running_cd_behaviour_waiting(self, event) :
        catched = False
        enableds = []
        if event.name == "create_window" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "delete_window" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_cd_behaviour_waiting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_running_cd_behaviour_waiting()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "windows",event_parameters["class_name"],event_parameters["constructor_parameters"]]))
                self.enter_Root_root_running_cd_behaviour_creating()
            elif enabled == 2 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_cd_behaviour_waiting()
                self.nr_of_windows -= 1
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, association_name]))
                self.enter_Root_root_running_cd_behaviour_check_nr_of_windows()
            catched = True
        
        return catched
    
    def transition_Root_root_running_cd_behaviour_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_cd_behaviour_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_cd_behaviour_creating()
                self.nr_of_windows += 1
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                self.enter_Root_root_running_cd_behaviour_starting()
            catched = True
        
        return catched
    
    def transition_Root_root_running_cd_behaviour_starting(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_started" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_cd_behaviour_starting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_cd_behaviour_starting()
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.addEvent(Event("window_started", parameters = [association_name]))
                self.enter_Root_root_running_cd_behaviour_waiting()
            catched = True
        
        return catched
    
    def transition_Root_root_running_cd_behaviour_check_nr_of_windows(self, event) :
        catched = False
        enableds = []
        if self.nr_of_windows == 0 :
            enableds.append(1)
        
        if self.nr_of_windows != 0 :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_cd_behaviour_check_nr_of_windows. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_running_cd_behaviour_check_nr_of_windows()
                self.addEvent(Event("stop", parameters = []))
                self.enter_Root_root_running_cd_behaviour_check_nr_of_windows()
            elif enabled == 2 :
                self.exit_Root_root_running_cd_behaviour_check_nr_of_windows()
                self.enter_Root_root_running_cd_behaviour_waiting()
            catched = True
        
        return catched
    
    def transition_Root_root_running_listening_client(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_listening_client][0] == self.Root_root_running_listening_client_listening_client:
                catched = self.transition_Root_root_running_listening_client_listening_client(event)
        return catched
    
    def transition_Root_root_running_listening_client_listening_client(self, event) :
        catched = False
        enableds = []
        if event.name == "client_request" and event.getPort() == "" :
            parameters = event.getParameters()
            association_name = parameters[0]
            data = parameters[1]
            if data['event_name'] == 'read' :
                enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_listening_client_listening_client. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                data = parameters[1]
                self.exit_Root_root_running_listening_client_listening_client()
                send_event = Event("read", parameters = ['parent' + '/' + association_name,data['request_parameters']['data']])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'client' , send_event]))
                self.enter_Root_root_running_listening_client_listening_client()
            catched = True
        
        return catched
    
    def transition_Root_root_stopped(self, event) :
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
    

class Window(MvKWidget, tk.Toplevel, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_idle = 1
    
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
        super(Window, self).start()
        self.enter_Root_idle()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        tk.Toplevel.__init__(self)
        MvKWidget.__init__(self, self.controller)
    
    # User defined destructor
    def __del__(self):
        self.destroy()				
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_idle(self):
        self.current_state[self.Root].append(self.Root_idle)
    
    def exit_Root_idle(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_idle:
                catched = self.transition_Root_idle(event)
        return catched
    
    def transition_Root_idle(self, event) :
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
    

class NewInstanceAttributeEditor(Window, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_root = 1
    Root_root_main_behaviour = 2
    Root_root_main_behaviour_creating_editors = 3
    Root_root_initializing = 4
    Root_root_main_behaviour_creating_editors_loop = 5
    Root_root_main_behaviour_creating_editors_creating = 6
    Root_root_main_behaviour_creating_editors_running = 7
    Root_root_deleting = 8
    Root_root_stopped = 9
    
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
        self.current_state[self.Root_root_main_behaviour] = []
        self.current_state[self.Root_root_main_behaviour_creating_editors] = []
    
    def start(self):
        super(NewInstanceAttributeEditor, self).start()
        self.enterDefault_Root_root()
    
    #The actual constructor
    def __init__(self, controller, constructor_parameters = {}):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        Window.__init__(self, self.controller)
        self.minsize(width=256, height=256)
        self.t = constructor_parameters['type']
        self.title('Create New %s Instance' % self.t.name)
        self.grab_set()
        
        if isinstance(self.t, client_object.Model):
        	self.editors = [{'class_name': 'StringEditor', 'constructor_parameters': {'attr_name': StringValue('location')}}]
        elif isinstance(self.t, client_object.Association):
        	self.editors = [{'class_name': 'StringEditor', 'constructor_parameters': {'attr_name': StringValue(self.t.from_multiplicity.port_name)}},
        					{'class_name': 'StringEditor', 'constructor_parameters': {'attr_name': StringValue(self.t.to_multiplicity.port_name)}}]
        else:
        	self.editors = []
        
        for a in self.t.attributes:
        	class_name = None
        	the_type = a.the_type
        	if isinstance(the_type, StringType):
        		class_name = 'StringEditor'
        	elif isinstance(the_type, BooleanType):
        		class_name = 'BooleanEditor'
        	elif isinstance(the_type, NumericType):
        		class_name = 'NumericEditor'
        	elif isinstance(the_type, AnyType):
        		class_name = 'AnyEditor'
        	self.editors.append({'class_name': class_name, 'constructor_parameters': {'attr_name': StringValue(a.name)}})
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_root(self):
        self.current_state[self.Root].append(self.Root_root)
    
    def exit_Root_root(self):
        if self.Root_root_initializing in self.current_state[self.Root_root] :
            self.exit_Root_root_initializing()
        if self.Root_root_main_behaviour in self.current_state[self.Root_root] :
            self.exit_Root_root_main_behaviour()
        if self.Root_root_deleting in self.current_state[self.Root_root] :
            self.exit_Root_root_deleting()
        if self.Root_root_stopped in self.current_state[self.Root_root] :
            self.exit_Root_root_stopped()
        self.current_state[self.Root] = []
    
    def enter_Root_root_main_behaviour(self):
        self.current_state[self.Root_root].append(self.Root_root_main_behaviour)
    
    def exit_Root_root_main_behaviour(self):
        self.exit_Root_root_main_behaviour_creating_editors()
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_main_behaviour_creating_editors(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_creating_editors)
    
    def exit_Root_root_main_behaviour_creating_editors(self):
        if self.Root_root_main_behaviour_creating_editors_loop in self.current_state[self.Root_root_main_behaviour_creating_editors] :
            self.exit_Root_root_main_behaviour_creating_editors_loop()
        if self.Root_root_main_behaviour_creating_editors_creating in self.current_state[self.Root_root_main_behaviour_creating_editors] :
            self.exit_Root_root_main_behaviour_creating_editors_creating()
        if self.Root_root_main_behaviour_creating_editors_running in self.current_state[self.Root_root_main_behaviour_creating_editors] :
            self.exit_Root_root_main_behaviour_creating_editors_running()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_initializing(self):
        self.current_state[self.Root_root].append(self.Root_root_initializing)
    
    def exit_Root_root_initializing(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_main_behaviour_creating_editors_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_editors].append(self.Root_root_main_behaviour_creating_editors_loop)
    
    def exit_Root_root_main_behaviour_creating_editors_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_editors] = []
    
    def enter_Root_root_main_behaviour_creating_editors_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_editors].append(self.Root_root_main_behaviour_creating_editors_creating)
    
    def exit_Root_root_main_behaviour_creating_editors_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_editors] = []
    
    def enter_Root_root_main_behaviour_creating_editors_running(self):
        self.current_state[self.Root_root_main_behaviour_creating_editors].append(self.Root_root_main_behaviour_creating_editors_running)
    
    def exit_Root_root_main_behaviour_creating_editors_running(self):
        self.current_state[self.Root_root_main_behaviour_creating_editors] = []
    
    def enter_Root_root_deleting(self):
        self.timers[0] = 0.05
        self.current_state[self.Root_root].append(self.Root_root_deleting)
    
    def exit_Root_root_deleting(self):
        self.timers.pop(0, None)
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_stopped(self):
        self.current_state[self.Root_root].append(self.Root_root_stopped)
    
    def exit_Root_root_stopped(self):
        self.current_state[self.Root_root] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_root(self):
        self.enter_Root_root()
        self.enter_Root_root_initializing()
    
    def enterDefault_Root_root_main_behaviour(self):
        self.enter_Root_root_main_behaviour()
        self.enterDefault_Root_root_main_behaviour_creating_editors()
    
    def enterDefault_Root_root_main_behaviour_creating_editors(self):
        self.enter_Root_root_main_behaviour_creating_editors()
        self.enter_Root_root_main_behaviour_creating_editors_loop()
    
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
            if self.current_state[self.Root_root][0] == self.Root_root_initializing:
                catched = self.transition_Root_root_initializing(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_main_behaviour:
                catched = self.transition_Root_root_main_behaviour(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_deleting:
                catched = self.transition_Root_root_deleting(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_stopped:
                catched = self.transition_Root_root_stopped(event)
        return catched
    
    def transition_Root_root_initializing(self, event) :
        catched = False
        enableds = []
        if event.name == "set_association_name" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_initializing()
                self.association_name = association_name
                self.enterDefault_Root_root_main_behaviour()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour(self, event) :
        catched = False
        enableds = []
        if event.name == "close" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "window-close" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour()
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, 'editors']))
                self.enter_Root_root_deleting()
            elif enabled == 2 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_root_main_behaviour()
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, 'editors']))
                self.enter_Root_root_deleting()
            catched = True
        
        if not catched :
            catched = self.transition_Root_root_main_behaviour_creating_editors(event) or catched
        return catched
    
    def transition_Root_root_main_behaviour_creating_editors(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_creating_editors][0] == self.Root_root_main_behaviour_creating_editors_loop:
                catched = self.transition_Root_root_main_behaviour_creating_editors_loop(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_editors][0] == self.Root_root_main_behaviour_creating_editors_creating:
                catched = self.transition_Root_root_main_behaviour_creating_editors_creating(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_editors][0] == self.Root_root_main_behaviour_creating_editors_running:
                catched = self.transition_Root_root_main_behaviour_creating_editors_running(event)
        return catched
    
    def transition_Root_root_main_behaviour_creating_editors_loop(self, event) :
        catched = False
        enableds = []
        if self.editors :
            enableds.append(1)
        
        if not self.editors :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_editors_loop. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour_creating_editors_loop()
                ctor_parameters = self.editors.pop(0)
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "editors",ctor_parameters["class_name"],ctor_parameters]))
                self.enter_Root_root_main_behaviour_creating_editors_creating()
            elif enabled == 2 :
                self.exit_Root_root_main_behaviour_creating_editors_loop()
                self.enter_Root_root_main_behaviour_creating_editors_running()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_editors_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_editors_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_main_behaviour_creating_editors_creating()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_root_main_behaviour_creating_editors_loop()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_editors_running(self, event) :
        catched = False
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
                send_event = Event("delete_window", parameters = [self.association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_stopped()
            catched = True
        
        return catched
    
    def transition_Root_root_stopped(self, event) :
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
    

class Editor(RuntimeClassBase):
    
    def commonConstructor(self):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
    
    def start(self):
        super(Editor, self).start()
    
    #The actual constructor
    def __init__(self, controller, attr_name):
        self.commonConstructor()
        
        #constructor body (user-defined)
        self.attr_name = attr_name
    

class EntryEditor(Editor, tk.Entry, RuntimeClassBase):
    
    def commonConstructor(self):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
    
    def start(self):
        super(EntryEditor, self).start()
    
    #The actual constructor
    def __init__(self, controller, constructor_parameters):
        self.commonConstructor()
        
        #constructor body (user-defined)
        tk.Entry.__init__(constructor_parameters['parent'])
        Editor.__init__(self, constructor_parameters['attr_name'])
    

class StringEditor(EntryEditor, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_initializing = 1
    
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
        super(StringEditor, self).start()
        self.enter_Root_initializing()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_initializing(self):
        self.current_state[self.Root].append(self.Root_initializing)
    
    def exit_Root_initializing(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_initializing:
                catched = self.transition_Root_initializing(event)
        return catched
    
    def transition_Root_initializing(self, event) :
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
    

class NumericEditor(EntryEditor, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_initializing = 1
    
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
        super(NumericEditor, self).start()
        self.enter_Root_initializing()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_initializing(self):
        self.current_state[self.Root].append(self.Root_initializing)
    
    def exit_Root_initializing(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_initializing:
                catched = self.transition_Root_initializing(event)
        return catched
    
    def transition_Root_initializing(self, event) :
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
    

class AnyEditor(EntryEditor, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_initializing = 1
    
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
        super(AnyEditor, self).start()
        self.enter_Root_initializing()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_initializing(self):
        self.current_state[self.Root].append(self.Root_initializing)
    
    def exit_Root_initializing(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_initializing:
                catched = self.transition_Root_initializing(event)
        return catched
    
    def transition_Root_initializing(self, event) :
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
    

class BooleanEditor(EntryEditor, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_initializing = 1
    
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
        super(BooleanEditor, self).start()
        self.enter_Root_initializing()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_initializing(self):
        self.current_state[self.Root].append(self.Root_initializing)
    
    def exit_Root_initializing(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_initializing:
                catched = self.transition_Root_initializing(event)
        return catched
    
    def transition_Root_initializing(self, event) :
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
    

class TypeModelBrowser(Window, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_root = 1
    Root_root_main_behaviour = 2
    Root_root_main_behaviour_creating_buttons = 3
    Root_root_main_behaviour_creating_buttons_running = 4
    Root_root_main_behaviour_creating_buttons_running_populating_frame = 5
    Root_root_main_behaviour_packing_widgets = 6
    Root_root_main_behaviour_listening_client = 7
    Root_root_initializing = 8
    Root_root_main_behaviour_creating_buttons_loop = 9
    Root_root_main_behaviour_creating_buttons_creating = 10
    Root_root_main_behaviour_creating_buttons_running_getting_children = 11
    Root_root_main_behaviour_creating_buttons_running_waiting_client = 12
    Root_root_main_behaviour_creating_buttons_running_populating_frame_loop = 13
    Root_root_main_behaviour_creating_buttons_running_populating_frame_creating = 14
    Root_root_main_behaviour_creating_buttons_running_running = 15
    Root_root_main_behaviour_creating_buttons_running_waiting_for_second = 16
    Root_root_main_behaviour_creating_buttons_running_get_type_model = 17
    Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model = 18
    Root_root_main_behaviour_packing_widgets_packing = 19
    Root_root_main_behaviour_listening_client_listening_client = 20
    Root_root_deleting = 21
    Root_root_stopped = 22
    
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
        self.current_state[self.Root_root_main_behaviour] = []
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running] = []
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running_populating_frame] = []
        self.current_state[self.Root_root_main_behaviour_packing_widgets] = []
        self.current_state[self.Root_root_main_behaviour_listening_client] = []
    
    def start(self):
        super(TypeModelBrowser, self).start()
        self.enterDefault_Root_root()
    
    #The actual constructor
    def __init__(self, controller, constructor_parameters = {}):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        Window.__init__(self, self.controller)
        self.minsize(width=256, height=256)
        self.title('Browse Type Models')
        self.curr_location = LocationValue('.')
        
        self.buttons = [{"class_name": "Button", "parent": self, "visual": ImageVisual('icons/back-icon.png'), "tooltip_text": 'Go Up One Level', "event_parameters": {"event_name": "up_level"}},
        				{"class_name": "Button", "parent": self, "visual": TextVisual('SELECT'), "tooltip_text": 'Select Type Model', "event_parameters": {"event_name": "select_type_model"}}]
        
        self.f = tk.Frame(self, pady=30, bg="white")
        self.curr_location = LocationValue("")
        self.selected_location = LocationValue("")
        self.history = []
        self.append_history = True
        self.curr_children = []
        self.name_to_loc = {}
        self.name_to_assoc = {}
        self.curr_name = ""
        self.grab_set()
        self.curr_b = 0
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_root(self):
        self.current_state[self.Root].append(self.Root_root)
    
    def exit_Root_root(self):
        if self.Root_root_initializing in self.current_state[self.Root_root] :
            self.exit_Root_root_initializing()
        if self.Root_root_main_behaviour in self.current_state[self.Root_root] :
            self.exit_Root_root_main_behaviour()
        if self.Root_root_deleting in self.current_state[self.Root_root] :
            self.exit_Root_root_deleting()
        if self.Root_root_stopped in self.current_state[self.Root_root] :
            self.exit_Root_root_stopped()
        self.current_state[self.Root] = []
    
    def enter_Root_root_main_behaviour(self):
        self.current_state[self.Root_root].append(self.Root_root_main_behaviour)
    
    def exit_Root_root_main_behaviour(self):
        self.exit_Root_root_main_behaviour_creating_buttons()
        self.exit_Root_root_main_behaviour_packing_widgets()
        self.exit_Root_root_main_behaviour_listening_client()
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_main_behaviour_creating_buttons(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_creating_buttons)
    
    def exit_Root_root_main_behaviour_creating_buttons(self):
        if self.Root_root_main_behaviour_creating_buttons_loop in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_loop()
        if self.Root_root_main_behaviour_creating_buttons_creating in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_creating()
        if self.Root_root_main_behaviour_creating_buttons_running in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_running()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_running)
    
    def exit_Root_root_main_behaviour_creating_buttons_running(self):
        if self.Root_root_main_behaviour_creating_buttons_running_getting_children in self.current_state[self.Root_root_main_behaviour_creating_buttons_running] :
            self.exit_Root_root_main_behaviour_creating_buttons_running_getting_children()
        if self.Root_root_main_behaviour_creating_buttons_running_waiting_client in self.current_state[self.Root_root_main_behaviour_creating_buttons_running] :
            self.exit_Root_root_main_behaviour_creating_buttons_running_waiting_client()
        if self.Root_root_main_behaviour_creating_buttons_running_populating_frame in self.current_state[self.Root_root_main_behaviour_creating_buttons_running] :
            self.exit_Root_root_main_behaviour_creating_buttons_running_populating_frame()
        if self.Root_root_main_behaviour_creating_buttons_running_running in self.current_state[self.Root_root_main_behaviour_creating_buttons_running] :
            self.exit_Root_root_main_behaviour_creating_buttons_running_running()
        if self.Root_root_main_behaviour_creating_buttons_running_waiting_for_second in self.current_state[self.Root_root_main_behaviour_creating_buttons_running] :
            self.exit_Root_root_main_behaviour_creating_buttons_running_waiting_for_second()
        if self.Root_root_main_behaviour_creating_buttons_running_get_type_model in self.current_state[self.Root_root_main_behaviour_creating_buttons_running] :
            self.exit_Root_root_main_behaviour_creating_buttons_running_get_type_model()
        if self.Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model in self.current_state[self.Root_root_main_behaviour_creating_buttons_running] :
            self.exit_Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model()
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running_populating_frame(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running].append(self.Root_root_main_behaviour_creating_buttons_running_populating_frame)
    
    def exit_Root_root_main_behaviour_creating_buttons_running_populating_frame(self):
        if self.Root_root_main_behaviour_creating_buttons_running_populating_frame_loop in self.current_state[self.Root_root_main_behaviour_creating_buttons_running_populating_frame] :
            self.exit_Root_root_main_behaviour_creating_buttons_running_populating_frame_loop()
        if self.Root_root_main_behaviour_creating_buttons_running_populating_frame_creating in self.current_state[self.Root_root_main_behaviour_creating_buttons_running_populating_frame] :
            self.exit_Root_root_main_behaviour_creating_buttons_running_populating_frame_creating()
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running] = []
    
    def enter_Root_root_main_behaviour_packing_widgets(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_packing_widgets)
    
    def exit_Root_root_main_behaviour_packing_widgets(self):
        if self.Root_root_main_behaviour_packing_widgets_packing in self.current_state[self.Root_root_main_behaviour_packing_widgets] :
            self.exit_Root_root_main_behaviour_packing_widgets_packing()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_main_behaviour_listening_client(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_listening_client)
    
    def exit_Root_root_main_behaviour_listening_client(self):
        if self.Root_root_main_behaviour_listening_client_listening_client in self.current_state[self.Root_root_main_behaviour_listening_client] :
            self.exit_Root_root_main_behaviour_listening_client_listening_client()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_initializing(self):
        self.current_state[self.Root_root].append(self.Root_root_initializing)
    
    def exit_Root_root_initializing(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_loop)
    
    def exit_Root_root_main_behaviour_creating_buttons_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_creating)
    
    def exit_Root_root_main_behaviour_creating_buttons_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running_getting_children(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running].append(self.Root_root_main_behaviour_creating_buttons_running_getting_children)
    
    def exit_Root_root_main_behaviour_creating_buttons_running_getting_children(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running_waiting_client(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running].append(self.Root_root_main_behaviour_creating_buttons_running_waiting_client)
    
    def exit_Root_root_main_behaviour_creating_buttons_running_waiting_client(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running_populating_frame_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running_populating_frame].append(self.Root_root_main_behaviour_creating_buttons_running_populating_frame_loop)
    
    def exit_Root_root_main_behaviour_creating_buttons_running_populating_frame_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running_populating_frame] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running_populating_frame_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running_populating_frame].append(self.Root_root_main_behaviour_creating_buttons_running_populating_frame_creating)
    
    def exit_Root_root_main_behaviour_creating_buttons_running_populating_frame_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running_populating_frame] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running_running(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running].append(self.Root_root_main_behaviour_creating_buttons_running_running)
    
    def exit_Root_root_main_behaviour_creating_buttons_running_running(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running_waiting_for_second(self):
        self.timers[0] = 0.5
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running].append(self.Root_root_main_behaviour_creating_buttons_running_waiting_for_second)
    
    def exit_Root_root_main_behaviour_creating_buttons_running_waiting_for_second(self):
        self.timers.pop(0, None)
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running_get_type_model(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running].append(self.Root_root_main_behaviour_creating_buttons_running_get_type_model)
    
    def exit_Root_root_main_behaviour_creating_buttons_running_get_type_model(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running].append(self.Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model)
    
    def exit_Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons_running] = []
    
    def enter_Root_root_main_behaviour_packing_widgets_packing(self):
        self.current_state[self.Root_root_main_behaviour_packing_widgets].append(self.Root_root_main_behaviour_packing_widgets_packing)
    
    def exit_Root_root_main_behaviour_packing_widgets_packing(self):
        self.current_state[self.Root_root_main_behaviour_packing_widgets] = []
    
    def enter_Root_root_main_behaviour_listening_client_listening_client(self):
        self.current_state[self.Root_root_main_behaviour_listening_client].append(self.Root_root_main_behaviour_listening_client_listening_client)
    
    def exit_Root_root_main_behaviour_listening_client_listening_client(self):
        self.current_state[self.Root_root_main_behaviour_listening_client] = []
    
    def enter_Root_root_deleting(self):
        self.timers[1] = 0.05
        self.current_state[self.Root_root].append(self.Root_root_deleting)
    
    def exit_Root_root_deleting(self):
        self.timers.pop(1, None)
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_stopped(self):
        self.current_state[self.Root_root].append(self.Root_root_stopped)
    
    def exit_Root_root_stopped(self):
        self.current_state[self.Root_root] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_root(self):
        self.enter_Root_root()
        self.enter_Root_root_initializing()
    
    def enterDefault_Root_root_main_behaviour(self):
        self.enter_Root_root_main_behaviour()
        self.enterDefault_Root_root_main_behaviour_creating_buttons()
        self.enterDefault_Root_root_main_behaviour_packing_widgets()
        self.enterDefault_Root_root_main_behaviour_listening_client()
    
    def enterDefault_Root_root_main_behaviour_creating_buttons(self):
        self.enter_Root_root_main_behaviour_creating_buttons()
        self.enter_Root_root_main_behaviour_creating_buttons_loop()
    
    def enterDefault_Root_root_main_behaviour_creating_buttons_running(self):
        self.enter_Root_root_main_behaviour_creating_buttons_running()
        self.enter_Root_root_main_behaviour_creating_buttons_running_getting_children()
    
    def enterDefault_Root_root_main_behaviour_creating_buttons_running_populating_frame(self):
        self.enter_Root_root_main_behaviour_creating_buttons_running_populating_frame()
        self.enter_Root_root_main_behaviour_creating_buttons_running_populating_frame_loop()
    
    def enterDefault_Root_root_main_behaviour_packing_widgets(self):
        self.enter_Root_root_main_behaviour_packing_widgets()
        self.enter_Root_root_main_behaviour_packing_widgets_packing()
    
    def enterDefault_Root_root_main_behaviour_listening_client(self):
        self.enter_Root_root_main_behaviour_listening_client()
        self.enter_Root_root_main_behaviour_listening_client_listening_client()
    
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
            if self.current_state[self.Root_root][0] == self.Root_root_initializing:
                catched = self.transition_Root_root_initializing(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_main_behaviour:
                catched = self.transition_Root_root_main_behaviour(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_deleting:
                catched = self.transition_Root_root_deleting(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_stopped:
                catched = self.transition_Root_root_stopped(event)
        return catched
    
    def transition_Root_root_initializing(self, event) :
        catched = False
        enableds = []
        if event.name == "set_association_name" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_initializing()
                self.association_name = association_name
                self.enterDefault_Root_root_main_behaviour()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour(self, event) :
        catched = False
        enableds = []
        if event.name == "close" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "window-close" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour()
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, 'labels']))
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, 'buttons']))
                self.enter_Root_root_deleting()
            elif enabled == 2 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_root_main_behaviour()
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, 'labels']))
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, 'buttons']))
                self.enter_Root_root_deleting()
            catched = True
        
        if not catched :
            catched = self.transition_Root_root_main_behaviour_creating_buttons(event) or catched
            catched = self.transition_Root_root_main_behaviour_packing_widgets(event) or catched
            catched = self.transition_Root_root_main_behaviour_listening_client(event) or catched
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_loop:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_loop(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_creating:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_creating(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_running:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running(event)
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_loop(self, event) :
        catched = False
        enableds = []
        if self.buttons :
            enableds.append(1)
        
        if not self.buttons :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_loop. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour_creating_buttons_loop()
                ctor_parameters = self.buttons.pop(0)
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "buttons",ctor_parameters["class_name"],ctor_parameters]))
                self.enter_Root_root_main_behaviour_creating_buttons_creating()
            elif enabled == 2 :
                self.exit_Root_root_main_behaviour_creating_buttons_loop()
                self.enterDefault_Root_root_main_behaviour_creating_buttons_running()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_creating()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_root_main_behaviour_creating_buttons_loop()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_creating_buttons_running][0] == self.Root_root_main_behaviour_creating_buttons_running_getting_children:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running_getting_children(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons_running][0] == self.Root_root_main_behaviour_creating_buttons_running_waiting_client:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running_waiting_client(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons_running][0] == self.Root_root_main_behaviour_creating_buttons_running_populating_frame:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running_populating_frame(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons_running][0] == self.Root_root_main_behaviour_creating_buttons_running_running:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running_running(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons_running][0] == self.Root_root_main_behaviour_creating_buttons_running_waiting_for_second:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running_waiting_for_second(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons_running][0] == self.Root_root_main_behaviour_creating_buttons_running_get_type_model:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running_get_type_model(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons_running][0] == self.Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model(event)
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running_getting_children(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_running_getting_children. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour_creating_buttons_running_getting_children()
                send_event = Event("client_request", parameters = [self.association_name,{'event_name': 'read', 'request_parameters': {'data': self.selected_location}}])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_main_behaviour_creating_buttons_running_waiting_client()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running_waiting_client(self, event) :
        catched = False
        enableds = []
        if event.name == "client_response" and event.getPort() == "" :
            parameters = event.getParameters()
            result = parameters[0]
            if hasattr(result[StringValue('item')], 'children') :
                enableds.append(1)
        
        if event.name == "client_response" and event.getPort() == "" :
            if not hasattr(result[StringValue('item')], 'children') :
                enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_running_waiting_client. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                result = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_running_waiting_client()
                if self.append_history:
                	self.history.append(self.curr_location)
                self.curr_location = self.selected_location
                self.curr_children = result[StringValue("item")].children
                self.curr_item = result[StringValue('item')]
                self.name_to_loc = {}
                self.name_to_assoc = {}
                for c in self.curr_children:
                	self.name_to_loc[c[0]] = c[1]
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, 'labels']))
                self.enterDefault_Root_root_main_behaviour_creating_buttons_running_populating_frame()
            elif enabled == 2 :
                self.exit_Root_root_main_behaviour_creating_buttons_running_waiting_client()
                self.enter_Root_root_main_behaviour_creating_buttons_running_running()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running_populating_frame(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_creating_buttons_running_populating_frame][0] == self.Root_root_main_behaviour_creating_buttons_running_populating_frame_loop:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running_populating_frame_loop(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons_running_populating_frame][0] == self.Root_root_main_behaviour_creating_buttons_running_populating_frame_creating:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running_populating_frame_creating(event)
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running_populating_frame_loop(self, event) :
        catched = False
        enableds = []
        if self.curr_children :
            enableds.append(1)
        
        if not self.curr_children :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_running_populating_frame_loop. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour_creating_buttons_running_populating_frame_loop()
                text = self.curr_children.pop()[0]
                self.curr_name = text
                ctor_parameters = {"parent": self.f, "text": text}
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "labels","Label",ctor_parameters]))
                self.enter_Root_root_main_behaviour_creating_buttons_running_populating_frame_creating()
            elif enabled == 2 :
                self.exit_Root_root_main_behaviour_creating_buttons_running_populating_frame()
                self.enter_Root_root_main_behaviour_creating_buttons_running_running()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running_populating_frame_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_running_populating_frame_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_running_populating_frame_creating()
                self.name_to_assoc[self.curr_name] = association_name
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_root_main_behaviour_creating_buttons_running_populating_frame_loop()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running_running(self, event) :
        catched = False
        enableds = []
        if event.name == "label_pressed" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "button_pressed" and event.getPort() == "" :
            parameters = event.getParameters()
            event_parameters = parameters[0]
            if event_parameters['event_name'] == 'up_level' and self.history :
                enableds.append(2)
        
        if event.name == "button_pressed" and event.getPort() == "" :
            parameters = event.getParameters()
            event_parameters = parameters[0]
            if event_parameters['event_name'] == 'select_type_model' :
                enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_running_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                text = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_running_running()
                send_event = Event("unhighlight", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'labels' , send_event]))
                send_event = Event("highlight", parameters = [])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, self.name_to_assoc[StringValue(text)] , send_event]))
                self.append_history = True
                self.selected_location = self.name_to_loc[StringValue(text)]
                self.enter_Root_root_main_behaviour_creating_buttons_running_waiting_for_second()
            elif enabled == 2 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_running_running()
                self.append_history = False
                self.selected_location = self.history.pop()
                self.enter_Root_root_main_behaviour_creating_buttons_running_getting_children()
            elif enabled == 3 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_running_running()
                self.enter_Root_root_main_behaviour_creating_buttons_running_get_type_model()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running_waiting_for_second(self, event) :
        catched = False
        enableds = []
        if event.name == "label_pressed" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "_0after" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_running_waiting_for_second. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour_creating_buttons_running_waiting_for_second()
                self.enter_Root_root_main_behaviour_creating_buttons_running_getting_children()
            elif enabled == 2 :
                self.exit_Root_root_main_behaviour_creating_buttons_running_waiting_for_second()
                self.enter_Root_root_main_behaviour_creating_buttons_running_running()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running_get_type_model(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_running_get_type_model. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour_creating_buttons_running_get_type_model()
                send_event = Event("client_request", parameters = [self.association_name,{'event_name': 'read', 'request_parameters': {'data': self.selected_location}}])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model(self, event) :
        catched = False
        enableds = []
        if event.name == "client_response" and event.getPort() == "" :
            parameters = event.getParameters()
            result = parameters[0]
            if isinstance(result[StringValue('item')], client_object.Model) and result[StringValue('item')].potency > IntegerValue(0) :
                enableds.append(1)
        
        if event.name == "client_response" and event.getPort() == "" :
            if not (isinstance(result[StringValue('item')], client_object.Model) and result[StringValue('item')].potency > IntegerValue(0)) :
                enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                result = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model()
                send_event = Event("type_model_selected", parameters = [result[StringValue('item')]])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.addEvent(Event("close", parameters = []))
                self.enterDefault_Root_root_main_behaviour_creating_buttons_running_populating_frame()
            elif enabled == 2 :
                self.exit_Root_root_main_behaviour_creating_buttons_running_waiting_client_type_model()
                self.enter_Root_root_main_behaviour_creating_buttons_running_running()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_packing_widgets(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_packing_widgets][0] == self.Root_root_main_behaviour_packing_widgets_packing:
                catched = self.transition_Root_root_main_behaviour_packing_widgets_packing(event)
        return catched
    
    def transition_Root_root_main_behaviour_packing_widgets_packing(self, event) :
        catched = False
        enableds = []
        if event.name == "button_created" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "label_created" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_packing_widgets_packing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                widget = parameters[0]
                self.exit_Root_root_main_behaviour_packing_widgets_packing()
                if self.curr_b == 0:
                	widget.pack(side=tk.TOP, fill=tk.Y)
                	self.f.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                else:
                	widget.pack(side=tk.TOP, fill=tk.Y)
                self.enter_Root_root_main_behaviour_packing_widgets_packing()
            elif enabled == 2 :
                parameters = event.getParameters()
                widget = parameters[0]
                self.exit_Root_root_main_behaviour_packing_widgets_packing()
                widget.pack(side=tk.TOP, fill=tk.X)
                self.enter_Root_root_main_behaviour_packing_widgets_packing()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_listening_client(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_listening_client][0] == self.Root_root_main_behaviour_listening_client_listening_client:
                catched = self.transition_Root_root_main_behaviour_listening_client_listening_client(event)
        return catched
    
    def transition_Root_root_main_behaviour_listening_client_listening_client(self, event) :
        catched = False
        enableds = []
        if event.name == "client_request" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_listening_client_listening_client. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                data = parameters[1]
                self.exit_Root_root_main_behaviour_listening_client_listening_client()
                send_event = Event("client_request", parameters = [self.association_name + '/' + association_name,data])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_main_behaviour_listening_client_listening_client()
            catched = True
        
        return catched
    
    def transition_Root_root_deleting(self, event) :
        catched = False
        enableds = []
        if event.name == "_1after" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_deleting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_deleting()
                send_event = Event("delete_window", parameters = [self.association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_stopped()
            catched = True
        
        return catched
    
    def transition_Root_root_stopped(self, event) :
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
    

class Label(MvKWidget, tk.Label, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_root = 1
    Root_root_initializing = 2
    Root_root_running = 3
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_root] = []
    
    def start(self):
        super(Label, self).start()
        self.enterDefault_Root_root()
    
    #The actual constructor
    def __init__(self, controller, constructor_parameters = {}):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        tk.Label.__init__(self, constructor_parameters["parent"], text=constructor_parameters["text"], bg="white")
        MvKWidget.__init__(self, controller)
    
    # User defined destructor
    def __del__(self):
        self.destroy()
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_root(self):
        self.current_state[self.Root].append(self.Root_root)
    
    def exit_Root_root(self):
        if self.Root_root_initializing in self.current_state[self.Root_root] :
            self.exit_Root_root_initializing()
        if self.Root_root_running in self.current_state[self.Root_root] :
            self.exit_Root_root_running()
        self.current_state[self.Root] = []
    
    def enter_Root_root_initializing(self):
        self.current_state[self.Root_root].append(self.Root_root_initializing)
    
    def exit_Root_root_initializing(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_running(self):
        self.current_state[self.Root_root].append(self.Root_root_running)
    
    def exit_Root_root_running(self):
        self.current_state[self.Root_root] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_root(self):
        self.enter_Root_root()
        self.enter_Root_root_initializing()
    
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
            if self.current_state[self.Root_root][0] == self.Root_root_initializing:
                catched = self.transition_Root_root_initializing(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_running:
                catched = self.transition_Root_root_running(event)
        return catched
    
    def transition_Root_root_initializing(self, event) :
        catched = False
        enableds = []
        if event.name == "set_association_name" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_initializing()
                self.association_name = association_name
                send_event = Event("label_created", parameters = [self])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_running()
            catched = True
        
        return catched
    
    def transition_Root_root_running(self, event) :
        catched = False
        enableds = []
        if event.name == "left-click" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(1)
        
        if event.name == "highlight" and event.getPort() == "" :
            enableds.append(2)
        
        if event.name == "unhighlight" and event.getPort() == "" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_root_running()
                send_event = Event("label_pressed", parameters = [self.cget('text')])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_running()
            elif enabled == 2 :
                self.exit_Root_root_running()
                self.config(bg="yellow")
                self.enter_Root_root_running()
            elif enabled == 3 :
                self.exit_Root_root_running()
                self.config(bg="white")
                self.enter_Root_root_running()
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
    

class ModelEditor(Window, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_root = 1
    Root_root_running = 2
    Root_root_running_main_behaviour = 3
    Root_root_running_main_behaviour_creating_model = 4
    Root_root_running_toolbar_behaviour = 5
    Root_root_running_window_behaviour = 6
    Root_root_running_listening_client = 7
    Root_root_initializing = 8
    Root_root_running_main_behaviour_running = 9
    Root_root_running_main_behaviour_creating_model_waiting = 10
    Root_root_running_main_behaviour_creating_model_entering_model_details = 11
    Root_root_running_main_behaviour_creating_model_waiting_client = 12
    Root_root_running_toolbar_behaviour_waiting = 13
    Root_root_running_toolbar_behaviour_creating = 14
    Root_root_running_window_behaviour_waiting = 15
    Root_root_running_window_behaviour_creating = 16
    Root_root_running_window_behaviour_starting = 17
    Root_root_running_listening_client_listening_client = 18
    Root_root_deleting = 19
    Root_root_stopped = 20
    
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
        self.current_state[self.Root_root_running_main_behaviour_creating_model] = []
        self.current_state[self.Root_root_running_toolbar_behaviour] = []
        self.current_state[self.Root_root_running_window_behaviour] = []
        self.current_state[self.Root_root_running_listening_client] = []
    
    def start(self):
        super(ModelEditor, self).start()
        self.enterDefault_Root_root()
    
    #The actual constructor
    def __init__(self, controller, constructor_parameters = {}):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        Window.__init__(self, controller)
        self.title('ModelEditor')
        
        self.maxsize(self.winfo_screenwidth() - 15, self.winfo_screenheight() - 15)
        
        self.INTER_SPACING = 5
        
        self.toolbar_frame = HorizontalScrolledFrame(parent=self)
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X, expand=0)
        
        CANVAS_SIZE_TUPLE = (0, 0, self.winfo_screenwidth() * 2, self.winfo_screenheight() * 2)
        self.c = tk.Canvas(self, relief=tk.RIDGE, scrollregion=CANVAS_SIZE_TUPLE)
        
        vbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vbar.config(command=self.c.yview)
        vbar.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 16))
        
        hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        hbar.config(command=self.c.xview)
        hbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.c.config(background='white', yscrollcommand=vbar.set, xscrollcommand=hbar.set)
        self.c.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        
        MvKWidget.__init__(self, self.controller, self.c)
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_root(self):
        self.current_state[self.Root].append(self.Root_root)
    
    def exit_Root_root(self):
        if self.Root_root_initializing in self.current_state[self.Root_root] :
            self.exit_Root_root_initializing()
        if self.Root_root_running in self.current_state[self.Root_root] :
            self.exit_Root_root_running()
        if self.Root_root_deleting in self.current_state[self.Root_root] :
            self.exit_Root_root_deleting()
        if self.Root_root_stopped in self.current_state[self.Root_root] :
            self.exit_Root_root_stopped()
        self.current_state[self.Root] = []
    
    def enter_Root_root_running(self):
        self.current_state[self.Root_root].append(self.Root_root_running)
    
    def exit_Root_root_running(self):
        self.exit_Root_root_running_main_behaviour()
        self.exit_Root_root_running_toolbar_behaviour()
        self.exit_Root_root_running_window_behaviour()
        self.exit_Root_root_running_listening_client()
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_running_main_behaviour(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_main_behaviour)
    
    def exit_Root_root_running_main_behaviour(self):
        if self.Root_root_running_main_behaviour_running in self.current_state[self.Root_root_running_main_behaviour] :
            self.exit_Root_root_running_main_behaviour_running()
        if self.Root_root_running_main_behaviour_creating_model in self.current_state[self.Root_root_running_main_behaviour] :
            self.exit_Root_root_running_main_behaviour_creating_model()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_running_main_behaviour_creating_model(self):
        self.current_state[self.Root_root_running_main_behaviour].append(self.Root_root_running_main_behaviour_creating_model)
    
    def exit_Root_root_running_main_behaviour_creating_model(self):
        if self.Root_root_running_main_behaviour_creating_model_waiting in self.current_state[self.Root_root_running_main_behaviour_creating_model] :
            self.exit_Root_root_running_main_behaviour_creating_model_waiting()
        if self.Root_root_running_main_behaviour_creating_model_entering_model_details in self.current_state[self.Root_root_running_main_behaviour_creating_model] :
            self.exit_Root_root_running_main_behaviour_creating_model_entering_model_details()
        if self.Root_root_running_main_behaviour_creating_model_waiting_client in self.current_state[self.Root_root_running_main_behaviour_creating_model] :
            self.exit_Root_root_running_main_behaviour_creating_model_waiting_client()
        self.current_state[self.Root_root_running_main_behaviour] = []
    
    def enter_Root_root_running_toolbar_behaviour(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_toolbar_behaviour)
    
    def exit_Root_root_running_toolbar_behaviour(self):
        if self.Root_root_running_toolbar_behaviour_waiting in self.current_state[self.Root_root_running_toolbar_behaviour] :
            self.exit_Root_root_running_toolbar_behaviour_waiting()
        if self.Root_root_running_toolbar_behaviour_creating in self.current_state[self.Root_root_running_toolbar_behaviour] :
            self.exit_Root_root_running_toolbar_behaviour_creating()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_running_window_behaviour(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_window_behaviour)
    
    def exit_Root_root_running_window_behaviour(self):
        if self.Root_root_running_window_behaviour_waiting in self.current_state[self.Root_root_running_window_behaviour] :
            self.exit_Root_root_running_window_behaviour_waiting()
        if self.Root_root_running_window_behaviour_creating in self.current_state[self.Root_root_running_window_behaviour] :
            self.exit_Root_root_running_window_behaviour_creating()
        if self.Root_root_running_window_behaviour_starting in self.current_state[self.Root_root_running_window_behaviour] :
            self.exit_Root_root_running_window_behaviour_starting()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_running_listening_client(self):
        self.current_state[self.Root_root_running].append(self.Root_root_running_listening_client)
    
    def exit_Root_root_running_listening_client(self):
        if self.Root_root_running_listening_client_listening_client in self.current_state[self.Root_root_running_listening_client] :
            self.exit_Root_root_running_listening_client_listening_client()
        self.current_state[self.Root_root_running] = []
    
    def enter_Root_root_initializing(self):
        self.current_state[self.Root_root].append(self.Root_root_initializing)
    
    def exit_Root_root_initializing(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_running_main_behaviour_running(self):
        self.current_state[self.Root_root_running_main_behaviour].append(self.Root_root_running_main_behaviour_running)
    
    def exit_Root_root_running_main_behaviour_running(self):
        self.current_state[self.Root_root_running_main_behaviour] = []
    
    def enter_Root_root_running_main_behaviour_creating_model_waiting(self):
        self.current_state[self.Root_root_running_main_behaviour_creating_model].append(self.Root_root_running_main_behaviour_creating_model_waiting)
    
    def exit_Root_root_running_main_behaviour_creating_model_waiting(self):
        self.current_state[self.Root_root_running_main_behaviour_creating_model] = []
    
    def enter_Root_root_running_main_behaviour_creating_model_entering_model_details(self):
        self.current_state[self.Root_root_running_main_behaviour_creating_model].append(self.Root_root_running_main_behaviour_creating_model_entering_model_details)
    
    def exit_Root_root_running_main_behaviour_creating_model_entering_model_details(self):
        self.current_state[self.Root_root_running_main_behaviour_creating_model] = []
    
    def enter_Root_root_running_main_behaviour_creating_model_waiting_client(self):
        self.current_state[self.Root_root_running_main_behaviour_creating_model].append(self.Root_root_running_main_behaviour_creating_model_waiting_client)
    
    def exit_Root_root_running_main_behaviour_creating_model_waiting_client(self):
        self.current_state[self.Root_root_running_main_behaviour_creating_model] = []
    
    def enter_Root_root_running_toolbar_behaviour_waiting(self):
        self.current_state[self.Root_root_running_toolbar_behaviour].append(self.Root_root_running_toolbar_behaviour_waiting)
    
    def exit_Root_root_running_toolbar_behaviour_waiting(self):
        self.current_state[self.Root_root_running_toolbar_behaviour] = []
    
    def enter_Root_root_running_toolbar_behaviour_creating(self):
        self.current_state[self.Root_root_running_toolbar_behaviour].append(self.Root_root_running_toolbar_behaviour_creating)
    
    def exit_Root_root_running_toolbar_behaviour_creating(self):
        self.current_state[self.Root_root_running_toolbar_behaviour] = []
    
    def enter_Root_root_running_window_behaviour_waiting(self):
        self.current_state[self.Root_root_running_window_behaviour].append(self.Root_root_running_window_behaviour_waiting)
    
    def exit_Root_root_running_window_behaviour_waiting(self):
        self.current_state[self.Root_root_running_window_behaviour] = []
    
    def enter_Root_root_running_window_behaviour_creating(self):
        self.current_state[self.Root_root_running_window_behaviour].append(self.Root_root_running_window_behaviour_creating)
    
    def exit_Root_root_running_window_behaviour_creating(self):
        self.current_state[self.Root_root_running_window_behaviour] = []
    
    def enter_Root_root_running_window_behaviour_starting(self):
        self.current_state[self.Root_root_running_window_behaviour].append(self.Root_root_running_window_behaviour_starting)
    
    def exit_Root_root_running_window_behaviour_starting(self):
        self.current_state[self.Root_root_running_window_behaviour] = []
    
    def enter_Root_root_running_listening_client_listening_client(self):
        self.current_state[self.Root_root_running_listening_client].append(self.Root_root_running_listening_client_listening_client)
    
    def exit_Root_root_running_listening_client_listening_client(self):
        self.current_state[self.Root_root_running_listening_client] = []
    
    def enter_Root_root_deleting(self):
        self.timers[0] = 0.05
        self.current_state[self.Root_root].append(self.Root_root_deleting)
    
    def exit_Root_root_deleting(self):
        self.timers.pop(0, None)
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_stopped(self):
        self.current_state[self.Root_root].append(self.Root_root_stopped)
    
    def exit_Root_root_stopped(self):
        self.current_state[self.Root_root] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_root(self):
        self.enter_Root_root()
        self.enter_Root_root_initializing()
    
    def enterDefault_Root_root_running(self):
        self.enter_Root_root_running()
        self.enterDefault_Root_root_running_main_behaviour()
        self.enterDefault_Root_root_running_toolbar_behaviour()
        self.enterDefault_Root_root_running_window_behaviour()
        self.enterDefault_Root_root_running_listening_client()
    
    def enterDefault_Root_root_running_main_behaviour(self):
        self.enter_Root_root_running_main_behaviour()
        self.enter_Root_root_running_main_behaviour_running()
    
    def enterDefault_Root_root_running_main_behaviour_creating_model(self):
        self.enter_Root_root_running_main_behaviour_creating_model()
        self.enter_Root_root_running_main_behaviour_creating_model_waiting()
    
    def enterDefault_Root_root_running_toolbar_behaviour(self):
        self.enter_Root_root_running_toolbar_behaviour()
        self.enter_Root_root_running_toolbar_behaviour_waiting()
    
    def enterDefault_Root_root_running_window_behaviour(self):
        self.enter_Root_root_running_window_behaviour()
        self.enter_Root_root_running_window_behaviour_waiting()
    
    def enterDefault_Root_root_running_listening_client(self):
        self.enter_Root_root_running_listening_client()
        self.enter_Root_root_running_listening_client_listening_client()
    
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
            if self.current_state[self.Root_root][0] == self.Root_root_initializing:
                catched = self.transition_Root_root_initializing(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_running:
                catched = self.transition_Root_root_running(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_deleting:
                catched = self.transition_Root_root_deleting(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_stopped:
                catched = self.transition_Root_root_stopped(event)
        return catched
    
    def transition_Root_root_initializing(self, event) :
        catched = False
        enableds = []
        if event.name == "set_association_name" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_initializing()
                self.association_name = association_name
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
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'toolbars' , send_event]))
                self.enter_Root_root_deleting()
            catched = True
        
        if not catched :
            catched = self.transition_Root_root_running_main_behaviour(event) or catched
            catched = self.transition_Root_root_running_toolbar_behaviour(event) or catched
            catched = self.transition_Root_root_running_window_behaviour(event) or catched
            catched = self.transition_Root_root_running_listening_client(event) or catched
        return catched
    
    def transition_Root_root_running_main_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_main_behaviour][0] == self.Root_root_running_main_behaviour_running:
                catched = self.transition_Root_root_running_main_behaviour_running(event)
            elif self.current_state[self.Root_root_running_main_behaviour][0] == self.Root_root_running_main_behaviour_creating_model:
                catched = self.transition_Root_root_running_main_behaviour_creating_model(event)
        return catched
    
    def transition_Root_root_running_main_behaviour_running(self, event) :
        catched = False
        enableds = []
        if event.name == "button_pressed" and event.getPort() == "" :
            parameters = event.getParameters()
            event_parameters = parameters[0]
            if event_parameters["event_name"] == "create_toolbar" :
                enableds.append(1)
        
        if event.name == "button_pressed" and event.getPort() == "" :
            parameters = event.getParameters()
            event_parameters = parameters[0]
            if event_parameters["event_name"] == "delete_toolbar" :
                enableds.append(2)
        
        if event.name == "button_pressed" and event.getPort() == "" :
            parameters = event.getParameters()
            event_parameters = parameters[0]
            if event_parameters["event_name"] == "create_model" :
                enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_running_main_behaviour_running()
                self.addEvent(Event("create_toolbar", parameters = [event_parameters]))
                self.enter_Root_root_running_main_behaviour_running()
            elif enabled == 2 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_running_main_behaviour_running()
                self.addEvent(Event("delete_toolbar", parameters = [event_parameters['association_name']]))
                self.enter_Root_root_running_main_behaviour_running()
            elif enabled == 3 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_running_main_behaviour_running()
                self.addEvent(Event("create_window", parameters = [{"class_name": "TypeModelBrowser", "constructor_parameters": {}}]))
                self.enterDefault_Root_root_running_main_behaviour_creating_model()
            catched = True
        
        return catched
    
    def transition_Root_root_running_main_behaviour_creating_model(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_main_behaviour_creating_model][0] == self.Root_root_running_main_behaviour_creating_model_waiting:
                catched = self.transition_Root_root_running_main_behaviour_creating_model_waiting(event)
            elif self.current_state[self.Root_root_running_main_behaviour_creating_model][0] == self.Root_root_running_main_behaviour_creating_model_entering_model_details:
                catched = self.transition_Root_root_running_main_behaviour_creating_model_entering_model_details(event)
            elif self.current_state[self.Root_root_running_main_behaviour_creating_model][0] == self.Root_root_running_main_behaviour_creating_model_waiting_client:
                catched = self.transition_Root_root_running_main_behaviour_creating_model_waiting_client(event)
        return catched
    
    def transition_Root_root_running_main_behaviour_creating_model_waiting(self, event) :
        catched = False
        enableds = []
        if event.name == "type_model_selected" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_creating_model_waiting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                formalism = parameters[0]
                self.exit_Root_root_running_main_behaviour_creating_model_waiting()
                self.addEvent(Event("create_window", parameters = [{"class_name": "NewInstanceAttributeEditor", "constructor_parameters": {"type": formalism}}]))
                self.enter_Root_root_running_main_behaviour_creating_model_entering_model_details()
            catched = True
        
        return catched
    
    def transition_Root_root_running_main_behaviour_creating_model_entering_model_details(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_details_entered" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_creating_model_entering_model_details. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                data = parameters[0]
                self.exit_Root_root_running_main_behaviour_creating_model_entering_model_details()
                send_event = Event("client_request", parameters = [self.association_name,{'event_name': 'create', 'request_parameters': {'data': data}}])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_running_main_behaviour_creating_model_waiting_client()
            catched = True
        
        return catched
    
    def transition_Root_root_running_main_behaviour_creating_model_waiting_client(self, event) :
        catched = False
        enableds = []
        if event.name == "client_response" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_main_behaviour_creating_model_waiting_client. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_running_main_behaviour_creating_model()
                self.enter_Root_root_running_main_behaviour_running()
            catched = True
        
        return catched
    
    def transition_Root_root_running_toolbar_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_toolbar_behaviour][0] == self.Root_root_running_toolbar_behaviour_waiting:
                catched = self.transition_Root_root_running_toolbar_behaviour_waiting(event)
            elif self.current_state[self.Root_root_running_toolbar_behaviour][0] == self.Root_root_running_toolbar_behaviour_creating:
                catched = self.transition_Root_root_running_toolbar_behaviour_creating(event)
        return catched
    
    def transition_Root_root_running_toolbar_behaviour_waiting(self, event) :
        catched = False
        enableds = []
        if event.name == "create_toolbar" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "delete_toolbar" and event.getPort() == "" :
            enableds.append(2)
        
        if event.name == "toolbar_created" and event.getPort() == "" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_toolbar_behaviour_waiting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_running_toolbar_behaviour_waiting()
                event_parameters["constructor_parameters"]["parent"] = self.toolbar_frame.interior
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "toolbars",event_parameters["class_name"],event_parameters["constructor_parameters"]]))
                self.enter_Root_root_running_toolbar_behaviour_creating()
            elif enabled == 2 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_toolbar_behaviour_waiting()
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, association_name]))
                self.enter_Root_root_running_toolbar_behaviour_waiting()
            elif enabled == 3 :
                parameters = event.getParameters()
                toolbar = parameters[0]
                self.exit_Root_root_running_toolbar_behaviour_waiting()
                toolbar.pack(side=tk.LEFT, fill=tk.Y, padx=self.INTER_SPACING, pady=self.INTER_SPACING)
                self.enter_Root_root_running_toolbar_behaviour_waiting()
            catched = True
        
        return catched
    
    def transition_Root_root_running_toolbar_behaviour_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_toolbar_behaviour_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_toolbar_behaviour_creating()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_root_running_toolbar_behaviour_waiting()
            catched = True
        
        return catched
    
    def transition_Root_root_running_window_behaviour(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_window_behaviour][0] == self.Root_root_running_window_behaviour_waiting:
                catched = self.transition_Root_root_running_window_behaviour_waiting(event)
            elif self.current_state[self.Root_root_running_window_behaviour][0] == self.Root_root_running_window_behaviour_creating:
                catched = self.transition_Root_root_running_window_behaviour_creating(event)
            elif self.current_state[self.Root_root_running_window_behaviour][0] == self.Root_root_running_window_behaviour_starting:
                catched = self.transition_Root_root_running_window_behaviour_starting(event)
        return catched
    
    def transition_Root_root_running_window_behaviour_waiting(self, event) :
        catched = False
        enableds = []
        if event.name == "create_window" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "delete_window" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_window_behaviour_waiting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_running_window_behaviour_waiting()
                event_parameters["constructor_parameters"]["parent"] = self
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "windows",event_parameters["class_name"],event_parameters["constructor_parameters"]]))
                self.enter_Root_root_running_window_behaviour_creating()
            elif enabled == 2 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_window_behaviour_waiting()
                self.object_manager.addEvent(Event("delete_instance", parameters = [self, association_name]))
                self.enter_Root_root_running_window_behaviour_waiting()
            catched = True
        
        return catched
    
    def transition_Root_root_running_window_behaviour_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_window_behaviour_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_window_behaviour_creating()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                self.enter_Root_root_running_window_behaviour_starting()
            catched = True
        
        return catched
    
    def transition_Root_root_running_window_behaviour_starting(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_started" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_window_behaviour_starting. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_running_window_behaviour_starting()
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_root_running_window_behaviour_waiting()
            catched = True
        
        return catched
    
    def transition_Root_root_running_listening_client(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_running_listening_client][0] == self.Root_root_running_listening_client_listening_client:
                catched = self.transition_Root_root_running_listening_client_listening_client(event)
        return catched
    
    def transition_Root_root_running_listening_client_listening_client(self, event) :
        catched = False
        enableds = []
        if event.name == "client_request" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running_listening_client_listening_client. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                data = parameters[1]
                self.exit_Root_root_running_listening_client_listening_client()
                send_event = Event("client_request", parameters = [self.association_name + '/' + association_name,data])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_running_listening_client_listening_client()
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
                send_event = Event("delete_window", parameters = [self.association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_stopped()
            catched = True
        
        return catched
    
    def transition_Root_root_stopped(self, event) :
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
    

class Toolbar(tk.Frame, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_idle = 1
    
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
        super(Toolbar, self).start()
        self.enter_Root_idle()
    
    #The actual constructor
    def __init__(self, controller, parent, name):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        tk.Frame.__init__(self, parent)
        
        self.config(relief=tk.RAISED, bd=1)
        
        tk.Label(self, text=name).pack(side=tk.TOP, pady=5)
    
    # User defined destructor
    def __del__(self):
        self.destroy()
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_idle(self):
        self.current_state[self.Root].append(self.Root_idle)
    
    def exit_Root_idle(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_idle:
                catched = self.transition_Root_idle(event)
        return catched
    
    def transition_Root_idle(self, event) :
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
    

class MainToolbar(Toolbar, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_root = 1
    Root_root_main_behaviour = 2
    Root_root_main_behaviour_creating_buttons = 3
    Root_root_main_behaviour_packing_buttons = 4
    Root_root_main_behaviour_listening = 5
    Root_root_main_behaviour_listening_client = 6
    Root_root_initializing = 7
    Root_root_main_behaviour_creating_buttons_loop = 8
    Root_root_main_behaviour_creating_buttons_creating = 9
    Root_root_main_behaviour_creating_buttons_running = 10
    Root_root_main_behaviour_packing_buttons_packing = 11
    Root_root_main_behaviour_listening_listening = 12
    Root_root_main_behaviour_listening_client_listening_client = 13
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_root] = []
        self.current_state[self.Root_root_main_behaviour] = []
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
        self.current_state[self.Root_root_main_behaviour_packing_buttons] = []
        self.current_state[self.Root_root_main_behaviour_listening] = []
        self.current_state[self.Root_root_main_behaviour_listening_client] = []
    
    def start(self):
        super(MainToolbar, self).start()
        self.enterDefault_Root_root()
    
    #The actual constructor
    def __init__(self, controller, constructor_parameters = {}):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        Toolbar.__init__(self, self.controller, constructor_parameters["parent"], 'Main')
        self.PADDING = 2
        self.buttons = [{"parent": self, "visual": ImageVisual('icons/new-icon.png'), "tooltip_text": 'Create New Model', "event_parameters": {"event_name": "create_model"}},
        				{"parent": self, "visual": ImageVisual('icons/load-type-model.png'), "tooltip_text": 'Load a Type Model', "event_parameters": {}},
        				{"parent": self, "visual": ImageVisual('icons/open-icon.png'), "tooltip_text": 'Open a Model', "event_parameters": {}},
        				{"parent": self, "visual": ImageVisual('icons/save-icon.png'), "tooltip_text": 'Save Modelverse', "event_parameters": {}},
        				{"parent": self, "visual": ImageVisual('icons/undo-icon.png'), "tooltip_text": 'Undo', "event_parameters": {}},
        				{"parent": self, "visual": ImageVisual('icons/redo-icon.png'), "tooltip_text": 'Redo', "event_parameters": {}}]
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_root(self):
        self.current_state[self.Root].append(self.Root_root)
    
    def exit_Root_root(self):
        if self.Root_root_initializing in self.current_state[self.Root_root] :
            self.exit_Root_root_initializing()
        if self.Root_root_main_behaviour in self.current_state[self.Root_root] :
            self.exit_Root_root_main_behaviour()
        self.current_state[self.Root] = []
    
    def enter_Root_root_main_behaviour(self):
        self.current_state[self.Root_root].append(self.Root_root_main_behaviour)
    
    def exit_Root_root_main_behaviour(self):
        self.exit_Root_root_main_behaviour_creating_buttons()
        self.exit_Root_root_main_behaviour_packing_buttons()
        self.exit_Root_root_main_behaviour_listening()
        self.exit_Root_root_main_behaviour_listening_client()
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_main_behaviour_creating_buttons(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_creating_buttons)
    
    def exit_Root_root_main_behaviour_creating_buttons(self):
        if self.Root_root_main_behaviour_creating_buttons_loop in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_loop()
        if self.Root_root_main_behaviour_creating_buttons_creating in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_creating()
        if self.Root_root_main_behaviour_creating_buttons_running in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_running()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_main_behaviour_packing_buttons(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_packing_buttons)
    
    def exit_Root_root_main_behaviour_packing_buttons(self):
        if self.Root_root_main_behaviour_packing_buttons_packing in self.current_state[self.Root_root_main_behaviour_packing_buttons] :
            self.exit_Root_root_main_behaviour_packing_buttons_packing()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_main_behaviour_listening(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_listening)
    
    def exit_Root_root_main_behaviour_listening(self):
        if self.Root_root_main_behaviour_listening_listening in self.current_state[self.Root_root_main_behaviour_listening] :
            self.exit_Root_root_main_behaviour_listening_listening()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_main_behaviour_listening_client(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_listening_client)
    
    def exit_Root_root_main_behaviour_listening_client(self):
        if self.Root_root_main_behaviour_listening_client_listening_client in self.current_state[self.Root_root_main_behaviour_listening_client] :
            self.exit_Root_root_main_behaviour_listening_client_listening_client()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_initializing(self):
        self.current_state[self.Root_root].append(self.Root_root_initializing)
    
    def exit_Root_root_initializing(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_loop)
    
    def exit_Root_root_main_behaviour_creating_buttons_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_creating)
    
    def exit_Root_root_main_behaviour_creating_buttons_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_running)
    
    def exit_Root_root_main_behaviour_creating_buttons_running(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_packing_buttons_packing(self):
        self.current_state[self.Root_root_main_behaviour_packing_buttons].append(self.Root_root_main_behaviour_packing_buttons_packing)
    
    def exit_Root_root_main_behaviour_packing_buttons_packing(self):
        self.current_state[self.Root_root_main_behaviour_packing_buttons] = []
    
    def enter_Root_root_main_behaviour_listening_listening(self):
        self.current_state[self.Root_root_main_behaviour_listening].append(self.Root_root_main_behaviour_listening_listening)
    
    def exit_Root_root_main_behaviour_listening_listening(self):
        self.current_state[self.Root_root_main_behaviour_listening] = []
    
    def enter_Root_root_main_behaviour_listening_client_listening_client(self):
        self.current_state[self.Root_root_main_behaviour_listening_client].append(self.Root_root_main_behaviour_listening_client_listening_client)
    
    def exit_Root_root_main_behaviour_listening_client_listening_client(self):
        self.current_state[self.Root_root_main_behaviour_listening_client] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_root(self):
        self.enter_Root_root()
        self.enter_Root_root_initializing()
    
    def enterDefault_Root_root_main_behaviour(self):
        self.enter_Root_root_main_behaviour()
        self.enterDefault_Root_root_main_behaviour_creating_buttons()
        self.enterDefault_Root_root_main_behaviour_packing_buttons()
        self.enterDefault_Root_root_main_behaviour_listening()
        self.enterDefault_Root_root_main_behaviour_listening_client()
    
    def enterDefault_Root_root_main_behaviour_creating_buttons(self):
        self.enter_Root_root_main_behaviour_creating_buttons()
        self.enter_Root_root_main_behaviour_creating_buttons_loop()
    
    def enterDefault_Root_root_main_behaviour_packing_buttons(self):
        self.enter_Root_root_main_behaviour_packing_buttons()
        self.enter_Root_root_main_behaviour_packing_buttons_packing()
    
    def enterDefault_Root_root_main_behaviour_listening(self):
        self.enter_Root_root_main_behaviour_listening()
        self.enter_Root_root_main_behaviour_listening_listening()
    
    def enterDefault_Root_root_main_behaviour_listening_client(self):
        self.enter_Root_root_main_behaviour_listening_client()
        self.enter_Root_root_main_behaviour_listening_client_listening_client()
    
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
            if self.current_state[self.Root_root][0] == self.Root_root_initializing:
                catched = self.transition_Root_root_initializing(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_main_behaviour:
                catched = self.transition_Root_root_main_behaviour(event)
        return catched
    
    def transition_Root_root_initializing(self, event) :
        catched = False
        enableds = []
        if event.name == "set_association_name" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_initializing()
                self.association_name = association_name
                send_event = Event("toolbar_created", parameters = [self])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enterDefault_Root_root_main_behaviour()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour(self, event) :
        catched = False
        if not catched :
            catched = self.transition_Root_root_main_behaviour_creating_buttons(event) or catched
            catched = self.transition_Root_root_main_behaviour_packing_buttons(event) or catched
            catched = self.transition_Root_root_main_behaviour_listening(event) or catched
            catched = self.transition_Root_root_main_behaviour_listening_client(event) or catched
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_loop:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_loop(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_creating:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_creating(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_running:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running(event)
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_loop(self, event) :
        catched = False
        enableds = []
        if self.buttons :
            enableds.append(1)
        
        if not self.buttons :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_loop. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour_creating_buttons_loop()
                ctor_parameters = self.buttons.pop(0)
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "buttons","Button",ctor_parameters]))
                self.enter_Root_root_main_behaviour_creating_buttons_creating()
            elif enabled == 2 :
                self.exit_Root_root_main_behaviour_creating_buttons_loop()
                self.enter_Root_root_main_behaviour_creating_buttons_running()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_creating()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_root_main_behaviour_creating_buttons_loop()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running(self, event) :
        catched = False
        return catched
    
    def transition_Root_root_main_behaviour_packing_buttons(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_packing_buttons][0] == self.Root_root_main_behaviour_packing_buttons_packing:
                catched = self.transition_Root_root_main_behaviour_packing_buttons_packing(event)
        return catched
    
    def transition_Root_root_main_behaviour_packing_buttons_packing(self, event) :
        catched = False
        enableds = []
        if event.name == "button_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_packing_buttons_packing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                button = parameters[0]
                self.exit_Root_root_main_behaviour_packing_buttons_packing()
                button.pack(side=tk.LEFT, fill=tk.Y, padx=self.PADDING)
                self.enter_Root_root_main_behaviour_packing_buttons_packing()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_listening(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_listening][0] == self.Root_root_main_behaviour_listening_listening:
                catched = self.transition_Root_root_main_behaviour_listening_listening(event)
        return catched
    
    def transition_Root_root_main_behaviour_listening_listening(self, event) :
        catched = False
        enableds = []
        if event.name == "button_pressed" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_listening_listening. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_main_behaviour_listening_listening()
                send_event = Event("button_pressed", parameters = [event_parameters])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_main_behaviour_listening_listening()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_listening_client(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_listening_client][0] == self.Root_root_main_behaviour_listening_client_listening_client:
                catched = self.transition_Root_root_main_behaviour_listening_client_listening_client(event)
        return catched
    
    def transition_Root_root_main_behaviour_listening_client_listening_client(self, event) :
        catched = False
        enableds = []
        if event.name == "client_request" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_listening_client_listening_client. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                data = parameters[1]
                self.exit_Root_root_main_behaviour_listening_client_listening_client()
                send_event = Event("client_request", parameters = [self.association_name + '/' + association_name,data])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_main_behaviour_listening_client_listening_client()
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
    

class FormalismToolbar(Toolbar, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_root = 1
    Root_root_main_behaviour = 2
    Root_root_main_behaviour_creating_buttons = 3
    Root_root_main_behaviour_packing_buttons = 4
    Root_root_main_behaviour_listening = 5
    Root_root_main_behaviour_listening_client = 6
    Root_root_initializing = 7
    Root_root_main_behaviour_creating_buttons_reading_formalism = 8
    Root_root_main_behaviour_creating_buttons_waiting_client = 9
    Root_root_main_behaviour_creating_buttons_loop = 10
    Root_root_main_behaviour_creating_buttons_creating = 11
    Root_root_main_behaviour_creating_buttons_running = 12
    Root_root_main_behaviour_packing_buttons_packing = 13
    Root_root_main_behaviour_listening_listening = 14
    Root_root_main_behaviour_listening_client_listening_client = 15
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_root] = []
        self.current_state[self.Root_root_main_behaviour] = []
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
        self.current_state[self.Root_root_main_behaviour_packing_buttons] = []
        self.current_state[self.Root_root_main_behaviour_listening] = []
        self.current_state[self.Root_root_main_behaviour_listening_client] = []
    
    def start(self):
        super(FormalismToolbar, self).start()
        self.enterDefault_Root_root()
    
    #The actual constructor
    def __init__(self, controller, constructor_parameters = {}):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.formalism = constructor_parameters["formalism"]
        Toolbar.__init__(self, self.controller, constructor_parameters["parent"], self.formalism.name)
        self.i = 0
        self.buttons = []
        self.PADDING = 2
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_root(self):
        self.current_state[self.Root].append(self.Root_root)
    
    def exit_Root_root(self):
        if self.Root_root_initializing in self.current_state[self.Root_root] :
            self.exit_Root_root_initializing()
        if self.Root_root_main_behaviour in self.current_state[self.Root_root] :
            self.exit_Root_root_main_behaviour()
        self.current_state[self.Root] = []
    
    def enter_Root_root_main_behaviour(self):
        self.current_state[self.Root_root].append(self.Root_root_main_behaviour)
    
    def exit_Root_root_main_behaviour(self):
        self.exit_Root_root_main_behaviour_creating_buttons()
        self.exit_Root_root_main_behaviour_packing_buttons()
        self.exit_Root_root_main_behaviour_listening()
        self.exit_Root_root_main_behaviour_listening_client()
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_main_behaviour_creating_buttons(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_creating_buttons)
    
    def exit_Root_root_main_behaviour_creating_buttons(self):
        if self.Root_root_main_behaviour_creating_buttons_reading_formalism in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_reading_formalism()
        if self.Root_root_main_behaviour_creating_buttons_waiting_client in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_waiting_client()
        if self.Root_root_main_behaviour_creating_buttons_loop in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_loop()
        if self.Root_root_main_behaviour_creating_buttons_creating in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_creating()
        if self.Root_root_main_behaviour_creating_buttons_running in self.current_state[self.Root_root_main_behaviour_creating_buttons] :
            self.exit_Root_root_main_behaviour_creating_buttons_running()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_main_behaviour_packing_buttons(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_packing_buttons)
    
    def exit_Root_root_main_behaviour_packing_buttons(self):
        if self.Root_root_main_behaviour_packing_buttons_packing in self.current_state[self.Root_root_main_behaviour_packing_buttons] :
            self.exit_Root_root_main_behaviour_packing_buttons_packing()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_main_behaviour_listening(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_listening)
    
    def exit_Root_root_main_behaviour_listening(self):
        if self.Root_root_main_behaviour_listening_listening in self.current_state[self.Root_root_main_behaviour_listening] :
            self.exit_Root_root_main_behaviour_listening_listening()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_main_behaviour_listening_client(self):
        self.current_state[self.Root_root_main_behaviour].append(self.Root_root_main_behaviour_listening_client)
    
    def exit_Root_root_main_behaviour_listening_client(self):
        if self.Root_root_main_behaviour_listening_client_listening_client in self.current_state[self.Root_root_main_behaviour_listening_client] :
            self.exit_Root_root_main_behaviour_listening_client_listening_client()
        self.current_state[self.Root_root_main_behaviour] = []
    
    def enter_Root_root_initializing(self):
        self.current_state[self.Root_root].append(self.Root_root_initializing)
    
    def exit_Root_root_initializing(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_reading_formalism(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_reading_formalism)
    
    def exit_Root_root_main_behaviour_creating_buttons_reading_formalism(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_waiting_client(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_waiting_client)
    
    def exit_Root_root_main_behaviour_creating_buttons_waiting_client(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_loop)
    
    def exit_Root_root_main_behaviour_creating_buttons_loop(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_creating)
    
    def exit_Root_root_main_behaviour_creating_buttons_creating(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_creating_buttons_running(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons].append(self.Root_root_main_behaviour_creating_buttons_running)
    
    def exit_Root_root_main_behaviour_creating_buttons_running(self):
        self.current_state[self.Root_root_main_behaviour_creating_buttons] = []
    
    def enter_Root_root_main_behaviour_packing_buttons_packing(self):
        self.current_state[self.Root_root_main_behaviour_packing_buttons].append(self.Root_root_main_behaviour_packing_buttons_packing)
    
    def exit_Root_root_main_behaviour_packing_buttons_packing(self):
        self.current_state[self.Root_root_main_behaviour_packing_buttons] = []
    
    def enter_Root_root_main_behaviour_listening_listening(self):
        self.current_state[self.Root_root_main_behaviour_listening].append(self.Root_root_main_behaviour_listening_listening)
    
    def exit_Root_root_main_behaviour_listening_listening(self):
        self.current_state[self.Root_root_main_behaviour_listening] = []
    
    def enter_Root_root_main_behaviour_listening_client_listening_client(self):
        self.current_state[self.Root_root_main_behaviour_listening_client].append(self.Root_root_main_behaviour_listening_client_listening_client)
    
    def exit_Root_root_main_behaviour_listening_client_listening_client(self):
        self.current_state[self.Root_root_main_behaviour_listening_client] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_root(self):
        self.enter_Root_root()
        self.enter_Root_root_initializing()
    
    def enterDefault_Root_root_main_behaviour(self):
        self.enter_Root_root_main_behaviour()
        self.enterDefault_Root_root_main_behaviour_creating_buttons()
        self.enterDefault_Root_root_main_behaviour_packing_buttons()
        self.enterDefault_Root_root_main_behaviour_listening()
        self.enterDefault_Root_root_main_behaviour_listening_client()
    
    def enterDefault_Root_root_main_behaviour_creating_buttons(self):
        self.enter_Root_root_main_behaviour_creating_buttons()
        self.enter_Root_root_main_behaviour_creating_buttons_reading_formalism()
    
    def enterDefault_Root_root_main_behaviour_packing_buttons(self):
        self.enter_Root_root_main_behaviour_packing_buttons()
        self.enter_Root_root_main_behaviour_packing_buttons_packing()
    
    def enterDefault_Root_root_main_behaviour_listening(self):
        self.enter_Root_root_main_behaviour_listening()
        self.enter_Root_root_main_behaviour_listening_listening()
    
    def enterDefault_Root_root_main_behaviour_listening_client(self):
        self.enter_Root_root_main_behaviour_listening_client()
        self.enter_Root_root_main_behaviour_listening_client_listening_client()
    
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
            if self.current_state[self.Root_root][0] == self.Root_root_initializing:
                catched = self.transition_Root_root_initializing(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_main_behaviour:
                catched = self.transition_Root_root_main_behaviour(event)
        return catched
    
    def transition_Root_root_initializing(self, event) :
        catched = False
        enableds = []
        if event.name == "set_association_name" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_initializing()
                self.association_name = association_name
                send_event = Event("toolbar_created", parameters = [self])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enterDefault_Root_root_main_behaviour()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour(self, event) :
        catched = False
        if not catched :
            catched = self.transition_Root_root_main_behaviour_creating_buttons(event) or catched
            catched = self.transition_Root_root_main_behaviour_packing_buttons(event) or catched
            catched = self.transition_Root_root_main_behaviour_listening(event) or catched
            catched = self.transition_Root_root_main_behaviour_listening_client(event) or catched
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_reading_formalism:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_reading_formalism(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_waiting_client:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_waiting_client(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_loop:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_loop(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_creating:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_creating(event)
            elif self.current_state[self.Root_root_main_behaviour_creating_buttons][0] == self.Root_root_main_behaviour_creating_buttons_running:
                catched = self.transition_Root_root_main_behaviour_creating_buttons_running(event)
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_reading_formalism(self, event) :
        catched = False
        enableds = []
        if self.i < len(self.formalism.elements) :
            enableds.append(1)
        
        if self.i == len(self.formalism.elements) :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_reading_formalism. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour_creating_buttons_reading_formalism()
                send_event = Event("client_request", parameters = [self.association_name,{'event_name': 'read', 'request_parameters': {'data': self.formalism.elements[self.i][1]}}])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.i += 1
                self.enter_Root_root_main_behaviour_creating_buttons_waiting_client()
            elif enabled == 2 :
                self.exit_Root_root_main_behaviour_creating_buttons_reading_formalism()
                self.enter_Root_root_main_behaviour_creating_buttons_loop()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_waiting_client(self, event) :
        catched = False
        enableds = []
        if event.name == "client_response" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_waiting_client. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                result = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_waiting_client()
                item = result[StringValue("item")]
                if isinstance(item, client_object.Clabject) and item.potency > IntegerValue(0) and not isinstance(item, client_object.Composition) and not item.abstract:
                	self.buttons.append({"parent": self, "visual": TextVisual(item.name), "tooltip_text": 'Create New %s' % item.name, "event_parameters": {"event_name": "create_instance", "type": item}})
                self.enter_Root_root_main_behaviour_creating_buttons_reading_formalism()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_loop(self, event) :
        catched = False
        enableds = []
        if self.buttons :
            enableds.append(1)
        
        if not self.buttons :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_loop. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_root_main_behaviour_creating_buttons_loop()
                ctor_parameters = self.buttons.pop(0)
                self.object_manager.addEvent(Event("create_instance", parameters = [self, "buttons","Button",ctor_parameters]))
                self.enter_Root_root_main_behaviour_creating_buttons_creating()
            elif enabled == 2 :
                self.exit_Root_root_main_behaviour_creating_buttons_loop()
                self.enter_Root_root_main_behaviour_creating_buttons_running()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_creating(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_creating_buttons_creating. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_main_behaviour_creating_buttons_creating()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, association_name]))
                send_event = Event("set_association_name", parameters = [association_name])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_root_main_behaviour_creating_buttons_loop()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_creating_buttons_running(self, event) :
        catched = False
        return catched
    
    def transition_Root_root_main_behaviour_packing_buttons(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_packing_buttons][0] == self.Root_root_main_behaviour_packing_buttons_packing:
                catched = self.transition_Root_root_main_behaviour_packing_buttons_packing(event)
        return catched
    
    def transition_Root_root_main_behaviour_packing_buttons_packing(self, event) :
        catched = False
        enableds = []
        if event.name == "button_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_packing_buttons_packing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                button = parameters[0]
                self.exit_Root_root_main_behaviour_packing_buttons_packing()
                button.pack(side=tk.LEFT, fill=tk.Y, padx=self.PADDING)
                self.enter_Root_root_main_behaviour_packing_buttons_packing()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_listening(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_listening][0] == self.Root_root_main_behaviour_listening_listening:
                catched = self.transition_Root_root_main_behaviour_listening_listening(event)
        return catched
    
    def transition_Root_root_main_behaviour_listening_listening(self, event) :
        catched = False
        enableds = []
        if event.name == "button_pressed" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_listening_listening. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                event_parameters = parameters[0]
                self.exit_Root_root_main_behaviour_listening_listening()
                send_event = Event("button_pressed", parameters = [event_parameters])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_main_behaviour_listening_listening()
            catched = True
        
        return catched
    
    def transition_Root_root_main_behaviour_listening_client(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_root_main_behaviour_listening_client][0] == self.Root_root_main_behaviour_listening_client_listening_client:
                catched = self.transition_Root_root_main_behaviour_listening_client_listening_client(event)
        return catched
    
    def transition_Root_root_main_behaviour_listening_client_listening_client(self, event) :
        catched = False
        enableds = []
        if event.name == "client_request" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_main_behaviour_listening_client_listening_client. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                data = parameters[1]
                self.exit_Root_root_main_behaviour_listening_client_listening_client()
                send_event = Event("client_request", parameters = [self.association_name + '/' + association_name,data])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_main_behaviour_listening_client_listening_client()
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
    

class Button(MvKWidget, tk.Button, RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_root = 1
    Root_root_initializing = 2
    Root_root_running = 3
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        RuntimeClassBase.__init__(self)
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_root] = []
    
    def start(self):
        super(Button, self).start()
        self.enterDefault_Root_root()
    
    #The actual constructor
    def __init__(self, controller, constructor_parameters = {}):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        tk.Button.__init__(self, constructor_parameters["parent"], **(constructor_parameters["visual"].get_params()))
        MvKWidget.__init__(self, self.controller)
        self.event_parameters = constructor_parameters["event_parameters"]
        self.tooltip = ToolTip(self, constructor_parameters["tooltip_text"])
        self.visual = constructor_parameters["visual"]
    
    # User defined destructor
    def __del__(self):
        self.destroy()
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_root(self):
        self.current_state[self.Root].append(self.Root_root)
    
    def exit_Root_root(self):
        if self.Root_root_initializing in self.current_state[self.Root_root] :
            self.exit_Root_root_initializing()
        if self.Root_root_running in self.current_state[self.Root_root] :
            self.exit_Root_root_running()
        self.current_state[self.Root] = []
    
    def enter_Root_root_initializing(self):
        self.current_state[self.Root_root].append(self.Root_root_initializing)
    
    def exit_Root_root_initializing(self):
        self.current_state[self.Root_root] = []
    
    def enter_Root_root_running(self):
        self.current_state[self.Root_root].append(self.Root_root_running)
    
    def exit_Root_root_running(self):
        self.current_state[self.Root_root] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_root(self):
        self.enter_Root_root()
        self.enter_Root_root_initializing()
    
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
            if self.current_state[self.Root_root][0] == self.Root_root_initializing:
                catched = self.transition_Root_root_initializing(event)
            elif self.current_state[self.Root_root][0] == self.Root_root_running:
                catched = self.transition_Root_root_running(event)
        return catched
    
    def transition_Root_root_initializing(self, event) :
        catched = False
        enableds = []
        if event.name == "set_association_name" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_initializing. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_root_initializing()
                self.association_name = association_name
                send_event = Event("button_created", parameters = [self])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_running()
            catched = True
        
        return catched
    
    def transition_Root_root_running(self, event) :
        catched = False
        enableds = []
        if event.name == "left-click" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(1)
        
        if event.name == "enter" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(2)
        
        if event.name == "leave" and event.getPort() == "input" :
            parameters = event.getParameters()
            tagorid = parameters[0]
            if tagorid == id(self) :
                enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_root_running. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_root_running()
                send_event = Event("button_pressed", parameters = [self.event_parameters])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, 'parent' , send_event]))
                self.enter_Root_root_running()
            elif enabled == 2 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_root_running()
                self.tooltip.showtip()
                self.enter_Root_root_running()
            elif enabled == 3 :
                parameters = event.getParameters()
                tagorid = parameters[0]
                self.exit_Root_root_running()
                self.tooltip.hidetip()
                self.enter_Root_root_running()
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
    

class MvKClient(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_main = 1
    
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
        super(MvKClient, self).start()
        self.enter_Root_main()
    
    #The actual constructor
    def __init__(self, controller):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.requesturl = "http://%s:%s/" % (host, port)
        self.encoder = MvKEncoder()
        self.decoder = MvKDecoder()
    
    # User defined method
    def requestGET(self, function, data):
        query = "?func=" + function + "&args=" + urllib.quote(data)
        response = urllib2.urlopen(self.requesturl + query)
        response = response.read()
        return self.decoder.decode(response)
        
    # User defined method
    def requestPOST(self, function, data):
        query = "func=" + function + "&args=" + str(data)
        response = urllib2.urlopen(self.requesturl, query)
        return self.decoder.decode(response.read())
        
    # Statechart enter/exit action method(s) :
    
    def enter_Root_main(self):
        self.current_state[self.Root].append(self.Root_main)
    
    def exit_Root_main(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_main:
                catched = self.transition_Root_main(event)
        return catched
    
    def transition_Root_main(self, event) :
        catched = False
        enableds = []
        if event.name == "read" and event.getPort() == "" :
            enableds.append(1)
        
        if event.name == "create" and event.getPort() == "" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "" :
            enableds.append(3)
        
        if event.name == "delete" and event.getPort() == "" :
            enableds.append(4)
        
        if event.name == "clear" and event.getPort() == "" :
            enableds.append(5)
        
        if event.name == "conforms_to" and event.getPort() == "" :
            enableds.append(6)
        
        if event.name == "evaluate" and event.getPort() == "" :
            enableds.append(7)
        
        if event.name == "backup" and event.getPort() == "" :
            enableds.append(8)
        
        if event.name == "restore" and event.getPort() == "" :
            enableds.append(9)
        
        if event.name == "run" and event.getPort() == "" :
            enableds.append(10)
        
        if event.name == "execute" and event.getPort() == "" :
            enableds.append(11)
        
        if event.name == "apply" and event.getPort() == "" :
            enableds.append(12)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_main. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                parameters = event.getParameters()
                association_name = parameters[0]
                data = parameters[1]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestGET('read', self.encoder.encode(data))])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 2 :
                parameters = event.getParameters()
                association_name = parameters[0]
                data = parameters[1]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('create', self.encoder.encode(data))])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 3 :
                parameters = event.getParameters()
                association_name = parameters[0]
                data = parameters[1]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('update', self.encoder.encode(data))])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 4 :
                parameters = event.getParameters()
                association_name = parameters[0]
                data = parameters[1]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('delete', self.encoder.encode(data))])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 5 :
                parameters = event.getParameters()
                association_name = parameters[0]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('clear', [[], {}])])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 6 :
                parameters = event.getParameters()
                association_name = parameters[0]
                model = parameters[1]
                type_model = parameters[2]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('conforms_to', '[[' + self.encoder.encode(model) + ', ' + self.encoder.encode(type_model) + '], {}]')])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 7 :
                parameters = event.getParameters()
                association_name = parameters[0]
                args = parameters[1]
                kwargs = parameters[2]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('evaluate', '[' + self.encoder.encode(args) + ', ' + self.encoder.encode(kwargs) + ']')])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 8 :
                parameters = event.getParameters()
                association_name = parameters[0]
                filename = parameters[1]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('backup', '[[' + self.encoder.encode(filename) + '], {}]')])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 9 :
                parameters = event.getParameters()
                association_name = parameters[0]
                filename = parameters[1]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('restore', '[[' + self.encoder.encode(filename) + '], {}]')])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 10 :
                parameters = event.getParameters()
                association_name = parameters[0]
                opname = parameters[1]
                kwargs = parameters[2]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('run', '[[' + self.encoder.encode(opname) + '], {' + self.encoder.encode(kwargs) + '}]')])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 11 :
                parameters = event.getParameters()
                association_name = parameters[0]
                location = parameters[1]
                args = parameters[2]
                self.exit_Root_main()
                new_args = [location]
                new_args.extend(args)
                send_event = Event("client_response", parameters = [self.requestPOST('execute', '[' + self.encoder.encode(new_args) + ', {}]')])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
            elif enabled == 12 :
                parameters = event.getParameters()
                association_name = parameters[0]
                params = parameters[1]
                self.exit_Root_main()
                send_event = Event("client_response", parameters = [self.requestPOST('apply', '[[' + self.encoder.encode(params) + '], {}]')])
                self.object_manager.addEvent(Event("narrow_cast", parameters = [self, association_name , send_event]))
                self.enter_Root_main()
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
        if class_name == "MvKFrontend" :
            instance =  MvKFrontend(self.controller, *construct_params)
            associations.append(Association("windows", "Window", 0, -1))
            associations.append(Association("client", "Client", 1, 1))
        elif class_name == "Window" :
            instance =  Window(self.controller, *construct_params)
        elif class_name == "NewInstanceAttributeEditor" :
            instance =  NewInstanceAttributeEditor(self.controller, *construct_params)
            associations.append(Association("editors", "AttributeEditors", 0, -1))
            associations.append(Association("parent", "Window", 1, 1))
        elif class_name == "Editor" :
            instance =  Editor(*construct_params)
        elif class_name == "EntryEditor" :
            instance =  EntryEditor(*construct_params)
        elif class_name == "StringEditor" :
            instance =  StringEditor(self.controller, *construct_params)
        elif class_name == "NumericEditor" :
            instance =  NumericEditor(self.controller, *construct_params)
        elif class_name == "AnyEditor" :
            instance =  AnyEditor(self.controller, *construct_params)
        elif class_name == "BooleanEditor" :
            instance =  BooleanEditor(self.controller, *construct_params)
        elif class_name == "TypeModelBrowser" :
            instance =  TypeModelBrowser(self.controller, *construct_params)
            associations.append(Association("buttons", "Button", 0, -1))
            associations.append(Association("labels", "Label", 0, -1))
            associations.append(Association("parent", "Window", 1, 1))
        elif class_name == "Label" :
            instance =  Label(self.controller, *construct_params)
            associations.append(Association("widgets", "MvKWidget", 0, -1))
            associations.append(Association("parent", "Window", 1, 1))
        elif class_name == "ModelEditor" :
            instance =  ModelEditor(self.controller, *construct_params)
            associations.append(Association("toolbars", "Toolbar", 0, -1))
            associations.append(Association("windows", "Window", 0, -1))
            associations.append(Association("parent", "MvKFrontEnd", 1, 1))
        elif class_name == "Toolbar" :
            instance =  Toolbar(self.controller, *construct_params)
            associations.append(Association("buttons", "Button", 0, -1))
        elif class_name == "MainToolbar" :
            instance =  MainToolbar(self.controller, *construct_params)
            associations.append(Association("buttons", "Button", 0, -1))
            associations.append(Association("parent", "Window", 0, -1))
        elif class_name == "FormalismToolbar" :
            instance =  FormalismToolbar(self.controller, *construct_params)
            associations.append(Association("buttons", "Button", 0, -1))
            associations.append(Association("parent", "Window", 0, -1))
        elif class_name == "Button" :
            instance =  Button(self.controller, *construct_params)
            associations.append(Association("parent", "Toolbar", 1, 1))
        elif class_name == "MvKClient" :
            instance =  MvKClient(self.controller, *construct_params)
            associations.append(Association("parent", "FrontEnd", 0, -1))
        if instance:
            return InstanceWrapper(instance, associations)
        else :
            return None

from python_runtime.statecharts_core import GameLoopControllerBase
class Controller(GameLoopControllerBase):
    def __init__(self, keep_running = True):
        super(Controller, self).__init__(ObjectManager(self), keep_running)
        self.addInputPort("input")
        self.object_manager.createInstance("MvKFrontend", [])
        
def main():
    controller = Controller()
    controller.start()

if __name__ == "__main__":
    main()
