# Objective: Segment neighborhoods based on various features, evaluate the quality of the clusters, and then predict property prices within each cluster.

## Overall steps (details in Trello)

### Data Collection:

- Gather a dataset of property sales with relevant features (can be scraped in case no API is available.)

### Feature Engineering:

- Extract and process relevant features that influence property prices.

### Neighborhood Clustering with k-means:

- Use the k-means algorithm to cluster neighborhoods based on the average values of the features.
- Determine the optimal number of clusters using methods like the Elbow method.
- Cluster Evaluation using Davies-Bouldin Index:
- After clustering, evaluate the quality of the clusters using the Davies-Bouldin index. This index helps assess the compactness and separation of the clusters. Lower values of the Davies-Bouldin index indicate better clustering.
- If the index suggests poor clustering, consider adjusting the number of clusters or revisiting the features used for clustering.

### Price Prediction within Clusters:
- For each cluster, train a regression model to predict property prices based on the features.
- Validate the model's performance using a test set.

### Visualization:

- Visualize the clusters on a map (if geographical data is available) and represent different clusters with different colors.
- Plot the predicted vs. actual prices for the test set.

### Interpretation:

- Analyze the characteristics of each cluster and the prediction accuracy within each cluster.
- Reflect on the Davies-Bouldin index results and how it might have influenced the quality of the price predictions.

### Tools & Libraries:

- Python
- Pandas for data manipulation
- Scikit-learn for k-means clustering, Davies-Bouldin index evaluation, and regression modeling
- Matplotlib or Seaborn for visualization

## Datasets available on Drive (*temporal solution cause I cannot edit the repo settings*)

[Datasets on Drive](https://drive.google.com/drive/folders/1jSHKgj2lhCqtPCAkrRKxvvovMqEWPDtU?usp=sharing)