weather = (1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0)
rainy= 0
sunny= 0
for i in weather:
    if i == 1:
        rainy=rainy+1
    else:
        sunny=sunny+1
print("Chance of rain:  ",rainy)
print("Chance of heat:  ",sunny)
if rainy<sunny:
    print("Hot weather today")
elif rainy==sunny:
    print("Moderate weather today")
else:
    print("Rainy weather today")
    