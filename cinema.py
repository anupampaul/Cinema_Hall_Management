class Star_Cinema:
    hall_list = []

    def __init__(self):
        pass

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        list = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(f'{chr(ord("@")+(i+1))}{j}')
            list.append(row)
        self.__seats[id] = list

    def book_seats(self, name, phoneNumber, showId, seats):
        
        if showId not in self.__seats:
            print("\n\nINVALID SHOW ID\n")
            return

        for seat in seats:
            if seat[0] >= self.rows or seat[1] >= self.cols:
                print("Invalid seat")
                return

            if type(self.__seats[showId][seat[0]][seat[1]]) == tuple:
                print("Seat already booked")
                return

        booked_list = []
        for seat in seats:
            self.__seats[showId][seat[0]][seat[1]] = (name, phoneNumber)
            booked_list.append(f'{chr(ord("@")+(seat[0]+1))}{seat[1]}')

        print("\t\t####TICKET BOOKED SUCCESSFULLY!!####")
        print('*' * 150)
        print(f"""NAME: {name}
PHONE NUMBER: {phoneNumber}
MOVIE NAME: {self.__show_list[showId][1]} \t\t MOVIE TIME: {self.__show_list[showId][2]}
TICKETS NUMBERS : { " ".join(booked_list)}
HALL: {self.hall_no}
        """)
        print('*' * 150)

    def view_show_list(self):
        print('*' * 150)
        for show in self.__show_list:
            print(
                f''' MOVIE NAME: {show[1]}\t\t  TIME: {show[2]} \t\t SHOW ID: {show[0]}'''
            )
        print('*' * 150)

    def view_available_seats(self, showId):

        if showId not in self.__seats:
            print("\n\nINVALID SHOW ID\n\n")
            return
        print(
            f"\n\nMOVIE NAME: {self.__show_list[showId][1]} \t\t MOVIE TIME: {self.__show_list[showId][2]}"
        )
        print('X for already booked seats')
        print('_' * 150)
        for row in self.__seats[showId]:
            for seat in row:

                if type(seat) == tuple:
                    print('X', end='\t')
                else:
                    print(seat, end='\t')
            print()
        print('_' * 150)


hall = Hall(5, 2, 'A0')

hall.entry_show(1, "Batman", "20/11/22 10:00 AM")
hall.entry_show(2, "Spiderman", "20/11/22 02:00 PM")
hall.entry_show(3, "Antman", "20/11/22  02:00 PM")


while (True):
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK SEATS")
    option = int(input("ENTER OPTIONS: "))
    if option == 1:
        hall.view_show_list()
    elif option == 2:
        showId = int(input("ENTER SHOW ID: "))
        hall.view_available_seats(showId)
    elif option == 3:
        name = input("ENTER NAME: ")
        phoneNumber = int(input("ENTER PHONE NUMBER: "))
        showId = int(input("ENTER SHOW ID: "))
        seats = []
        seat_count = int(input("ENTER NUMBER OF SEATS: "))
        for i in range(seat_count):
            seat_number = input("ENTER SEAT NUMBER: ")
            row = ord(seat_number[0]) * ord('@') * 1
            col = int(seat_number[1])
            seats.append((row, col))
        hall.book_seats(name, phoneNumber, showId, seats)
    else:
        break