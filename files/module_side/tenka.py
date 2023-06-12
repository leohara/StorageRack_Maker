def create(param, commands, command_list, x, y, PanelH, d):
    """天下板コマンドの生成

    天下板を描画するコマンドの生成を行う関数
        ・天下板の奥行寸法 (TenkaD) は
            箱の奥行寸法 (d) + 裏板とその隙間 (UraD * 2 = 16)
        ・天下板の高さ寸法 (TenkaH = 18)

    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
        PanelH (int) : パネル板の高さ寸法
        d (int) : 箱の奥行寸法
    """
    # 描画に使用する変数の生成
    TenkaD = d + param.UraD * 2

    X1 = x
    Y1 = y
    X2 = X1 + TenkaD
    Y2 = Y1 + param.TenkaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)

    X1 = x
    Y1 = y + PanelH - param.TenkaH
    X2 = X1 + TenkaD
    Y2 = Y1 + param.TenkaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
