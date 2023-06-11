from .module_main import command_builder as cb
from .module_front import *


class Front(cb.CommandBuilder):

    def __init__(self):

        super().__init__()

        self.x = self.param.x_front
        self.y = self.param.y_front

        values = {prefix: [] for prefix in ["w", "h", "d", "P", "T"]}
        suffixes = [i for i in self.param.order_from_left]

        for prefix in ["w_", "h_", "d_", "PanelH_", "TenkaW_"]:
            for suffix in suffixes:
                var_name = "{}{}".format(prefix, suffix)
                if hasattr(self.param, var_name):
                    values[prefix[0]].append(getattr(self.param, var_name))

        var_dict = values
        self.w_list = var_dict["w"]
        self.h_list = var_dict["h"]
        self.d_list = var_dict["d"]
        self.PanelH_list = var_dict["P"]
        self.TenkaW_list = var_dict["T"]

        self.W = sum(self.w_list) + 18 * (len(self.w_list) + 1)

        # 高さからリストを取得してくる
        self.maepin_dict = {var: self.maepin_list_dict[str(var)] for var in self.h_list}

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

        self.args = self.param, self.commands, self.command_list, self.x, self.y

    def make_list(self):

        values = {prefix: [] for prefix in ["w", "h", "d"]}
        suffixes = ["A", "B", "C", "D"]

        for prefix in ["w_", "h_", "d_"]:
            for suffix in suffixes:
                var_name = "{}{}".format(prefix, suffix)
                if hasattr(self.param, var_name):
                    values[prefix[0]].append(getattr(self.param, var_name))

        return values

    # コマンドをプリントする
    def mk_command_front(self):
        """
        """

        var_dict = self.make_list()
        w_list_temp = var_dict['w']
        # h_list_temp = var_dict['h']
        # d_list_temp = var_dict['d']

        self.args = self.param, self.commands, self.command_list, self.x, self.y

        self.layer_change(self, 'WHITE')
        door.create(*self.args, self.PanelH_list, self.TenkaW_list)
        ground.create(*self.args)

        self.layer_change(self, 'PHANTOM2')
        cross.create(*self.args, self.PanelH_list, self.TenkaW_list)

        self.layer_change(self, 'TNSN3')
        frame.create(*self.args, self.PanelH_list, self.TenkaW_list)  # 青い点線
        shelf.create(*self.args, w_list_temp, self.maepin_dict, self.write_flag)

        self.layer_change(self, 'CYAN')
        cyan.create(*self.args, self.PanelH_list, self.TenkaW_list, self.bump_list)  # 青い実線

        # layer_change('CYAN')
        # HP() # ハンガーパイプの高さがわかったら描く

        self.layer_change(self, 'MAGENTA')
        magenta.create(*self.args, w_list_temp, self.PanelH_list)

        command_line = '\n'.join(self.command_list)

        path_w = 'scripts/front.txt'
        with open(path_w, mode='w') as f:
            f.write(command_line)
