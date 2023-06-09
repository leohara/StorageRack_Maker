def green_line(param, commands, command_list, x, y, h, d):
    vertical_line_1 = 280  # Hの列
    vertical_line_2 = 180  # DHの列

    X1 = x + 13.5
    Y1 = y - 310
    X2 = X1
    Y2 = Y1 - 108
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    X1 = x + param.TenkaD + 65.5
    X2 = X1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    X1 = x + 13.5
    Y1 = Y2
    X2 = x + param.TenkaD + 65.5
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X2, Y2, 10)
    command_list.append(command)
    command = commands.text((X1 + X2) / 2, Y1 + 10, 0, "{}".format(X2 - X1))
    command_list.append(command)

    X1 = x - 500
    Y1 = y - 60
    Y2 = Y1 + h
    line = commands.line_command(X1, Y1, X1, Y2)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X1, Y2, 10)
    command_list.append(command)
    command = commands.text(X1 - 50, (Y1 + Y2) / 2, 90, "H={}".format(Y2 - Y1))
    command_list.append(command)
    X2 = X1 + vertical_line_1
    line = commands.line_command(X1, Y1, X2, Y1)
    command_list.append(line)
    line = commands.line_command(X1, Y2, X2, Y2)
    command_list.append(line)

    X1 = x - 400
    Y1 = y - 60
    Y2 = Y1 + 60
    line = commands.line_command(X1, Y1, X1, Y2)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X1, Y2, 10)
    command_list.append(command)
    command = commands.text(X1 - 50, (Y1 + Y2) / 2, 90, "{}".format(Y2 - Y1))
    command_list.append(command)
    X2 = X1 + vertical_line_2
    line = commands.line_command(X1, Y1, X2, Y1)
    command_list.append(line)
    line = commands.line_command(X1, Y2, X2, Y2)
    command_list.append(line)

    X1 = x - 400
    Y1 = Y2
    Y2 = Y1 + 10.5
    line = commands.line_command(X1, Y1, X1, Y2)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X1, Y2, 10)
    command_list.append(command)
    command = commands.text(X1 + 60, (Y1 + Y2) / 2 + 40, 90, "{}".format(Y2 - Y1))
    command_list.append(command)
    X2 = X1 + vertical_line_2
    line = commands.line_command(X1, Y1, X2, Y1)
    command_list.append(line)
    line = commands.line_command(X1, Y2, X2, Y2)
    command_list.append(line)

    X1 = x - 400
    Y1 = Y2
    Y2 = Y1 + h - 60 - 10.5 * 2
    line = commands.line_command(X1, Y1, X1, Y2)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X1, Y2, 10)
    command_list.append(command)
    command = commands.text(X1 - 50, (Y1 + Y2) / 2, 90, "DH={}".format(Y2 - Y1))
    command_list.append(command)
    X2 = X1 + vertical_line_2
    line = commands.line_command(X1, Y1, X2, Y1)
    command_list.append(line)
    line = commands.line_command(X1, Y2, X2, Y2)
    command_list.append(line)

    X1 = x - 400
    Y1 = Y2
    Y2 = Y1 + 10.5
    line = commands.line_command(X1, Y1, X1, Y2)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X1, Y2, 10)
    command_list.append(command)
    command = commands.text(X1 - 50, (Y1 + Y2) / 2, 90, "{}".format(Y2 - Y1))
    command_list.append(command)
    X2 = X1 + vertical_line_2
    line = commands.line_command(X1, Y1, X2, Y1)
    command_list.append(line)
    line = commands.line_command(X1, Y2, X2, Y2)
    command_list.append(line)

    X1 = x - param.DoorD
    X2 = X1 + param.DoorD
    Y1 = y + h * 0.7
    line = commands.line_command(X1, Y1, X2, Y1)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X2, Y1, 10)
    command_list.append(command)
    command = commands.text((X1 + X2) / 2 - 50, Y1 + 50, 0, "{}".format(X2 - X1))
    command_list.append(command)

    X1 = X2
    X2 = X1 + d
    Y1 = y + h * 0.7
    line = commands.line_command(X1, Y1, X2, Y1)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X2, Y1, 10)
    command_list.append(command)
    command = commands.text((X1 + X2) / 2, Y1 + 50, 0, "{}".format(X2 - X1))
    command_list.append(command)

    X1 = X2
    X2 = X1 + param.UraD * 2
    Y1 = y + h * 0.7
    line = commands.line_command(X1, Y1, X2, Y1)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X2, Y1, 10)
    command_list.append(command)
    command = commands.text((X1 + X2) / 2 - 50, Y1 + 50, 0, "{}".format(X2 - X1))
    command_list.append(command)

    X1 = x - param.DoorD
    X2 = X1 + param.DoorD + d + param.UraD * 2
    Y1 = y + h * 0.6
    line = commands.line_command(X1, Y1, X2, Y1)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X2, Y1, 10)
    command_list.append(command)
    command = commands.text((X1 + X2) / 2, Y1 + 50, 0, "D={}".format(X2 - X1))
    command_list.append(command)
