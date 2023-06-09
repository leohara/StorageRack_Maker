from .module import commands
from . import command_builder as cb
from .side_module import *


class Side(cb.CommandBuilder):

    def __init__(self):
        super().__init__()
        self.x = self.param.x_side
        self.y = self.param.y_side

        # 高さからリストを取得してくる
        self.maepin_list = self.maepin_list_dict[str(int(self.param.h_B))]

        # フラグの作成
        required_vars = ["h_{}".format(i) for i in self.param.order_from_left]
        self.h_list = list()
        for name in required_vars:
            if hasattr(self.param, name):
                self.h_list.append(getattr(self.param, name))

        self.variables = ["PanelH_A", "PanelH_B", "PanelH_C", "PanelH_D", "h_A", "h_B", "h_C", "h_D"]

    def switch(self, key):
        var_list = []
        for prefix in ["PanelH_", "w_", "h_", "d_"]:
            if hasattr(self.param, prefix + key):
                var_list.append(getattr(self.param, prefix + key))
        return var_list

    def mk_command_side(self, key):

        var_list = self.switch(key)
        PanelH = var_list[0]
        # w = var_list[1]
        h = var_list[2]
        d = var_list[3]

        self.args = self.param, commands, self.command_list, self.x, self.y

        self.layer_change(self, 'RED')
        daiwa.create(*self.args)
        tenka.tenka_under(*self.args, PanelH)
        tenka.tenka_top(*self.args, PanelH)
        ura.ura(*self.args, h, d)
        guide.guide(*self.args, PanelH)
        self.layer_change(self, 'WHITE')
        door.door(*self.args, PanelH)
        white_line.white_lines(*self.args, PanelH, h)
        tyoban_lines.tyoban_lines(*self.args, self.tyoban_list)
        self.layer_change(self, 'YELLOW')
        yellow_lines.yellow_lines(*self.args)
        self.layer_change(self, 'CYAN')
        hole.hole(*self.args, PanelH, d)
        self.command_list.append('')
        tyoban.tyoban(*self.args, self.tyoban_list)
        self.command_list.append('ATTDIA 0 ')
        self.command_list.append('')
        maepin_and_ushiropin.body(*self.args, self.maepin_list)
        self.command_list.append('')
        self.command_list.append('ATTDIA 0 ')
        self.layer_change(self, 'MAGENTA')
        maepin_and_ushiropin.line(*self.args, self.maepin_list)
        self.layer_change(self, 'WHITE')
        shelf.m_shelf_board(*self.args, self.maepin_list)
        self.layer_change(self, 'GREEN')
        dimension.green_line(*self.args, h, d)
        command_line = '\n'.join(self.command_list)

        path_w = 'scripts\side.txt'
        with open(path_w, mode='w') as f:
            f.write(command_line)
