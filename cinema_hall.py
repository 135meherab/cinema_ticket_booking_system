class Star_Cinema:
    hall_list = []
    def entry_hall(self,hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, row, col, hall_no) -> None:
        self.hall_no = hall_no
        self.__row = row
        self.__col = col
        self.__sits = {self.hall_no:[[0 for i in range(self.__col)] for j in range(self.__row)]}
        self.__show_list = []
    
    def entry_show(self,id, movie_name, date, time):
        self.__show_list.append((id, movie_name, date, time))
    
    def book_sits(self, id, sit):
        sit_r = sit[0]-1
        sit_c = sit[1] -1
        sit_list = self.__sits[id]
        if (sit_r > 0 and sit_r < len(sit_list)) and (sit_c > 0 and sit_c < len(sit_list[0])):
                if sit_list[sit_r][sit_c] == 0:
                    sit_list[sit_r][sit_c] = 1
                    print("You successfully book a ticket\n")
                else:
                    print("Sorry The sit is already booked\n")
        else:
            print("There is no sit at this position")
                   
    
    def view_show_list(self):
        for lst in self.__show_list:
            print(f"MOVIE NAME: {lst[1]}   ID: {lst[0]}   DATE: {lst[2]}   TIME: {lst[3]}\n")
    
    def view_available_sits(self, id):
        if id in self.__sits.keys():
            sit_list = self.__sits[id]
            for i in range(len(sit_list)):
                for j in range(len(sit_list[0])):
                    print(sit_list[i][j],end=" ")
                print()
            print()
        else:
            print(f"Sorry there is no Show with this id: {id}\n")        



ShemoliCinema = Hall(5,10,"1100")
abcCinema = Hall(5,7,"2010")
ShemoliCinema.entry_hall(ShemoliCinema)
abcCinema.entry_hall(abcCinema)
ShemoliCinema.entry_show(ShemoliCinema.hall_no,"Jawan Majhi","07 / 10 / 2023","11:00 AM")
abcCinema.entry_show(abcCinema.hall_no,"Buda Majhi","07 / 10 / 2023","05:00 PM")

while True:
    print()
    print("1. View All Show Today")
    print("2. View Available Sits")
    print("3. Book A Ticket")
    print("4. Press any kye to exit")
    print()
    op = input("Enter an Option: ")
    if op == "1":
        print()
        for token in Star_Cinema.hall_list:
            token.view_show_list()
    elif op =="2":
        id = input("Enter movie id: ")
        is_found = False
        print()
        for token in Star_Cinema.hall_list:
            if token.hall_no == id:
                is_found=True
                break
        if is_found:
            token.view_available_sits(id)
        else:
                print(f"Sorry there is no Show with this id: {id}\n")    
    elif op == "3":
        id = input("Enter movie id: ")
        is_found = False
        for token in Star_Cinema.hall_list:
            if token.hall_no == id:
                is_found=True
                break
        if is_found:
            r = int(input("Enter sit's row: "))
            c = int(input("Enter sit's column: "))
            print()
            token.book_sits(id,(r,c))
        else:
            print()
            print(f"Sorry there is no Show with this id: {id}\n")
    elif op == "4":
        break
    else: 
        print("!!!---> You entered a wrong key <---!!!")
        print("!!!-------- Let's try again --------!!!\n")
    
