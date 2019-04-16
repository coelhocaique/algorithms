import file_reader as reader
import random


def choose_edge_randomly(n_len, adj_dict):
    rand = random.randint(1, n_len)
    u = list(adj_dict.keys())[rand - 1]
    v = adj_dict.get(u)
    v_index = -1
    while v == -1 or v[v_index - 1] == u:
        v_index = random.randint(1, len(v))

    return u, v[v_index - 1]


def contract(u, v, adj_dict):
    u_list = adj_dict.get(u)
    v_list = adj_dict.pop(v, None)

    # fuse lists
    u_list+= v_list

    to_remove = []
    index = 0
    # remove self loops
    while index < len(u_list):
        if u_list[index] == v or u_list[index] == u:
            del u_list[index]
        index+=1

    # change index in adj list of v
    for key in adj_dict.keys():
        adj = adj_dict.get(key)
        if adj:
            for i in range(len(adj)):
                if adj[i] == v:
                    adj[i] = u


def get_number_of_edges(adj_dict):
    output = []
    edges = 0

    for key in adj_dict.keys():
        adj_list = list(adj_dict.get(key))
        for d in adj_list:
            output.append([key, d])
            edges+=1

    return output, edges // 2


def get_min_cut(adj_dict):
    n_len = len(adj_dict.keys())

    while n_len > 2:
        #print(adj_dict)
        u, v = choose_edge_randomly(n_len, adj_dict)
        #print('%g u=%g, v=%g chosen' % (n_len, u, v))
        # contract from u to v
        contract(u, v, adj_dict)
        n_len = len(adj_dict.keys())

    return get_number_of_edges(adj_dict)


#adj_dict = reader.get_dict_as_adj_list(reader.FilePath.MIN_CUT)
# adj_dict = {1:[2, 3], 2:[1, 3, 4], 3:[1, 2, 4], 4:[2, 3]}
min_cut = 1_000_000_000_0000

for i in range(10):
    edges, min_cut_cur = get_min_cut(reader.get_dict_as_adj_list(reader.FilePath.MIN_CUT))
    print('iteration %g , min_cut=%g' % (i, min_cut_cur))
    min_cut = min(min_cut, min_cut_cur)

print('min_cut: %g' % min_cut)