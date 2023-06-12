def create(param, commands, command_list, x, y, PanelH, d):
    """ダボ穴コマンドの生成

    ダボ穴を描画するコマンドの生成を行う関数
        ・y座標の開始位置: 基準のy座標 (y)
        ・最前列 (front_column) :
            基準のx座標 (x) + 扉との隙間 (margin_Door = 36)
        ・最後列 (back_column) :
            基準のx座標 + 天下板の奥行寸法 (TenkaD) - 裏板との隙間 (margin_Ura = 53)
        ・ダボ穴の列数:
            d < 550 → 2列
            d in [550, 580, 650] → 3列
            d = 845 → 5列
        ・3列の場合:
            真ん中の列 (middle_column) : 最後列 (back_column) - 250
        ・5列の場合:
            2番目の列: 最前列 (front_column) + 257
            3番目の列: 2番目の列 (second_column) + 220
            4番目の列: 3番目の列 (third_column) + 52
        ・ダボ穴は y から32mm (interval) ごとに生成

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
    three_columns_list = [550, 580, 650]  # 3列になる奥行寸法の条件
    columns = 0  # 列数を表す
    margin_Door = 36  # 最前列と扉の間のキョリ
    margin_Ura = 53  # 最後列と裏板の間のキョリ
    interval = 32  # ダボ穴の縦の間隔
    dowel_n = int((PanelH + 10) / interval + 1)  # 縦に並ぶダボ穴の数

    front_column = x + margin_Door
    back_column = x + param.TenkaD - margin_Ura

    # 必要な列の生成
    if d in three_columns_list:  # 3列のパターン
        columns = 3
        middle_column = back_column - 250
        column_list = [middle_column]
    if d == 835:  # 5列のパターン
        columns = 5
        second_column = front_column + 257
        third_column = second_column + 220
        forth_column = third_column + 52
        column_list = [second_column, third_column, forth_column]

    # ダボ穴の生成
    dowel_y = y
    dowel_list = list()

    for i in range(dowel_n):
        if dowel_y == y:
            dowel_y += 8.5
        else:
            dowel_y += interval
        dowel_list.append(commands.circle_command(front_column, dowel_y, 3))
        dowel_list.append(commands.circle_command(back_column, dowel_y, 3))
        for i, column in zip(range(columns - 2), column_list):
            dowel_list.append(commands.circle_command(column, dowel_y, 3))

    command = dowel_list
    command_list.extend(command)
