input_value = int(input("enter a value\n"))
while True:
  
  if input_value>=20:
    status = "value is greater than or equal to  20"
    break
  elif input_value>=5:
    status = "the value is greater than 5"
    break
  else:
    print ("your value is not valid")
    input_value = int(input("enter a value again \n"))
  #take the logic out of status out for further logic
print(f'value you have entered is  {input_value} which is{status}')


exit()
value = int(input("enter a value\n"))
while True:
  
  if value>=5:
    print("value is greater than or equal to 5")
    break
  elif value>=30:
    print("the value is greater than 30")
    break
  else:
    print("your value is not valid")
    value = int(input("enter a value again \n"))
exit()