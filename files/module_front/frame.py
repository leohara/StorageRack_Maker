def create(param, commands, command_list, x, y, PanelH_list, TenkaW_list):
    flame_flag = [int(
        (PanelH_list[i] - PanelH_list[i + 1]) / abs(PanelH_list[i] - PanelH_list[i + 1])) if (PanelH_list[i] - PanelH_list[i + 1] != 0) else 0 for i in range(param.num - 1)]
    flame_flag.append(0)
    # 外枠
    enum = 0
    prevH = PanelH_list[0]
    prev_flag = 0
    X2 = x
    for PanelH, TenkaW, f_flag in zip(PanelH_list, TenkaW_list, flame_flag):
        X1 = X2
        Y1 = y
        if PanelH > prevH:  # H方向
            Y1 = Y1 + prevH
            Y2 = Y1 + PanelH - prevH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        elif PanelH < prevH:
            Y1 = Y1 + PanelH
            Y2 = Y1 + prevH - PanelH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        elif enum == 0:
            Y2 = Y1 + PanelH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        #######################
        # 基準
        if enum == 0:  # W方向
            X2 = X1 + TenkaW + param.PanelW_outer * 2 + param.PanelW_inner - 2 + f_flag * 9
        elif enum != param.num - 1:
            X2 = X1 + TenkaW + 2 * param.PanelW_inner + 2 * 2 + prev_flag * (-9) + f_flag * 9
        else:
            Y1 = y
            Y2 = Y1 + PanelH
            X2 = X1 + TenkaW + param.PanelW_outer + 2 * param.PanelW_inner + 2 + prev_flag * (-9) + f_flag * 9
        command = commands.line_command(X1, Y2, X2, Y2)
        command_list.append(command)
        #######################
        if enum == param.num - 1:  # 右端のパターン
            Y1 = y
            Y2 = Y1 + PanelH
            command = commands.line_command(X2, Y1, X2, Y2)
            command_list.append(command)
        enum += 1
        prevH = PanelH
        prev_flag = f_flag

    # 内枠
    X1 = x
    for TenkaW, PanelH in zip(TenkaW_list, PanelH_list):
        X1 = X1 + param.PanelW
        Y1 = y + param.TenkaH
        X2 = X1 + TenkaW
        Y2 = y + PanelH - param.TenkaH
        command = commands.rec_command(X1, Y1, X2, Y2)
        command_list.append(command)
        X1 = X2
