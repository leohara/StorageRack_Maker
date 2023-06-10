# 下側の天下板を描く
def create_under(param, commands, command_list, x, y, PanelH, d):

    TenkaD = d + param.UraD * 2

    X1 = x
    Y1 = y
    X2 = X1 + TenkaD
    Y2 = Y1 + param.TenkaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)


# 上側の天下板を描く
def create_top(param, commands, command_list, x, y, PanelH, d):

    TenkaD = d + param.UraD * 2

    X1 = x
    Y1 = y + PanelH - param.TenkaH
    X2 = X1 + TenkaD
    Y2 = Y1 + param.TenkaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
