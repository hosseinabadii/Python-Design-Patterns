from bridge import DrawingAPIOne, DrawingAPITwo, Circle

def main():
    print('Circle use DrawingAPIOne')
    c1 = Circle(10, 20, 40, DrawingAPIOne)
    c1.draw()
    c1.scale(0.4)
    c1.draw()

    print('Circle use DrawingAPITwo')
    c2 = Circle(2, 6, 70, DrawingAPITwo)
    c2.draw()
    c2.scale(0.5)
    c2.draw()

if __name__ == "__main__":
    main()