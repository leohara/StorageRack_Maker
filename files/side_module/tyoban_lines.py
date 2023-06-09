def tyoban_lines(param, commands, command_list, x, y, y_list):

    Y1 = y
    for height in y_list:
        X1 = x + param.gap_dowel_front - param.tyobanW / 2
        X2 = x + param.gap_dowel_front + param.tyobanW / 2
        Y1 += height
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
