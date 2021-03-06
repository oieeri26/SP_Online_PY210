#!/usr/bin/env python3
import sys

donor_records = {}

# Initial donations
initial_donations ={"Rhianna": [747, 3030303, 1968950],
    "Grumps": [5.99],
    "EatPraySlay": [100000, 200000, 300000], 
    "Muir": [469503, 50000, 186409],
    "Spacewalker": [4406, 342]}

# Helper function: Update donor record after a new donation
def update_record(donor_name):
    donations = donor_records[donor_name]["donations"]
    donor_records[donor_name]["sum"] = sum(donations, 0)
    donor_records[donor_name]["numGifts"] = len(donations)
    donor_records[donor_name]["avgGift"] = sum(donations, 0)/len(donations)

# Populate initial donor records
for donor in initial_donations:
    donor_records[donor] = {"name": donor,
        "donations": initial_donations[donor]}
    update_record(donor)

# Helper function: Write letter
def write_letter(donor_name):
    last_donation = donor_records[donor_name]["donations"][-1]
    return f"To the esteemed {donor_name}:\n\n" \
    "Thank you for generous donation of " \
    f"${last_donation:.2f}. You're a champion!"
    
# Store new donation record, then create e-mail to thank donor
def thank_donor():

    while True:
        donor_name = input("Who would you like to thank? "
            "(Type 'list' to see a list of donors.)\n  Full Name: ")

        # Print list of existing donors to choose from
        if donor_name.lower() == "list":
            for k in donor_records:
                print(k)

        else: # Find or make donor record, then add new donation
            if donor_name in donor_records:
                donation_amount = float(input(
                    "Please enter the donation amount: "))
                donor_records[donor_name]["donations"].append(donation_amount)

            else: # If this is a new donor, collect and store donor info
                donation_amount = float(input(f"Adding {donor_name} to "
                    "the database.\nPlease enter the donation amount: "))
                donor_records[donor_name] = {
                    "name": donor_name,
                    "donations": [donation_amount]}
            
            print(write_letter(donor_name)) # write thank you
            update_record(donor_name) # update the donor's record
            return donor_records

# Thank all donors for their most recent donations
def thank_all():
    for donor in donor_records:
        f = donor + ".txt"
        with open(f, 'w') as f:
            f.write(write_letter(donor))
            f.close()
    print("\nThank you notes complete!\n")

# Create a report of all donor records to date
def create_report():
    # Set up column headers
    print(" "+"-"*60+"\n Donor Name"+" "*10+
        "| Total Given | Num Gifts | Average Gift\n "+"-"*60)

    # Sort donors by amount, then print donor summary
    for i in sorted(donor_records.items(), key=lambda x: x[1]["sum"], 
        reverse = True):
        print(" {name:<20} ${sum:>11.2f}{numGifts:>12}  ${avgGift:>12.2f}".format(**i[1]))

def end_game():
    print("\nThanks for playing!")
    sys.exit()

# Display a user menu, then act on the user's selection
def main():
    
    main_menu = {"1": thank_donor, "2": thank_all, "3": create_report, "q": end_game}
    
    while True:
        
        user_action = input("\n".join(("\nWhat would you like to do?", 
            "  Enter 1 to create a thank you for a single donor",
            "  Enter 2 to create a thank you for all donors",
            "  Enter 3 to create a report",
            "  Enter q to quit.",
            "  >>>")))

        try:
            main_menu[user_action]()
        
        except SystemExit:
            e = sys.exit(1)
        
        except:
            print("Let's behave. Try again using one of the options!")

if __name__ == "__main__":
    main()
