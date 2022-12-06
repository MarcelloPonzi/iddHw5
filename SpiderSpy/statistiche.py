import math

class Statistiche:

    hit = False
    hit_count = 0
    request_count = 0

    def __init__(self):
        return

    def inc_hit(self):
        self.hit_count = self.hit_count+1

    def inc_request(self):
        self.request_count = self.request_count + 1

    def reset_hit(self):
        self.hit = False

    def hitted(self):
        self.hit = True
        self.inc_hit()

    def print_stats(self):
        print("Numero di richieste: " + str(self.request_count))
        print("Risposte contenenti informazioni: " + str(self.hit_count))
        print("Accuratezza: " + str(math.trunc((self.hit_count/self.request_count)*100)) + "%")
        f = open("statistiche.txt", "w")
        f.write("Numero di richieste: " + str(self.request_count) + "\n" + "Risposte contenenti informazioni: " + str(self.hit_count) + "\n" + "Accuratezza: " + str(math.trunc((self.hit_count/self.request_count)*100)) + "%")
        f.close()


