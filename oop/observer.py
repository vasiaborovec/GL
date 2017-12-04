class Observer(object):
    def __init__(self):
        self.observers = set()

    def add(self, observer):
        self.observers.add(observer)

    def delete(self, observer):
        self.observers.discard(observer)


    def update(self, message, address):
        for observer in self.observers:
            observer.update(message, address)




class Fire_service(object):
    def update(self, message, address):
        print("Fire at the address: {}".format(address))

class Ofice(object):
    def update(self, message, address):

        print("Oopss {} alarm ".format(message))


if __name__ == "__main__":
    Observer = Observer()

    Observer.add(Fire_service())
    Observer.add(Ofice())

    Observer.update("Fire","some address")

