# 0.1 - First Approach to the Data

## Summary
This report contains the initial steps taken to analyze the data. The objective here was to understand the data and start looking for patterns in order to group individuals according to their answers to the survey.

## Data
The dataset contains a little over a million entries of different people who answered 50 personality questions. Each of these questions is identified by its type from the 5 types of personality. And there are 10 questions per type.

Furthermore, the time spent answering each question was recorded as well as the time spent in the landing and finalization page.

Another variable is the IPC which states how many questions were recorder from the user's ip address. When the value is higher than 1, it means multiple submissions were made from the same network. These could be either re-submissions or shared networks such as a university.

# Methods
The approach considered was semi-supervised. Since each individual answered a total of 50 questions and each question is identified by its type (of the 5 types of personality), we decided to summarize each individual by their average score on each of the 5 types of questions. The summarization was performed by taking the mean score of each type of question. From here we only considered the resulting 5 features (mean of **extraversion**, **neuroticism**, **agreeableness**, **conscientiousness** and **openness to experience** questions), leaving out the rest of the features.

Our main purpose is to find clear clusters of individuals, therefore we decided to use a radvis visualization using the 5 customized features as axis, in order to look for patterns. The resulting visualization from fig.1 unfortunately didn't provide any relevant information.

![](../media/participants_avg_qtype_radvis.png)
*Fig. 1: Radvis of all individuals summarized by their mean score on the tests*


Our second approach consisted in attempting K-means in order to find clusters of individuals. The first thing we considered was which K to use. Despite us knowing that there are 5 main personality types, what we are attempting to do is to find clear clusters of individuals in the dataset. Therefore, an unsupervisionized approach to to choose K is the *elbow plot* in fig. 2.

![](../media/Kmeans_elbow_plot_summarized_individuals.png)
*Fig. 2: Elbow plot for choosing optimal K to cluster the dataset (using Within performance metric).*

Despite not there being a correct answer to the usage of these plots, this plot led us to choose K=6. From there we applied Kmeans clustering to the dataset and plotted the clusters in 2D using the dimensionality reduction technique **Principal Component Analysis**.

![](../media/k_6means_summarizedIndividuals.png)
*Fig. 3: Plot of K=6-means using PCA on the summarized individuals by their mean score on each question type*

Fig. 3 Shows us that there are individuals with clear differences due to the distance between them. However, most clusters are ambiguous on their frontiers.


# Conclusions

Most methods used weren't sufficient to find clear patterns in the individuals. One explanation would be that we decided to summarize the individual's information on the predefined personality questions. This decision was, on one hand, biased due to us already knowing what personality type is each question testing the individual for.

# Next Steps

We will follow the unsupervised approach and search for patterns in the individuals from their answers to the questions, without summarizing any of them. While doing this, we will also consider other clustering techniques such as: Mean-shift clustering, DBSCAN, GMM and Agglomerative Hierarchical Clustering.
