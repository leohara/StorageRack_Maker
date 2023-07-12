def create(param, commands, command_list, x, y, y_list):
    """棚コマンドの生成

    棚を描画するコマンドの生成を行う関数
        ・x座標の開始位置: 基準のx座標 + 扉と棚の間のキョリ (Door_shelf = 24)

    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
        y_list (list) : 棚の高さが入ったリスト
    """
    X1 = x + param.Door_shelf
    X2 = X1 + param.TenkaD - param.gap_back - param.UraD - param.Door_shelf
    Y = y + param.shelfH - 0.5
    for h in y_list:
        Y1 = Y + h
        Y2 = Y1 + param.shelfH
        command = commands.rec_command(X1, Y1, X2, Y2)
        command_list.append(command)
