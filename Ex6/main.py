import math
import pandas as pd
import numpy as np

point = [1, 0, 0, '?']
data1 = [1, 1, 1, 'M']
data2 = [1, 3, 0, 'F']

# The code that I add is here:
tag1 = data1[-1]
data1.pop()
tag2 = data2[-1]
data2.pop()

print("The vector", data1, "has tag", tag1)
print("The vector", data2, "has tag", tag2)
# end of the code I add in this section


"""The different distance algorithm"""
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        # print ('x is ' , x)
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += pow(num1 - num2, 2)
    return math.sqrt(distance)


# Hamming distance
from scipy.spatial import distance


def manhattan_dist(point, instance):
    sum = 0
    for i in range(3):
        sum += abs(float(point[i]) - float(instance[i]))
    return sum


# The code that I add is here:
point.pop()
distance1 = euclideanDistance(data1, point, 3)
distance2 = euclideanDistance(data2, point, 3)
if distance1 < distance2:
    print("The distance between", point, "and", data1, "is", distance1, "and the label is", tag1)
else:
    print("The distance between", point, "and", data2, "is", distance2, "and the label is", tag2)
# end of the code I add in this section


url = 'https://github.com/rosenfa/ai/blob/master/myFile.csv?raw=true'
df = pd.read_csv(url, header=0, error_bad_lines=False)
# put data in dataset without header line
dataset = np.array(df)

# The code that I add is here:
vector1 = dataset[0]
vector2 = dataset[1]
print("The first vector is", vector1, "and the second vector is", vector2)
vector1 = vector1.tolist()
vector1.pop()
vector2 = vector2.tolist()
vector2.pop()
distance = euclideanDistance(vector1, vector2, 3)
print("The distance of the 2 first vectors is", distance)
# end of the code I add in this section


class distClass:
    dist = -1  # distance of current point from test point
    tag = '-'  # tag of current point


def take_the_label(distance_func, k):
    arr_labels = []
    for i in range(k):
        arr_labels.append(distance_func[i].tag)

    labels_m = arr_labels.count('M')
    labels_f = arr_labels.count('F')
    if labels_m > labels_f:
        return 'M'
    else:
        return 'F'


"""knn algo of the different algorithm"""
def euclidan_algo(dataset, point):
    eucDistances = []  # list of distances, will hold objects of type distClass
    for i in range(len(dataset)):
        # print("type", type(i))
        # print("i", i)
        temp = dataset[i]
        label = temp[-1]
        d = euclideanDistance(point, temp, len(point)-1)
        # print("The distances between " + str(point) + " and " + str(temp) + " is " + str(d))
        # print(" and the label is " + label)
        obj = distClass()
        obj.dist = d
        obj.tag = label
        eucDistances.append(obj)

    eucDistances.sort(key=lambda x: x.dist)
    return eucDistances


p = [0, 0, 100]
euc_distances = euclidan_algo(dataset, p)
label_euclidean_k_1 = take_the_label(euc_distances, 1)
label_euclidean_k_3 = take_the_label(euc_distances, 3)
print("The label for point (with euclidean) if k=1 is", label_euclidean_k_1)
print("The label for point (with euclidean) if k=3 is", label_euclidean_k_3)

# Question 3: The result would be different if we use a different distance function.


def hamming_algo(dataset, point):
    hamming_distance = []

    for i in range(len(dataset)):
        temp = dataset[i]
        label = temp[-1]
        temp = temp.tolist()
        temp.pop()
        d = distance.hamming(point, temp)
        # print("The distances between " + str(point) + " and " + str(temp) + " is " + str(d))
        # print(" and the label is " + label)
        obj = distClass()
        obj.dist = d
        obj.tag = label
        hamming_distance.append(obj)

    hamming_distance.sort(key=lambda x: x.dist)
    return hamming_distance


hamming_dist = hamming_algo(dataset, point)
label_hamming_k_1 = take_the_label(hamming_dist, 1)
label_hamming_k_3 = take_the_label(hamming_dist, 3)
print("The label for point (with hamming) if k=1 is", label_hamming_k_1)
print("The label for point (with hamming) if k=3 is", label_hamming_k_3)


def manhattan_algo(dataset, point):
    manhattan_distance = []

    for i in range(len(dataset)):
        temp = dataset[i]
        label = temp[-1]
        temp = temp.tolist()
        temp.pop()
        d = manhattan_dist(point, temp)
        # print("The distances between " + str(point) + " and " + str(temp) + " is " + str(d))
        # print(" and the label is " + label)
        obj = distClass()
        obj.dist = d
        obj.tag = label
        manhattan_distance.append(obj)

    manhattan_distance.sort(key=lambda x: x.dist)
    return manhattan_distance


manh_distance = manhattan_algo(dataset, point)
label_manhattan_k_1 = take_the_label(manh_distance, 1)
label_manhattan_k_3 = take_the_label(manh_distance, 3)
print("The label for point (with manhattan) if k=1 is", label_manhattan_k_1)
print("The label for point (with manhattan) if k=3 is", label_manhattan_k_3)


url = 'https://github.com/rosenfa/ai/blob/master/mytrain.csv?raw=true'
train_data = np.array(pd.read_csv(url, header=0, error_bad_lines=False))
url = 'https://github.com/rosenfa/ai/blob/master/mytest.csv?raw=true'
test_data = np.array(pd.read_csv(url, header=0, error_bad_lines=False))

# print(train_data.shape)  # number of records and features
# print(train_data)
#
#
# print(test_data.shape)  # number of records and features
# print(test_data)

for i in test_data:
    # euclidean:
    euc_d = euclidan_algo(train_data, i)
    label_euclidean_k_1 = take_the_label(euc_d, 1)
    label_euclidean_k_7 = take_the_label(euc_d, 7)
    label_euclidean_k_15 = take_the_label(euc_d, 15)
    print("The label for point", i, "(with euclidean) if k=1 is", label_euclidean_k_1)
    print("The label for point", i, "(with euclidean) if k=7 is", label_euclidean_k_7)
    print("The label for point", i, "(with euclidean) if k=15 is", label_euclidean_k_15)

    # hamming:
    i = i.tolist()
    i.pop()
    ham_d = hamming_algo(train_data, i)
    label_hamming_k_1 = take_the_label(ham_d, 1)
    label_hamming_k_7 = take_the_label(ham_d, 7)
    label_hamming_k_15 = take_the_label(ham_d, 15)
    print("The label for point", i, "(with hamming) if k=1 is", label_hamming_k_1)
    print("The label for point", i, "(with hamming) if k=7 is", label_hamming_k_7)
    print("The label for point", i, "(with hamming) if k=15 is", label_hamming_k_15)

    # manhattan
    i.pop()
    man_d = manhattan_algo(train_data, i)
    label_manhattan_k_1 = take_the_label(man_d, 1)
    label_manhattan_k_3 = take_the_label(man_d, 7)
    label_manhattan_k_15 = take_the_label(man_d, 15)
    print("The label for point", i, "(with manhattan) if k=1 is", label_manhattan_k_1)
    print("The label for point", i, "(with manhattan) if k=7 is", label_manhattan_k_3)
    print("The label for point", i, "(with manhattan) if k=15 is", label_manhattan_k_15)


