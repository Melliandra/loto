import random
class Ticket:
    def __init__(self, name):
        self.name = name
        list_ticket = list(range(1,91))
        ok = False
        while not ok:
            self.ticket=random.sample(list_ticket,15)
            ok = self._check_ticket()
        self.ticket = sorted(self.ticket)
        self.view_ticket = self._generate_ticket()
        self.count = 15


    def _check_ticket(self):
        def func(a):
            a = a//10
            if a==9:
                a =8
            return a

        list_check = list(map(func,self.ticket))
        ok = True
        for i in range(0,10):
            amount = list_check.count(i)
            if amount>3:
                ok = False
                break
        return ok



    def _generate_ticket(self):

        def min_val(list_v):
            if (list_v[0][9] <= list_v[1][9]) and  (list_v[0][9] <= list_v[2][9]):
                return 0
            elif  (list_v[1][9] <= list_v[0][9]) and  (list_v[1][9] <= list_v[2][9]):
                return 1
            else:
                return 2

        list_view =[
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        list_1 = [[],[],[],[],[],[],[],[],[]]
        for i in range(0,9):
            for j in self.ticket:
                if j//10==i:
                    list_1[i].append(j)
        if self.ticket[14]==90:
            list_1[8].append(90)


        for i in range(0,9):
            if (len(list_1[i]) == 3):
                for j in range(0,3):
                    list_view[j][i] = list_1[i][j]
                    list_view[j][9] +=1
            else:
                for j in range(0,len(list_1[i])):
                    m = min_val(list_view)
                    list_view[m][i] = list_1[i][j]
                    list_view[m][9] +=1
        for i in range(0,len(list_view)):
            del list_view[i][9]
        return(list_view)

    def print_ticket(self):
        print(f'Билет игрока {self.name}')
        print('_ '*20)
        for i in self.view_ticket:
            for j in i:
                if j == 0:
                    print('  ', end=" |")
                elif j<10:
                    print('',j, end=" |")
                else:
                     print(j, end=" |")
            print(' ')
        print('_ ' * 20)


def check_value(val,tiket):
    ok = None
    for i in range(len(tiket.view_ticket)):
        for j in range(len(tiket.view_ticket[i])):
            if tiket.view_ticket[i][j] == val:
                tiket.view_ticket[i][j] = 0
                tiket.count -= 1
                print (f'У игрока {tiket.name} есть число {val} в билете! Осталось зачеркнуть {tiket.count} чисел(а)')
                break

    return tiket

bag_loto =list(range(1,91))
ticket1 = Ticket('Иван')
ticket2 = Ticket('Компьютер')
winner = True
comp_on = False
while winner:
    value = random.choice(bag_loto)
    bag_loto.remove(value)
    print(value)
    ticket1.print_ticket()
    ticket1 = check_value(value,ticket1)
    ticket2.print_ticket()
    ticket2 = check_value(value,ticket2)
    if (ticket1.count == 0):
        print (f'Игрок {ticket1.name} Победил!')
        winner = False
    elif(ticket2.count == 0):
        print(f'Игрок {ticket2.name} Победил!')
        winner = False









