def create(param, commands, command_list, x, y, w_list, maepin_dict, write_flag):
    inc = 0
    list_i = 0
    maepin = maepin_dict.values()
    for w in w_list:
        if inc == 0:
            X1 = x + param.PanelW
            X2 = X1 + w
        else:
            X1 = X2 + param.PanelW
            X2 = X1 + w
        Y = y + param.shelfH - 5 + 4.5  # 5を引かないと合わない
        maepin_tmp = list(maepin)[list_i]
        for h in maepin_tmp:
            Y1 = Y + h
            Y2 = Y1 + param.shelfH
            command = commands.rec_command(X1, Y1, X2, Y2)
            command_list.append(command)
        if inc != param.num - 1:
            if write_flag[inc + 1]:
                list_i += 1
        inc += 1
