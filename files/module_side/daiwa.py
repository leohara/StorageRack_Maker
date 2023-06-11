def create(param, commands, command_list, x, y, d):
    """台輪コマンドの生成

    台輪を描画するコマンドの生成を行う関数
        ・基準のx座標から12mm右側から開始
        ・台輪の奥行寸法 (DaiwaD) は
            箱の奥行寸法 + 裏板とその隙間(16mm)
        ・台輪の足の奥行寸法 (daiwa_legD) は18mm

    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
        d (int) : 箱の奥行寸法
    """
    # 描画に使用する変数の生成
    from_x = 12  # 基準から台輪までのx方向のキョリ
    daiwa_legD = 18  # 台輪の足の奥行方向の長さ
    DaiwaD = d + param.UraD * 2  # 台輪の奥行寸法

    # 手前の足
    X1 = x + from_x
    Y1 = y
    X2 = X1 + daiwa_legD
    Y2 = Y1 - param.DaiwaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)

    # 奥の足
    X1 = x + from_x + DaiwaD - daiwa_legD
    Y1 = y
    X2 = X1 + daiwa_legD
    Y2 = Y1 - param.DaiwaH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
