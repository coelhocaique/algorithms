import sys, datetime, time
sys.path.append("..")
from utils.file_reader import *

"""
    In this assignment you will implement one or more algorithms for the 2SAT problem.  Here are 6 different 2SAT instances:
    The file format is as follows.  In each instance, the number of variables and the number of clauses is the same, and this number is specified on the first line of the file.  Each subsequent line specifies a clause via its two literals, with a number denoting the variable and a "-" sign denoting logical "not".  For example, the second line of the first data file is "-16808 75250", 
    which indicates the clause \neg x_{16808} \vee x_{75250}¬x 16808 ∨x 75250.
    
    Your task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable.  In the box below, enter a 6-bit string, where the ith bit should be 1 if the ith instance is satisfiable, and 0 otherwise.  For example, if you think that the first 3 instances are satisfiable and the last 3 are not, then you should enter the string 111000 in the box below.
    
    DISCUSSION: This assignment is deliberately open-ended, and you can implement whichever 2SAT algorithm you want.  
    For example, 2SAT reduces to computing the strongly connected components of a suitable graph (with two vertices per variable and two directed edges per clause, you should think through the details).  
    This might be an especially attractive option for those of you who coded up an SCC algorithm in Part 2 of this specialization.  
    Alternatively, you can use Papadimitriou's randomized local search algorithm.  (The algorithm from lecture is probably too slow as stated, so you might want to make one or more simple modifications to it --- even if this means breaking the analysis given in lecture --- to ensure that it runs in a reasonable amount of time.)  A third approach is via backtracking.  
    In lecture we mentioned this approach only in passing; see Chapter 9 of the Dasgupta-Papadimitriou-Vazirani book, for example, for more details.
"""

def add_edge(graph, u, v):
    if graph.get(u, None) is None:
        graph[u] = {v}
    else:
        graph[u].add(v)

def get_data(filename):
    lines = list(map(lambda s: s.split(), read_input(filename)))
    num_nodes = int(lines[0][0])
    graph, graph_inverted = {}, {}

    for line in lines[1:]:
        a, b = map(int, line)

        add_edge(graph, -a, b)
        add_edge(graph, -b, a)

        add_edge(graph_inverted, a, -b)
        add_edge(graph_inverted, b, -a)

    return graph, graph_inverted, num_nodes

def kosaraju_scc(graph, graph_inverted):

    def dfs(g, node, visited, res=[]):
        visited.add(node)
        neighbours = g.get(node)
        if neighbours:
            for cur_node in neighbours:
                if cur_node not in visited:
                    dfs(g, cur_node, visited, res)

        res.append(node)

        return res

    def compute_finishing_times(g, visited):
        finishing_times = []
        for node in g.keys():
            if node not in visited:
                dfs(g, node, visited, finishing_times)

        return finishing_times

    def compute_scc(g, finishing_times, visited):
        result = {}
        for node in reversed(finishing_times):
            if node not in visited:
                result[node] = dfs(g, node, visited, [])

        return result

    finishing_times = compute_finishing_times(graph, set())
    leaders_dict = compute_scc(graph_inverted, finishing_times, set())
    return leaders_dict


def scc_2_sat(graph, graph_inverted):
    components = kosaraju_scc(graph, graph_inverted)

    for key in components.keys():
        edges = set(components.get(key))
        for e in edges:
            if -e in edges:
                return False

    return True


def execute_2_sat():
    data = [get_data(FilePath.TWO_SAT_1), get_data(FilePath.TWO_SAT_2), get_data(FilePath.TWO_SAT_3), get_data(FilePath.TWO_SAT_4), get_data(FilePath.TWO_SAT_5), get_data(FilePath.TWO_SAT_6)]
    output = []
    for graph, graph_inverted, num_nodes in data:
        print('dataset iteration start time %s' % datetime.datetime.now())
        is_satisfiable = scc_2_sat(graph, graph_inverted)
        output.append('1' if is_satisfiable else '0')

    return ''.join(output)

start = time.time()

print('2sat start time %s' % datetime.datetime.now())

output = execute_2_sat()

print('2sat output = %s' % output)

print('2sat finish time %s' % datetime.datetime.now())
print('total time elapsed %f' % (time.time() - start))

