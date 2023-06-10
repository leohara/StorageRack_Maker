def create(param, commands, command_list, x, y, PanelH_list, TenkaW_list):
    X1 = x + param.PanelW_outer
    Y1 = y + param.Door_Tenka
    for TenkaW, PanelH in zip(TenkaW_list, PanelH_list):
        Y2 = Y1 + PanelH - 2 * param.Door_Tenka
        X2 = X1 + TenkaW + param.PanelW_inner * 2
        command = commands.rec_command(X1, Y1, X2, Y2)
        command_list.append(command)
        X1 = X2 + 4
