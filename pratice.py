# import mesa
# class ChatAgent(mesa.Agent):
#     def __init__(self, model):

#         super().__init__(model)
#         self.Chat = 0


#     def step(self):
#         print("Agenet :  What's up?"
#                "Answer :  I'm doing good" )
        

# class ChatModel(mesa.Model):
#     def __init__(self, N):
#         super().__init__()
#         self.num_agent(N)
#         for i in range(self.num_agent):
#             a = ChatModel()
#     def step(self):


# class student:
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name,"ur avg is ", round(sum/3,2))

# s1 = student("Tony", [50,40,80])
# # s1.get_avg()

# class Account:
#     def __init__(self, acc, bal):
#         self.balance = bal
#         self.account = acc

#     # credited
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("Last balance was", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs. ", amount, "was credited")
#         print("Last balance was" , self.get_balance())

#     def get_balance(self):
#         return self.balance
    
# acc1 = Account(122334, 500000)
# acc1.credit(5000)
# acc1.debit(500)
# acc1.credit(10000)



# import mesa
# import matplotlib.pyplot as plt

# class MoneyAgent(mesa.Agent):
#     def __init__(self, model):
#         super().__init__(model)
#         self.wealth = 1

#     def step(self):
#         if self.wealth > 0:
#             other = self.random.choice(self.model.agents)
#             other.wealth += 1
#             self.wealth -= 1

#         print(f"Agent {self.unique_id} has wealth {self.wealth}")


# class MoneyModel(mesa.Model):
#     def __init__(self, N, seed=None):
#         super().__init__(seed=seed)
#         self.num_agents = N

#         # create agents
#         for _ in range(self.num_agents):
#             MoneyAgent(self)

#     def step(self):
#         self.agents.shuffle_do("step")

# all_wealth = []
# for j in range(100):
#     model = MoneyModel(10)
#     for i in range(10):
#         model.step()
#     for agent in model.agents:

#         all_wealth.append(agent.wealth)

# plt.hist(all_wealth,bins=range(max(all_wealth) + 1))
# plt.show()



# import mesa
# class MoneyAgent(mesa.Agent):
#     def __init__(self, model):
#         super().__init__(model)
#         self.wealth = 1

#     def step(self):
#         pass

# class MoneyModel(mesa.Model):
    
#     def __init__(self,N, width , height):
#         super().__init__()
#         self.num_agents = N
#         self.grid = mesa.space.MultiGrid(width, height,torus = True)

#         for i in range(self.num_agents):
#             a = MoneyAgent(self)

#             x = self.random.randrange(self.grid.width)
#             y = self.random.randrange(self.grid.height)
#             self.grid.place_agent(a, (x,y))


        
# import mesa

# class MesaAgent(mesa.Agent):
#     def __init__(self,model):

#         super().__init__(model)
#         # self.money = int(input("Enter Money "))

#     def step(self):
#         self.money = 0
#         if self.money == 0:
#             print(f"Agent My id is {self.unique_id}")

# class MesaModel(mesa.Model):
#     def __init__(self,N):
#         super().__init__()
#         self.num_agents = N
#         for i in range(self.num_agents):
#             MesaAgent(self)

#     def step(self):
#         self.agents.shuffle_do("step")
# model = MesaModel(10)
# model.step()



import mesa
from mesa_llm.agent import LLMAgent
from mesa_llm.llm.ollama import OllamaLLM


class SimpleAgent(LLMAgent):
    def __init__(self, model):
        llm = OllamaLLM(model="llama3")
        super().__init__(model, llm=llm)

    def step(self):
        response = self.llm.complete("Say hello in one short sentence.")
        print(f"Agent {self.unique_id}: {response}")


class SimpleModel(mesa.Model):
    def __init__(self):
        super().__init__()
        SimpleAgent(self)

    def step(self):
        self.agents.shuffle_do("step")


model = SimpleModel()
model.step()
