def create(param, commands, command_list, x, y, PanelH, d):
    """裏板コマンドの生成

    裏板を描画するコマンドの生成を行う関数
        ・x座標の開始位置: 基準のx座標 (x) + 箱の奥行寸法 (d)
        ・y座標の開始位置: 基準のy座標 (y) + (天下板の高さ寸法 - 裏板と天下板の干渉部分 (5mm) (start_Ura = 13))
        ・裏板の高さ寸法 (UraH):
            パネル板の寸法 (PanelH) - (天下板の高さ寸法 - 裏板と天下板の干渉部分 (5mm) (start_Ura = 13)) * 2

    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
        PanelH (int) : 箱の高さ寸法
        d (int) : 箱の奥行寸法
    """
    # 描画に使用する変数の生成
    start_Ura = param.TenkaH - 5
    UraH = PanelH - start_Ura * 2

    X1 = x + d
    Y1 = y + start_Ura
    X2 = X1 + param.UraD
    Y2 = Y1 + UraH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
