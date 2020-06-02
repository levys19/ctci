"""
Problem:
You are given a list of projects and a list of dependencies (whichi s a list of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built.
If there is no valid order, return [-1]

Explanation:
First I created an adjacency matrix where param_0 builds param_1, this will allow us to see what a project's requirements are, and what they can build
Then I create a list of all the projects that don't have any requirements to be built so they can automatically be added to my finished_build whenever,
Then I create do DFS by using a list(visiting) and treating it like a stack
As I pop projects off of visiting, I add all the projects that project can build and hasn't been built yet to the visiting stack.
When a path ends, I will still have items in the visiting stack since I added all the project that doesn't have requirements to the visiting stack, ensuring all nodes are reached.
When I'm done, I compare the final_list to the length of the initial project list to see if every project has been built. If they're equal, I return the finished_list; otherwise I will return [-1]
"""
#Chapter 4 4.7
def build_order(project_list: [], dependencies:[])-> []:
    adj_matrix = {key: {key: False for key in project_list} for key in project_list}
    for adj in dependencies:
        adj_matrix[adj[0]][adj[1]] = True
    def no_requirement(input):
        for requirement in adj_matrix:
            if adj_matrix[requirement][input] == True:
                return False
        return True
    visiting = []
    finished_build = []
    built = set()
    for project in project_list:
        if no_requirement(project):
            visiting.append(project)
            built.add(project)
    while visiting:
        current_build = visiting.pop()
        finished_build.append(current_build)
        for can_build in adj_matrix[current_build].keys():
            if adj_matrix[current_build][can_build] == True and can_build not in built:
                visiting.append(can_build)
                built.add(can_build)
    if len(finished_build) == len(project_list):
        return finished_build
    else:
        return [-1]



# def build_order_test_1():
#     if build_order(project_list, dependencies) == :
#         print("It's good")

def test_1():
    project_list = ['a','b','c','d','e','f']
    dependencies = [('a','d'), ('f','b'),('b','d'),('f','a'),('d','c')]
    print(build_order(project_list,dependencies))

def test_2():
    project_list = ['a','b']
    dependencies = [('b','a'),('a','b')]
    print(build_order(project_list,dependencies))

def test_3():
    project_list = ['a','b','c']
    dependencies = [('a','b'),('b','c'),('c','a')]
    print(build_order(project_list,dependencies))

def test_4():
    project_list = []
    dependencies = []
    print(build_order(project_list,dependencies))

def test_5():
    project_list = ['a','b','c']
    dependencies = [('a','b'),('a','c'),('a','a')]
    print(build_order(project_list,dependencies))

test_1()
test_2()
test_3()
test_4()
test_5()

