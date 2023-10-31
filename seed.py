# Cars added to the sytem for testing
from project.models.Car import save_car


def main():
    save_car("Ford", "Focus", "11D1234", 2011, 5, 1, "available")
    save_car("Nissan", "Micra", "12D1234", 2012, 5, 2, "available")
    save_car("Toyota", "Yaris", "13D1234", 2013, 5, 3, "available")
    save_car("Ford", "Fiesta", "14D1234", 2014, 5, 4, "available")
    save_car("Volkswagen", "Golf", "15D1234", 2015, 5, 5, "available")
    save_car("Volkswagen", "Polo", "16D1234", 2016, 5, 6, "available")
    save_car("Toyota", "Corolla", "17D1234", 2017, 5, 7, "available")


if __name__ == "__main__":
    main()
