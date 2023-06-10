# 実線の方
def create(param, commands, command_list, x, y, PanelH_list, TenkaW_list, bump_list):
    enum = 0
    prevH = PanelH_list[0]
    X2 = x + 6
    for PanelH, TenkaW in zip(PanelH_list, TenkaW_list):
        X1 = X2
        Y1 = y
        if PanelH > prevH:
            Y1 = Y1 + prevH - 6
            Y2 = Y1 + PanelH - prevH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        elif PanelH < prevH:
            Y1 = Y1 + PanelH - 6
            Y2 = Y1 + prevH - PanelH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        elif enum == 0:
            Y1 = y - 60
            Y2 = Y1 + PanelH + 54
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)

        if enum == 0:
            X2 = X1 + TenkaW + param.Frame_inner + param.Frame_outer - 3 * bump_list[enum + 1]
        elif enum == param.num - 1:
            Y1 = y - 60
            Y2 = Y1 + PanelH + 54
            X2 = X1 + TenkaW + param.Frame_inner + param.Frame_outer + 3 * bump_list[enum]
        else:
            X2 = X1 + TenkaW + param.Frame_inner * 2 + 3 * (bump_list[enum] - bump_list[enum + 1])
        command = commands.line_command(X1, Y2, X2, Y2)
        command_list.append(command)
        if enum == param.num - 1:
            Y1 = y - 60
            Y2 = Y1 + PanelH + 54
            command = commands.line_command(X2, Y1, X2, Y2)
            command_list.append(command)
        enum += 1
        prevH = PanelH
