from os import stat
import random
import statistics
from numpy import median
import plotly.figure_factory as ff
import pandas as pd
 
df = pd.read_csv("data.csv")
weight_list = df["Weight(Pounds)"].tolist()

mean = statistics.mean(weight_list)
median = statistics.median(weight_list)
mode = statistics.mode(weight_list)
std_dev = statistics.stdev(weight_list)

# print("Mean, median, mode, and std_dev of weight is {}, {}, {}, {} respectively".format(mean, median, mode, std_dev))
# fig = ff.create_distplot([weight_list], ["Result"], show_hist=False)
# fig.show()

weight_first_std_dev_start, weight_first_std_dev_end = mean - std_dev, mean + std_dev
weight_second_std_dev_start, weight_second_std_dev_end = mean - (2 * std_dev), mean + (2 * std_dev)
weight_third_std_dev_start, weight_third_std_dev_end = mean - (3 * std_dev), mean + (3 * std_dev)

weight_list_of_data_within_1_stddev = [result for result in weight_list if result > weight_first_std_dev_start and result < weight_first_std_dev_end]
weight_list_of_data_within_2_stddev = [result for result in weight_list if result > weight_second_std_dev_start and result < weight_second_std_dev_end]
weight_list_of_data_within_3_stddev = [result for result in weight_list if result > weight_third_std_dev_start and result < weight_third_std_dev_end] 

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_stddev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_stddev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_stddev)*100.0/len(weight_list)))