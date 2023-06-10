def create(param, commands, command_list, x, y, PanelH, h):
    # 手前側

    guideH = 10  # ガイド材の高さ

    X1 = x - 9  # 壁と収納の奥行差
    Y1 = y + PanelH + guideH
    X2 = X1 + 45  # 壁の厚さ45
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    Y2 = 3400
    line = commands.line_command(X1, Y1, X1, Y2)
    command_list.append(line)
    line = commands.line_command(X2, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 22
    Y1 = y + 10.5 + 2076 + 15.5
    X2 = X1
    Y2 = 3400
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
    # 奥
    X1 = x + param.TenkaD
    Y1 = y + 18
    X2 = X1
    Y2 = Y1 + h - 96
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x + param.TenkaD + 30
    Y1 = y - 310
    X2 = X1
    Y2 = Y1 + 3000
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X1 + 13
    X2 = X1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X1 + 45
    X2 = X1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    # 床
    X1 = x - 781.78
    Y1 = y - 310
    X2 = x + 1579.5
    Y2 = y - 310
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 781.78
    Y1 = y - 60
    X2 = x + 12
    Y2 = y - 60
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 781.78
    Y1 = y - 72
    X2 = x + 1494
    Y2 = y - 72
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 781.78
    Y1 = y - 98
    X2 = x + 1494
    Y2 = y - 98
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
