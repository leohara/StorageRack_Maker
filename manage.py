import pandas as pd
import glob
import os

from setup import prepare
from files import side
from files import front


def load():
    sheet = prepare.Sheet()
    prepare.to_txt(sheet)


if __name__ == "__main__":

    columns = ['name', 'update_time']
    df = pd.read_csv('csv/update.csv')
    df_name = df['name']
    df_update_time = df['update_time']
    df_new = pd.DataFrame(columns=columns)

    files = glob.glob("setup/*")
    flag = 0
    for i, file in enumerate(files):
        path = file
        for name in df['name']:
            if path == name:
                file_info = os.stat(file)
                update_time = file_info.st_mtime
                data = [[path, update_time]]
                df_unit = pd.DataFrame(data=data, columns=columns)
                df_new = pd.concat([df_new, df_unit])
                if (update_time > df.iloc[i, 1]) & (flag == 0):
                    print('変更が検出されたので変数を読み込みます')
                    print('読み込み中...')
                    load()
                    print('読み込みが終わりました')
                    flag = 1
    if flag == 0:
        print('変更は検出されませんでした')

    df_new.to_csv('csv/update.csv', index=False)

    write_side = side.Side()
    write_flag = [0 if write_side.h_list[i] in write_side.h_list[:i] else 1 for i in range(len(write_side.h_list))]
    for i in range(len(write_flag)):
        if not i:
            write_side.mk_command_side(write_side.param.order_from_left[i])
            inc = 0
        else:
            if write_flag[i]:
                inc += 1
                write_side.x = -inc * 2000
                write_side.mk_command_side(write_side.param.order_from_left[i])

    write_front = front.Front()
    write_front.mk_command_front()

    side_f = open('scripts/side.txt', 'r')
    side_script = side_f.read()
    side_f.close()
    front_f = open('scripts/front.txt', 'r')
    front_script = front_f.read()
    front_f.close()
    all_f = open('scripts/all.txt', 'w')
    all_f.write(side_script + front_script)
    all_f.close()
