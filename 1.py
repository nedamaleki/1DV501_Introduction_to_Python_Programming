import matplotlib.pyplot as plt
import math

# x = 0.25, 0.5, 0.75, ... , 10.0
x = [n/4 for n in range(0,40)]
y1 = [math.sin(i) for i in x]
y2 = [math.cos(i) for i in x]
plt.plot(x, y1,'ro') # Plot 1
plt.plot(x, y2, 'b+') # Plot 2
plt.title('Sinus and cosinus')
plt.xlabel('x in range 0 to 10')
plt.ylabel('sin(x) as red, cos(x) as blue')
plt.show() # Display plot