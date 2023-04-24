from . import parameters
from . import commands

param = parameters.Param()

command_list = list()
x = param.x_front
y = param.y_front

# tyoban_lines & tyoban
margin1 = 142  # 最上下端
margin2 = 576  # 固定棚なしの上下
margin3 = 608  # 固定棚ありの上下
margin4 = param.DaiwaH - 12  # 台輪 - フローリング
# 固定棚無し
if param.H <= 2157:
    tyoban_center_h = param.H - (param.Door_Tenka * 2 + margin1 * 2 + margin2 * 2 + margin4)
    tyoban_list = [param.Door_Tenka + margin1,
                   margin2,
                   tyoban_center_h,
                   margin2]
# 固定棚有り
elif param.H > 2157:
    tyoban_center_h = param.H - (param.Door_Tenka * 2 + margin1 * 2 + margin3 * 2 + margin4)
    tyoban_list = [param.Door_Tenka + margin1,
                   margin3,
                   tyoban_center_h,
                   margin3]

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
exec('maepin_list = maepin_list_dict[str(int(param.h_{}))]'.format(param.left_and_right[0]))  # Aだけにしない直す

w_list = list()
h_list = list()
d_list = list()
PanelD_list = list()
PanelH_list = list()
PanelW_list = list()
TenkaD_list = list()
TenkaH_list = list()
TenkaW_list = list()
TenkaD_list = list()
UraH_list = list()
UraW_list = list()
UraD_List = list()
for block in param.order_from_left:
    exec(f'w_list.append(param.w_{block})')
    exec(f'h_list.append(param.h_{block})')
    exec(f'd_list.append(param.d_{block})')
    exec(f'PanelH_list.append(param.PanelH_{block})')
    exec(f'TenkaW_list.append(param.TenkaW_{block})')


# デコレーターで初期化する
def decorator(func):
    def inner(*args, **kwargs):
        command_list.append('ATTDIA 0 ')
        command_list.append('')
        func(*args, **kwargs)
        command_list.append('')
        command_list.append('ATTDIA 1 ')
    return inner


@decorator
# 画層を変更する
def layer_change(color):
    command = '-LAYER s {}'.format(color)
    command_list.append(command)


@decorator
def dimexo(d):
    command = 'dimexo {} '.format(d)
    command_list.append(command)


# コマンドをプリントする
def mk_command_front():
    """
    """
    layer_change('WHITE')
    Door()
    ground()
    layer_change('PHANTOM2')
    cross_line()
    layer_change('TNSN3')
    Frame()  # 青い点線
    m_shelf_board()
    layer_change('CYAN')
    cyan_Frame()  # 青い実線
    # layer_change('CYAN')
    # HP() # ハンガーパイプの高さがわかったら描く
    layer_change('MAGENTA')
    magenta_line()
    layer_change('GREEN')
    green_line()

    command_line = '\n'.join(command_list)

    path_w = 'scripts/front.txt'
    with open(path_w, mode='w') as f:
        f.write(command_line)


def Door():
    X1 = x + param.PanelW_outer
    Y1 = y + param.Door_Tenka
    for TenkaW, PanelH in zip(TenkaW_list, PanelH_list):
        Y2 = Y1 + PanelH - 2 * param.Door_Tenka
        X2 = X1 + TenkaW + param.PanelW_inner * 2
        command = commands.rec_command(X1, Y1, X2, Y2)
        command_list.append(command)
        X1 = X2 + 4


def Frame():
    flame_flag = [int(
        (PanelH_list[i] - PanelH_list[i + 1]) / abs(PanelH_list[i] - PanelH_list[i + 1])) if (PanelH_list[i] - PanelH_list[i + 1] != 0) else 0 for i in range(param.num - 1)]
    flame_flag.append(0)
    # 外枠
    enum = 0
    prevH = PanelH_list[0]
    prev_flag = 0
    X2 = x
    for PanelH, TenkaW, f_flag in zip(PanelH_list, TenkaW_list, flame_flag):
        X1 = X2
        Y1 = y
        if PanelH > prevH:  # H方向
            Y1 = Y1 + prevH
            Y2 = Y1 + PanelH - prevH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        elif PanelH < prevH:
            Y1 = Y1 + PanelH
            Y2 = Y1 + prevH - PanelH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        elif enum == 0:
            Y2 = Y1 + PanelH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        #######################
        # 基準
        if enum == 0:  # W方向
            X2 = X1 + TenkaW + param.PanelW_outer * 2 + param.PanelW_inner - 2 + f_flag * 9
        elif enum != param.num - 1:
            X2 = X1 + TenkaW + 2 * param.PanelW_inner + 2 * 2 + prev_flag * (-9) + f_flag * 9
        else:
            X2 = X1 + TenkaW + param.PanelW_outer + 2 * param.PanelW_inner + 2 + prev_flag * (-9) + f_flag * 9
        command = commands.line_command(X1, Y2, X2, Y2)
        command_list.append(command)
        #######################
        if enum == param.num - 1:  # 右端のパターン
            Y1 = y
            Y2 = Y1 + PanelH
            command = commands.line_command(X2, Y1, X2, Y2)
            command_list.append(command)
        enum += 1
        prevH = PanelH
        prev_flag = f_flag

    # 内枠
    X1 = x
    for TenkaW, PanelH in zip(TenkaW_list, PanelH_list):
        X1 = X1 + param.PanelW
        Y1 = y + param.TenkaH
        X2 = X1 + TenkaW
        Y2 = y + PanelH - param.TenkaH
        command = commands.rec_command(X1, Y1, X2, Y2)
        command_list.append(command)
        X1 = X2


def m_shelf_board():
    X1 = x + param.PanelW
    X2 = x + param.W - param.PanelW
    Y = y + param.shelfH - 5 + 4.5  # 5を引かないと合わない
    for h in maepin_list:
        Y1 = Y + h
        Y2 = Y1 + param.shelfH
        command = commands.rec_command(X1, Y1, X2, Y2)
        command_list.append(command)


def HP():
    X1 = x + param.PanelW
    Y = y + param.shelfH - 5 + 4.5  # 5を引かないと合わない
    for h in maepin_list:
        Y1 = Y + h
        X2 = X1 + 13
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y2 = Y1 + 16.8
        line = commands.line_command(X2, Y1, X2, Y2)
        command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1 - 10
        Y2 = Y1 + 8.13
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        Y1 = Y2
        Y2 = Y1 + 19
        line = commands.line_command(X2, Y1, X2, Y2)
        command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1 - 3
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y2 = Y1 - 22
        line = commands.line_command(X2, Y1, X2, Y2)
        command_list.append(line)
        X_reset = X2
        ###############
        X1 = X2 - param.PanelW + param.W - param.PanelW
        Y1 = Y + h
        X2 = X1 - 13
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y2 = Y1 + 16.8
        line = commands.line_command(X2, Y1, X2, Y2)
        command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1 + 10
        Y2 = Y1 + 8.13
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        Y1 = Y2
        Y2 = Y1 + 19
        line = commands.line_command(X2, Y1, X2, Y2)
        command_list.append(line)
        X1 = X2
        Y1 = Y2
        X2 = X1 + 3
        line = commands.line_command(X1, Y1, X2, Y1)
        command_list.append(line)
        Y2 = Y1 - 22
        line = commands.line_command(X2, Y1, X2, Y2)
        command_list.append(line)
        X1 = X_reset


def cross_line():
    X1 = x + param.PanelW_outer
    for PanelH, TenkaW, boolean in zip(PanelH_list, TenkaW_list, param.flag):
        Y1 = y + PanelH / 2 + param.PanelW_inner
        if boolean:
            X2 = X1 + TenkaW / 2 + param.PanelW_inner
        else:
            X2 = X1 + TenkaW + param.PanelW_inner * 2
        Y2 = y + PanelH - param.Door_Tenka
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        Y2 = y + param.Door_Tenka
        line = commands.line_command(X1, Y1, X2, Y2)
        command_list.append(line)
        if boolean:
            X1 = X2
            X2 = X1 + TenkaW / 2 + param.PanelW_inner
            Y2 = y + PanelH - param.Door_Tenka
            line = commands.line_command(X1, Y2, X2, Y1)
            command_list.append(line)
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y2, X2, Y1)
            command_list.append(line)
        X1 = X2 + 4


def magenta_line():
    X_ = x
    for block, boolean in zip(w_list, param.flag):
        if not boolean:
            X_ = X_ + param.PanelW + block
        else:
            X1 = X_ + block / 2 + param.PanelW
            Y1 = y + param.PanelH - param.Door_Tenka
            X2 = X_ + block / 2 + param.PanelW
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X1 = X_ + block / 2 + 15 + param.PanelW
            Y1 = y + param.PanelH - param.Door_Tenka
            X2 = X_ + block / 2 + 15 + param.PanelW
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X1 = X_ + block / 2 - 15 + param.PanelW
            Y1 = y + param.PanelH - param.Door_Tenka
            X2 = X_ + block / 2 - 15 + param.PanelW
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X1 = X_ + block / 2 - 15 + param.PanelW
            Y1 = y + param.PanelH - param.Door_Tenka
            X2 = X_ + block / 2 + 15 + param.PanelW
            Y2 = y + param.PanelH - param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X1 = X_ + block / 2 - 15 + param.PanelW
            Y1 = y + param.Door_Tenka
            X2 = X_ + block / 2 + 15 + param.PanelW
            Y2 = y + param.Door_Tenka
            line = commands.line_command(X1, Y1, X2, Y2)
            command_list.append(line)
            X_ = X_ + param.PanelW + block


# 実線の方
def cyan_Frame():
    enum = 0
    prevH = PanelH_list[0]
    X2 = x + 6
    for PanelH, TenkaW in zip(PanelH_list, TenkaW_list):
        X1 = X2
        Y1 = y
        if PanelH > prevH:
            Y1 = Y1 + prevH - 6
            Y2 = Y1 + PanelH - prevH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        elif PanelH < prevH:
            Y1 = Y1 + PanelH - 6
            Y2 = Y1 + prevH - PanelH
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)
        elif enum == 0:
            Y1 = y - 60
            Y2 = Y1 + PanelH + 54
            command = commands.line_command(X1, Y1, X1, Y2)
            command_list.append(command)

        if enum == 0:
            X2 = X1 + TenkaW + param.PanelW_inner + param.PanelW_outer
        elif enum == param.num - 1:
            X2 = X1 + TenkaW + 2 * param.PanelW_inner + 4 + 5
        else:
            X2 = X1 + TenkaW + 2 * param.PanelW_inner + 4
        command = commands.line_command(X1, Y2, X2, Y2)
        command_list.append(command)
        if enum == param.num - 1:
            Y1 = y - 60
            Y2 = Y1 + PanelH + 54
            command = commands.line_command(X2, Y1, X2, Y2)
            command_list.append(command)
        enum += 1
        prevH = PanelH


def ground():
    # 床
    X1 = x - 300
    Y1 = y - 310
    X2 = x + 3000
    Y2 = y - 310
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 300
    Y1 = y - 60
    X2 = x + 3000
    Y2 = y - 60
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 300
    Y1 = y - 72
    X2 = x + 3000
    Y2 = y - 72
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    X1 = x - 300
    Y1 = y - 98
    X2 = x + 3000
    Y2 = y - 98
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)


def green_line():
    X1 = 900
    X2 = 900
    Y1 = 600
    Y2 = 900
    line = commands.line_command(X1, Y1, X2, Y2)
    command_list.append(line)
    command = commands.circle_command(X1, Y1, 10)
    command_list.append(command)
    command = commands.circle_command(X2, Y2, 10)
    command_list.append(command)
    command = commands.text(X1 - 20, (Y1 + Y2) / 2, 90, "{}".format(Y2 - Y1))
    command_list.append(command)
