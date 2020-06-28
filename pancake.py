from search import *
from random import shuffle
from datetime import datetime
#Problem Class
class PancakeProblem(Problem):

    def __init__(self, initial):
        super().__init__(initial)
        self.initial = tuple(initial)
        self.goal = tuple(sorted(initial))
        self.size = len(initial)

    def actions(self,state):
        possible_actions = []
        for i in range(2,self.size+1):
            possible_actions.append(i)
        return possible_actions

    def result(self,state,action):
        firstPart = state[:action]
        secondPart = state[action:self.size]

        new_state = tuple(reversed(firstPart)) + secondPart

        return new_state

    def goal_test(self,state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c+1

    def h(self,node):
        return sum(s != g for (s, g) in zip(node.state, self.goal))

#Searching functions
def UCS(problem):
    before = datetime.now()
    search = uniform_cost_search(problem)
    after = datetime.now()
    print("---Uniform Cost Search---")
    print("Actions -->",search.solution())
    print("Path -->",search.path())
    print("Path Cost -->", search.path_cost)
    print("Time -->",(after - before).total_seconds())
    print("-"*25)
def BFS(problem):
    before = datetime.now()
    search = breadth_first_tree_search(problem)
    after = datetime.now()
    print("---Breadth First Search---")
    print("Actions -->", search.solution())
    print("Path -->", search.path())
    print("Path Cost -->",search.path_cost)
    print("Time -->", (after - before).total_seconds())
    print("-" * 26)
def DFS(problem):
    before = datetime.now()
    search = depth_first_graph_search(problem)
    after = datetime.now()
    print("---Depth First Search---")
    print("Actions -->",search.solution())
    print("Path -->",search.path())
    print("Path Cost -->", search.path_cost)
    print("Time -->", (after - before).total_seconds())
    print("-" * 24)
def DLS(problem):
    before = datetime.now()
    search = depth_limited_search(problem)
    after = datetime.now()
    print("---Depth Limited Search---")
    print("Actions -->",search.solution())
    print("Path -->",search.path())
    print("Path Cost -->", search.path_cost)
    print("Time -->", (after - before).total_seconds())
    print("-" * 26)
def IDS(problem):
    before = datetime.now()
    search = iterative_deepening_search(problem)
    after = datetime.now()
    print("---Iterative DLS Search---")
    print("Actions -->",search.solution())
    print("Path -->",search.path())
    print("Path Cost -->", search.path_cost)
    print("Time -->", (after - before).total_seconds())
    print("-" * 26)
def GBFS(problem):
    before = datetime.now()
    search = greedy_best_first_graph_search(problem,lambda node: node.state)
    after = datetime.now()
    print("---Greedy Best First Search---")
    print("Actions -->", search.solution())
    print("Path -->", search.path())
    print("Path Cost -->", search.path_cost)
    print("Time -->", (after - before).total_seconds())
    print("-" * 30)
def Astar(problem):
    before = datetime.now()
    search = astar_search(problem)
    after = datetime.now()
    print("---AStar Search---")
    print("Actions -->",search.solution())
    print("Path -->",search.path())
    print("Path Cost -->", search.path_cost)
    print("Time -->", (after - before).total_seconds())
    print("-" * 18)
def AllAlgorithms(problem):
    print(("#" * 22) + "\n# Uniformed Searchss #\n" + ("#" * 22))
    BFS(problem)
    UCS(problem)
    DFS(problem)
    DLS(problem)
    IDS(problem)
    print(("#" * 22) + "\n# Informed Searchss  #\n" + ("#" * 22))
    GBFS(problem)
    Astar(problem)

print(("#" * 61)+"\nWelcome to Pancake Sorter with Artificial Intellegent Program\n"
      "developed by Can Gur and Elif Firtana\n"+("#" * 61))

while True:
    try:
        numberOfPancakes = int(input("Numbers of Pancakes: "))
    except:
        print("Type an integer")
        continue

    pancakes = []

    while True:
        orderChoice = input("Want to determine initial order of {} pancakes [y] \\ [n]\n".format(numberOfPancakes))
        if orderChoice.lower() == "y":
            for i in range(numberOfPancakes):
                items = int(input("Pancake size: "))
                pancakes.append(items)
            break
        elif orderChoice.lower() == "n":
            for i in range(1, numberOfPancakes + 1):
                pancakes.append(i)
            shuffle(pancakes)
            break
        else:
            print("Type only 'y' or 'n' ")

    pancake_problem = PancakeProblem(pancakes)

    print("Pancakes order --> {} \n".format(pancakes))
    for i in pancakes:
        print("-"*i)

    while True:
        print("\nChoose searching algorithm to calculate")
        algorithm = int(input("1 - All algorithms\n"
              "2 - Breadth First Search\n"
              "3 - Uniform Cost Search\n"
              "4 - Depth First Search\n"
              "5 - Depth Limited Search\n"
              "6 - Iterative DLS Search\n"
              "7 - Greedy Best First Search\n"
              "8 - Astar Search\n"))
        if algorithm == 1:
            AllAlgorithms(pancake_problem)
        elif algorithm == 2:
            BFS(pancake_problem)
        elif algorithm == 3:
            UCS(pancake_problem)
        elif algorithm == 4:
            DFS(pancake_problem)
        elif algorithm == 5:
            DLS(pancake_problem)
        elif algorithm == 6:
            IDS(pancake_problem)
        elif algorithm == 7:
            GBFS(pancake_problem)
        elif algorithm == 8:
            Astar(pancake_problem)
        else:
            print("Invalid input")
            continue
        if input("Want to calculate with different algorithm? [y]/[n]") =="n":
            break

    if input("\nWant to calculate different pancakes order? [y]/[n]") == "n":
        break