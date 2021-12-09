  if d[ny][nx][0] > d[y][x][0]+(0 if maze[ny][nx]!='.' else 1):
            d[ny][nx][0] = d[y][x][0]+(0 if maze[ny][nx]!='.' else 1)
            d[ny][nx][1] = d[y][x][1]+(maze[ny][nx] if maze[ny][nx]!='.' else '')
            q