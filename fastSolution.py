def fast_solution(n, list_tasks: list[Task]):
    sum_penalty = 0
    parent = [-1] * n
    rank = [0] * n
    list_tasks.sort(reverse=True)
    for i in range(n):
        dead = list_tasks[i].dead
        if parent[dead] == -1:
            set_task(list_tasks[i], parent,rank)
            continue
        new_place = find_comp(dead, parent) - 1
        if new_place >= 0:
            list_tasks[i].dead=new_place
            set_task(list_tasks[i], parent,rank)
            continue
        sum_penalty += list_tasks[i].penalty
        list_tasks[i].dead=len(parent)-1
        set_task_right(list_tasks[i], parent,rank)
    return sum_penalty
