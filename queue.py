class Group:
    def __init__(self, numberOfPeople, nextGroup=None):
        self.numberOfPeople = numberOfPeople
        self.nextGroup = nextGroup
    

class Ride:
    def __init__(self, limit=12):
        self.limit = limit
        self.first = None
        self.last = None
        self.length = 0
        self.waitingTime = 0
    
    def is_full(self):
        return self.length == self.limit
    
    def is_empty(self):
        return self.length == 0
        
    def get_length(self):
        return self.length

    def peek(self):
        if self.is_empty():
            print("Nothing to see here, move along.")
        else:
            return self.waitingTime
    
    def enqueue(self, data):
        if not self.is_full():
            # add to queue
            if self.is_empty():
                # add to queue and set node == first
                if data <= 12:
                    new_group = Group(data)
                    self.first = new_group
                    self.last = new_group
                else:
                    while i > 0 :
                        i = data -12
                        new_group = Group(i)
                        self.first = new_group
                        self.last = new_group
                self.length +=1
                self.waitingTime += 30
            # its not empty
            else:
                if data <= 12:
                    new_group = Group(data)
                    self.last.nextGroup = new_group
                    self.last = new_group
                    self.length +=1
                    self.waitingTime += 30

                else:
                    while data > 0 :
                        data -= 12
                        new_group = Group(data)
                        self.last.nextGroup = new_group
                        self.last = new_group
                        self.length +=1
                        self.waitingTime += 30
        else:
            print(f"please wait for {self.waitingTime} seconds, the ride is full")
    
    def dequeue(self):
        if not self.is_empty():
            removed_group = self.first
            if self.get_length() == 1:
                self.first = None
                self.last = None
            else:
                self.first = removed_group.nextGroup
            self.length -= 1
            self.waitingTime -= 30
            return removed_group.numberOfPeople
        else:
            print("there is no people in line")
        
new_ride = Ride()

while True:
    print("_"*25)
    print(f"waiting time {new_ride.waitingTime}")
    print("_"*25)
    num = int(input("enter the number of people in the group (or enter 0 to exit): "))
    if num == 0:
        break
    new_ride.enqueue(num)
