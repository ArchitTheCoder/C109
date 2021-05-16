from os import stat
import random
import statistics
from numpy import median
import plotly.figure_factory as ff
import pandas as pd
 
df = pd.read_csv("data.csv")
height_list = df["Height(Inches)"].tolist()

mean = statistics.mean(height_list)
median = statistics.median(height_list)
mode = statistics.mode(height_list)
std_dev = statistics.stdev(height_list)

# print("Mean, median, mode, and std_dev of height is {}, {}, {}, {} respectively".format(mean, median, mode, std_dev))
# fig = ff.create_distplot([height_list], ["Result"], show_hist=False)
# fig.show()

height_first_std_dev_start, height_first_std_dev_end = mean - std_dev, mean + std_dev
height_second_std_dev_start, height_second_std_dev_end = mean - (2 * std_dev), mean + (2 * std_dev)
height_third_std_dev_start, height_third_std_dev_end = mean - (3 * std_dev), mean + (3 * std_dev)

height_list_of_data_within_1_stddev = [result for result in height_list if result > height_first_std_dev_start and result < height_first_std_dev_end]
height_list_of_data_within_2_stddev = [result for result in height_list if result > height_second_std_dev_start and result < height_second_std_dev_end]
height_list_of_data_within_3_stddev = [result for result in height_list if result > height_third_std_dev_start and result < height_third_std_dev_end] 

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_stddev)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_stddev)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_stddev)*100.0/len(height_list)))