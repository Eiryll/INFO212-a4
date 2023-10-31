# Cars added to the sytem for testing
from project.models.my_cars import save_car


def main():
    save_car("Ford", "Focus", "11D1234", 2011, 5)
    save_car("Nissan", "Micra", "12D1234", 2012, 5)
    save_car("Toyota", "Yaris", "13D1234", 2013, 5)
    save_car("Ford", "Fiesta", "14D1234", 2014, 5)
    save_car("Volkswagen", "Golf", "15D1234", 2015, 5)
    save_car("Volkswagen", "Polo", "16D1234", 2016, 5)
    save_car("Toyota", "Corolla", "17D1234", 2017, 5)


if __name__ == "__main__":
    main()
