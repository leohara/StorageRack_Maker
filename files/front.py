from .module import commands
from . import command_builder as cb


class Front(cb.CommandBuilder):

    def __init__(self):
        super().__init__()
        self.x = self.param.x_front
        self.y = self.param.y_front
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
        self.W = sum(self.w_list) + 18 * (len(self.w_list) + 1)

        # -1: 後者が低い
        # 0: フラット
        # 1: 後者が高い
        self.bump_list = list()
        for i in range(len(self.PanelH_list)):
            if i == 0:
                self.bump_list.append(0)
            else:
                if self.PanelH_list[i] == self.PanelH_list[i - 1]:
                    self.bump_list.append(0)
                else:
                    self.bump_list.append(int((self.PanelH_list[i] - self.PanelH_list[i - 1]) / abs(self.PanelH_list[i] - self.PanelH_list[i - 1])))

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
            elif PanelH < prevH:
                Y1 = Y1 + PanelH
                Y2 = Y1 + prevH - PanelH
                command = commands.line_command(X1, Y1, X1, Y2)
                self.command_list.append(command)
            elif enum == 0:
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
                Y1 = self.y
                Y2 = Y1 + PanelH
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
        X2 = self.x + self.W - self.param.PanelW
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
            X1 = X2 - self.param.PanelW + self.W - self.param.PanelW
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
        for block, boolean, height in zip(self.w_list, self.param.flag, self.PanelH_list):
            if not boolean:
                X_ = X_ + self.param.PanelW + block
            else:
                X1 = X_ + block / 2 + self.param.PanelW
                Y1 = self.y + height - self.param.Door_Tenka
                X2 = X_ + block / 2 + self.param.PanelW
                Y2 = self.y + self.param.Door_Tenka
                line = commands.line_command(X1, Y1, X2, Y2)
                self.command_list.append(line)
                X1 = X_ + block / 2 + 15 + self.param.PanelW
                Y1 = self.y + height - self.param.Door_Tenka
                X2 = X_ + block / 2 + 15 + self.param.PanelW
                Y2 = self.y + self.param.Door_Tenka
                line = commands.line_command(X1, Y1, X2, Y2)
                self.command_list.append(line)
                X1 = X_ + block / 2 - 15 + self.param.PanelW
                Y1 = self.y + height - self.param.Door_Tenka
                X2 = X_ + block / 2 - 15 + self.param.PanelW
                Y2 = self.y + self.param.Door_Tenka
                line = commands.line_command(X1, Y1, X2, Y2)
                self.command_list.append(line)
                X1 = X_ + block / 2 - 15 + self.param.PanelW
                Y1 = self.y + height - self.param.Door_Tenka
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
                X2 = X1 + TenkaW + self.param.Frame_inner + self.param.Frame_outer - 3 * self.bump_list[enum + 1]
            elif enum == self.param.num - 1:
                Y1 = self.y - 60
                Y2 = Y1 + PanelH + 54
                X2 = X1 + TenkaW + self.param.Frame_inner + self.param.Frame_outer + 3 * self.bump_list[enum]
            else:
                X2 = X1 + TenkaW + self.param.Frame_inner * 2 + 3 * (self.bump_list[enum] - self.bump_list[enum + 1])
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

    # コマンドをプリントする
    def mk_command_front(self):
        """
        """

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

        command_line = '\n'.join(self.command_list)

        path_w = 'scripts/front.txt'
        with open(path_w, mode='w') as f:
            f.write(command_line)
