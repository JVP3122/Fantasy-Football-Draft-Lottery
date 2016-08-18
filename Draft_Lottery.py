import os, sys, random, csv
os.system('cls')  # on windows

## Range function that can take floats
def frange(n, x, y):
  if n > x and n <= y:
    return True
  else:
    return False

## Import team names, standings, lottery percentages
with open('Monkeys with Crayons Results.csv',newline = '') as inputfile:
    results = list(csv.reader(inputfile,delimiter = ','))

## Unzip results and create numeric lists
place_list,team_list,odds_list,lottery_list = zip(*results)
place_list = list(place_list)
team_list = list(team_list)
odds_list = list(odds_list)
lottery_list = list(lottery_list)
place_list = [float(i) for i in place_list]
odds_list = [float(i) for i in odds_list]
lottery_list = [float(i) for i in lottery_list]
odds_list = [1000 * i for i in odds_list]
lottery_list = [1000 * i for i in lottery_list]
lottery_list.insert(0,0)

## Create list to track whether someone has already come up in "random" number generation
result_list = []
for i in range(len(team_list)):
  result_list.append(False)

print("Lottery Result".center(20), "Team Name".center(30))
print()
print()
temp_val = sum(odds_list)
for j in range(len(odds_list)):
  odds_list[j] = round(1000 * odds_list[j]/temp_val)/10
print("Lottery Position".center(20), "Team Name".center(30), "Prob of Next Pick".center(20))
for i in reversed(range(len(team_list))):
  odds_temp_var = str(odds_list[i])+" %"
  print(str(len(team_list)-i).center(20),team_list[i].center(30),odds_temp_var.center(20))
print()
print()


## Random number generated results
final_list = []
iter_count = 0
while result_list.count(False) > 0 and iter_count < 1000:
  odds_list_temp = []
  team_list_temp = []
  place_list_temp = []
  x = random.randrange(1,1001)
  for i in range(len(team_list)):
    if frange(x,lottery_list[i],lottery_list[i+1]) and result_list[i] == False:
      final_list.append(team_list[i])
      result_list[i] = True
      for k in range(len(result_list)):
        if result_list[k] == False:
          team_list_temp.append(team_list[k])
          odds_list_temp.append(odds_list[k])
        else:
          continue
      temp_val = sum(odds_list_temp)
      for j in range(len(odds_list_temp)):
        odds_list_temp[j] = round(1000 * odds_list_temp[j]/temp_val)/10
      input("Press <ENTER> to continue")
      os.system('cls')  # on windows
      print("Lottery Result".center(20), "Team Name".center(30))
      for i in range(len(final_list)):
        print(str(i+1).center(20),final_list[i].center(30))
      print()
      print()
      if i != len(team_list)-1:
        print("Lottery Position".center(20), "Team Name".center(30), "Prob of Next Pick".center(20))
      for i in reversed(range(len(team_list_temp))):
        odds_temp_var = str(odds_list_temp[i])+" %"
        print(str(len(team_list_temp)-i).center(20),team_list_temp[i].center(30),odds_temp_var.center(20))
    else:
      continue
    print()
    print()
  iter_count += 1
