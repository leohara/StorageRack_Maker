# 台輪を描く
def create(param, commands, command_list, x, y):
    daiwa_legD = 18
    X1 = x + 12
    Y1 = y
    X2 = X1 + param.DaiwaD - 2
    Y2 = Y1 - param.DaiwaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
    # 手前の足
    X1 = x + 12
    Y1 = y
    X2 = x + 12 + daiwa_legD
    Y2 = Y1 - param.DaiwaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
    # 奥の足
    X1 = x + 12 + param.DaiwaD - 2 - daiwa_legD
    Y1 = y
    X2 = x + 12 + param.DaiwaD - 2
    Y2 = Y1 - param.DaiwaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
