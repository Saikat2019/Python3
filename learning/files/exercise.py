temperatures = [10, -20, -289, 100]
myfile=open("temperatures.txt","w")
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        with open("Ctemp.text","a") as myfil:
            myfil.write(str(f)+"\n")
        return f
t=0.0
for t in temperatures:
    if t > -273.15:
        myfile.write(str(c_to_f(t))+"\n")
myfile.close()
