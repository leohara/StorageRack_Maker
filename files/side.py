from . import parameters
from . import commands


class Side:

    def __init__(self):
        self.command_list = list()

    def create_parameters(self):
        self.param = parameters.Param()
        self.x = self.param.x_side
        self.y = self.param.y_side
        # tyoban_lines & tyoban
        margin1 = 142  # 最上下端
        margin2 = 576  # 固定棚なしの上下
        margin3 = 608  # 固定棚ありの上下
        margin4 = self.param.DaiwaH - 12  # 台輪 - フローリング

        # 固定棚無し
        if self.param.H <= 2157:
            tyoban_center_h = self.param.H - (
                self.param.Door_Tenka * 2 + margin1 * 2 + margin2 * 2 + margin4
            )
            self.tyoban_list = [self.param.Door_Tenka + margin1, margin2, tyoban_center_h, margin2]
        # 固定棚有り
        elif self.param.H > 2157:
            tyoban_center_h = self.param.H - (
                self.param.Door_Tenka * 2 + margin1 * 2 + margin3 * 2 + margin4
            )
            self.tyoban_list = [self.param.Door_Tenka + margin1, margin3, tyoban_center_h, margin3]

        # 全然合わないので2061だけ603.5スタートでそこから468ずつ足した
        # CD51のリスト
        maepin_list_dict = {'1965': [539.5, 987.5, 1435.5],
                            '2061': [603.5, 1083.5, 1563.5],
                            '2125': [603.5, 1083.5, 1563.5],
                            '2157': [603.5, 1083.5, 1563.5],
                            '2253': [603.5, 1211.5],
                            '2349': [603.5, 1211.5],
                            '2445': [603.5, 1211.5],
                            }
        # 高さからリストを取得してくる
        self.maepin_list = maepin_list_dict[str(int(self.param.h_B))]

    # デコレーターで初期化する
    def decorator(func):
        def inner(self, *args, **kwargs):
            self.command_list.append('ATTDIA 0 ')
            self.command_list.append('')
            func(*args, **kwargs)
            self.command_list.append('')
            self.command_list.append('ATTDIA 1 ')
        return inner

    @decorator
    # 画層を変更する
    def layer_change(self, color):
        command = '-LAYER s {}'.format(color)
        self.command_list.append(command)

    @decorator
    def dimexo(self, d):
        command = 'dimexo {} '.format(d)
        self.command_list.append(command)

    # 台輪を描く
    def daiwa(self):
        daiwa_legD = 18
        X1 = self.x + 12
        Y1 = self.y
        X2 = X1 + self.param.DaiwaD - 2
        Y2 = Y1 - self.param.DaiwaH
        command = commands.rec_command(X1, Y1, X2, Y2)
        self.command_list.append(command)
        # 手前の足
        X1 = self.x + 12
        Y1 = self.y
        X2 = self.x + 12 + daiwa_legD
        Y2 = Y1 - self.param.DaiwaH
        command = commands.rec_command(X1, Y1, X2, Y2)
        self.command_list.append(command)
        # 奥の足
        X1 = self.x + 12 + self.param.DaiwaD - 2 - daiwa_legD
        Y1 = self.y
        X2 = self.x + 12 + self.param.DaiwaD - 2
        Y2 = Y1 - self.param.DaiwaH
        command = commands.rec_command(X1, Y1, X2, Y2)
        self.command_list.append(command)

    # 下側の天下板を描く
    def tenka_under(self):
        X1 = self.x
        Y1 = self.y
        X2 = X1 + self.param.TenkaD
        Y2 = Y1 + self.param.TenkaH
        command = commands.rec_command(X1, Y1, X2, Y2)
        self.command_list.append(command)

    # 例外があるかも
    # 上側の天下板を描く
    def tenka_top(self):
        X1 = self.x
        Y1 = self.y + self.param.PanelH - self.param.TenkaH
        X2 = X1 + self.param.TenkaD
        Y2 = Y1 + self.param.TenkaH
        command = commands.rec_command(X1, Y1, X2, Y2)
        self.command_list.append(command)

    # 裏板を描く
    def ura(self):
        X1 = self.x + self.param.D
        Y1 = self.y + 13
        X2 = X1 + self.param.UraD
        Y2 = Y1 + self.param.h_B - 87
        command = commands.rec_command(X1, Y1, X2, Y2)
        self.command_list.append(command)

    # ガイド材を描く
    # もっと簡単に描けそう
    def guide(self):
        X1 = self.x
        Y1 = self.y + self.param.PanelH
        X2 = X1 + 30
        Y2 = Y1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1
        Y2 = Y1 + 10
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1 - 39
        Y2 = Y1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1
        Y2 = Y1 - 5
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1 - 13
        Y2 = Y1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1
        Y2 = Y1 - 10
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1 + 22
        Y2 = Y1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1
        Y2 = Y1 + 5
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)

    # 扉を描く
    def door(self):
        """
        上下天下板の上端下端それぞれ10.5内側からスタート
        Y2 の計算だけ直す
        """
        X1 = self.x
        Y1 = self.y + self.param.Door_Tenka
        X2 = X1 - self.param.DoorD
        Y2 = Y1 + self.param.PanelH - 2 * self.param.Door_Tenka
        command = commands.rec_command(X1, Y1, X2, Y2)
        self.command_list.append(command)

    def m_shelf_board(self):
        X1 = self.x + self.param.Door_shelf
        X2 = X1 + self.param.TenkaD - self.param.gap_back - self.param.UraD - self.param.Door_shelf
        Y = self.y + self.param.shelfH - 5 + 4.5  # 5を引かないと合わない
        for h in self.maepin_list:
            Y1 = Y + h
            Y2 = Y1 + self.param.shelfH
            command = commands.rec_command(X1, Y1, X2, Y2)
            self.command_list.append(command)

    def white_lines(self):
        # 手前側

        guideH = 10  # ガイド材の高さ

        X1 = self.x - 9  # 壁と収納の奥行差
        Y1 = self.y + self.param.PanelH + guideH
        X2 = X1 + 45  # 壁の厚さ45
        Y2 = Y1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        Y2 = 3400
        line = commands.line_command(X1, Y1, X1, Y2)
        self.command_list.append(line)
        line = commands.line_command(X2, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = self.x - 22
        Y1 = self.y + 10.5 + 2076 + 15.5
        X2 = X1
        Y2 = 3400
        command = commands.rec_command(X1, Y1, X2, Y2)
        self.command_list.append(command)
        # 奥
        X1 = self.x + self.param.TenkaD
        Y1 = self.y + 18
        X2 = X1
        Y2 = Y1 + self.param.h_B - 96
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = self.x + self.param.TenkaD + 30
        Y1 = self.y - 310
        X2 = X1
        Y2 = Y1 + 3000
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = X1 + 13
        X2 = X1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = X1 + 45
        X2 = X1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)

        # 床
        X1 = self.x - 781.78
        Y1 = self.y - 310
        X2 = self.x + 1579.5
        Y2 = self.y - 310
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = self.x - 781.78
        Y1 = self.y - 60
        X2 = self.x + 12
        Y2 = self.y - 60
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = self.x - 781.78
        Y1 = self.y - 72
        X2 = self.x + 1494
        Y2 = self.y - 72
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = self.x - 781.78
        Y1 = self.y - 98
        X2 = self.x + 1494
        Y2 = self.y - 98
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)

    def tyoban_lines(self):

        Y1 = self.y
        for h in self.tyoban_list:
            X1 = self.x + self.param.gap_dowel_front - self.param.tyobanW / 2
            X2 = self.x + self.param.gap_dowel_front + self.param.tyobanW / 2
            Y1 += h
            self.param.H = Y1
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)

    # ダボ穴を描く
    def dowel_hole(self):
        """
        D寸法が900以上でダボが5個
        600以上で3列
        それ以下で2列

        とりあえず2列で書く

        最前列は 基準のx + 36
        最後列は 基準のx + tenkaD - 55

        lの導出
        裏板と天下上の重なり 4mm
        裏板と天下下の重なり 5mm
        裏板のH: 2070 など
        天下板 のH寸法 18
        よって H + 18*2 - 9 = H + 27
        """
        three_columns_flag = 0
        five_columns_flag = 0

        front_column = self.x + self.param.gap_dowel_front
        back_column = self.x + self.param.TenkaD - self.param.gap_dowel_back

        # 3列のパターン
        three_columns_list = [550, 580, 650]
        if self.param.D in three_columns_list:
            three_columns_flag = 1
            if self.param.D == 566:
                middle_column = front_column + 257
            else:
                middle_column = back_column - 250

        if self.param.D == 835:
            five_columns_flag = 1
            second_column = front_column + 257
            third_column = second_column + 220
            forth_column = third_column + 52

        dowel_y = self.y

        n = int((self.param.PanelH + 10) / self.param.gap_dowel + 1)

        dowel_list = list()

        for i in range(n):
            if dowel_y == self.y:
                dowel_y += 8.5
                dowel_list.append(commands.circle_command(front_column, dowel_y, 3))
                dowel_list.append(commands.circle_command(back_column, dowel_y, 3))
                if three_columns_flag:
                    dowel_list.append(commands.circle_command(middle_column, dowel_y, 3))
                if five_columns_flag:
                    dowel_list.append(commands.circle_command(second_column, dowel_y, 3))
                    dowel_list.append(commands.circle_command(third_column, dowel_y, 3))
                    dowel_list.append(commands.circle_command(forth_column, dowel_y, 3))
            else:
                dowel_y += self.param.gap_dowel
                dowel_list.append(commands.circle_command(front_column, dowel_y, 3))
                dowel_list.append(commands.circle_command(back_column, dowel_y, 3))
                if three_columns_flag:
                    dowel_list.append(commands.circle_command(middle_column, dowel_y, 3))
                if five_columns_flag:
                    dowel_list.append(commands.circle_command(second_column, dowel_y, 3))
                    dowel_list.append(commands.circle_command(third_column, dowel_y, 3))
                    dowel_list.append(commands.circle_command(forth_column, dowel_y, 3))

        command = dowel_list
        self.command_list.extend(command)

    # 周りの線を描く
    def yellow_lines(self):
        # 手前側
        X1 = self.x + 13.5
        Y1 = self.y - 310
        X2 = X1
        Y2 = Y1 + 3000
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        # 奥側
        X1 = self.x + self.param.TenkaD + 65.5
        X2 = X1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)

    # 蝶番を描く
    def tyoban(self):

        """
        固定棚が取り付けられるタイミングで真ん中の間隔が576→608になる
        """
        # X = x + param.gap_dowel_front
        Y1 = self.y
        for h in self.tyoban_list:
            X1 = self.x + self.param.gap_dowel_front - self.param.tyobanW / 2
            X2 = self.x + self.param.gap_dowel_front + self.param.tyobanW / 2
            Y1 += h
            height = Y1
            # もっと簡略化したい
            X2 = X1 + 9
            Y1 = height + 8.5
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            Y1 = height - 8.5
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            X1 = self.x + 36 + 13.5
            X2 = X1 + 9
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            Y1 = height + 8.5
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            X1 = self.x + 36 - 10.5
            X2 = self.x + 36 + 10.5
            Y1 = height + 25
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            Y1 = height - 25
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            X1 = self.x + 36 - 22.5
            Y1 = height + 8.5
            Y2 = height - 8.5
            line = commands.line_command(X1, Y1, X1, Y2)
            self.command_list.append(line)
            X1 = self.x + 36 + 22.5
            line = commands.line_command(X1, Y1, X1, Y2)
            self.command_list.append(line)
            X1 = self.x + 36 - 10.5
            Y1 = height + 25
            Y2 = Y1 - 13.5
            line = commands.line_command(X1, Y1, X1, Y2)
            self.command_list.append(line)
            X1 = self.x + 36 + 10.5
            line = commands.line_command(X1, Y1, X1, Y2)
            self.command_list.append(line)
            X1 = self.x + 36 - 10.5
            Y1 = height - 25
            Y2 = Y1 + 13.5
            line = commands.line_command(X1, Y1, X1, Y2)
            self.command_list.append(line)
            X1 = self.x + 36 + 10.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = self.x + 36 - 13.5
            Y1 = height + 8.5
            X2 = X1 + 3
            Y2 = Y1 + 3
            arc = commands.arc_command(X1, Y1, X2, Y2, 3)
            self.command_list.append(arc)
            X1 = self.x + 36 + 10.5
            Y1 = height + 11.5
            X2 = X1 + 3
            Y2 = Y1 - 3
            arc = commands.arc_command(X1, Y1, X2, Y2, 3)
            self.command_list.append(arc)
            X1 = self.x + 36 + 13.5
            Y1 = height - 8.5
            X2 = X1 - 3
            Y2 = Y1 - 3
            arc = commands.arc_command(X1, Y1, X2, Y2, 3)
            self.command_list.append(arc)
            X1 = self.x + 36 - 10.5
            Y1 = height - 11.5
            X2 = X1 - 3
            Y2 = Y1 + 3
            arc = commands.arc_command(X1, Y1, X2, Y2, 3)
            self.command_list.append(arc)
            Y1 = height

    def maepin_and_ushiropin(self):

        X = self.x + self.param.gap_dowel_front
        # なぜか5引かないとうまくいかない
        Y = self.y + 18 - 5

        for h in self.maepin_list:
            # maepin
            X = self.x + self.param.gap_dowel_front
            Y += h
            X1 = X - 12.5
            X2 = X + 12.5
            Y1 = Y + 4.5
            Y2 = Y + 4.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 15.2
            X2 = X - 15.2
            Y1 = Y + 2.39
            Y2 = Y1 + 21.81
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 14.2
            X2 = X - 7.5
            Y1 = Y + 25.2
            Y2 = Y + 25.2
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X + 12.5
            X2 = X + 12.5
            Y1 = Y + 4.5
            Y2 = Y + 2.6
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X + 4.5
            X2 = X + 11.72
            Y1 = Y
            Y2 = Y + 1.62
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 14.6
            X2 = X - 1.8
            Y1 = Y + 1.47
            Y2 = Y - 4.12
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 6.5
            X2 = X - 6.5
            Y1 = Y + 23.5
            Y2 = Y + 24.2
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 12.5
            X2 = X - 7.65
            Y1 = Y + 23.24
            Y2 = Y + 22.51
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 12.5
            X2 = X - 12.5
            Y1 = Y + 23.24
            Y2 = Y + 4.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X + 11.72
            X2 = X + 12.5
            Y1 = Y + 1.62
            Y2 = Y + 2.6
            arc = commands.arc_command(X1, Y1, X2, Y2, 1)
            self.command_list.append(arc)
            X1 = X - 1.8
            X2 = X + 4.5
            Y1 = Y - 4.12
            Y2 = Y
            arc = commands.arc_command(X1, Y1, X2, Y2, 4.5)
            self.command_list.append(arc)
            X1 = X - 15.2
            X2 = X - 14.6
            Y1 = Y + 2.39
            Y2 = Y + 1.47
            arc = commands.arc_command(X1, Y1, X2, Y2, 1)
            self.command_list.append(arc)
            X1 = X - 14.2
            X2 = X - 15.2
            Y1 = Y + 25.2
            Y2 = Y + 24.2
            arc = commands.arc_command(X1, Y1, X2, Y2, 1)
            self.command_list.append(arc)
            X1 = X - 6.5
            X2 = X - 7.5
            Y1 = Y + 24.2
            Y2 = Y + 25.2
            arc = commands.arc_command(X1, Y1, X2, Y2, 1)
            self.command_list.append(arc)
            X1 = X - 7.65
            X2 = X - 6.5
            Y1 = Y + 22.51
            Y2 = Y + 23.45
            arc = commands.arc_command(X1, Y1, X2, Y2, 1)
            self.command_list.append(arc)
            circle = commands.circle_command(X, Y, 2.5)
            self.command_list.append(circle)
            circle = commands.circle_command(X, Y, 3.5)
            self.command_list.append(circle)
            # ushiropin
            X = self.x + self.param.TenkaD - self.param.gap_dowel_back
            X1 = X - 5.25
            X2 = X + 5.25
            Y1 = Y + 4.5
            Y2 = Y + 4.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 4.5
            X2 = X - 4.5
            Y1 = Y
            Y2 = Y + 4.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X + 4.5
            X2 = X + 4.5
            Y1 = Y
            Y2 = Y + 4.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 5.25
            X2 = X - 5.25
            Y1 = Y
            Y2 = Y + 4.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X + 5.25
            X2 = X + 5.25
            Y1 = Y
            Y2 = Y + 4.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 5.25
            X2 = X - 3.87
            Y1 = Y
            Y2 = Y - 9.6
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X + 3.87
            X2 = X + 5.25
            Y1 = Y - 9.6
            Y2 = Y
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 2.88
            X2 = X + 2.88
            Y1 = Y - 10.5
            Y2 = Y - 10.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X - 3.87
            X2 = X - 2.88
            Y1 = Y - 9.6
            Y2 = Y - 10.5
            arc = commands.arc_command(X1, Y1, X2, Y2, 1)
            self.command_list.append(arc)
            X1 = X + 2.88
            X2 = X + 3.87
            Y1 = Y - 10.5
            Y2 = Y - 9.6
            arc = commands.arc_command(X1, Y1, X2, Y2, 1)
            self.command_list.append(arc)
            X1 = X - 4.5
            X2 = X + 4.5
            Y1 = Y
            Y2 = Y
            arc = commands.arc_command(X1, Y1, X2, Y2, 4.5)
            self.command_list.append(arc)
            # リセット
            Y = self.y + 18 - 5

    def maepin_and_ushiropin_lines(self):
        X = self.x + self.param.gap_dowel_front
        # なぜか5引かないとうまくいかない
        Y = self.y + 18 - 5
        for h in self.maepin_list:
            # maepin
            X = self.x + 36
            Y += h
            X1 = X - 4.5
            X2 = X + 4.5
            Y1 = Y
            Y2 = Y
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X
            X2 = X
            Y1 = Y - 4.5
            Y2 = Y + 4.5
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            # ushiropin
            X = self.x + self.param.TenkaD - 55
            X1 = X - 1
            X2 = X - 1
            Y1 = Y - 10.5
            Y2 = Y - 4.39
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X + 1
            X2 = X + 1
            Y1 = Y - 10.5
            Y2 = Y - 4.39
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            # リセット
            Y = self.y + 18 - 5

    # 寸法線を描くコマンドを生成
    def dimension_lines_green(self):
        height = self.param.h + 12 + - 72 - 36
        commands = []
        X = self.x + self.param.TenkaD - 10
        Y1 = self.y
        Y2 = self.y + height + 36
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        Y1 = self.y - 72
        Y2 = self.y
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        Y1 = self.y
        Y2 = self.y + 18
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        Y1 = self.y + height + 18
        Y2 = self.y + height + 36
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        Y1 = self.y + 18
        Y2 = self.y + height - 18
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        X1 = self.x - 9 + 22.5
        X2 = self.x + self.param.TenkaD + 65.5
        Y = self.y - 310
        commands.append(commands.dimaligned(X1, Y, X2, Y, 0))
        X1 = self.x + 24
        X2 = X1 + self.param.TenkaD - 18 - 24
        Y = self.y + 18 - 5 + 4.5 + self.maepin_list[0]
        commands.append(commands.dimaligned(X1, Y, X2, Y, 30))
        # ダボの間隔 -------
        X1 = self.x
        X2 = self.x + 36
        Y = self.y + height + 18 + 158
        commands.append(commands.dimaligned(X1, Y, X2, Y, 0))
        X1 = self.x + 36
        X2 = self.x + self.param.TenkaD - 53
        Y = self.y + height + 18 + 158
        commands.append(commands.dimaligned(X1, Y, X2, Y, 0))
        X1 = self.x + self.param.TenkaD - 53
        X2 = self.x + self.param.TenkaD
        Y = self.y + height + 18 + 158
        commands.append(commands.dimaligned(X1, Y, X2, Y, 0))
        X = self.x + self.param.TenkaD - 53
        Y1 = self.y + 8.5 + 64
        Y2 = self.y + 8.5 + 96
        commands.append(commands.dimaligned(X, Y1, X, Y2, 20))
        X = self.x + self.param.TenkaD - 53
        Y1 = self.y + 8.5 + 96
        Y2 = self.y + 8.5 + 128
        commands.append(commands.dimaligned(X, Y1, X, Y2, 20))
        # -------
        X1 = self.x - 22
        X2 = self.x
        Y = self.y + height / 2
        commands.append(commands.dimaligned(X1, Y, X2, Y, 0))
        X1 = self.x
        X2 = self.x + self.param.TenkaD - 18
        commands.append(commands.dimaligned(X1, Y, X2, Y, 0))
        X1 = self.x + self.param.TenkaD - 18
        X2 = self.x + self.param.TenkaD
        commands.append(commands.dimaligned(X1, Y, X2, Y, 0))
        X1 = self.x
        X2 = self.x + self.param.TenkaD
        Y = self.y + height / 2 - 100
        commands.append(commands.dimaligned(X1, Y, X2, Y, 0))
        # 一番手前の寸法線------
        X = self.x - 540
        Y1 = self.y - 72
        Y2 = self.y - 60
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        X = self.x - 540
        Y1 = self.y - 60
        Y2 = self.y + height + 18
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        # ------
        # 2番目の寸法線
        X = self.x - 400
        Y1 = self.y - 60
        Y2 = self.y
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        X = self.x - 400
        Y1 = self.y
        Y2 = self.y + 10.5
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        X = self.x - 400
        Y1 = self.y + 10.5
        Y2 = self.y + height + 18 - 10.5
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        X = self.x - 400
        Y1 = self.y + height + 18 - 10.5
        Y2 = self.y + height + 18
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        Y = self.y + 18 - 5
        X = self.x - 400
        Y1 = self.y + height + 18 - 10.5
        Y2 = self.y + height + 18
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        Y1 = self.y + 9
        X = self.x
        Y2 = self.y + 9 + 142
        commands.append(commands.dimaligned(X, Y1, X, Y2, 0))
        self.command_list.extend(commands)

    def back_plate(self):
        # 高さがわからないので保留
        """
        X = x + D - 4
        height = h + 12 + - 72 - 36
        if ((height - 45) / 32) % 2 == 0:
        """

    def green_line(self):
        # 手前側
        X1 = self.x + 13.5
        Y1 = self.y - 310
        X2 = X1
        Y2 = Y1 - 108
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        # 奥側
        X1 = self.x + self.param.TenkaD + 65.5
        X2 = X1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        # 繋ぐ線
        X1 = self.x + 13.5
        Y1 = Y2
        X2 = self.x + self.param.TenkaD + 65.5
        Y2 = Y1
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        command = commands.circle_command(X1, Y1, 10)
        self.command_list.append(command)
        command = commands.circle_command(X2, Y2, 10)
        self.command_list.append(command)
        command = commands.text((X1 + X2) / 2, Y1 + 10, 0, "{}".format(X2 - X1))
        self.command_list.append(command)

    def mk_command_side(self):

        self.create_parameters()

        self.layer_change(self, 'RED')
        self.daiwa()
        self.tenka_under()
        self.tenka_top()
        self.ura()
        self.guide()
        self.layer_change(self, 'WHITE')
        self.door()
        self.white_lines()
        self.tyoban_lines()
        self.layer_change(self, 'YELLOW')
        self.yellow_lines()
        self.layer_change(self, 'CYAN')
        self.dowel_hole()
        self.command_list.append('')
        self.tyoban()
        self.command_list.append('ATTDIA 0 ')
        self.command_list.append('')
        self.maepin_and_ushiropin()
        self.command_list.append('')
        self.command_list.append('ATTDIA 0 ')
        self.layer_change(self, 'MAGENTA')
        self.maepin_and_ushiropin_lines()
        self.layer_change(self, 'WHITE')
        self.m_shelf_board()
        self.layer_change(self, 'GREEN')
        self.green_line()
        # dimexo(0) ### 保留
        # command_list.append('') ### 保留
        # dimension_lines_green() ### 保留
        command_line = '\n'.join(self.command_list)

        path_w = 'scripts\side.txt'
        with open(path_w, mode='w') as f:
            f.write(command_line)
