import random

class Rule(object):

    def __init__(self):
        ''' 初始化的时候就赋予玩家一和玩家二各3张牌 '''
        self.data = list(range(0, 52))

        self.player1 = []
        for i in range(0, 3):
            poker = self.deal()
            self.player1.append({
                'color': poker[0],
                'value': poker[1]})

        self.player2 = []
        for i in range(0, 3):
            poker = self.deal()
            self.player2.append({
                'color': poker[0],
                'value': poker[1]})

    def deal(self):
        ''' 发牌规则 '''
        data = random.choice(self.data)
        index = self.data.index(data)  # index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
        self.data.pop(index)
        if data < 13:
            color = 'black'
            value = data % 13 + 1
            if value == 1:
                value == 14
        elif data < 26:
            color = 'red'
            value = data % 13 + 1
            if value == 1:
                value == 14
        elif data < 39:
            color = 'cube'
            value = data % 13 + 1
            if value == 1:
                value == 14
        elif data < 52:
            color = 'plum'
            value = data % 13 + 1
            if value == 1:
                value == 14
        return color, value

    def compare_value(self, data1, data2):
        ''' 先对其进行排序，排序后便于比较。
        data1: 这里是pai1的牌面值
        data2: 这里是pai2的牌面值
        '''
        data1.sort(reverse=True)
        data2.sort(reverse=True)
        for i in range(0, 3):
            if data1[i] == data2[i]:
                continue
            elif data1[i] > data2[i]:
                return 1
            else:
                return 2

    def get_color(self, player):
        ''' 获取花色 '''
        color = []
        for poker in player:
            color.append(poker['color'])
        return color

    def get_value(self, player):
        ''' 获取牌面值 '''
        value = []
        for poker in player:
            value.append(poker['value'])
        return value

    def is_jinhua(self, player):
        ''' 判断是否为金花：花色相同，非顺子。例：黑桃368，方块145 '''
        data = self.get_color(player)
        if data[0] != data[1] or \
                data[0] != data[2] or \
                data[1] != data[2]:
            return False
        else:
            return True

    def is_triple(self, player):
        ''' 判断否为豹子：三个数相同 '''
        data = self.get_value(player)
        if data[0] == data[1] and data[1] == data[2] and data[0] == data[2]:
            return True
        else:
            return False

    def is_shunzi(self, player):
        ''' 判断是否为花色不同的顺子。例：黑桃5红桃6方块7 '''
        data = self.get_value(player)
        data.sort(reverse=True)
        if data[0] - data[1] == 1 and data[1] - data[2] == 1 and data[0] - data[2] == 2:
            return True
        else:
            return False

    def is_shunjin(self, player):
        ''' 判断是否为顺金 '''
        if self.is_shunzi(player) and self.is_jinhua(player):
            return True
        else:
            return False

    def is_pair(self, player):
        ''' 判断是否为对子 '''
        data = self.get_value(player)
        if data[0] == data[1] or data[1] == data[2] or data[0] == data[2]:
            return True
        else:
            return False

    def find_pair(self, player):
        ''' 如果是对子，找出哪两张牌是一对 '''
        data = self.get_value(player)
        if data[0] == data[1]:
            return 0, 1
        if data[1] == data[2]:
            return 1, 2
        if data[0] == data[2]:
            return 0, 2

    def compare_baozi(self):
        ''' 豹子之间比较大小 '''
        if self.is_triple(self.player1) and not self.is_triple(self.player2):
            return 1
        if not self.is_triple(self.player1) and self.is_triple(self.player2):
            return 2
        if not self.is_triple(self.player1) and not self.is_triple(self.player2):
            return None
        if self.is_triple(self.player1) and self.is_triple(self.player2):
            data1 = self.get_value(self.player1)
            data2 = self.get_value(self.player2)
            return self.compare_value(data1, data2)

    def compare_shunjin(self):
        ''' 顺金之间比大小 '''
        if self.is_shunjin(self.player1) and not self.is_shunjin(self.player2):
            return 1
        if not self.is_shunjin(self.player1) and self.is_shunjin(self.player2):
            return 2
        if not self.is_shunjin(self.player1) and not self.is_shunjin(self.player2):
            return None
        if self.is_shunjin(self.player1) and self.is_shunjin(self.player2):
            data1 = self.get_value(self.player1)
            data2 = self.get_value(self.player2)
            return self.compare_value(data1, data2)

    def compare_jinhua(self):
        ''' 金花之间比大小 '''
        if self.is_jinhua(self.player1) and not self.is_jinhua(self.player2):
            return 1
        if not self.is_jinhua(self.player1) and self.is_jinhua(self.player2):
            return 2
        if not self.is_jinhua(self.player1) and not self.is_jinhua(self.player2):
            return None
        if self.is_jinhua(self.player1) and self.is_jinhua(self.player2):
            data1 = self.get_value(self.player1)
            data2 = self.get_value(self.player2)
            return self.compare_value(data1, data2)

    def compare_shunzi(self):
        ''' 关于顺子的比较 '''
        # 顺子大于非顺子
        if self.is_shunzi(self.player1) and not self.is_shunzi(self.player2):
            return 1
        if not self.is_shunzi(self.player1) and self.is_shunzi(self.player2):
            return 2
        if not self.is_shunzi(self.player1) and not self.is_shunzi(self.player2):
            return None
        # 都是顺子的话比较大小
        if self.is_shunzi(self.player1) and self.is_shunzi(self.player2):
            data1 = self.get_value(self.player1)
            data2 = self.get_value(self.player2)
            return self.compare_value(data1, data2)

    def compare_pair(self):
        ''' 对子之间的比较例：223，334 '''
        if self.is_pair(self.player1) and not self.is_pair(self.player2):
            return 1
        if not self.is_pair(self.player1) and self.is_pair(self.player2):
            return 2
        if not self.is_pair(self.player1) and not self.is_pair(self.player2):
            return None
        if self.is_pair(self.player1) and self.is_pair(self.player2):
            data1 = self.get_value(self.player1)
            data2 = self.get_value(self.player2)
            f1, s1 = self.find_pair(self.player1)
            f2, s2 = self.find_pair(self.player2)
            if data1[f1] > data2[f2]:
                return 1
            elif data1[f1] < data2[f2]:
                return 2
            else:
                data1.pop(f1)
                data1.pop(s1)
                data2.pop(f2)
                data2.pop(s2)
                if data1[0] > data2[0]:
                    return 1
                elif data1[0] < data2[0]:
                    return 2
                else:
                    return 3

    def comapre_common(self):
        ''' 这里是一般性的比较，不是豹子，顺子，金花等（散牌） '''
        data1 = self.get_value(self.player1)
        data2 = self.get_value(self.player2)
        return self.compare_value(data1, data2)

    def compare(self):
        ''' 比较双方的牌 '''
        player1, player2 = self.wrapper()
        flag = self.compare_baozi()
        if flag is not None:
            return flag, player1, player2
        flag = self.compare_shunjin()
        if flag is not None:
            return flag, player1, player2
        flag = self.compare_jinhua()
        if flag is not None:
            return flag, player1, player2
        flag = self.compare_shunzi()
        if flag is not None:
            return flag, player1, player2
        flag = self.compare_pair()
        if flag is not None:
            return flag, player1, player2
        flag = self.comapre_common()
        if flag is not None:
            return flag, player1, player2

    def wrapper(self):
        ''' 拼接玩家一二玩家二的牌的图片，用于展示 '''
        player1 = []
        for poker in self.player1:
            player1.append(poker['color'] + '_' + str('{0:02}'.format(poker['value']))+'.jpg')
        player2 = []
        for poker in self.player2:
            player2.append(poker['color'] + '_' + str('{0:02}'.format(poker['value'])) + '.jpg')
        return player1, player2


if __name__ == '__main__':
    rule = Rule()
    print(rule.compare())