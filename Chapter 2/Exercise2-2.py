import math

#Exercise 1.
radius=5
volume=4/3*math.pi*radius**3
print("Volume: "+str(volume))

#Exercise 2.
price=24.95*.6*60 #For 60 books
shipping=3+59*.75
print('Total wholesale cost: $%f'%(shipping+price))

#Exercise 3.
easy_pace=8*60+15 #Seconds per mile
tempo=7*60+12  #Seconds per mile
leave_house=6*3600+52*60 #Time in seconds
finish_hour=(leave_house+easy_pace*2+tempo*3)/3600
finish_hour_floored=int(finish_hour)
finish_minute=finish_hour%finish_hour_floored*60
print('Finish hour: %d:%d'%(finish_hour_floored,finish_minute))