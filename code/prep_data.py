
def parse_surnames(
    male_surname_txt,
    male_surname_tmp_txt,
     fem_surname_tmp_txt):

    with open(male_surname_txt,     "r", encoding="utf-8") as file_in,  \
         open(male_surname_tmp_txt, "w", encoding="utf-8") as file_male_out, \
         open( fem_surname_tmp_txt, "w", encoding="utf-8") as file_fem_out:

        for surname in file_in:

            surname = surname.strip()

            if surname.endswith(("ов", "ев", "ин")):
                file_fem_out.write(surname + "а\n")

            else:
                file_male_out.write(surname + "\n")