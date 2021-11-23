
# Find number of days above average temerature and return average temerature


days = input('How many day"s temerature?') 

temeratures = []
for day in range(1,int(days)+1):
    temp = input(f"Day {day}'s temperature:")
    temeratures.append(int(temp))
    
print(f'Average = {sum(temeratures)/len(temeratures)}')
print(f'{len([x for x in temeratures if x > sum(temeratures)/len(temeratures)])} day(s) above average')