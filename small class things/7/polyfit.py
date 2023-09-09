import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Return fitted model parameters to the dataset at datapath for each choice in degrees.
#Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
#Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
#coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []

    #read the input file, assuming it has two columns, where each row is of the form [x y] as in poly.txt.
    data = pd.read_csv(datapath, sep = ' ', header = None)
    X = data[0].tolist()
    Y = data[1].tolist()
    #print(type(X))
    #print(Y)

    #iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    #for the model parameters in each case. Append the result to paramFits each time.
    for n in degrees:
        matrix = feature_matrix(X, n)
        paramFits.append(least_squares(matrix, Y))

    return paramFits


#Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
#samples in x.
#Input: x as a list of the independent variable samples, and d as an integer.
#Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
#for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    #There are several ways to write this function. The most efficient would be a nested list comprehension
    #which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    X = []
    for i in x: 
        temp = []
        for j in range(d, -1, -1):
            temp.append(i**j)
        X.append(temp)
    return X


#Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
#Input: X as a list of features for each sample, and y as a list of target variable samples.
#Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)

    #Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    B = np.linalg.inv(X.T @ X) @ X.T @ y

    return B

if __name__ == '__main__':
    datapath = 'poly.txt'
    #degrees = [2, 4]
    degrees = [1,2,3,4,5]

    paramFits = main(datapath, degrees)
    print(paramFits)

    #graph stuff
    data = pd.read_csv(datapath, sep = ' ', header = None)
    X = data[0].tolist()
    Y = data[1].tolist()
    X.sort()
    Y.sort()

    matrix = feature_matrix(X, 1)
    X1 = np.array(matrix)
    Y1 = X1 @ paramFits[0] # x values * coefs
    matrix = feature_matrix(X, 2)
    X2 = np.array(matrix)
    Y2 = X2 @ paramFits[1]
    matrix = feature_matrix(X, 3)
    X3 = np.array(matrix)
    Y3 = X3 @ paramFits[2]
    matrix = feature_matrix(X, 4)
    X4 = np.array(matrix)
    Y4 = X4 @ paramFits[3]
    matrix = feature_matrix(X, 5)
    X5 = np.array(matrix)
    Y5 = X5 @paramFits[4]

    plt.scatter(X, Y, label='Data Given', color='gray') #original data
    plt.plot(X, Y1, label='Degree 1', color='b') 
    plt.plot(X, Y2, label='Degree 2', color='g') 
    plt.plot(X, Y3, label='Degree 3', color='r') 
    plt.plot(X, Y4, label='Degree 4', color='c') 
    plt.plot(X, Y5, label='Degree 5', color='m') 
    plt.legend()

    plt.show()