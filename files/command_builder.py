from .module import parameters


class CommandBuilder():
    def __init__(self):
        self.command_list = list()
        self.param = parameters.Param()
        self.x = 0
        self.y = 0

        # tyoban_lines & tyoban
        margin1 = 142  # 最上下端
        margin2 = 576  # 固定棚なしの上下
        margin3 = 608  # 固定棚ありの上下
        margin4 = self.param.DaiwaH - 12  # 台輪 - フローリング
        # 固定棚無し
        if self.param.h_B <= 2157:
            tyoban_center_h = self.param.h_B - (
                self.param.Door_Tenka * 2 + margin1 * 2 + margin2 * 2 + margin4
            )
            self.tyoban_list = [self.param.Door_Tenka + margin1, margin2, tyoban_center_h, margin2]
        # 固定棚有り
        elif self.param.h_B > 2157:
            tyoban_center_h = self.param.h_B - (
                self.param.Door_Tenka * 2 + margin1 * 2 + margin3 * 2 + margin4
            )
            self.tyoban_list = [self.param.Door_Tenka + margin1, margin3, tyoban_center_h, margin3]

        self.maepin_list_dict = {'1965': [539.5, 987.5, 1435.5],
                                 '2061': [603.5, 1083.5, 1563.5],
                                 '2125': [603.5, 1083.5, 1563.5],
                                 '2157': [603.5, 1083.5, 1563.5],
                                 '2253': [603.5, 1211.5],
                                 '2349': [603.5, 1211.5],
                                 '2445': [603.5, 1211.5]
                                 }

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
