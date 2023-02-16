def philo():
    philosophers = open('philosophers.txt', 'r')
    # print(philosophers.readline())
    # print(philosophers.readline())
    # print(philosophers.readline())
    
    line1 = philosophers.readline()
    line2 = philosophers.readline()
    line3 = philosophers.readline()
    
    print(line1)
    print(line2)
    print(line3)
    philosophers.close()

philo()