def create(param, commands, command_list, x, y, y_list):
    """蝶番コマンドの生成

    蝶番の中心線を描画するコマンドの生成を行う関数

    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
        y_list (list) : 棚の高さが入ったリスト
    """
    margin_Door = 36  # 最前列と扉の間のキョリ

    Y1 = y
    for height in y_list:
        X1 = x + margin_Door - param.tyobanW / 2
        X2 = x + margin_Door + param.tyobanW / 2
        Y1 += height
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
