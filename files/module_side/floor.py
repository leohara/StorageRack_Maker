def create(param, commands, command_list, x, y):
    """床コマンドの生成

    床を描画するコマンドの生成を行う関数
        ・x座標の開始位置:
            基準のx座標 (x) + 12
        ・y座標の開始位置: 基準のy座標
        ・台輪の奥行寸法 (DaiwaD) は
            箱の奥行寸法 (d) + 裏板とその隙間 (UraD * 2 = 16)
        ・台輪の足の奥行寸法 (daiwa_legD = 18)

    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
    """
    from_x = 12
    under_floor = 26
    bottom = 212
    floorH = 12
    offset_left = 782
    offset_right = 30

    X1 = x - offset_left
    Y1 = y - param.DaiwaH
    X2 = x + param.TenkaD + offset_right
    Y2 = y - param.DaiwaH
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - offset_left
    Y1 = y - param.DaiwaH + floorH
    X2 = x + from_x
    Y2 = y - param.DaiwaH + floorH
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - offset_left
    Y1 = y - param.DaiwaH - under_floor
    X2 = x + param.TenkaD + offset_right
    Y2 = y - param.DaiwaH - under_floor
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - offset_left
    Y1 = y - param.DaiwaH - under_floor - bottom
    X2 = x + param.TenkaD + offset_right
    Y2 = y - param.DaiwaH - under_floor - bottom
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
