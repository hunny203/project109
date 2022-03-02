import imp
import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff

df=pd.read_csv("StudentsPerformance.csv")
math_list=df["math_score"].tolist()

mean_marks=statistics.mean(math_list)
print("mean of marks is: {}".format(mean_marks))

median_marks=statistics.median(math_list)
print("median of marks is: {}".format(median_marks))

mode_marks=statistics.mode(math_list)
print("mode of marks is: {}".format(mode_marks))

std_dev_math=statistics.stdev(math_list)
print("standard deviation for marks is: {}".format(std_dev_math))

first_std_dev_ht_start,first_std_dev_ht_end=mean_marks-std_dev_math,mean_marks+std_dev_math
list_of_data_within_first_std_dev_ht=[result for result in math_list if result>first_std_dev_ht_start and result<first_std_dev_ht_end]
print("{}% of data lies within first standard deviation marks".format(len(list_of_data_within_first_std_dev_ht)*100.0/len(math_list)))

second_std_deviation_ht_start, second_std_deviation_ht_end = mean_marks-(2*std_dev_math), mean_marks+(2*std_dev_math)
list_of_data_within_2_std_deviation_ht = [result for result in math_list if result > second_std_deviation_ht_start and result < second_std_deviation_ht_end] 
print("{}% of data lies within 2 standard deviations marks".format(len(list_of_data_within_2_std_deviation_ht)*100.0/len(math_list)))


third_std_deviation_ht_start, third_std_deviation_ht_end = mean_marks-(3*std_dev_math), mean_marks+(3*std_dev_math)
list_of_data_within_3_std_deviation_ht = [result for result in math_list if result > third_std_deviation_ht_start and result < third_std_deviation_ht_end]
print("{}% of data lies within 3 standard deviations marks".format(len(list_of_data_within_3_std_deviation_ht)*100.0/len(math_list)))

fig=ff.create_distplot([math_list],["Maths"])
fig.show()