from ortools.linear_solver import pywraplp

# get solver
solver = pywraplp.Solver.CreateSolver('GLOP')

n, m, s, t = map(int, input().split())

edges = []
peso = {}
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v))
    peso[(u, v)] = w

# declare decision variables
x = {}
for (u, v) in edges:
    x[u, v] = solver.NumVar(0.0, 1.0, 'x{}'.format((u, v)))

# declare objective
c = solver.Objective()
for (u, v) in edges:
    c.SetCoefficient(x[u, v], peso[(u, v)])
c.SetMinimization()

# declare constraints
for u in range(n):
    if u != s and u != t:
        outflow = sum(x[u, v] for (u_, v) in edges if u_ == u)
        inflow = sum(x[u_, v] for (u_, v) in edges if v == u)
        solver.Add(outflow - inflow == 0)
    elif u == s:
        outflow = sum(x[u, v] for (u_, v) in edges if u_ == u)
        inflow = sum(x[u_, v] for (u_, v) in edges if v == u)
        solver.Add(outflow - inflow == 1)
    elif u == t:
        outflow = sum(x[u, v] for (u_, v) in edges if u_ == u)
        inflow = sum(x[u_, v] for (u_, v) in edges if v == u)
        solver.Add(outflow - inflow == -1)

# solve
results = solver.Solve()

# print results
if results == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())

    for (u, v) in edges:
        print("x[{}, {}] = {}".format(u, v, x[u, v].solution_value()))
else:
    print('The problem does not have an optimal solution.')
