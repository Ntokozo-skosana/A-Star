import heapq

def all_moves(state):
    position_of_blank = state.index('#')
    state_list = list(state)

    moves = {}
    if position_of_blank >= 3:
       moves["UP"] = -3
    else:
       moves["UP"] = None

    if position_of_blank <= 5:
       moves["DOWN"] = 3
    else:
       moves["DOWN"] = None

    if position_of_blank % 3 != 0:
       moves["LEFT"] = -1
    else:
       moves["LEFT"] = None

    if position_of_blank % 3 != 2:
       moves["RIGHT"] = 1
    else:
       moves["RIGHT"] = None

    next_states = []
    for move, movement in moves.items():
        if movement is not None:
            pos = position_of_blank + movement
            new_state = state_list[:]
            new_state[position_of_blank], new_state[pos] = (
                new_state[pos],
                new_state[position_of_blank],
            )
            next_states.append((move, "".join(new_state)))
    return next_states

def manhattan(state, goal_state):
    dist = 0
    for i, tile in enumerate(state):
        if tile != '#':
            j = goal_state.index(tile)
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(j, 3)
            dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

def a_star(initial_state, goal_state):
    if initial_state == goal_state:
        return 0

    pq = [(manhattan(initial_state, goal_state), 0, initial_state)]
    visited = {initial_state: 0}

    while pq:
        est_total, cost, state = heapq.heappop(pq)
        if state == goal_state:
            return cost

        for move, next_state in all_moves(state):
            new_cost = cost + 1
            if next_state not in visited or new_cost < visited[next_state]:
                visited[next_state] = new_cost
                est = new_cost + manhattan(next_state, goal_state)
                heapq.heappush(pq, (est, new_cost, next_state))

    return -1

initial_state = input().strip()
goal_state = input().strip()
print(a_star(initial_state, goal_state))
