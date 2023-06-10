# ダボ穴を描く
def create(param, commands, command_list, x, y, PanelH, d):
    """
    D寸法が900以上でダボが5個
    600以上で3列
    それ以下で2列

    とりあえず2列で書く

    最前列は 基準のx + 36
    最後列は 基準のx + tenkaD - 55

    lの導出
    裏板と天下上の重なり 4mm
    裏板と天下下の重なり 5mm
    裏板のH: 2070 など
    天下板 のH寸法 18
    よって H + 18*2 - 9 = H + 27
    """
    three_columns_flag = 0
    five_columns_flag = 0

    front_column = x + param.gap_dowel_front
    back_column = x + param.TenkaD - param.gap_dowel_back

    # 3列のパターン
    three_columns_list = [550, 580, 650]
    if d in three_columns_list:
        three_columns_flag = 1
        if d == 566:
            middle_column = front_column + 257
        else:
            middle_column = back_column - 250

    if d == 835:
        five_columns_flag = 1
        second_column = front_column + 257
        third_column = second_column + 220
        forth_column = third_column + 52

    dowel_y = y

    n = int((PanelH + 10) / param.gap_dowel + 1)

    dowel_list = list()

    for i in range(n):
        if dowel_y == y:
            dowel_y += 8.5
            dowel_list.append(commands.circle_command(front_column, dowel_y, 3))
            dowel_list.append(commands.circle_command(back_column, dowel_y, 3))
            if three_columns_flag:
                dowel_list.append(commands.circle_command(middle_column, dowel_y, 3))
            if five_columns_flag:
                dowel_list.append(commands.circle_command(second_column, dowel_y, 3))
                dowel_list.append(commands.circle_command(third_column, dowel_y, 3))
                dowel_list.append(commands.circle_command(forth_column, dowel_y, 3))
        else:
            dowel_y += param.gap_dowel
            dowel_list.append(commands.circle_command(front_column, dowel_y, 3))
            dowel_list.append(commands.circle_command(back_column, dowel_y, 3))
            if three_columns_flag:
                dowel_list.append(commands.circle_command(middle_column, dowel_y, 3))
            if five_columns_flag:
                dowel_list.append(commands.circle_command(second_column, dowel_y, 3))
                dowel_list.append(commands.circle_command(third_column, dowel_y, 3))
                dowel_list.append(commands.circle_command(forth_column, dowel_y, 3))

    command = dowel_list
    command_list.extend(command)
