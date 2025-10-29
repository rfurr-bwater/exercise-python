import matplotlib.pyplot as plt

def average(ls):
    '''Returns the average of a list'''
    sum = 0
    for i in ls:
        sum+=i
    return sum/len(ls)

def prop_above(ls):
    '''Returns the proportion of above-average students'''
    avg = average(ls)
    count = 0
    for i in ls:
        if i > avg:
            count+=1
    #return count/len(ls) # Return percentage?
    return count


def median(ls):
    '''Returns the median of a list'''
    ls.sort()
    if len(ls) % 2 == 0:
        upper_idx = int(len(ls)/2)
        lower_idx = upper_idx - 1
        median = (ls[upper_idx] + ls[lower_idx]) / 2
        return median
    else:
        middle_idx = len(ls) // 2
        return ls[middle_idx]

def show_histogram(data,title=None,xlabel=None,ylabel=None,avg=False):
    '''Displays a histogram'''
    plt.hist(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

fname = "StudentExercise.csv"
f = open(fname)
data = []

for line in f:
    nums = line.split(",")
    # Try-catch to bypass issues with blank values that return as '' and the header row
    # Why haven't you taught us how to use the csv module yet Dr. O'Neil?
    try:
        data.append(float(nums[0]))
    except ValueError:
        pass

show_histogram(data,"Exercise Hours Per Student","Hours","Students")