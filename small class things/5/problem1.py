#Hypothesis Testing
import numpy as np
from scipy.stats import norm
from scipy.stats import t
import scipy.stats as stats
import math

myFile = open('engagement_1.txt')
data1 = myFile.readlines()
myFile.close()
data1 = [float(x) for x in data1]

myFile = open('engagement_0.txt')
data0 = myFile.readlines()
myFile.close()
data0 = [float(x) for x in data0]


#p = norm.cdf(z_c) #probability that a value lies below a particular point
#z_c = norm.ppf(p) #find the point `z_c` below which the probability is `p`
#t_c = t.ppf(p) #find the point `t_c` below which the probability is `p`

#question 1: see pdf

#question 2
null = 0.75 #null hypothesis
#data is loaded in above
size = len(data1)
mean = np.mean(data1)
stand_dev = np.std(data1, ddof=1) #we know the mean so ddof = 1
stand_error = stand_dev / math.sqrt(size)
stand_score = (mean - null) / stand_error #z-score
p_value = 2 * stats.norm.cdf(-abs(stand_score))

print(f"Question 2 answers: ")
print(f"size = {size}, mean = {mean},")
print(f"standard error = {stand_error}, standard score= {stand_score},")
print(f"p-value = {p_value}")

#question 3: see pdf
#question 4: see pdf

#question 5
null = 0.75 #null hypothesis
size0 = len(data0)
mean0 = np.mean(data0)
stand_dev0 = np.std(data1, ddof=1) #we know the mean so ddof = 1
size1 = len(data1)
mean1 = np.mean(data1)
stand_dev1 = np.std(data1, ddof=1) #we know the mean so ddof = 1

stand_error = math.sqrt( (stand_dev0 * stand_dev0 / size0) + (stand_dev1 * stand_dev1 / size1))

stand_score0 = (mean0 - null) / stand_error #z-score
p_value0 = 2 * stats.norm.cdf(-abs(stand_score0))
stand_score1 = (mean1 - null) / stand_error #z-score
p_value1 = 2 * stats.norm.cdf(-abs(stand_score1))

print(f"Question 5 answers: ")
print("engagement_0")
print(f"size = {size0}, mean = {mean0},")
print(f"standard error = {stand_error}, standard score= {stand_score0},")
print(f"p-value = {p_value0}")
print("engagement_1")
print(f"size = {size1}, mean = {mean1},")
print(f"standard error = {stand_error}, standard score= {stand_score1},")
print(f"p-value = {p_value1}")