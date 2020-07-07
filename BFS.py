from collections import deque

def solve(maze):
  start = maze.start
  end = maze.end
  mat = maze.mat
  m = len(mat)
  n = len(mat[0])

  
  vist = []
  pat = []
  for y in range(0,m):
	  lst=[]
	  pst=[]
	  for x in range(0,n):
	  	lst.append(0)
	  	pst.append([-1,-1])
	  vist.append(lst)
	  pat.append(pst)
 
  
 
  path = []
  
  queue = []
  queue.append(start)

  vist[start[0]][start[1]] = 1;
  
  print("start BFS")
  complete = 0
  
  while queue :
    cur = queue.pop(0)
    x = cur[0]
    y = cur[1]


    if cur == end:
      complete = 1
      break
    if y+1 < n and vist[x][y+1]== 0  and mat[x][y+1]==1:
      vist[x][y+1]=1
      pat[x][y+1] = [x,y]
      queue.append([x,y+1])
      
    if y-1 >= 0 and vist[x][y-1]==0  and mat[x][y-1]==1 :
      vist[x][y-1]=1
      pat[x][y-1] = [x,y]
      queue.append([x,y-1])
    if x+1 < m and vist[x+1][y]==0 and  mat[x+1][y]==1 :
      vist[x+1][y]=1
      pat[x+1][y] = [x,y]
      queue.append([x+1,y])

    if x-1 >= 0 and vist[x-1][y]==0 and  mat[x-1][y]==1 :
      vist[x-1][y]=1
      pat[x-1][y] = [x,y]
      queue.append([x-1,y])
  
  print("end bfs")
  
  curr = end
  while(curr != start):
    path.append(curr)
    curr = pat[curr[0]][curr[1]]
  path.append(start)

  return path
  
