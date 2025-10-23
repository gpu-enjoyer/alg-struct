
import random

def get_rand_str(path_to_file):
    with open(path_to_file, encoding="utf-8") as file:
        lines = file.read().splitlines()
    return random.choice(lines)


class Row:

    def __init__(self, passport, snils):

        self.sex = random.choice(["male", "female"])

        if (self.sex == "male"):
            self.name    = get_rand_str("data/male/name.txt")
            self.surname = get_rand_str("data/male/surname.txt")
        else:
            self.name    = get_rand_str("data/fem/name.txt")
            self.surname = get_rand_str("data/fem/surname.txt")

        self.passport = passport
        self.snils    = snils

        # self.doctor_date 
        # self.doctor_next_date
        # self.tests_date
        # self.symp_type
        # self.doctor_type
        # self.tests_type
        # self.tests_price
        # self.card_num


    def __str__(self):
        return f"{self.name} {self.surname}, паспорт: {self.passport}"
    