# 0.1 - First Approach to the Data

## Summary
This report contains the initial steps taken to analyze the data. The objective here was to understand the data and start looking for patterns in order to group individuals according to their answers to the survey.

## Data
The dataset contains a little over a million entries of different people who answered 50 personality questions. Each of these questions is identified by its type from the 5 types of personality. And there are 10 questions per type.

Furthermore, the time spent answering each question was recorded as well as the time spent in the landing and finalization page.

Another variable is the IPC which states how many questions were recorder from the user's ip address. When the value is higher than 1, it means multiple submissions were made from the same network. These could be either re-submissions or shared networks such as a university.

# Methods
The approach considered was semi-supervised. Each individual answered a total of 50 questions. Each question is identified by its type such as if it is an **extraversion** type question or any of the other 5 personalities.
