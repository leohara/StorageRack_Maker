def create(param, commands, command_list, x, y, PanelH, h):
    """柱コマンドの生成

    台輪を描画するコマンドの生成を行う関数
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
        PanelH (int) : パネル板の高さ寸法
        d (int) : 箱の奥行寸法
    """
    guideH = 10  # ガイド材の高さ

    X1 = x - 9  # 壁と収納の奥行差
    Y1 = y + PanelH + guideH
    X2 = X1 + 45  # 壁の厚さ45
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    Y2 = 3400
    line = commands.line_command(X1, Y1, X1, Y2)
    command_list.append(line)
    line = commands.line_command(X2, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 22
    Y1 = y + 10.5 + 2076 + 15.5
    X2 = X1
    Y2 = 3400
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
    # 奥
    X1 = x + param.TenkaD
    Y1 = y + 18
    X2 = X1
    Y2 = Y1 + h - 96
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x + param.TenkaD + 30
    Y1 = y - 310
    X2 = X1
    Y2 = Y1 + 3000
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X1 + 13
    X2 = X1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = X1 + 45
    X2 = X1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
