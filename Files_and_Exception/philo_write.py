def philo():
    philosophers = open('philosophers.txt', 'w')
    philosophers.write('Aalok Sapkota\n')
    philosophers.write('John Locke\n')
    philosophers.write('Edmund Burke\n')
    philosophers.close()

philo()