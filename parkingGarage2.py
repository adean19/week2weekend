class Parking_garage():

    # The entire code was written by both Nick and Renat; we switched up driving and navigating
    # throughout our Friday coding session.

    def __init__(self,parkingSpaces):
        self.parkingSpaces = parkingSpaces
        self.tickets = parkingSpaces
        self.currentTicket = 1
        self.ticketStatus = dict()
    
    def print_info(self):
        print(f'Welcome to {self} parking garage. This garage has {self.parkingSpaces} spaces available.')

    def takeTicket(self):
        if self.parkingSpaces == 0:
            print("We apologize, the parking is currently full. Please try again later.")
        else:
            self.parkingSpaces -= 1
            self.tickets -= 1
            print(f"Your ticket number is: {self.currentTicket}. Please remember your ticket number!")
            self.ticketStatus[self.currentTicket] = False
            self.currentTicket += 1

    def payForParking(self, ticketNumber = None):
        
        if ticketNumber == None:
            while True:
                ticketNumber = int(input('Please insert your ticket number: '))
                if ticketNumber in self.ticketStatus:
                    self.ticketStatus[ticketNumber] = True
                    print("Thank you for your payment. You have 15 minutes to exit.")
                    break
                else:
                    print("That is not a valid response. Please provide your ticket number as a numeral.")
        
        else:
            while True:
                if ticketNumber in self.ticketStatus:
                    self.ticketStatus[ticketNumber] = True
                    print("Thank you for your payment. You have 15 minutes to exit.")
                    break
                else:
                    print("That is not a valid response. Please provide your ticket number as a numeral.")
    
    def leaveGarage(self,ticketNumber=None):
        while True:
            if ticketNumber == None:
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
            else:
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

    def main(self):
        
        while True:

            haveTicket = input(f"Do you have a previously issued ticket? (Yes/No): ")

            if haveTicket.lower() == "no" or haveTicket.lower() == "n":
                while True:
                    self.print_info()
                    welcome_response = input(f"Would you like to enter? (Yes/No): ")
                    if welcome_response.lower() == "yes" or welcome_response.lower() == "y":
                        self.takeTicket()
                        break
                    elif welcome_response.lower() == "no" or welcome_response.lower() == "n":
                        print("We appreciate your consideration of our garage. Have a wonderful day.")
                        return
                    else:
                        print("That is not a valid response. Please respond 'Yes' or 'No'.")
                return
            
            elif haveTicket.lower() == "yes" or haveTicket.lower() == "y":
                    
                    returnTicketNumber = input("What is your ticket number?: ")

                    if returnTicketNumber in self.ticketStatus and self.ticketStatus[returnTicketNumber] == True:
                        self.leaveGarage(returnTicketNumber)
                    
                    elif returnTicketNumber in self.ticketStatus:

                        while True:

                            response = input(f"What would you like to do? (Pay/Leave): ")

                            if response.lower() == "pay" or response.lower() == "p":
                                self.payForParking(returnTicketNumber)
                                break
                            elif response.lower() == "leave" or response.lower() == "l":
                                self.leaveGarage(returnTicketNumber)
                                break
                            else:
                                print("That is not a valid response. Please respond 'Pay' or 'Leave'.")

            else:
                print("That is not a valid response. Please respond 'Yes' or 'No'.")

        # while True:
        #     self.print_info()
        #     welcome_response = input(f"Would you like to enter? (Yes/No): ")
        #     if welcome_response.lower() == "yes" or welcome_response.lower() == "y":
        #         self.takeTicket()
        #         break
        #     elif welcome_response.lower() == "no" or welcome_response.lower() == "n":
        #         print("We appreciate your consideration of our garage. Have a wonderful day.")
        #         return
        #     else:
        #         print("That is not a valid response. Please respond 'Yes' or 'No'.")

        # while True:

        #     response = input(f"What would you like to do? (Pay/Leave): ")

        #     if response.lower() == "pay" or response.lower() == "p":
        #         self.payForParking()
        #         break
        #     elif response.lower() == "leave" or response.lower() == "l":
        #         self.leaveGarage()
        #         break
        #     else:
        #         print("That is not a valid response. Please respond 'Pay' or 'Leave'.")

            

ChicagoParkingGarage = Parking_garage(200)
ChicagoParkingGarage.main()



# ChicagoParkingGarage.print_info()
# ChicagoParkingGarage.takeTicket()
# ChicagoParkingGarage.print_info()
# ChicagoParkingGarage.takeTicket()
# ChicagoParkingGarage.print_info()
# ChicagoParkingGarage.takeTicket()
# print(ChicagoParkingGarage.ticketStatus)
# ChicagoParkingGarage.payForParking()
# print(ChicagoParkingGarage.ticketStatus)
# ChicagoParkingGarage.leaveGarage()
# print(ChicagoParkingGarage.ticketStatus)
# ChicagoParkingGarage.takeTicket()
# ChicagoParkingGarage.print_info()
# print(ChicagoParkingGarage.ticketStatus)
# ChicagoParkingGarage.leaveGarage()