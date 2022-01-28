def convert_time(duration: int) -> str:
    one_min_to_sec = 60
    one_hour_to_min = one_min_to_sec * one_min_to_sec
    one_day_to_hour = one_hour_to_min * 24
    one_week_to_days = one_day_to_hour * 7
    sec_name = ' сек '
    min_name = ' мин '
    hour_name = ' ч '
    day_name = ' дн '

    if (duration < one_min_to_sec): #Секунды
        return str(duration) + sec_name
    elif(duration < one_hour_to_min): #Минуты
        if (duration == one_min_to_sec):
            return str(1) + min_name
        else:
            sec = duration % one_min_to_sec
            min = duration // one_min_to_sec
            return str(min) + min_name + str(sec) + sec_name
    elif(duration < one_day_to_hour): #Часы 
        if (duration == one_hour_to_min):
            return str(1) + hour_name
        else:
            hour = duration // one_hour_to_min 
            min = (duration - hour * one_hour_to_min) // one_min_to_sec
            sec = duration % one_min_to_sec

            return str(hour) + hour_name + str(min) + min_name + str(sec) + sec_name
        sec = duration % 60
        min = duration // 60
        hour = min
        return str(min) + ' min ' + str(sec) + ' sec'
    elif (duration < one_week_to_days):  #Дни
        if (duration == one_day_to_hour):
            return str(1) + day_name
        else:
            days = duration // one_day_to_hour
            hour = (duration - days * one_day_to_hour) // one_hour_to_min
            min = (duration - days * one_day_to_hour - hour * one_hour_to_min) // one_min_to_sec
            sec = duration % one_min_to_sec
            
            return str(days) + day_name + str(hour) + hour_name + str(min) + min_name + str(sec) + sec_name
    else: 
        return 'На недели, месяца, года и века не договаривались!'

duration = 765865
result = convert_time(duration)
print(result)