def create(param, commands, command_list, x, y, PanelH_list, TenkaW_list):
    X1 = x + param.PanelW_outer
    for PanelH, TenkaW, boolean in zip(PanelH_list, TenkaW_list, param.flag):
        Y1 = y + PanelH / 2 + param.PanelW_inner
        if boolean:
            X2 = X1 + TenkaW / 2 + param.PanelW_inner
        else:
            X2 = X1 + TenkaW + param.PanelW_inner * 2
        Y2 = y + PanelH - param.Door_Tenka
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        Y2 = y + param.Door_Tenka
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        if boolean:
            X1 = X2
            X2 = X1 + TenkaW / 2 + param.PanelW_inner
            Y2 = y + PanelH - param.Door_Tenka
            line = commands.line_command(X1, Y2, X2, Y1)
            command_list.append(line)
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y2, X2, Y1)
            command_list.append(line)
        X1 = X2 + 4
