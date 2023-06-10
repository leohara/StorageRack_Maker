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