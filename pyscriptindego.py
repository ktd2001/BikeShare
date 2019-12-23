#!/home/ktd2001/anaconda3/bin/python

# Keiana Dunn
# Indego Bike Data Visualization Project

# Following code will take data files and create a 12 png files. 
 
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import csv

# Make empty lists
filenames = []
plotnames = []
# Loop over 12 filenames
for i in range(12):
    filenames.append('file'+str(i+1)+'.dat')
    plotnames.append('file'+str(i+1)+'.png')
    print(filenames[i])
    print(plotnames[i])

j = 0    
# Loop over filenames 
for i in filenames:
# Make empty lists for starts and ends data
    x_start = [] 
    y_start = []
    x_end = []
    y_end = []
    
# Open and read csv files
    with open(i) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
           print(row)
           xstart = float(row[0])   # Read start lat/lon rows
           ystart = float(row[1])
           xend = float(row[2])     # Read end lat/lon rows
           yend = float(row[3]) 
           x_start.append(xstart)   # Append start data with other start data files
           y_start.append(ystart)
           x_end.append(xend)       # Append end data with other end data files
           y_end.append(yend)
    
# Make a np.array list for x and y    
    x = np.array(x_start+x_end)
    y = np.array(y_start+y_end)

# Get the coordinates of the min and max for x and y    
    xmin = x.min()
    xmax = x.max()
    ymin = y.min()
    ymax = y.max()

# Make the plot with size and color 
    plt.hexbin(x, y, gridsize=(25,25), cmap=plt.cm.hot)
    plt.colorbar()
    # Add labels, title, and display the plot
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Bike #4051 Location')
    plt.tight_layout()
    txt= "Bike #4051 tracked from Jan 1 - Dec 31, 2017"
    plt.figtext(0.5, 0.01, txt, wrap= True, horizontalalignment='center', fontsize=12)
    
    # Save images in file
    plt.savefig(plotnames[j])
    j=j+1
    plt.close()


