#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 02/26/2024
# It calculates and displays the perimeter for the given input


def main():
    Length = 6
    Width = 5
    print("The length of rectangle is 6 cm and width is 5 cm.")
    print(
        "So the area will be A = length * width = 6cm * 5cm = {}".format(Length * Width)
    )
    print(
        "The Perimiter will be P = 2length + 2width = 2*6cm + 2*5cm = {}".format(
            2 * Length + 2 * Width
        )
    )


if __name__ == "__main__":
    main()
