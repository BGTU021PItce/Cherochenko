x=int(input("Введите кол-во секунд: "))
hour=int(x/3600)
min=int((x-hour*3600)/60)
sec=int(x-hour*3600-min*60)
print(hour,"часов +",min,"минут +",sec,"секунд")
