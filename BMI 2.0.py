#Taking the input in the below lines
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


a = round(weight/(height*height))
if a<18.5:
    print(f"Your BMI is {a}, you are underweight.")
elif 18.5<a<25:
    print(f"Your BMI is {a}, you have a normal weight.")
elif 25<a<30:
    print(f"Your BMI is {a}, you are slightly overweight.")
elif 30<a<35:
    print(f"Your BMI is {a}, you are obese.")
elif 35<a:
    print(f"Your BMI is {a}, you are clinically obese.")
else
    print(f"Your BMI IS {a}, you are clinically obese.")
