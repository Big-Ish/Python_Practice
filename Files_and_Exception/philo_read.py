def philo():
    philosophers = open('philosophers.txt', 'r')
    print(philosophers.read())
    philosophers.close()

philo()