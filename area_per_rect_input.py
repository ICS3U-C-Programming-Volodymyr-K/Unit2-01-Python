#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 02/26/2024
# It calculates and displays the perimeter for the given input


def main():
    Length = int(input("Enter length of the rectangle (cm): "))
    Width = int(input("Enter width of the rectangle (cm): "))
    print(
        "So the area will be A = length * width = 6cm * 5cm = {}".format(Length * Width)
    )
    print(
        "The Perimiter will be P = 2*length + 2*width = 2*6cm + 2*5cm = {}".format(
            2 * Length + 2 * Width
        )
    )


if __name__ == "__main__":
    main()
