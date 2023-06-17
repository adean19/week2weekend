class Parking_garage():

    # The entire code was written by both Nick and Renat; we switched up driving and navigating
    # throughout our Friday coding session.

    def __init__(self,parkingSpaces):
        self.parkingSpaces = parkingSpaces
        self.tickets = parkingSpaces
        self.currentTicket = 1
        self.ticketStatus = dict()
    
    def print_info(self):
        print(f'{self} parking garage has {self.parkingSpaces} space and {self.tickets} tickets.')

    def takeTicket(self):
        self.parkingSpaces -= 1
        self.tickets -= 1
        print(f"Your ticket number is: {self.currentTicket}. Please remember you ticket number!")
        self.ticketStatus[self.currentTicket] = False
        self.currentTicket += 1

    def payForParking(self):
        while True:
            ticketNumber = int(input('Please insert your ticket number: '))
            if ticketNumber in self.ticketStatus:
                self.ticketStatus[ticketNumber] = True
                print("Thank you for your payment. You have 15 minutes to exit.")
                break
            else:
                print("That is not a valid response. Please provide your ticket number as a numeral.")
    
    def leaveGarage(self):
        while True:
            ticketNumber = int(input('Your are trying to leave the garage. Please insert your ticket number: '))
            if ticketNumber in self.ticketStatus and self.ticketStatus[ticketNumber] == True:
                print("Thank You! Have a nice day.")
                self.parkingSpaces += 1
                self.tickets +=1
                del self.ticketStatus[ticketNumber]
                break
            
            elif ticketNumber in self.ticketStatus:
                print("Your ticket has not been paid. Please pay your ticket.")
                while True:
                    pay_ticket = input("Would you like to pay for your ticket? (Yes/No): ")
                    if pay_ticket.lower() == "yes" or pay_ticket.lower() == "y":
                        print("Thank you for your payment. You have 15 minutes to exit.")
                        break
                    elif pay_ticket.lower() == "no" or pay_ticket.lower() == "n":
                        print("You will need to pay for your ticket before you can leave the garage.")
                        break
                    else:
                        print("That is not a valid response. Please provide your ticket number as a numeral.")
                break
            
            else:
                print("That is not a valid response. Please provide your ticket number as a numeral.")

    
    # def payForParking(self):

ChicagoParkingGarage = Parking_garage(200)
ChicagoParkingGarage.print_info()
ChicagoParkingGarage.takeTicket()
ChicagoParkingGarage.print_info()
ChicagoParkingGarage.takeTicket()
ChicagoParkingGarage.print_info()
ChicagoParkingGarage.takeTicket()
print(ChicagoParkingGarage.ticketStatus)
ChicagoParkingGarage.payForParking()
print(ChicagoParkingGarage.ticketStatus)
ChicagoParkingGarage.leaveGarage()
print(ChicagoParkingGarage.ticketStatus)
ChicagoParkingGarage.takeTicket()
ChicagoParkingGarage.print_info()
print(ChicagoParkingGarage.ticketStatus)
ChicagoParkingGarage.leaveGarage()