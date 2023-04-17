class queue:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)
    
    def push(self, x):
        self.data.append(x)
        
    def pop(self):
        return self.data.pop(0)
    
def not_end(board):
    for y, row in enumerate(board):
        for x, s in enumerate(row):
            if s == 'G':
                if x ==0 or y ==0 or y == len(board) - 1 or x == len(row) - 1 :
                    return False
                elif board[y][x-1] == 'D' or board[y][x+1] == 'D' or board[y+1][x] =='D' or board[y-1][x] == 'D':
                    return False
                else :
                    return True

def possible_ways(game_map : list, visited : list, pos : [list, tuple]) -> list: 

    
    x, y = pos[0], pos[1]
    
    max_x = len(game_map[0])
    max_y = len(game_map)
    
    ways = []
    
    go_right = False
    go_left = False
    go_up = False
    go_down = False
    
    # 우
    x, y = pos[0], pos[1]
    while max_x > x + 1 and game_map[y][x+1] != 'D':
        x += 1
        go_right = True
    if go_right and not visited[y][x]:
        ways.append((x, y))
    
    # 좌
    x, y = pos[0], pos[1]
    while 0 <= x - 1 and game_map[y][x-1] != 'D':
        x -= 1
        go_left = True
    if go_left and not visited[y][x]:
        ways.append((x, y))
    
    # 아래
    x, y = pos[0], pos[1]
    while max_y > y + 1 and game_map[y+1][x] != 'D':
        y += 1
        go_down = True
    if go_down and not visited[y][x]:
        ways.append((x, y))
        
    # 위
    x, y = pos[0], pos[1]
    while 0 <= y - 1 and game_map[y-1][x] != 'D':
        y -= 1
        go_up = True
    if go_up and not visited[y][x]:
        ways.append((x, y))
        
    return ways

def get_start_pos(board : list) -> list:
    for j, row in enumerate(board):
        for i, v in enumerate(row):
            if v == "R":
                return [i, j]

def is_goal(board: list, pos: [tuple, list]) -> bool:
    x, y = pos
    if board[y][x] == 'G':
        return True
    return False

def print_map(game_map, cur_pos):
    x, y = cur_pos
    print("----------------")
    for j, row in enumerate(game_map):
        if y == j:
            if x < len(row) -2:
                row = row[:x] + 'R' + row[x+1 : ] 
            else:
                row = row[:x] + 'R'
        print(row)
        
            
def solution(board):
    if not_end(board):
        return -1
    
    answer = 0
    que = queue()
    start_pos = get_start_pos(board)
    
    que.push([tuple(start_pos)])
    visited = []
    
    for i, row in enumerate(board):
        visited.append([False for _ in range(len(row))])

    while(que):
        if answer > 10000:
            return -1
        cur_poses = que.pop()

        ways = []
        for cur_pos in cur_poses:
            visited[cur_pos[1]][cur_pos[0]] = True

            if is_goal(board, cur_pos): 
                return answer
        
            ways.extend(possible_ways(board, visited, cur_pos))

        que.push(ways)

        answer += 1
    
    
    return -1
