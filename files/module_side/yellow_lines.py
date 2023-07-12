def create(param, commands, command_list, x, y):
    """周りの黄色い線コマンドの生成

    周りの黄色い線を描画するコマンドの生成を行う関数

    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
    """
    # 手前側
    X1 = x + 13.5
    Y1 = y - 310
    X2 = X1
    Y2 = Y1 + 3000
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    # 奥側
    X1 = x + param.TenkaD + 65.5
    X2 = X1
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
