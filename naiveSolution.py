def simple_solution(n, list_tasks: list[Task]):
    list_tasks.sort(reverse=True)
    sum_penalty = 0
    for i in range(n):
        if i < list_tasks[i].dead:
            sum_penalty += list_tasks[i].penalty
    return sum_penalty
