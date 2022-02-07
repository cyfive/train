import carriage
import random

random.seed()

class Train:
    carriages = []
    current_carriage = 0
    current_pos = 0

    def __init__(self, train_lenght = 2):
        for pos in range(train_lenght):
            rnd_status = random.randint(0, 1)
            self.carriages.append(carriage.Carriage(rnd_status))
        self.current_carriage = self.carriages[self.current_pos]

    def step_fwd(self):
        self.current_pos += 1
        if self.current_pos > len(self.carriages) - 1:
            self.current_pos = 0
        self.current_carriage = self.carriages[self.current_pos]

    def step_bwd(self):
        self.current_pos -= 1
        if self.current_pos < 0:
            self.current_pos = len(self.carriages) - 1
        self.current_carriage = self.carriages[self.current_pos]
    
    def get_light_status(self):
        return self.current_carriage.light_on

    def set_light_status(self, light_status):
        self.current_carriage.light_on = light_status
    
    def print_train(self):
        train_str = ""
        for curr_carriage in self.carriages:
            if curr_carriage.light_on:
                train_str += "[ * ]-"
            else:
                train_str += "[   ]-"
        print(train_str)
