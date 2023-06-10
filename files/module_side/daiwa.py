# 台輪を描く
def create(param, commands, command_list, x, y, d):

    from_x = 12  # 基準から台輪までのx方向のキョリ
    daiwa_legD = 18  # 台輪の足の奥行方向の長さ
    DaiwaD = d + param.UraD * 2 - from_x

    # 手前の足
    X1 = x + from_x
    Y1 = y
    X2 = x + from_x + daiwa_legD
    Y2 = Y1 - param.DaiwaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)

    # 奥の足
    X1 = x + from_x + DaiwaD - daiwa_legD
    Y1 = y
    X2 = x + from_x + DaiwaD
    Y2 = Y1 - param.DaiwaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
