from .module_main import command_builder as cb
from .module_side import *


class Side(cb.CommandBuilder):

    def __init__(self):

        super().__init__()

        self.x = self.param.x_side
        self.y = self.param.y_side

        # 高さからリストを取得してくる
        self.maepin_list = self.maepin_list_dict[str(int(self.param.h_B))]

        self.args = self.param, self.commands, self.command_list, self.x, self.y

    def switch(self, key):
        var_list = []
        for prefix in ["w_", "h_", "d_"]:
            if hasattr(self.param, prefix + key):
                var_list.append(getattr(self.param, prefix + key))
        return var_list

    def mk_command_side(self, key):

        var_list = self.switch(key)
        # w = var_list[0] # 今のところ使わない
        h = var_list[1]
        d = var_list[2]

        flooring = 12  # フローリングの厚み
        PanelH = h - self.param.DaiwaH + flooring  # パネル板の高さ

        self.args = self.param, self.commands, self.command_list, self.x, self.y

        self.layer_change(self, 'RED')
        daiwa.create(*self.args, d)
        tenka.create(*self.args, PanelH, d)
        ura.create(*self.args, PanelH, d)
        guide.create(*self.args, PanelH)

        self.layer_change(self, 'WHITE')
        door.create(*self.args, PanelH)
        column.create(*self.args, PanelH, h)
        floor.create(*self.args)
        tyoban_lines.create(*self.args, self.tyoban_list)

        self.layer_change(self, 'YELLOW')
        yellow_lines.create(*self.args)

        self.layer_change(self, 'CYAN')
        dowel.create(*self.args, PanelH, d)
        self.command_list.append('')
        tyoban.create(*self.args, self.tyoban_list)
        self.command_list.append('ATTDIA 0 ')
        self.command_list.append('')
        maepin_and_ushiropin.create_body(*self.args, self.maepin_list)
        self.command_list.append('')
        self.command_list.append('ATTDIA 0 ')

        self.layer_change(self, 'MAGENTA')
        maepin_and_ushiropin.create_line(*self.args, self.maepin_list)

        self.layer_change(self, 'WHITE')
        shelf.create(*self.args, self.maepin_list)

        self.layer_change(self, 'GREEN')
        measurement.create(*self.args, h, d)

        command_line = '\n'.join(self.command_list)

        path_w = 'scripts\side.txt'
        with open(path_w, mode='w') as f:
            f.write(command_line)
