# 周りの線を描く
def yellow_lines(param, commands, command_list, x, y):
    # 手前側
    X1 = x + 13.5
    Y1 = y - 310
    X2 = X1
    Y2 = Y1 + 3000
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    # 奥側
    X1 = x + param.TenkaD + 65.5
    X2 = X1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
