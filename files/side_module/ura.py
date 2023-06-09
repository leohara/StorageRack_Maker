# 裏板を描く
def create(param, commands, command_list, x, y, h, d):
    X1 = x + d
    Y1 = y + 13
    X2 = X1 + param.UraD
    Y2 = Y1 + h - 87
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
