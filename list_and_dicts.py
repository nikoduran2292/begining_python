def run():
    my_list = [1,"hello", True, 4.5]
    my_dict = {"firstname":"camilo","lastname":"Gomez"}

    super_list = [
        {"firstname":"camilo","lastname":"Gomez"},
        {"firstname":"miguel","lastname":"roa"},
        {"firstname":"laura","lastname":"rodriguez"},
        {"firstname":"facundo","lastname":"garcia"},
        {"firstname":"maria","lastname":"paez"},
    ]

    super_dict = {
        "natural_numbs": [1,2,3,4,5],
        "integer_numbs": [-1,-2,0,1,2],
        "floating_nums": [1.1,2.1,4.5,6.43],
    }

    #for key, value in super_dict.items():
        #print(key, "-", value)
    for values in super_list:
        for key, values in values.items():
            print(values)


if __name__ == "__main__":
    run()