from cluster import *
from point import *

def kmeans(pointdata, clusterdata) :    
    #1. Make list of points using makePointList and pointdata
    list_points = makePointList(pointdata)
    
    #2. Make list of clusters using createClusters and clusterdata
    list_clusters = createClusters(clusterdata)

    #3. As long as points keep moving:
    moving = True
    while moving:
        #A. Move every point to its closest cluster (use Point.closest and
        #   Point.moveToCluster)
        #   Hint: keep track here whether any point changed clusters by
        #         seeing if any moveToCluster call returns "True"
        moving = False
        for p in list_points:
            holder = p.currCluster
            c = p.closest(list_clusters)
            p.moveToCluster(c)
            if holder != p.currCluster:
                moving = True

        #B. Update the centers for each cluster (use Cluster.updateCenter)
        for c in list_clusters:
            c.updateCenter()    

    #4. Return the list of clusters, with the centers in their final positions
    return list_clusters
    
    
    
if __name__ == '__main__' :
    data = np.array([[0.5, 2.5], [0.3, 4.5], [-0.5, 3], [0, 1.2], [10, -5], [11, -4.5], [8, -3]], dtype=float)
    centers = np.array([[0, 0], [1, 1]], dtype=float)
    
    clusters = kmeans(data, centers)
    for c in clusters :
        c.printAllPoints()
