def find_comp(v: int, parent: list):
    if v == parent[v]:
        return v
    else:
        parent[v] = find_comp(parent[v], parent)
        return parent[v]


def union_sets(a: int, b: int, parent: list):
    a = find_comp(a, parent)
    b = find_comp(b, parent)
    if a < b:
        parent[b] = a
    if b < a:
        parent[a] = b


class Task:
    dead = 0
    penalty = 0
    left = -1

    def __init__(self, dead, penalty):
        self.dead = dead
        self.penalty = penalty

    def __eq__(self, other):
        return self.penalty == other.penalty

    def __gt__(self, other):
        return self.penalty > other.penalty

    def __lt__(self, other):
        return self.penalty < other.penalty


def set_task(task:Task, parent,rank):
    parent[task.dead] = tasks.dead
    if tasks.dead > 0 and parent[tasks.dead - 1] != -1:
        union_sets(parent[tasks.dead - 1], parent[tasks.dead], parent,rank)
    if tasks.dead < len(parent) - 1 and parent[tasks.dead + 1] != -1:
        union_sets(parent[tasks.dead], parent[tasks.dead + 1], parent,rank)


def set_task_right(posT:Task, parent,rank):
    pos=posT.dead
    while parent[pos.dead] != -1:
        pos= find_comp(pos, parent) - 1
    posT.dead=pos
    set_task(pos, parent,rank)

