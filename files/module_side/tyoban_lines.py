def create(param, commands, command_list, x, y, y_list):
    margin_Door = 36  # 最前列と扉の間のキョリ

    Y1 = y
    for height in y_list:
        X1 = x + margin_Door - param.tyobanW / 2
        X2 = x + margin_Door + param.tyobanW / 2
        Y1 += height
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
