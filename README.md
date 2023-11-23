# Project: Segment properties based on various features, evaluate the quality of the clusters, and then predict property prices within each cluster.

### Data Collection:
- Scrape a dataset of property sales with relevant features 

### Feature Engineering:
- Extract and process relevant features that influence property prices.

### Neighborhood Clustering with k-means:
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

data: Contains all datasets used datasets
- converted_data: Contains data that has been converted from json to csv
- processed_data: Contains data that has undergone processing steps such as cleaning, merging, or transformation.
- raw_data: Contains the initial, scraped datasets in json format.
notebooks: Contains Jupyter notebooks used for interactive computing and data analysis.
- dataExploration.ipynb: A notebook used for exploring and understanding the data.
- kMeans.ipynb: A notebook for running the k-Means clustering algorithm.
- machineLearning.ipynb: A notebook for running the machine learning algorithm.
plots: This folder contains visualizations generated from the data.
src: Source directory for the project’s Python scripts.
- preprocessing: Contains scripts for data preprocessing.
-- dataCleaning.py: Script for cleaning data
-- featureEngineering.py: Script for feature engineering tasks.
scraping: Contains scripts related to the web scraping
requirements.txt: Contains a list of Python packages required for the project.