from collections import defaultdict, deque

class PrerequisiteGraph:
    def __init__(self, course_ids):
        self.graph = defaultdict(list)
        self.nodes = set(course_ids)

    def add_prerequisite(self, prereq_id, course_id):
        self.graph[prereq_id].append(course_id)

    def neighbors(self, course_id):
        return self.graph.get(course_id, [])

    def print_graph(self):
        for node in self.nodes:
            print(f"{node} -> {self.graph[node]}")

    def has_cycle(self):
        visited = set()
        recursion_stack = set()

        def dfs(node):
            visited.add(node)
            recursion_stack.add(node)
            for neighbor in self.graph[node]:

                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

                elif neighbor in recursion_stack:
                    return True

            recursion_stack.remove(node)

            return False

        for node in self.nodes:
            if node not in visited:
                if dfs(node):
                    return True

        return False


    def topological_sort(self):

        indegree = {node: 0 for node in self.nodes}

        for node in self.graph:
            for neighbor in self.graph[node]:
                indegree[neighbor] += 1

        queue = deque()

        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        order = []
        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(self.nodes):
            raise ValueError("Cycle detected. No valid enrollment order.")
        return order

g = PrerequisiteGraph([2, 3, 8, 9])

g.add_prerequisite(2, 3)
g.add_prerequisite(3, 8)

g.add_prerequisite(2, 9)
g.add_prerequisite(9, 8)

g.print_graph()

print("\nCycle Exists:", g.has_cycle())

print("\nValid Enrollment Order:")

print(g.topological_sort())