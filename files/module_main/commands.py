class Commands:
    # 長方形を描くコマンドを生成
    def rec_command(self, X1, Y1, X2, Y2):
        command = 'ATTDIA 1 rectang {},{} {},{} ATTDIA 0 '.format(X1, Y1, X2, Y2)
        return command

    # 線を描くコマンドを生成
    def line_command(self, X1, Y1, X2, Y2):
        command = 'ATTDIA 1 line {},{} {},{} ATTDIA 0 '.format(X1, Y1, X2, Y2)
        return command

    # 半径Rの円を描くコマンドを生成
    def circle_command(self, X, Y, R):
        command = 'ATTDIA 1 circle {},{} {} ATTDIA 0 '.format(X, Y, R)
        return command

    # 半径Rの円弧を描くコマンドを生成
    def arc_command(self, X1, Y1, X2, Y2, R):
        command = 'ATTDIA 1 arc {},{} e {},{} r {} ATTDIA 0 '.format(X1, Y1, X2, Y2, R)
        return command

    # 寸法線を描くコマンドを生成
    def dimaligned(self, X1, Y1, X2, Y2, d):
        command = 'ATTDIA 1 DIMALIGNED {},{} {},{} {} ATTDIA 0 '.format(X1, Y1, X2, Y2, d)
        return command

    # 文字列を描くコマンドを生成
    def text(self, X1, Y1, degree, text):
        command = """
DTEXTED
1
text
j
m
{},{}
60
{}
{}

DTEXTED
0
        """.format(X1, Y1, degree, text)
        return command

    # ブロックを描くコマンドを生成
    def insert_command(name, X, Y):
        command1 = '_-insert {}'.format(name)
        command2 = '{},{} 1 0 '.format(X, Y)
        return command1, command2
