# 蝶番を描く
def create(param, commands, command_list, x, y, y_list):
    """蝶番コマンドの生成

    蝶番の概形を描画するコマンドの生成を行う関数
        ・各寸法に関しては図を参照

    Args:
        param (Param) : Excelから取得してきた値が格納されているクラス
        commands (Commands) : AutoCadで使用するコマンドの生成を行う関数を集めたクラス
        command_list (list) : 実行したファイルが最終的に出力するAutoCadのコマンドを格納した配列
        x (int) : AutoCad上で描画をする際の基準となるx座標
        y (int) : AutoCad上で描画をする際の基準となるy座標
        y_list (list) : 棚の高さが入ったリスト
    """
    margin_Door = 36
    Y1 = y
    for h in y_list:
        X1 = x + margin_Door - param.tyobanW / 2
        X2 = x + margin_Door + param.tyobanW / 2
        Y1 += h
        height = Y1
        # もっと簡略化したい
        X2 = X1 + 9
        Y1 = height + 8.5
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y1 = height - 8.5
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        X1 = x + 36 + 13.5
        X2 = X1 + 9
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y1 = height + 8.5
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        X1 = x + 36 - 10.5
        X2 = x + 36 + 10.5
        Y1 = height + 25
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y1 = height - 25
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        X1 = x + 36 - 22.5
        Y1 = height + 8.5
        Y2 = height - 8.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 + 22.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 - 10.5
        Y1 = height + 25
        Y2 = Y1 - 13.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 + 10.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 - 10.5
        Y1 = height - 25
        Y2 = Y1 + 13.5
        line = commands.line_command(X1, Y1, X1, Y2)
        command_list.append(line)
        X1 = x + 36 + 10.5
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        X1 = x + 36 - 13.5
        Y1 = height + 8.5
        X2 = X1 + 3
        Y2 = Y1 + 3
        arc = commands.arc_command(X1, Y1, X2, Y2, 3)
        command_list.append(arc)
        X1 = x + 36 + 10.5
        Y1 = height + 11.5
        X2 = X1 + 3
        Y2 = Y1 - 3
        arc = commands.arc_command(X1, Y1, X2, Y2, 3)
        command_list.append(arc)
        X1 = x + 36 + 13.5
        Y1 = height - 8.5
        X2 = X1 - 3
        Y2 = Y1 - 3
        arc = commands.arc_command(X1, Y1, X2, Y2, 3)
        command_list.append(arc)
        X1 = x + 36 - 10.5
        Y1 = height - 11.5
        X2 = X1 - 3
        Y2 = Y1 + 3
        arc = commands.arc_command(X1, Y1, X2, Y2, 3)
        command_list.append(arc)
        Y1 = height
