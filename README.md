# Project: Segment properties based on various features, evaluate the quality of the clusters, and then predict property prices within each cluster.

### Data Collection:
- Scrape a dataset of property sales with relevant features 

### Feature Engineering:
- Extract and process relevant features that influence property prices.

### Clustering with k-means:
- Use the k-means algorithm to cluster properties based on the average values of the features.
- Determine the optimal number of clusters using methods like the Elbow method.
- Cluster Evaluation using Davies-Bouldin Index:
- After clustering, evaluate the quality of the clusters using the Davies-Bouldin index. This index helps assess the compactness and separation of the clusters. Lower values of the Davies-Bouldin index indicate better clustering.
- If the index suggests poor clustering, consider adjusting the number of clusters or revisiting the features used for clustering.

### Price Prediction within Clusters:
- Train a regression model to predict property prices based on the features.
- Validate the model's performance using a test set.

### Visualization:
- Visualize the clusters on a map (if geographical data is available) and represent different clusters with different colors.
- Visualize prediction

### Tools & Libraries:
- Python
- Pandas for data manipulation
- Scikit-learn for k-means clustering, Davies-Bouldin index evaluation, and regression modeling
- Matplotlib or Seaborn for visualization

# Folder structure

Empty