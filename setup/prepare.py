import openpyxl
import pandas as pd


class Sheet:
    def __init__(self,):
        sheet1 = openpyxl.load_workbook("setup\storage_drawing.xlsx",
                                        data_only=True)['ｲﾚｷﾞｭﾗｰ物入ダボ']
        sheet2 = openpyxl.load_workbook("setup\storage_drawing.xlsx",
                                        data_only=True)['ｲﾚｷﾞｭﾗｰ物入']

        self.x_side = sheet2['AB6'].value
        self.y_side = sheet2['AC6'].value
        self.x_front = sheet2['AB7'].value
        self.y_front = sheet2['AC7'].value

        # 変換後のパラメーター
        self.W = sheet1['J14'].value
        self.H = sheet1['L14'].value  # 地面から上天下板までの寸法
        self.D = sheet1['N14'].value  # 内法

        order_dict = {}
        for row, alphabet in zip(sheet2["O7:O11"], ['A', 'B', 'C', 'D']):
            for col in row:
                if col.value is not None:
                    order_dict[alphabet] = col.value
        order = sorted(order_dict.items(), key=lambda x: int(x[1]))
        self.order_from_left = list()
        for k in order:
            self.order_from_left.append(k[0])
        self.left_and_right = [self.order_from_left[0],
                               self.order_from_left[-1]]

        self.flag = [False if i == 'A' else True for i in self.order_from_left]

        sheet_range = sheet2['P7':'U10']  # 取得範囲
        conv_list = list()
        for row in sheet_range:
            for cell in row:
                cell_value = cell.value
                if cell_value != '×':
                    conv_list.append(cell_value)
        self.num = len(self.order_from_left)

        conv_dict = {'A': ['w_A', 'h_A', 'd_A'],
                     'B': ['w_B', 'h_B', 'd_B'],
                     'C': ['w_C', 'h_C', 'd_C'],
                     'D': ['w_D', 'h_D', 'd_D'],
                     }

        for i in range(int(len(conv_list) / 4)):
            param = conv_list[i * 4: i * 4 + 4]
            for j in list(conv_dict.keys()):
                if param[0][-1] == j:
                    if j in self.order_from_left:
                        for k in range(3):
                            # 変数を動的に生成
                            exec(
                                'self.{} = {}'.format(conv_dict[j][k], param[k + 1])
                            )

        exec('self.tall_Panel_flag = 0 if self.w_{} > self.w_{} else 1'.format(
            self.order_from_left[0],
            self.order_from_left[1]))

        sheet_range = sheet2['P16':'U47']  # 取得範囲
        conv_list = list()
        for row in sheet_range:
            for cell in row:
                cell_value = cell.value
                if (cell_value != '×') and (cell_value is not None):
                    conv_list.append(cell_value)

        conv_dict = {'台輪': ['DaiwaW', 'DaiwaD', 'DaiwaH'],
                     '天下板': ['TenkaW', 'TenkaD', 'TenkaH'],
                     '裏板': ['UraH', 'UraW', 'UraD'],
                     '側ﾊﾟﾈﾙ': ['PanelH', 'PanelD', 'PanelW']
                     }

        for i in range(int(len(conv_list) / 4)):
            param = conv_list[i * 4: i * 4 + 4]
            for j in list(conv_dict.keys()):
                if j in param[0]:
                    for k in range(3):
                        # 変数を動的に生成
                        exec(
                            'self.{} = {}'.format(conv_dict[j][k], param[k + 1])
                        )

        for i in self.order_from_left:
            exec('self.PanelH_{} = self.h_{} - 60'.format(i, i))
            exec('self.PanelD_{} = self.d_{} + 15'.format(i, i))
            exec('self.TenkaW_{} = self.w_{}'.format(i, i))
            exec('self.TenkaD_{} = self.d_{} - 14'.format(i, i))
            exec('self.UraH_{} = self.h_{} - 87'.format(i, i))
            exec('self.UraW_{} = self.w_{} - 9'.format(i, i))

        self.PanelW = 18
        self.TenkaH = 18
        self.TenkaD += 2

        # 扉
        self.DoorD = 22
        self.Door_Tenka = 10.5  # 扉と天下板(上下)の間隔

        # 棚
        self.Door_shelf = 24  # 扉と棚の隙間
        self.shelfH = 18

        self.gap_dowel_front = 36
        self.gap_dowel_back = 53
        self.gap_dowel = 32
        self.gap_back = 8
        self.tyobanW = 45

        self.Door_Tenka_inside = 7.5
        self.PanelW_inner = 7
        self.PanelW_outer = 11


def to_txt(sheet):
    # parameters.csvに変数を書き込み
    d = vars(sheet)
    path = "csv\parameters.csv"
    df = pd.DataFrame(list(sorted(d.items())), columns=['name', 'value'])
    df.to_csv(path, index=False)
    return
