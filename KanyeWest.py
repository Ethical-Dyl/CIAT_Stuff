import random
import os

def all_of_the_lights():
    print("Attempting to turn on all lights...")
    lights = [random.randint(0, 5) for _ in range(4)]
    faulty_light = check_lights(lights)
    if not faulty_light:
        print("All lights are on!")
    return faulty_light



def check_lights(lights):
    faulty_light = []
    for i, light in enumerate(lights, start=1):
        if light <= 0:
            print(f"Faulty light: light number: {i}")
            faulty_light.append(i)
    return faulty_light

def main():
    os.system('cls||clear')
    turn_on_lights = input("Would you like to turn on all lights? (Y/N): ").strip().upper()
    if turn_on_lights == 'Y':
        all_of_the_lights()
    else:
        print("All lights remaining off.")

if __name__ == '__main__':
    main()
