#Victor-Foscarini

#plots básicos

from matplotlib import pyplot as plt
import random


class Plots:
	def __init__ (self):
		self.variavel = 0
		
	def simple(self):
		years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
		gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
		
		#create a line chart, years on x axis, gdp on y-axis
		plt.plot(years,gdp,color='red',marker='o', linestyle='solid')
		
		#add a title
		plt.title('Nominal GDP')
		
		#add a label to the y-axis
		plt.ylabel('Billions of $')
		plt.show()
	
	def barcharts(self):
		movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
		num_oscars = [5, 11, 3, 8, 10]
		# plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
		plt.bar(range(len(movies)), num_oscars)
		plt.title("My Favorite Movies") # add a title
		plt.ylabel("# of Academy Awards") # label the y-axis
		# label x-axis with movie names at bar centers
		plt.xticks(range(len(movies)), movies)
		plt.show()
		
class Files:
	def __init__(self):
		self.variavel = 0
	
	def basics(self):		
		#file_for_reading = open("reading.txt",'r')
		file_for_writting = open('writing.txt','w')
		#file_for_appending = open('appending.txt','a')	
		
		for i in range(0,100):
			file_for_writting.write(str(random.randint(1,10))+'\n')
			
	def readplot(self):
		file = open('writing.txt')
		data = file.readlines()
		for line in data:
			line = float(line.replace(',','.'))
		data = sorted(data,key=float)
		#plot as a graphic
		plt.plot(data,[x for x in range(len(data))],color='blue',marker='o',linestyle='solid')
		plt.title('RandomNumbers')
		plt.ylabel('Random')
		plt.xlabel('Order')
		plt.show()
		#plot as a hystogram
		plt.hist(data,bins='auto',color='black',rwidth=0.9)
		plt.show()
		
txt = Files()
txt.basics()
txt.readplot()
