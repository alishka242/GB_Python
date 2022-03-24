from checker_error import CheckVal, MyErrIsInt

if __name__ == "__main__":

    user_list = []
    stop_word = 'stop'
    user_val = input('Введите число: ')

    while user_val != stop_word:        
        try:
            new_val = CheckVal.is_int(user_val) 
            user_list.append(new_val)
        except MyErrIsInt as er:
            print(er)

        user_val = input('Введите число: ')
    print(user_list)