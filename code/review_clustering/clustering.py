from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

def optimize_cluster(k_min, k_max, data):
    # elbow method 이용해서 최적의 k값 찾을 수 있도록
    X = data
    k_range = (k_min, k_max)
    # elbow point를 찾는 이유는 군집수를 늘렸음에도 불구하고
    # 거리 제곱의 합이 크게 줄어들지 않는 지점을 찾기 위함
    # 군집수를 늘렸을 때 군집 내 거리 제곱의 합은 당연히 줄어듬
    # 포인트는 크게 줄어들지 않는 그 순간을 찾는 것
    sum_of_dist = []

    for k in range(k_range):
        kmeans = KMeans(n_cluster=k, random_state=21)
        kmeans.fit(X)
        sum_of_dist.append(kmeans.inertia_)

    plt.figure(figsize=(12, 6))
    plt.plot(k_range, sum_of_dist, 'o')
    plt.plot(k_range, sum_of_dist, '-', alphaa=0.5)
    plt.title("Elbow Point")
    plt.xlable("Number of Clusters")
    plt.ylable("Inertia")
    



def vis_cluster(data, opt_k, x, y):
    # 시각화용 함수

    kmeans = KMeans(n_cluster=opt_k, random_state=21)

    label = kmeans.fit_predict(data)

    plt.figure(figsize=(20, 6))
    sns.scatterplot(data=data, x=x, y=y, hue=label)
