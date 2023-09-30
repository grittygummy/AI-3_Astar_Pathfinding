import heapq

def astar(maze, start, goal):

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    rows, cols = len(maze), len(maze[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    open_list = [(0, start)]
    heapq.heapify(open_list)  # Convert the list into a min-heap

    g_scores = {start: 0}
    parents = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstructs the path from the goal to the start
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]  

        for dx, dy in directions:
            new_x, new_y = current[0] + dx, current[1] + dy

            if is_valid(new_x, new_y) and maze[new_x][new_y] == 0:
               
                neighbor = (new_x, new_y)
                tentative_g_score = g_scores[current] + 1

                if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                  
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + \
                        abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1])

                    
                    heapq.heappush(open_list, (f_score, neighbor))
                    parents[neighbor] = current

    return None

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
goal = (4, 4)

path = astar(maze, start, goal)
if path:
    print("Shortest Path:", path)
else:
    print("No path found")
