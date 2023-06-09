# ガイド材を描く
# もっと簡単に描けそう
def guide(param, commands, command_list, x, y, PanelH):
    X1 = x
    Y1 = y + PanelH
    X2 = X1 + 30
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X2
    Y1 = Y2
    X2 = X1
    Y2 = Y1 + 10
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X2
    Y1 = Y2
    X2 = X1 - 39
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X2
    Y1 = Y2
    X2 = X1
    Y2 = Y1 - 5
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X2
    Y1 = Y2
    X2 = X1 - 13
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X2
    Y1 = Y2
    X2 = X1
    Y2 = Y1 - 10
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X2
    Y1 = Y2
    X2 = X1 + 22
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X2
    Y1 = Y2
    X2 = X1
    Y2 = Y1 + 5
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
