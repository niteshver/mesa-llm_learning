from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random


# ------------------- PERSON (AGENT) -------------------
class Person(Agent):
    def __init__(self, unique_id, model, infected=False):
        super().__init__(unique_id, model)

        # HEALTH STATE: S = Susceptible, I = Infected, R = Recovered
        self.health = "I" if infected else "S"

    def step(self):
        # 1) MOVE PERSON
        self.move()

        # 2) IF PERSON IS INFECTED, TRY TO INFECT OTHERS
        if self.health == "I":
            self.infect_neighbors()

            # 3) CHANCE TO RECOVER
            if random.random() < self.model.recovery_chance:
                self.health = "R"

    # ------------------------------------------------ CUSTOM FUNCTIONS ------------------------------------------------

    # MOVE TO A RANDOM NEARBY CELL
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,           # 8 directions
            include_center=False  # cannot stay in same place
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    # INFECT PEOPLE NEARBY (IN THE SAME CELL)
    def infect_neighbors(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        for other in cellmates:
            if other.health == "S":
                # chance infection
                if random.random() < self.model.infection_chance:
                    other.health = "I"


# ------------------- VIRUS MODEL (WORLD) -------------------
class VirusModel(Model):
    def __init__(
        self,
        N=50,              # Number of People
        width=10,
        height=10,
        infection_chance=0.3,
        recovery_chance=0.1,
        initial_infected=3
    ):
        super().__init__()
        self.num_agents = N
        self.grid = MultiGrid(width, height, torus=True)  # torus = wrap around edges
        self.schedule = RandomActivation(self)

        self.infection_chance = infection_chance
        self.recovery_chance = recovery_chance

        # CREATE AGENTS
        for i in range(self.num_agents):
            infected = i < initial_infected   # first few start infected
            a = Person(i, self, infected)
            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        # DATA COLLECTION
        self.datacollector = DataCollector(
            model_reporters={
                "Susceptible": lambda m: self.count_type("S"),
                "Infected": lambda m: self.count_type("I"),
                "Recovered": lambda m: self.count_type("R"),
            }
        )

    # RUN MODEL FOR ONE STEP (ONE DAY)
    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    # COUNT AGENTS WITH HEALTH STATE (S, I, or R)
    def count_type(self, health_state):
        return sum([1 for a in self.schedule.agents if a.health == health_state])


# ------------------- RUN THE MODEL -------------------
if __name__ == "__main__":
    model = VirusModel()

    for day in range(20):   # simulate 20 days
        model.step()

    results = model.datacollector.get_model_vars_dataframe()
    print(results)
