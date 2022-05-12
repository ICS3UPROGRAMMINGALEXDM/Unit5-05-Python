#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: gets input from a user, will return their address in the canada
# post format

# takes the parameters and formats a string using the inputted information
# that complies with the Canada Post rules. Also sets the apartment to have a
# default of none
def format_address(
    name, street_number, street_name, city, province, postal, apartment=None
):
    if apartment != None:
        # string formattiing for the case with an apartment
        formatted = "{} \n{}-{} {} \n{} {} {}".format(
            name, apartment, street_number, street_name, city, province, postal
        )
    else:
        # string formatting for the case without an apartment
        formatted = "{} \n{} {} \n{} {} {}".format(
            name, street_number, street_name, city, province, postal
        )
    # returning the formatted string to main
    return formatted


def main():
    # getting all of the needed information
    name = input("Enter your name: ").upper()
    answer = input("Do you live in an apartment(y/n): ").upper()
    if answer == "Y":
        apartment = input("Enter your apartment number: ").upper()
    street_number = input("Enter your street number: ").upper()
    street_name = input("Enter the street name AND the street class: ").upper()
    city = input("Enter your city: ").upper()
    province = input("Enter your province's abbreviation: ").upper()
    postal = input("Enter your postal code: ").upper()

    # chooses whether or not to call the function with the apartment
    if answer == "Y":
        address = format_address(
            name, street_number, street_name, city, province, postal, apartment
        )
    else:
        address = format_address(
            name, street_number, street_name, city, province, postal
        )

    print()
    print()
    print(address)


if __name__ == "__main__":
    main()
