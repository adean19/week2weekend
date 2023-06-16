class Parking_garage():

    def __init__(self,parkingSpaces, currentTicket):

        self.parkingSpaces = parkingSpaces
        self.tickets = parkingSpaces
        self.currentTicket = currentTicket
    
    def print_info(self):
        print(f'This parking garage has {self.parkingSpaces} space and {self.tickets} tickets.')

    def takeTicket(self):
        self.parkingSpaces -= 1
        self.tickets -= 1

    def payForParking(self,currentTicket):
        ans_pay_for_parking = input('Would you like to pay for your ticket? Yes/No: ')
        if ans_pay_for_parking.lower() == "yes" or ans_pay_for_parking == "y":
            print("Thank you for your payment. You have 15 minuntes to ")
            pass
        elif ans_pay_for_parking.lower() == "no" or ans_pay_for_parking.lower() == "n":
            pass
        else:
            print("That is not a valid response. Please write 'yes' or 'no' to indicate if you'd like to pay for your ticket")

    
    # def payForParking(self):

ChicagoParkingGarage = Parking_garage(200,1)
ChicagoParkingGarage.print_info()
ChicagoParkingGarage.takeTicket()
ChicagoParkingGarage.print_info()
