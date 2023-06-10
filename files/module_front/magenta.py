def create(param, commands, command_list, x, y, w_list, PanelH_list):
    X_ = x
    for block, boolean, height in zip(w_list, param.flag, PanelH_list):
        if not boolean:
            X_ = X_ + param.PanelW + block
        else:
            X1 = X_ + block / 2 + param.PanelW
            Y1 = y + height - param.Door_Tenka
            X2 = X_ + block / 2 + param.PanelW
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X1 = X_ + block / 2 + 15 + param.PanelW
            Y1 = y + height - param.Door_Tenka
            X2 = X_ + block / 2 + 15 + param.PanelW
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X1 = X_ + block / 2 - 15 + param.PanelW
            Y1 = y + height - param.Door_Tenka
            X2 = X_ + block / 2 - 15 + param.PanelW
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X1 = X_ + block / 2 - 15 + param.PanelW
            Y1 = y + height - param.Door_Tenka
            X2 = X_ + block / 2 + 15 + param.PanelW
            Y2 = y + param.PanelH - param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X1 = X_ + block / 2 - 15 + param.PanelW
            Y1 = y + param.Door_Tenka
            X2 = X_ + block / 2 + 15 + param.PanelW
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X_ = X_ + param.PanelW + block
