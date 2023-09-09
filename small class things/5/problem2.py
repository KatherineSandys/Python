#Confidence Intervals
import numpy as np
from scipy.stats import norm
from scipy.stats import t
import math
import stats

#negative is loss and positive is win
data = [3, -3, 3, 15, 15, -16, 14, 21, 30, -24, 32]
size = len(data)

#question 1
confidence_int = 0.90
mean = np.mean(data)
stand_dev = np.std(data, ddof=1) #we know the mean so ddof = 1
stand_error = stand_dev / math.sqrt(size)
average = np.average(data)
t_value = t.ppf(1 - (1 - confidence_int)/2, (size-1))
interval = (mean - (t_value*stand_error), mean + (t_value*stand_error))
print("Question 1 answers:")
print(f"sample mean: {mean}, standard error: {stand_error}")
print(f"standard statistic: {t_value}, interval: {interval}")

#question 2
confidence_int = 0.95 #given
mean = np.mean(data)
stand_dev = np.std(data, ddof=1) #we know the mean so ddof = 0
stand_error = stand_dev / math.sqrt(size)
average = np.average(data)
t_value = t.ppf(1 - (1 - confidence_int)/2, (size-1))
interval = (mean - (t_value*stand_error), mean + (t_value*stand_error))
print("Question 2 answers:")
print(f"sample mean: {mean}, standard error: {stand_error}")
print(f"standard statistic: {t_value}, interval: {interval}")

#question 3- should use z-test instead
confidence_int = 0.95 #given
stand_dev = 16.836 #given 
stand_error = stand_dev / math.sqrt(size)
average = np.average(data)
t_value = t.ppf(1 - (1 - confidence_int)/2, (size-1))
interval = (mean - (t_value*stand_error), mean + (t_value*stand_error))
print("Question 3 answers:")
print(f"sample mean: {mean}, standard error: {stand_error}")
print(f"standard statistic: {t_value}, interval: {interval}")

#question 4: see pdf
