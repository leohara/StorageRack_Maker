def create(param, commands, command_list, x, y, PanelH):
    """ガイド材コマンドの生成

    ダボ穴を描画するコマンドの生成を行う関数
        ・y座標の開始位置: 基準のy座標 (y) + パネル板の高さ寸法 (PanelH)
        ・各寸法に関しては図を参照

    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
        PanelH (int) : パネル板の高さ寸法
    """
    X1 = x
    Y1 = y + PanelH
    X2 = X1 + 30
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    X1 = X2
    Y1 = Y2
    X2 = X1
    Y2 = Y1 + 10
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    X1 = X2
    Y1 = Y2
    X2 = X1 - 39
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    X1 = X2
    Y1 = Y2
    X2 = X1
    Y2 = Y1 - 5
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    X1 = X2
    Y1 = Y2
    X2 = X1 - 13
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    X1 = X2
    Y1 = Y2
    X2 = X1
    Y2 = Y1 - 10
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    X1 = X2
    Y1 = Y2
    X2 = X1 + 22
    Y2 = Y1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)

    X1 = X2
    Y1 = Y2
    X2 = X1
    Y2 = Y1 + 5
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
