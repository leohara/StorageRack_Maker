def create(param, commands, command_list, x, y, y_list):
    X1 = x + param.Door_shelf
    X2 = X1 + param.TenkaD - param.gap_back - param.UraD - param.Door_shelf
    Y = y + param.shelfH - 5 + 4.5  # 5を引かないと合わない
    for h in y_list:
        Y1 = Y + h
        Y2 = Y1 + param.shelfH
        command = commands.rec_command(X1, Y1, X2, Y2)
        command_list.append(command)
