# Statechart compiler by Glenn De Jonghe
#
# Date:   Mon Jul 21 10:45:51 2014

# Model author: Glenn De Jonghe
# Model name:   Player Tank
# Model description:
"""
    Handling the player tank.
"""

from python_runtime.statecharts_core import ObjectManagerBase, Event, InstanceWrapper, RuntimeClassBase, Association


class Main(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_state_1 = 1
    Root_state_2 = 2
    Root_state_3 = 3
    Root_state_4 = 4
    Root_end = 5
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(Main, self).__init__()
        # User defined attributes
        self.tank = None
        
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
    def __init__(self, controller, tank):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_state_1(self):
        self.current_state[self.Root].append(self.Root_state_1)
    
    def exit_Root_state_1(self):
        self.current_state[self.Root] = []
    
    def enter_Root_state_2(self):
        self.current_state[self.Root].append(self.Root_state_2)
    
    def exit_Root_state_2(self):
        self.current_state[self.Root] = []
    
    def enter_Root_state_3(self):
        self.current_state[self.Root].append(self.Root_state_3)
    
    def exit_Root_state_3(self):
        self.current_state[self.Root] = []
    
    def enter_Root_state_4(self):
        self.current_state[self.Root].append(self.Root_state_4)
    
    def exit_Root_state_4(self):
        self.current_state[self.Root] = []
    
    def enter_Root_end(self):
        self.current_state[self.Root].append(self.Root_end)
    
    def exit_Root_end(self):
        self.current_state[self.Root] = []
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_state_1:
                catched = self.transition_Root_state_1(event)
            elif self.current_state[self.Root][0] == self.Root_state_2:
                catched = self.transition_Root_state_2(event)
            elif self.current_state[self.Root][0] == self.Root_state_3:
                catched = self.transition_Root_state_3(event)
            elif self.current_state[self.Root][0] == self.Root_state_4:
                catched = self.transition_Root_state_4(event)
            elif self.current_state[self.Root][0] == self.Root_end:
                catched = self.transition_Root_end(event)
        return catched
    
    def transition_Root_state_1(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_state_1. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_state_1()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'cannon',self.tank]))
                self.enter_Root_state_2()
            catched = True
        
        return catched
    
    def transition_Root_state_2(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_state_2. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_state_2()
                self.enter_Root_state_3()
            catched = True
        
        return catched
    
    def transition_Root_state_3(self, event) :
        catched = False
        enableds = []
        enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_state_3. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_state_3()
                self.object_manager.addEvent(Event("create_instance", parameters = [self, 'body',self.tank]))
                self.enter_Root_state_4()
            catched = True
        
        return catched
    
    def transition_Root_state_4(self, event) :
        catched = False
        enableds = []
        if event.name == "instance_created" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_state_4. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_state_4()
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'cannon']))
                self.object_manager.addEvent(Event("start_instance", parameters = [self, 'body']))
                self.enter_Root_end()
            catched = True
        
        return catched
    
    def transition_Root_end(self, event) :
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
    

class Cannon(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_container = 1
    Root_container_rotating = 2
    Root_container_shoot = 3
    Root_container_ammo = 4
    Root_container_rotating_none = 5
    Root_container_rotating_left = 6
    Root_container_rotating_both = 7
    Root_container_rotating_right = 8
    Root_container_shoot_hold = 9
    Root_container_shoot_shoot = 10
    Root_container_ammo_loaded = 11
    Root_container_ammo_unloaded = 12
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(Cannon, self).__init__()
        # User defined attributes
        self.tank = None
        self.reload_time = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        self.timers = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_container] = []
        self.current_state[self.Root_container_rotating] = []
        self.current_state[self.Root_container_shoot] = []
        self.current_state[self.Root_container_ammo] = []
    
    def start(self):
        super(Cannon, self).start()
        self.enterDefault_Root_container()
    
    #The actual constructor
    def __init__(self, controller, tank):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
        self.reload_time = tank.getReloadTime()
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_container(self):
        self.current_state[self.Root].append(self.Root_container)
    
    def exit_Root_container(self):
        self.exit_Root_container_rotating()
        self.exit_Root_container_shoot()
        self.exit_Root_container_ammo()
        self.current_state[self.Root] = []
    
    def enter_Root_container_rotating(self):
        self.current_state[self.Root_container].append(self.Root_container_rotating)
    
    def exit_Root_container_rotating(self):
        if self.Root_container_rotating_none in self.current_state[self.Root_container_rotating] :
            self.exit_Root_container_rotating_none()
        if self.Root_container_rotating_left in self.current_state[self.Root_container_rotating] :
            self.exit_Root_container_rotating_left()
        if self.Root_container_rotating_both in self.current_state[self.Root_container_rotating] :
            self.exit_Root_container_rotating_both()
        if self.Root_container_rotating_right in self.current_state[self.Root_container_rotating] :
            self.exit_Root_container_rotating_right()
        self.current_state[self.Root_container] = []
    
    def enter_Root_container_shoot(self):
        self.current_state[self.Root_container].append(self.Root_container_shoot)
    
    def exit_Root_container_shoot(self):
        if self.Root_container_shoot_hold in self.current_state[self.Root_container_shoot] :
            self.exit_Root_container_shoot_hold()
        if self.Root_container_shoot_shoot in self.current_state[self.Root_container_shoot] :
            self.exit_Root_container_shoot_shoot()
        self.current_state[self.Root_container] = []
    
    def enter_Root_container_ammo(self):
        self.current_state[self.Root_container].append(self.Root_container_ammo)
    
    def exit_Root_container_ammo(self):
        if self.Root_container_ammo_loaded in self.current_state[self.Root_container_ammo] :
            self.exit_Root_container_ammo_loaded()
        if self.Root_container_ammo_unloaded in self.current_state[self.Root_container_ammo] :
            self.exit_Root_container_ammo_unloaded()
        self.current_state[self.Root_container] = []
    
    def enter_Root_container_rotating_none(self):
        self.current_state[self.Root_container_rotating].append(self.Root_container_rotating_none)
    
    def exit_Root_container_rotating_none(self):
        self.current_state[self.Root_container_rotating] = []
    
    def enter_Root_container_rotating_left(self):
        self.current_state[self.Root_container_rotating].append(self.Root_container_rotating_left)
    
    def exit_Root_container_rotating_left(self):
        self.current_state[self.Root_container_rotating] = []
    
    def enter_Root_container_rotating_both(self):
        self.current_state[self.Root_container_rotating].append(self.Root_container_rotating_both)
    
    def exit_Root_container_rotating_both(self):
        self.current_state[self.Root_container_rotating] = []
    
    def enter_Root_container_rotating_right(self):
        self.current_state[self.Root_container_rotating].append(self.Root_container_rotating_right)
    
    def exit_Root_container_rotating_right(self):
        self.current_state[self.Root_container_rotating] = []
    
    def enter_Root_container_shoot_hold(self):
        self.current_state[self.Root_container_shoot].append(self.Root_container_shoot_hold)
    
    def exit_Root_container_shoot_hold(self):
        self.current_state[self.Root_container_shoot] = []
    
    def enter_Root_container_shoot_shoot(self):
        self.current_state[self.Root_container_shoot].append(self.Root_container_shoot_shoot)
    
    def exit_Root_container_shoot_shoot(self):
        self.current_state[self.Root_container_shoot] = []
    
    def enter_Root_container_ammo_loaded(self):
        self.current_state[self.Root_container_ammo].append(self.Root_container_ammo_loaded)
    
    def exit_Root_container_ammo_loaded(self):
        self.current_state[self.Root_container_ammo] = []
    
    def enter_Root_container_ammo_unloaded(self):
        self.timers[0] = self.reload_time
        self.current_state[self.Root_container_ammo].append(self.Root_container_ammo_unloaded)
    
    def exit_Root_container_ammo_unloaded(self):
        self.timers.pop(0, None)
        self.current_state[self.Root_container_ammo] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_container(self):
        self.enter_Root_container()
        self.enterDefault_Root_container_rotating()
        self.enterDefault_Root_container_shoot()
        self.enterDefault_Root_container_ammo()
    
    def enterDefault_Root_container_rotating(self):
        self.enter_Root_container_rotating()
        self.enter_Root_container_rotating_none()
    
    def enterDefault_Root_container_shoot(self):
        self.enter_Root_container_shoot()
        self.enter_Root_container_shoot_hold()
    
    def enterDefault_Root_container_ammo(self):
        self.enter_Root_container_ammo()
        self.enter_Root_container_ammo_loaded()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_container:
                catched = self.transition_Root_container(event)
        return catched
    
    def transition_Root_container(self, event) :
        catched = False
        if not catched :
            catched = self.transition_Root_container_rotating(event) or catched
            catched = self.transition_Root_container_shoot(event) or catched
            catched = self.transition_Root_container_ammo(event) or catched
        return catched
    
    def transition_Root_container_rotating(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_container_rotating][0] == self.Root_container_rotating_none:
                catched = self.transition_Root_container_rotating_none(event)
            elif self.current_state[self.Root_container_rotating][0] == self.Root_container_rotating_left:
                catched = self.transition_Root_container_rotating_left(event)
            elif self.current_state[self.Root_container_rotating][0] == self.Root_container_rotating_both:
                catched = self.transition_Root_container_rotating_both(event)
            elif self.current_state[self.Root_container_rotating][0] == self.Root_container_rotating_right:
                catched = self.transition_Root_container_rotating_right(event)
        return catched
    
    def transition_Root_container_rotating_none(self, event) :
        catched = False
        enableds = []
        if event.name == "cannon-left-pressed" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "cannon-right-pressed" and event.getPort() == "input" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_rotating_none. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_rotating_none()
                self.enter_Root_container_rotating_left()
            elif enabled == 2 :
                self.exit_Root_container_rotating_none()
                self.enter_Root_container_rotating_right()
            catched = True
        
        return catched
    
    def transition_Root_container_rotating_left(self, event) :
        catched = False
        enableds = []
        if event.name == "cannon-left-released" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "cannon-right-pressed" and event.getPort() == "input" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_rotating_left. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_rotating_left()
                self.enter_Root_container_rotating_none()
            elif enabled == 2 :
                self.exit_Root_container_rotating_left()
                self.enter_Root_container_rotating_both()
            elif enabled == 3 :
                self.exit_Root_container_rotating_left()
                self.tank.turnCannonLeft()
                self.enter_Root_container_rotating_left()
            catched = True
        
        return catched
    
    def transition_Root_container_rotating_both(self, event) :
        catched = False
        enableds = []
        if event.name == "cannon-left-released" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "cannon-right-released" and event.getPort() == "input" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_rotating_both. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_rotating_both()
                self.enter_Root_container_rotating_right()
            elif enabled == 2 :
                self.exit_Root_container_rotating_both()
                self.enter_Root_container_rotating_left()
            catched = True
        
        return catched
    
    def transition_Root_container_rotating_right(self, event) :
        catched = False
        enableds = []
        if event.name == "cannon-left-pressed" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "cannon-right-released" and event.getPort() == "input" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_rotating_right. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_rotating_right()
                self.enter_Root_container_rotating_both()
            elif enabled == 2 :
                self.exit_Root_container_rotating_right()
                self.enter_Root_container_rotating_none()
            elif enabled == 3 :
                self.exit_Root_container_rotating_right()
                self.tank.turnCannonRight()
                self.enter_Root_container_rotating_right()
            catched = True
        
        return catched
    
    def transition_Root_container_shoot(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_container_shoot][0] == self.Root_container_shoot_hold:
                catched = self.transition_Root_container_shoot_hold(event)
            elif self.current_state[self.Root_container_shoot][0] == self.Root_container_shoot_shoot:
                catched = self.transition_Root_container_shoot_shoot(event)
        return catched
    
    def transition_Root_container_shoot_hold(self, event) :
        catched = False
        enableds = []
        if event.name == "shoot-pressed" and event.getPort() == "input" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_shoot_hold. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_shoot_hold()
                self.addEvent(Event("shoot", parameters = []))
                self.enter_Root_container_shoot_shoot()
            catched = True
        
        return catched
    
    def transition_Root_container_shoot_shoot(self, event) :
        catched = False
        enableds = []
        if event.name == "shoot-released" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "loaded" and event.getPort() == "" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_shoot_shoot. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_shoot_shoot()
                self.enter_Root_container_shoot_hold()
            elif enabled == 2 :
                self.exit_Root_container_shoot_shoot()
                self.addEvent(Event("shoot", parameters = []))
                self.enter_Root_container_shoot_shoot()
            catched = True
        
        return catched
    
    def transition_Root_container_ammo(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_container_ammo][0] == self.Root_container_ammo_loaded:
                catched = self.transition_Root_container_ammo_loaded(event)
            elif self.current_state[self.Root_container_ammo][0] == self.Root_container_ammo_unloaded:
                catched = self.transition_Root_container_ammo_unloaded(event)
        return catched
    
    def transition_Root_container_ammo_loaded(self, event) :
        catched = False
        enableds = []
        if event.name == "shoot" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_ammo_loaded. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_ammo_loaded()
                self.tank.shoot()
                self.controller.outputEvent(Event("reloading", port="gui", parameters = []))
                self.enter_Root_container_ammo_unloaded()
            catched = True
        
        return catched
    
    def transition_Root_container_ammo_unloaded(self, event) :
        catched = False
        enableds = []
        if event.name == "_0after" and event.getPort() == "" :
            enableds.append(1)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_ammo_unloaded. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_ammo_unloaded()
                self.addEvent(Event("loaded", parameters = []))
                self.controller.outputEvent(Event("loaded", port="gui", parameters = []))
                self.enter_Root_container_ammo_loaded()
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
    

class Body(RuntimeClassBase):
    
    # Unique IDs for all statechart nodes
    Root = 0
    Root_container = 1
    Root_container_horizontal = 2
    Root_container_vertical = 3
    Root_container_horizontal_none = 4
    Root_container_horizontal_left = 5
    Root_container_horizontal_both = 6
    Root_container_horizontal_right = 7
    Root_container_vertical_none = 8
    Root_container_vertical_down = 9
    Root_container_vertical_both = 10
    Root_container_vertical_up = 11
    
    def commonConstructor(self, controller = None):
        """Constructor part that is common for all constructors."""
        super(Body, self).__init__()
        # User defined attributes
        self.tank = None
        
        self.controller = controller
        self.object_manager = controller.getObjectManager()
        self.current_state = {}
        self.history_state = {}
        
        #Initialize statechart :
        
        self.current_state[self.Root] = []
        self.current_state[self.Root_container] = []
        self.current_state[self.Root_container_horizontal] = []
        self.current_state[self.Root_container_vertical] = []
    
    def start(self):
        super(Body, self).start()
        self.enterDefault_Root_container()
    
    #The actual constructor
    def __init__(self, controller, tank):
        self.commonConstructor(controller)
        
        #constructor body (user-defined)
        self.tank = tank
    
    # Statechart enter/exit action method(s) :
    
    def enter_Root_container(self):
        self.current_state[self.Root].append(self.Root_container)
    
    def exit_Root_container(self):
        self.exit_Root_container_horizontal()
        self.exit_Root_container_vertical()
        self.current_state[self.Root] = []
    
    def enter_Root_container_horizontal(self):
        self.current_state[self.Root_container].append(self.Root_container_horizontal)
    
    def exit_Root_container_horizontal(self):
        if self.Root_container_horizontal_none in self.current_state[self.Root_container_horizontal] :
            self.exit_Root_container_horizontal_none()
        if self.Root_container_horizontal_left in self.current_state[self.Root_container_horizontal] :
            self.exit_Root_container_horizontal_left()
        if self.Root_container_horizontal_both in self.current_state[self.Root_container_horizontal] :
            self.exit_Root_container_horizontal_both()
        if self.Root_container_horizontal_right in self.current_state[self.Root_container_horizontal] :
            self.exit_Root_container_horizontal_right()
        self.current_state[self.Root_container] = []
    
    def enter_Root_container_vertical(self):
        self.current_state[self.Root_container].append(self.Root_container_vertical)
    
    def exit_Root_container_vertical(self):
        if self.Root_container_vertical_none in self.current_state[self.Root_container_vertical] :
            self.exit_Root_container_vertical_none()
        if self.Root_container_vertical_down in self.current_state[self.Root_container_vertical] :
            self.exit_Root_container_vertical_down()
        if self.Root_container_vertical_both in self.current_state[self.Root_container_vertical] :
            self.exit_Root_container_vertical_both()
        if self.Root_container_vertical_up in self.current_state[self.Root_container_vertical] :
            self.exit_Root_container_vertical_up()
        self.current_state[self.Root_container] = []
    
    def enter_Root_container_horizontal_none(self):
        self.current_state[self.Root_container_horizontal].append(self.Root_container_horizontal_none)
    
    def exit_Root_container_horizontal_none(self):
        self.current_state[self.Root_container_horizontal] = []
    
    def enter_Root_container_horizontal_left(self):
        self.current_state[self.Root_container_horizontal].append(self.Root_container_horizontal_left)
    
    def exit_Root_container_horizontal_left(self):
        self.current_state[self.Root_container_horizontal] = []
    
    def enter_Root_container_horizontal_both(self):
        self.current_state[self.Root_container_horizontal].append(self.Root_container_horizontal_both)
    
    def exit_Root_container_horizontal_both(self):
        self.current_state[self.Root_container_horizontal] = []
    
    def enter_Root_container_horizontal_right(self):
        self.current_state[self.Root_container_horizontal].append(self.Root_container_horizontal_right)
    
    def exit_Root_container_horizontal_right(self):
        self.current_state[self.Root_container_horizontal] = []
    
    def enter_Root_container_vertical_none(self):
        self.current_state[self.Root_container_vertical].append(self.Root_container_vertical_none)
    
    def exit_Root_container_vertical_none(self):
        self.current_state[self.Root_container_vertical] = []
    
    def enter_Root_container_vertical_down(self):
        self.current_state[self.Root_container_vertical].append(self.Root_container_vertical_down)
    
    def exit_Root_container_vertical_down(self):
        self.current_state[self.Root_container_vertical] = []
    
    def enter_Root_container_vertical_both(self):
        self.current_state[self.Root_container_vertical].append(self.Root_container_vertical_both)
    
    def exit_Root_container_vertical_both(self):
        self.current_state[self.Root_container_vertical] = []
    
    def enter_Root_container_vertical_up(self):
        self.current_state[self.Root_container_vertical].append(self.Root_container_vertical_up)
    
    def exit_Root_container_vertical_up(self):
        self.current_state[self.Root_container_vertical] = []
    
    #Statechart enter/exit default method(s) :
    
    def enterDefault_Root_container(self):
        self.enter_Root_container()
        self.enterDefault_Root_container_horizontal()
        self.enterDefault_Root_container_vertical()
    
    def enterDefault_Root_container_horizontal(self):
        self.enter_Root_container_horizontal()
        self.enter_Root_container_horizontal_none()
    
    def enterDefault_Root_container_vertical(self):
        self.enter_Root_container_vertical()
        self.enter_Root_container_vertical_none()
    
    #Statechart transitions :
    
    def transition_Root(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root][0] == self.Root_container:
                catched = self.transition_Root_container(event)
        return catched
    
    def transition_Root_container(self, event) :
        catched = False
        if not catched :
            catched = self.transition_Root_container_horizontal(event) or catched
            catched = self.transition_Root_container_vertical(event) or catched
        return catched
    
    def transition_Root_container_horizontal(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_container_horizontal][0] == self.Root_container_horizontal_none:
                catched = self.transition_Root_container_horizontal_none(event)
            elif self.current_state[self.Root_container_horizontal][0] == self.Root_container_horizontal_left:
                catched = self.transition_Root_container_horizontal_left(event)
            elif self.current_state[self.Root_container_horizontal][0] == self.Root_container_horizontal_both:
                catched = self.transition_Root_container_horizontal_both(event)
            elif self.current_state[self.Root_container_horizontal][0] == self.Root_container_horizontal_right:
                catched = self.transition_Root_container_horizontal_right(event)
        return catched
    
    def transition_Root_container_horizontal_none(self, event) :
        catched = False
        enableds = []
        if event.name == "left-pressed" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "right-pressed" and event.getPort() == "input" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_horizontal_none. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_horizontal_none()
                self.enter_Root_container_horizontal_left()
            elif enabled == 2 :
                self.exit_Root_container_horizontal_none()
                self.enter_Root_container_horizontal_right()
            catched = True
        
        return catched
    
    def transition_Root_container_horizontal_left(self, event) :
        catched = False
        enableds = []
        if event.name == "left-released" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "right-pressed" and event.getPort() == "input" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_horizontal_left. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_horizontal_left()
                self.enter_Root_container_horizontal_none()
            elif enabled == 2 :
                self.exit_Root_container_horizontal_left()
                self.enter_Root_container_horizontal_both()
            elif enabled == 3 :
                self.exit_Root_container_horizontal_left()
                self.tank.turnLeft()
                self.enter_Root_container_horizontal_left()
            catched = True
        
        return catched
    
    def transition_Root_container_horizontal_both(self, event) :
        catched = False
        enableds = []
        if event.name == "left-released" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "right-released" and event.getPort() == "input" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_horizontal_both. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_horizontal_both()
                self.enter_Root_container_horizontal_right()
            elif enabled == 2 :
                self.exit_Root_container_horizontal_both()
                self.enter_Root_container_horizontal_left()
            catched = True
        
        return catched
    
    def transition_Root_container_horizontal_right(self, event) :
        catched = False
        enableds = []
        if event.name == "left-pressed" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "right-released" and event.getPort() == "input" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_horizontal_right. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_horizontal_right()
                self.enter_Root_container_horizontal_both()
            elif enabled == 2 :
                self.exit_Root_container_horizontal_right()
                self.enter_Root_container_horizontal_none()
            elif enabled == 3 :
                self.exit_Root_container_horizontal_right()
                self.tank.turnRight()
                self.enter_Root_container_horizontal_right()
            catched = True
        
        return catched
    
    def transition_Root_container_vertical(self, event) :
        catched = False
        if not catched :
            if self.current_state[self.Root_container_vertical][0] == self.Root_container_vertical_none:
                catched = self.transition_Root_container_vertical_none(event)
            elif self.current_state[self.Root_container_vertical][0] == self.Root_container_vertical_down:
                catched = self.transition_Root_container_vertical_down(event)
            elif self.current_state[self.Root_container_vertical][0] == self.Root_container_vertical_both:
                catched = self.transition_Root_container_vertical_both(event)
            elif self.current_state[self.Root_container_vertical][0] == self.Root_container_vertical_up:
                catched = self.transition_Root_container_vertical_up(event)
        return catched
    
    def transition_Root_container_vertical_none(self, event) :
        catched = False
        enableds = []
        if event.name == "down-pressed" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "up-pressed" and event.getPort() == "input" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_vertical_none. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_vertical_none()
                self.enter_Root_container_vertical_down()
            elif enabled == 2 :
                self.exit_Root_container_vertical_none()
                self.enter_Root_container_vertical_up()
            catched = True
        
        return catched
    
    def transition_Root_container_vertical_down(self, event) :
        catched = False
        enableds = []
        if event.name == "down-released" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "up-pressed" and event.getPort() == "input" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_vertical_down. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_vertical_down()
                self.enter_Root_container_vertical_none()
            elif enabled == 2 :
                self.exit_Root_container_vertical_down()
                self.enter_Root_container_vertical_both()
            elif enabled == 3 :
                self.exit_Root_container_vertical_down()
                self.tank.moveDown()
                self.enter_Root_container_vertical_down()
            catched = True
        
        return catched
    
    def transition_Root_container_vertical_both(self, event) :
        catched = False
        enableds = []
        if event.name == "down-released" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "up-released" and event.getPort() == "input" :
            enableds.append(2)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_vertical_both. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_vertical_both()
                self.enter_Root_container_vertical_up()
            elif enabled == 2 :
                self.exit_Root_container_vertical_both()
                self.enter_Root_container_vertical_down()
            catched = True
        
        return catched
    
    def transition_Root_container_vertical_up(self, event) :
        catched = False
        enableds = []
        if event.name == "down-pressed" and event.getPort() == "input" :
            enableds.append(1)
        
        if event.name == "up-released" and event.getPort() == "input" :
            enableds.append(2)
        
        if event.name == "update" and event.getPort() == "engine" :
            enableds.append(3)
        
        if len(enableds) > 1 :
            print "Runtime warning : indeterminism detected in a transition from node Root_container_vertical_up. Only the first in document order enabled transition is executed."
        
        if len(enableds) > 0 :
            enabled = enableds[0]
            if enabled == 1 :
                self.exit_Root_container_vertical_up()
                self.enter_Root_container_vertical_both()
            elif enabled == 2 :
                self.exit_Root_container_vertical_up()
                self.enter_Root_container_vertical_none()
            elif enabled == 3 :
                self.exit_Root_container_vertical_up()
                self.tank.moveUp()
                self.enter_Root_container_vertical_up()
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
            associations.append(Association("cannon", "Cannon", 1, 1))
            associations.append(Association("body", "Body", 1, 1))
        elif class_name == "Cannon" :
            instance =  Cannon(self.controller, *construct_params)
        elif class_name == "Body" :
            instance =  Body(self.controller, *construct_params)
        if instance:
            return InstanceWrapper(instance, associations)
        else :
            return None

from python_runtime.statecharts_core import GameLoopControllerBase
class Controller(GameLoopControllerBase):
    def __init__(self, tank, keep_running = True):
        super(Controller, self).__init__(ObjectManager(self), keep_running)
        self.addInputPort("engine")
        self.addInputPort("input")
        self.addOutputPort("gui")
        self.object_manager.createInstance("Main", [tank])
        
def main():
    controller = Controller()
    controller.start()

if __name__ == "__main__":
    main()
