# 扉を描く
def create(param, commands, command_list, x, y, PanelH):
    """
    """
    X1 = x
    Y1 = y + param.Door_Tenka
    X2 = X1 - param.DoorD
    Y2 = Y1 + PanelH - 2 * param.Door_Tenka
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
