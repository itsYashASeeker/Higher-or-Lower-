import random
from replit import clear
from arts import logo_one, logo_two
age={
  'Akshay Kumar':53,
  'Hrithik Roshan':46,
  'Anushka Sharma':32,
  'Aishwarya Rai Bachhan':47,
  'Kriti Sanon':30,
  'Abhishek Bachchan':44,
  'Jackie Shroff':63,
  'John Abraham':42,
  'Anil Kapoor':64,
  'Ranbir Kapoor':38
}
score=0
game_status=True
name=['Akshay Kumar', 'Hrithik Roshan', 'Anushka Sharma', 'Aishwarya Rai Bachhan','Kriti Sanon', 'Abhishek Bachchan', 'Jackie Shroff', 'John Abraham','Anil Kapoor', 'Ranbir Kapoor']
while(game_status==True):
  print(logo_one)
  name_one=random.choice(name)
  print(f"Compare A: {name_one}")
  print(logo_two)
  name_two=random.choice(name)
  while(name_two==name_one):
    name_two=random.choice(name)
  print(f"Against B: {name_two}")
  compare=input("Who is older than the other? 'A' or 'B'?? ").lower() 
  clear() 
  if compare=="a":
    if age[name_one] > age[name_two]:
      score += 1
      print(f"You are right! Your Score: {score}\n*****************************")
      game_status=True
    else:
      print(f"You chose it Wrong!! Your Final Score: {score}")
      game_status=False
  elif compare=="b":
    if age[name_one] < age[name_two]:
      score += 1
      print(f"You chose it Right! Your Score: {score}\n*****************************")
      game_status=True 
    else:
      print(f"You chose it Wrong!! Your Final Score: {score}")
      game_status=False
  else:
    print("Invalid Input!")
    game_status=False          