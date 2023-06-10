def create_body(param, commands, command_list, x, y, y_list):

    X = x + param.gap_dowel_front
    # なぜか5引かないとうまくいかない
    Y = y + 18 - 5

    for h in y_list:
        # maepin
        X = x + param.gap_dowel_front
        Y += h
        X1 = X - 12.5
        X2 = X + 12.5
        Y1 = Y + 4.5
        Y2 = Y + 4.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 15.2
        X2 = X - 15.2
        Y1 = Y + 2.39
        Y2 = Y1 + 21.81
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 14.2
        X2 = X - 7.5
        Y1 = Y + 25.2
        Y2 = Y + 25.2
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X + 12.5
        X2 = X + 12.5
        Y1 = Y + 4.5
        Y2 = Y + 2.6
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X + 4.5
        X2 = X + 11.72
        Y1 = Y
        Y2 = Y + 1.62
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 14.6
        X2 = X - 1.8
        Y1 = Y + 1.47
        Y2 = Y - 4.12
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 6.5
        X2 = X - 6.5
        Y1 = Y + 23.5
        Y2 = Y + 24.2
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 12.5
        X2 = X - 7.65
        Y1 = Y + 23.24
        Y2 = Y + 22.51
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 12.5
        X2 = X - 12.5
        Y1 = Y + 23.24
        Y2 = Y + 4.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X + 11.72
        X2 = X + 12.5
        Y1 = Y + 1.62
        Y2 = Y + 2.6
        arc = commands.arc_command(X1, Y1, X2, Y2, 1)
        command_list.append(arc)
        X1 = X - 1.8
        X2 = X + 4.5
        Y1 = Y - 4.12
        Y2 = Y
        arc = commands.arc_command(X1, Y1, X2, Y2, 4.5)
        command_list.append(arc)
        X1 = X - 15.2
        X2 = X - 14.6
        Y1 = Y + 2.39
        Y2 = Y + 1.47
        arc = commands.arc_command(X1, Y1, X2, Y2, 1)
        command_list.append(arc)
        X1 = X - 14.2
        X2 = X - 15.2
        Y1 = Y + 25.2
        Y2 = Y + 24.2
        arc = commands.arc_command(X1, Y1, X2, Y2, 1)
        command_list.append(arc)
        X1 = X - 6.5
        X2 = X - 7.5
        Y1 = Y + 24.2
        Y2 = Y + 25.2
        arc = commands.arc_command(X1, Y1, X2, Y2, 1)
        command_list.append(arc)
        X1 = X - 7.65
        X2 = X - 6.5
        Y1 = Y + 22.51
        Y2 = Y + 23.45
        arc = commands.arc_command(X1, Y1, X2, Y2, 1)
        command_list.append(arc)
        circle = commands.circle_command(X, Y, 2.5)
        command_list.append(circle)
        circle = commands.circle_command(X, Y, 3.5)
        command_list.append(circle)
        # ushiropin
        X = x + param.TenkaD - param.gap_dowel_back
        X1 = X - 5.25
        X2 = X + 5.25
        Y1 = Y + 4.5
        Y2 = Y + 4.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 4.5
        X2 = X - 4.5
        Y1 = Y
        Y2 = Y + 4.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X + 4.5
        X2 = X + 4.5
        Y1 = Y
        Y2 = Y + 4.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 5.25
        X2 = X - 5.25
        Y1 = Y
        Y2 = Y + 4.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X + 5.25
        X2 = X + 5.25
        Y1 = Y
        Y2 = Y + 4.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 5.25
        X2 = X - 3.87
        Y1 = Y
        Y2 = Y - 9.6
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X + 3.87
        X2 = X + 5.25
        Y1 = Y - 9.6
        Y2 = Y
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 2.88
        X2 = X + 2.88
        Y1 = Y - 10.5
        Y2 = Y - 10.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X - 3.87
        X2 = X - 2.88
        Y1 = Y - 9.6
        Y2 = Y - 10.5
        arc = commands.arc_command(X1, Y1, X2, Y2, 1)
        command_list.append(arc)
        X1 = X + 2.88
        X2 = X + 3.87
        Y1 = Y - 10.5
        Y2 = Y - 9.6
        arc = commands.arc_command(X1, Y1, X2, Y2, 1)
        command_list.append(arc)
        X1 = X - 4.5
        X2 = X + 4.5
        Y1 = Y
        Y2 = Y
        arc = commands.arc_command(X1, Y1, X2, Y2, 4.5)
        command_list.append(arc)
        # リセット
        Y = y + 18 - 5


def create_line(param, commands, command_list, x, y, y_list):
    X = x + param.gap_dowel_front
    # なぜか5引かないとうまくいかない
    Y = y + 18 - 5
    for h in y_list:
        # maepin
        X = x + 36
        Y += h
        X1 = X - 4.5
        X2 = X + 4.5
        Y1 = Y
        Y2 = Y
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X
        X2 = X
        Y1 = Y - 4.5
        Y2 = Y + 4.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        # ushiropin
        X = x + param.TenkaD - 55
        X1 = X - 1
        X2 = X - 1
        Y1 = Y - 10.5
        Y2 = Y - 4.39
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = X + 1
        X2 = X + 1
        Y1 = Y - 10.5
        Y2 = Y - 4.39
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        # リセット
        Y = y + 18 - 5
