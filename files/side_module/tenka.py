# 下側の天下板を描く
def create_under(param, commands, command_list, x, y, PanelH):
    X1 = x
    Y1 = y
    X2 = X1 + param.TenkaD
    Y2 = Y1 + param.TenkaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)


# 例外があるかも
# 上側の天下板を描く
def create_top(param, commands, command_list, x, y, PanelH):
    X1 = x
    Y1 = y + PanelH - param.TenkaH
    X2 = X1 + param.TenkaD
    Y2 = Y1 + param.TenkaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
