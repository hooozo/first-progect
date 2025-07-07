#take seconds from the user
user_input = int(input('Enter the duration in seconds:'))
#convert
hour = 3600
t =  user_input//hour
print('the duration is:',t,'hour',user_input//60,'minutes and',user_input%60)
#print hours,minutes,and seconds.