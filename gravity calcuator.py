# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 18:47:40 2025

@author: kanna
"""

def calculate_gratuity(salary, years_of_service):
    if years_of_service < 5:
        return 0
    gratuity = (salary * 15 * years_of_service) / 26
    return gratuity

def main():
    print(" Gratuity Calculator\n")
    
    try:
        name = input("Enter employee name: ")
        salary = float(input("Enter last drawn monthly salary (in ₹): "))
        years = int(input("Enter number of years of service: "))
        
        gratuity_amount = calculate_gratuity(salary, years)
        
        print("\n Gratuity Details")
        print("--------------------")
        print(f"Name: {name}")
        print(f"Years of Service: {years} years")
        print(f"Last Drawn Salary: ₹{salary:.2f}")
        
        if gratuity_amount == 0:
            print("Gratuity Amount: Not eligible (less than 5 years of service)")
        else:
            print(f"Gratuity Amount: ₹{gratuity_amount:.2f}")
    
    except ValueError:
        print(" Please enter valid numeric input for salary and years.")


if __name__ == "__main__":

    main()