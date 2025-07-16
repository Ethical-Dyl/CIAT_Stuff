"""
Import OS for terminal clearing.
"""
import os

def get_height():
    """
    This function allows the user to enter in their height.
    Input: inch_height
    Output: return inch_height
    """
    while True:
        try:
            inch_height = float(input("Enter in your height in inches: "))
            if not isinstance(inch_height, (float, int)):
                raise ValueError
            if isinstance(inch_height, (float, int)):
                return inch_height

        except KeyboardInterrupt:
            print("User has requested exit. Goodbye.")
        except ValueError as e:
            print(e)

def conv_height(inch_height):
    """
    This function converts the inch_height from inches to meters.
    Input: inch_height
    Output: converted_height
    """
    converted_height = inch_height * 0.0254
    return converted_height

def get_weight():
    """
    This function allows the user to enter in their weight.
    Input: pound_weight
    Output: return pound_weight
    """
    while True:
        try:
            pound_weight = float(input("Enter in your weight in pounds: "))
            if not isinstance(pound_weight, (float, int)):
                raise ValueError
            if isinstance(pound_weight, (float, int)):
                return pound_weight

        except KeyboardInterrupt:
            print("User has requested exit. Goodbye.")
        except ValueError as e:
            print(e)

def conv_weight(pound_weight):
    """
    This function converts the pound_weight from lbs to kgs.
    Input: pound_weight
    Output: kg_weight
    """
    kg_weight = pound_weight / 2.205
    return kg_weight

def calculate_calculate_bmi(height, weight):
    """
    This function calculated bmi from height and weight.
    Input: height, weight
    Output: calculated_bmi
    """
    os.system('cls||clear')
    print(f'Your height in meters is: {height:g}m, and weight in kilograms is: {weight:g}kg')
    calculated_bmi = weight / (height ** 2)
    return calculated_bmi

def explain_bmi(bmi):
    """
    This function tells the user their bmi.
    Input: bmi
    Output: bmi message
    """
    if bmi < 16:
        print(f"Your calculated_bmi is {bmi:.2f}. You are severely underweight.")
    elif bmi <= 16.9:
        print(f"Your calculated_bmi is {bmi:.2f}. You are underweight.")
    elif bmi <= 18.4:
        print(f"Your calculated_bmi is {bmi:.2f}. You are mildly underweight.")
    elif bmi <= 24.9:
        print(f"Your calculated_bmi is {bmi:.2f}. You have a normal weight.")
    elif bmi <= 29.9:
        print(f"Your calculated_bmi is {bmi:.2f}. You are overweight.")
    elif bmi <= 34.9:
        print(f"Your calculated_bmi is {bmi:.2f}. You are obese class 1 (Moderate).")
    elif bmi <= 39.9:
        print(f"Your calculated_bmi is {bmi:.2f}. You are obese class 2 (Severe).")
    else:
        print(f"Your calculated_bmi is {bmi:.2f}. You are obese class 3 \
              (Very severe or morbidly obese).")

def main():
    """
    Main Function    
    """
    inch_height = get_height()
    height = conv_height(inch_height)
    pound_weight = get_weight()
    weight = conv_weight(pound_weight)
    bmi = calculate_calculate_bmi(height, weight)
    explain_bmi(bmi)


if __name__ == '__main__':
    main()
