# 蝶番を描く
def tyoban(param, commands, command_list, x, y, y_list):

    """
    固定棚が取り付けられるタイミングで真ん中の間隔が576→608になる
    """
    Y1 = y
    for h in y_list:
        X1 = x + param.gap_dowel_front - param.tyobanW / 2
        X2 = x + param.gap_dowel_front + param.tyobanW / 2
        Y1 += h
        height = Y1
        # もっと簡略化したい
        X2 = X1 + 9
        Y1 = height + 8.5
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y1 = height - 8.5
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        X1 = x + 36 + 13.5
        X2 = X1 + 9
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y1 = height + 8.5
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        X1 = x + 36 - 10.5
        X2 = x + 36 + 10.5
        Y1 = height + 25
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y1 = height - 25
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        X1 = x + 36 - 22.5
        Y1 = height + 8.5
        Y2 = height - 8.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 + 22.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 - 10.5
        Y1 = height + 25
        Y2 = Y1 - 13.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 + 10.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 - 10.5
        Y1 = height - 25
        Y2 = Y1 + 13.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 + 10.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = x + 36 - 13.5
        Y1 = height + 8.5
        X2 = X1 + 3
        Y2 = Y1 + 3
        arc = commands.arc_command(X1, Y1, X2, Y2, 3)
        command_list.append(arc)
        X1 = x + 36 + 10.5
        Y1 = height + 11.5
        X2 = X1 + 3
        Y2 = Y1 - 3
        arc = commands.arc_command(X1, Y1, X2, Y2, 3)
        command_list.append(arc)
        X1 = x + 36 + 13.5
        Y1 = height - 8.5
        X2 = X1 - 3
        Y2 = Y1 - 3
        arc = commands.arc_command(X1, Y1, X2, Y2, 3)
        command_list.append(arc)
        X1 = x + 36 - 10.5
        Y1 = height - 11.5
        X2 = X1 - 3
        Y2 = Y1 + 3
        arc = commands.arc_command(X1, Y1, X2, Y2, 3)
        command_list.append(arc)
        Y1 = height
