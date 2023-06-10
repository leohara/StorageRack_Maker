def create(param, commands, command_list, x, y):
    # 床
    X1 = x - 300
    Y1 = y - 310
    X2 = x + 3000
    Y2 = y - 310
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 300
    Y1 = y - 60
    X2 = x + 3000
    Y2 = y - 60
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 300
    Y1 = y - 72
    X2 = x + 3000
    Y2 = y - 72
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 300
    Y1 = y - 98
    X2 = x + 3000
    Y2 = y - 98
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
