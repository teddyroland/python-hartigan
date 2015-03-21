from sklearn.cluster import KMeans
from numpy import array

def hartigan_K(list_of_tuples, threshold = 12):
    # 'list_of_tuples' is a list containing the points you want to cluster
    # 'threshold' optimizes goodness of fit values
    #     Hartigan recommends setting threshold to 10, but Chiang & Mirkin confirm up to 12
    # returns integer, "correct" number of clusters
    
    inertia_list = zeros(len(list_of_tuples)+1) # initializes for maximum possible clusters
    num = 0                                     # counter
    H_Rule = threshold+1                        # simply initializes above threshold to meet 'while' condition
    
    # NOTE: 'inertia' is equivalent to the sum of within-cluster distances to centroids
    
    while num < len(list_of_tuples) and H_Rule > threshold:
        kmn = KMeans(n_clusters = num+1)
        kmn.fit(list_of_tuples)
        inertia_list[num+1]+=kmn.inertia_
        if num > 0:
            H_Rule = ((float(inertia_list[num])/inertia_list[num+1])-1)*(len(list_of_tuples)-(num)-1)
        num+=1
    
    if H_Rule > threshold:
      num+=1
    # NOTE: if while-loop reaches the number of K-Means clusters equal to the length of list_of_tuples
    # without hitting the threshold, then function returns trivial solution that there are N clusters
    # (where N is the number of points under observation)
    
    return num-1
