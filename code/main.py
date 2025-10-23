
# import prep_data
import class_row

if __name__ == "__main__":

    rows = []

    for i in range(15):
        rows.append(class_row.Row(i, 10 * i))

    for i in range(15):
        print(rows[i])

    # get_data.parse_surnames(
    #     "../data/male/surname.txt",
    #     "../data/male/surname_tmp.txt",
    #     "../data/fem/surname_tmp.txt"
    # )
