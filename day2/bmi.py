weight = float(input("enter weight in kg"))
height = float(input("enter height in m"))

bmi = weight / (height * height * height)

if bmi <= 18.5:
    print("bmi is underweighted")
elif 18.5 < bmi <= 25:
    print (" bmi is perfect")
else :
    print("bmi is overweights")