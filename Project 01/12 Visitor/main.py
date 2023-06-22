from visitor import House, HvacSpecialist, Electrician

def main():
    hv = HvacSpecialist()
    e = Electrician()
    house = House()

    house.accept(hv)
    house.accept(e)


if __name__ == "__main__":
    main()