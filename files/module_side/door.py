def create(param, commands, command_list, x, y, PanelH):
    """扉コマンドの生成

    扉を描画するコマンドの生成を行う関数
        ・x座標の開始位置: 基準のx座標
        ・y座標の開始位置:
            基準のy座標 (y) + 扉と天下板の隙間 (Door_Tenka = 10.5)
        ・扉の奥行寸法: DoorD = 22
        ・扉の高さ寸法 (DoorH):
            パネル板の高さ (PanelH) - 上下の扉と天下板の隙間 (Door_Tenka * 2 = 21)
    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
        PanelH (int) : パネル板の高さ寸法
    """
    # 描画に使用する変数の生成
    DoorH = PanelH - 2 * param.Door_Tenka

    X1 = x
    Y1 = y + param.Door_Tenka
    X2 = X1 - param.DoorD
    Y2 = Y1 + DoorH
    command = commands.rec_command(X1, Y1, X2, Y2)
    command_list.append(command)
