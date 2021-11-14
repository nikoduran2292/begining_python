def run():
   # my_dict = {}

   # for i in range (1, 101):
    #    if i % 3 !=0: 
     #       my_dict[i] = i**3

    #my_dict = {i: i**3 for i in range (1,101) if i % 3 != 0}


    new_dict ={i: round(i**0.5,2) for i in range (1,101)}
    print(new_dict)


if __name__ == "__main__":
    run()