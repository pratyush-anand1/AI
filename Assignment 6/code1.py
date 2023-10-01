#Matrix multiplifation via AO*
import math

# define the matrix chain as a list of dimensions
matrix_chain = [(2, 3), (3, 4), (4, 5), (5, 6)]

# define the heuristic function based on the dimensions of the remaining matrices
def heuristic(remaining_chain):
    if len(remaining_chain) == 1:
        return 0
    else:
        return sum([remaining_chain[i][0] * remaining_chain[i][1] for i in range(len(remaining_chain))])

# define a function to compute the cost of multiplying a subchain of matrices
def matrix_chain_cost(subchain):
    if len(subchain) == 1:
        return 0
    else:
        cost = 0
        for i in range(1, len(subchain)):
            cost += subchain[i-1][0] * subchain[i][0] * subchain[i][1]
        return cost

# define the AO* algorithm
def ao_star(matrix_chain):
    root = {'chain': matrix_chain, 'children': [],'type' : 'and'}
    stack = [root]
    while stack:
        node = stack.pop()
        if len(node['chain']) == 1:
            node['cost'] = 0
            continue
        if node['type'] == 'and':
            subchains = []
            for i in range(1, len(node['chain'])):
                subchains.append({'chain': node['chain'][:i], 'cost': None})
                subchains.append({'chain': node['chain'][i:], 'cost': None})
            subchains.sort(key=lambda x: heuristic(x['chain']) + matrix_chain_cost(x['chain']))
            node['children'] = subchains
            stack.extend(subchains)
        else:
            solutions = []
            for i in range(1, len(node['chain'])):
                solution = {'left': node['chain'][:i], 'right': node['chain'][i:], 'cost': None}
                solution['cost'] = matrix_chain_cost(solution['left']) + matrix_chain_cost(solution['right']) + \
                                   node['children'][0]['cost'] + node['children'][1]['cost']
                solutions.append(solution)
            solutions.sort(key=lambda x: x['cost'])
            node['children'] = solutions
            node['cost'] = solutions[0]['cost']
    return root['cost']

# test the algorithm
cost = ao_star(matrix_chain)
print('Minimum cost:', cost)