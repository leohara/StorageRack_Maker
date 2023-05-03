from . import parameters
from . import commands


class Front:

    def __init__(self):
        self.command_list = list()

    def create_parameters(self):
        self.param = parameters.Param()
        self.x = self.param.x_front
        self.y = self.param.y_front

        # tyoban_lines & tyoban
        margin1 = 142  # 最上下端
        margin2 = 576  # 固定棚なしの上下
        margin3 = 608  # 固定棚ありの上下
        margin4 = self.param.DaiwaH - 12  # 台輪 - フローリング
        # 固定棚無し
        if self.param.H <= 2157:
            tyoban_center_h = self.param.H - (self.param.Door_Tenka * 2 + margin1 * 2 + margin2 * 2 + margin4)
            tyoban_list = [self.param.Door_Tenka + margin1, margin2, tyoban_center_h, margin2]
        # 固定棚有り
        elif self.param.H > 2157:
            tyoban_center_h = self.param.H - (self.param.Door_Tenka * 2 + margin1 * 2 + margin3 * 2 + margin4)
            tyoban_list = [self.param.Door_Tenka + margin1, margin3, tyoban_center_h, margin3]

        # 全然合わないので2061だけ603.5スタートでそこから468ずつ足した
        # CD51のリスト
        self.maepin_list_dict = {'1965': [539.5, 987.5, 1435.5],
                                 '2061': [603.5, 1083.5, 1563.5],
                                 '2125': [603.5, 1083.5, 1563.5],
                                 '2157': [603.5, 1083.5, 1563.5],
                                 '2253': [603.5, 1211.5],
                                 '2349': [603.5, 1211.5],
                                 '2445': [603.5, 1211.5]
                                 }

        # 高さからリストを取得してくる
        exec('self.maepin_list = self.maepin_list_dict[str(int(self.param.h_{}))]'.format(self.param.left_and_right[0]))  # Aだけにしない直す

        self.w_list = list()
        self.h_list = list()
        self.d_list = list()
        self.PanelD_list = list()
        self.PanelH_list = list()
        self.PanelW_list = list()
        self.TenkaD_list = list()
        self.TenkaH_list = list()
        self.TenkaW_list = list()
        self.TenkaD_list = list()
        self.UraH_list = list()
        self.UraW_list = list()
        self.UraD_List = list()
        for block in self.param.order_from_left:
            exec(f'self.w_list.append(self.param.w_{block})')
            exec(f'self.h_list.append(self.param.h_{block})')
            exec(f'self.d_list.append(self.param.d_{block})')
            exec(f'self.PanelH_list.append(self.param.PanelH_{block})')
            exec(f'self.TenkaW_list.append(self.param.TenkaW_{block})')

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

    def Door(self):
        X1 = self.x + self.param.PanelW_outer
        Y1 = self.y + self.param.Door_Tenka
        for TenkaW, PanelH in zip(self.TenkaW_list, self.PanelH_list):
            Y2 = Y1 + PanelH - 2 * self.param.Door_Tenka
            X2 = X1 + TenkaW + self.param.PanelW_inner * 2
            command = commands.rec_command(X1, Y1, X2, Y2)
            self.command_list.append(command)
            X1 = X2 + 4

    def Frame(self):
        flame_flag = [int(
            (self.PanelH_list[i] - self.PanelH_list[i + 1]) / abs(self.PanelH_list[i] - self.PanelH_list[i + 1])) if (self.PanelH_list[i] - self.PanelH_list[i + 1] != 0) else 0 for i in range(self.param.num - 1)]
        flame_flag.append(0)
        # 外枠
        enum = 0
        prevH = self.PanelH_list[0]
        prev_flag = 0
        X2 = self.x
        for PanelH, TenkaW, f_flag in zip(self.PanelH_list, self.TenkaW_list, flame_flag):
            X1 = X2
            Y1 = self.y
            if PanelH > prevH:  # H方向
                Y1 = Y1 + prevH
                Y2 = Y1 + PanelH - prevH
                command = commands.line_command(X1, Y1, X1, Y2)
                self.command_list.append(command)
            if PanelH < prevH:
                Y1 = Y1 + PanelH
                Y2 = Y1 + prevH - PanelH
                command = commands.line_command(X1, Y1, X1, Y2)
                self.command_list.append(command)
            if enum == 0:
                Y2 = Y1 + PanelH
                command = commands.line_command(X1, Y1, X1, Y2)
                self.command_list.append(command)
            #######################
            # 基準
            if enum == 0:  # W方向
                X2 = X1 + TenkaW + self.param.PanelW_outer * 2 + self.param.PanelW_inner - 2 + f_flag * 9
            elif enum != self.param.num - 1:
                X2 = X1 + TenkaW + 2 * self.param.PanelW_inner + 2 * 2 + prev_flag * (-9) + f_flag * 9
            else:
                X2 = X1 + TenkaW + self.param.PanelW_outer + 2 * self.param.PanelW_inner + 2 + prev_flag * (-9) + f_flag * 9
            command = commands.line_command(X1, Y2, X2, Y2)
            self.command_list.append(command)
            #######################
            if enum == self.param.num - 1:  # 右端のパターン
                Y1 = self.y
                Y2 = Y1 + PanelH
                command = commands.line_command(X2, Y1, X2, Y2)
                self.command_list.append(command)
            enum += 1
            prevH = PanelH
            prev_flag = f_flag

        # 内枠
        X1 = self.x
        for TenkaW, PanelH in zip(self.TenkaW_list, self.PanelH_list):
            X1 = X1 + self.param.PanelW
            Y1 = self.y + self.param.TenkaH
            X2 = X1 + TenkaW
            Y2 = self.y + PanelH - self.param.TenkaH
            command = commands.rec_command(X1, Y1, X2, Y2)
            self.command_list.append(command)
            X1 = X2

    def m_shelf_board(self):
        X1 = self.x + self.param.PanelW
        X2 = self.x + self.param.W - self.param.PanelW
        Y = self.y + self.param.shelfH - 5 + 4.5  # 5を引かないと合わない
        for h in self.maepin_list:
            Y1 = Y + h
            Y2 = Y1 + self.param.shelfH
            command = commands.rec_command(X1, Y1, X2, Y2)
            self.command_list.append(command)

    def HP(self):
        X1 = self.x + self.param.PanelW
        Y = self.y + self.param.shelfH - 5 + 4.5  # 5を引かないと合わない
        for h in self.maepin_list:
            Y1 = Y + h
            X2 = X1 + 13
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            Y2 = Y1 + 16.8
            line = commands.line_command(X2, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X2
            Y1 = Y2
            X2 = X1 - 10
            Y2 = Y1 + 8.13
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            Y1 = Y2
            Y2 = Y1 + 19
            line = commands.line_command(X2, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X2
            Y1 = Y2
            X2 = X1 - 3
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            Y2 = Y1 - 22
            line = commands.line_command(X2, Y1, X2, Y2)
            self.command_list.append(line)
            X_reset = X2
            ###############
            X1 = X2 - self.param.PanelW + self.param.W - self.param.PanelW
            Y1 = Y + h
            X2 = X1 - 13
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            Y2 = Y1 + 16.8
            line = commands.line_command(X2, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X2
            Y1 = Y2
            X2 = X1 + 10
            Y2 = Y1 + 8.13
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            Y1 = Y2
            Y2 = Y1 + 19
            line = commands.line_command(X2, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X2
            Y1 = Y2
            X2 = X1 + 3
            line = commands.line_command(X1, Y1, X2, Y1)
            self.command_list.append(line)
            Y2 = Y1 - 22
            line = commands.line_command(X2, Y1, X2, Y2)
            self.command_list.append(line)
            X1 = X_reset

    def cross_line(self):
        X1 = self.x + self.param.PanelW_outer
        for PanelH, TenkaW, boolean in zip(self.PanelH_list, self.TenkaW_list, self.param.flag):
            Y1 = self.y + PanelH / 2 + self.param.PanelW_inner
            if boolean:
                X2 = X1 + TenkaW / 2 + self.param.PanelW_inner
            else:
                X2 = X1 + TenkaW + self.param.PanelW_inner * 2
            Y2 = self.y + PanelH - self.param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            Y2 = self.y + self.param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            self.command_list.append(line)
            if boolean:
                X1 = X2
                X2 = X1 + TenkaW / 2 + self.param.PanelW_inner
                Y2 = self.y + PanelH - self.param.Door_Tenka
                line = commands.line_command(X1, Y2, X2, Y1)
                self.command_list.append(line)
                Y2 = self.y + self.param.Door_Tenka
                line = commands.line_command(X1, Y2, X2, Y1)
                self.command_list.append(line)
            X1 = X2 + 4

    def magenta_line(self):
        X_ = self.x
        for block, boolean in zip(self.w_list, self.param.flag):
            if not boolean:
                X_ = X_ + self.param.PanelW + block
            else:
                X1 = X_ + block / 2 + self.param.PanelW
                Y1 = self.y + self.param.PanelH - self.param.Door_Tenka
                X2 = X_ + block / 2 + self.param.PanelW
                Y2 = self.y + self.param.Door_Tenka
                line = commands.line_command(X1, Y1, X2, Y2)
                self.command_list.append(line)
                X1 = X_ + block / 2 + 15 + self.param.PanelW
                Y1 = self.y + self.param.PanelH - self.param.Door_Tenka
                X2 = X_ + block / 2 + 15 + self.param.PanelW
                Y2 = self.y + self.param.Door_Tenka
                line = commands.line_command(X1, Y1, X2, Y2)
                self.command_list.append(line)
                X1 = X_ + block / 2 - 15 + self.param.PanelW
                Y1 = self.y + self.param.PanelH - self.param.Door_Tenka
                X2 = X_ + block / 2 - 15 + self.param.PanelW
                Y2 = self.y + self.param.Door_Tenka
                line = commands.line_command(X1, Y1, X2, Y2)
                self.command_list.append(line)
                X1 = X_ + block / 2 - 15 + self.param.PanelW
                Y1 = self.y + self.param.PanelH - self.param.Door_Tenka
                X2 = X_ + block / 2 + 15 + self.param.PanelW
                Y2 = self.y + self.param.PanelH - self.param.Door_Tenka
                line = commands.line_command(X1, Y1, X2, Y2)
                self.command_list.append(line)
                X1 = X_ + block / 2 - 15 + self.param.PanelW
                Y1 = self.y + self.param.Door_Tenka
                X2 = X_ + block / 2 + 15 + self.param.PanelW
                Y2 = self.y + self.param.Door_Tenka
                line = commands.line_command(X1, Y1, X2, Y2)
                self.command_list.append(line)
                X_ = X_ + self.param.PanelW + block

    # 実線の方
    def cyan_Frame(self):
        enum = 0
        prevH = self.PanelH_list[0]
        X2 = self.x + 6
        for PanelH, TenkaW in zip(self.PanelH_list, self.TenkaW_list):
            X1 = X2
            Y1 = self.y
            if PanelH > prevH:
                Y1 = Y1 + prevH - 6
                Y2 = Y1 + PanelH - prevH
                command = commands.line_command(X1, Y1, X1, Y2)
                self.command_list.append(command)
            elif PanelH < prevH:
                Y1 = Y1 + PanelH - 6
                Y2 = Y1 + prevH - PanelH
                command = commands.line_command(X1, Y1, X1, Y2)
                self.command_list.append(command)
            elif enum == 0:
                Y1 = self.y - 60
                Y2 = Y1 + PanelH + 54
                command = commands.line_command(X1, Y1, X1, Y2)
                self.command_list.append(command)

            if enum == 0:
                X2 = X1 + TenkaW + self.param.PanelW_inner + self.param.PanelW_outer
            elif enum == self.param.num - 1:
                X2 = X1 + TenkaW + 2 * self.param.PanelW_inner + 4 + 5
            else:
                X2 = X1 + TenkaW + 2 * self.param.PanelW_inner + 4
            command = commands.line_command(X1, Y2, X2, Y2)
            self.command_list.append(command)
            if enum == self.param.num - 1:
                Y1 = self.y - 60
                Y2 = Y1 + PanelH + 54
                command = commands.line_command(X2, Y1, X2, Y2)
                self.command_list.append(command)
            enum += 1
            prevH = PanelH

    def ground(self):
        # 床
        X1 = self.x - 300
        Y1 = self.y - 310
        X2 = self.x + 3000
        Y2 = self.y - 310
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = self.x - 300
        Y1 = self.y - 60
        X2 = self.x + 3000
        Y2 = self.y - 60
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = self.x - 300
        Y1 = self.y - 72
        X2 = self.x + 3000
        Y2 = self.y - 72
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        X1 = self.x - 300
        Y1 = self.y - 98
        X2 = self.x + 3000
        Y2 = self.y - 98
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)

    def green_line(self):
        X1 = 900
        X2 = 900
        Y1 = 600
        Y2 = 900
        line = commands.line_command(X1, Y1, X2, Y2)
        self.command_list.append(line)
        command = commands.circle_command(X1, Y1, 10)
        self.command_list.append(command)
        command = commands.circle_command(X2, Y2, 10)
        self.command_list.append(command)
        command = commands.text(X1 - 20, (Y1 + Y2) / 2, 90, "{}".format(Y2 - Y1))
        self.command_list.append(command)

    # コマンドをプリントする
    def mk_command_front(self):
        """
        """

        self.create_parameters()

        self.layer_change(self, 'WHITE')
        self.Door()
        self.ground()
        self.layer_change(self, 'PHANTOM2')
        self.cross_line()
        self.layer_change(self, 'TNSN3')
        self.Frame()  # 青い点線
        self.m_shelf_board()
        self.layer_change(self, 'CYAN')
        self.cyan_Frame()  # 青い実線
        # layer_change('CYAN')
        # HP() # ハンガーパイプの高さがわかったら描く
        self.layer_change(self, 'MAGENTA')
        self.magenta_line()
        self.layer_change(self, 'GREEN')
        self.green_line()

        command_line = '\n'.join(self.command_list)

        path_w = 'scripts/front.txt'
        with open(path_w, mode='w') as f:
            f.write(command_line)
