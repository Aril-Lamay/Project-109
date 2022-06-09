import csv
import plotly.figure_factory as pff
import plotly.graph_objects as go
import pandas as pd
import statistics

df = pd.read_csv("Project-109/StudentsPerformance.csv")

math_score = df["math score"].tolist()
read_score = df["reading score"].tolist()
write_score = df["writing score"].tolist()

#Analyzing For Maths Scores
math_mean = statistics.mean(math_score)
math_median = statistics.median(math_score)
math_mode = statistics.mode(math_score)
math_sd = statistics.stdev(math_score)

print("For Maths -")
print("Mean for Maths : "+str(math_mean))
print("Median for Maths : "+str(math_median))
print("Mode for Maths : "+str(math_mode))
print("Standard Deviation for Maths : "+str(math_sd))

math_1_sd_start,math_1_sd_end = math_mean - math_sd,math_mean + math_sd

data_1_sd_deviation = [result for result in math_score if result > math_1_sd_start and result < math_1_sd_end]
percent_for_1_sd = (len(data_1_sd_deviation)*100/len(math_score))
print(str(percent_for_1_sd)+ "% of data lies within 1 standard deviation")

math_2_sd_start,math_2_sd_end = math_mean - (2*math_sd),math_mean + (2*math_sd)

data_2_sd_deviation = [result for result in math_score if result > math_2_sd_start and result < math_2_sd_end]
percent_for_2_sd = (len(data_2_sd_deviation)*100/len(math_score))
print(str(percent_for_2_sd)+ "% of data lies within 2 standard deviation")

math_3_sd_start,math_3_sd_end = math_mean - (3*math_sd),math_mean + (3*math_sd)

data_3_sd_deviation = [result for result in math_score if result > math_3_sd_start and result < math_3_sd_end]
percent_for_3_sd = (len(data_3_sd_deviation)*100/len(math_score))
print(str(percent_for_3_sd)+ "% of data lies within 3 standard deviation")
print()

figure = pff.create_distplot([math_score],["Maths Score"],show_hist= False)
figure.add_trace(go.Scatter(x=[math_mean,math_mean],y=[0,0.05],mode="lines",name="Mean"))
figure.add_trace(go.Scatter(x=[math_1_sd_start,math_1_sd_start], y=[0,0.05],mode="lines", name="Standard Deviation 1"))
figure.add_trace(go.Scatter(x=[math_2_sd_start,math_2_sd_start], y=[0,0.05],mode="lines", name="Standard Deviation 2"))
figure.add_trace(go.Scatter(x=[math_3_sd_start,math_3_sd_start], y=[0,0.05],mode="lines", name="Standard Deviation 3"))
figure.show()


#Analyzing for Reading score

read_mean = statistics.mean(read_score)
read_median = statistics.median(read_score)
read_mode = statistics.mode(read_score)
read_sd = statistics.stdev(read_score)

print("For Reading -")
print("Mean for Reading : "+str(read_mean))
print("Median for Reading : "+str(read_median))
print("Mode for Reading : "+str(read_mode))
print("Standard Deviation for Reading : "+str(read_sd))

read_1_sd_start,read_1_sd_end = read_mean - read_sd,read_mean + read_sd

data_1_sd_deviation = [result for result in read_score if result > read_1_sd_start and result < read_1_sd_end]
percent_for_1_sd = (len(data_1_sd_deviation)*100/len(read_score))
print(str(percent_for_1_sd)+ "% of data lies within 1 standard deviation")

read_2_sd_start,read_2_sd_end = read_mean - (2*read_sd),read_mean + (2*read_sd)

data_2_sd_deviation = [result for result in read_score if result > read_2_sd_start and result < read_2_sd_end]
percent_for_2_sd = (len(data_2_sd_deviation)*100/len(read_score))
print(str(percent_for_2_sd)+ "% of data lies within 2 standard deviation")

read_3_sd_start,read_3_sd_end = read_mean - (3*read_sd),read_mean + (3*read_sd)

data_3_sd_deviation = [result for result in read_score if result > read_3_sd_start and result < read_3_sd_end]
percent_for_3_sd = (len(data_3_sd_deviation)*100/len(read_score))
print(str(percent_for_3_sd)+ "% of data lies within 3 standard deviation")
print()

figure = pff.create_distplot([read_score],["Reading Score"],show_hist= False)
figure.add_trace(go.Scatter(x=[read_mean,read_mean],y=[0,0.03],mode="lines",name="Mean"))
figure.add_trace(go.Scatter(x=[read_1_sd_start,read_1_sd_start], y=[0,0.03],mode="lines", name="Standard Deviation 1"))
figure.add_trace(go.Scatter(x=[read_2_sd_start,read_2_sd_start], y=[0,0.03],mode="lines", name="Standard Deviation 2"))
figure.add_trace(go.Scatter(x=[read_3_sd_start,read_3_sd_start], y=[0,0.03],mode="lines", name="Standard Deviation 3"))
figure.show()

#Analyzing for writing
write_mean = statistics.mean(write_score)
write_median = statistics.median(write_score)
write_mode = statistics.mode(write_score)
write_sd = statistics.stdev(write_score)

print("For Writing -")
print("Mean for Writing : "+str(write_mean))
print("Median for Writing : "+str(write_median))
print("Mode for Writing : "+str(write_mode))
print("Standard Deviation for writes : "+str(write_sd))

write_1_sd_start,write_1_sd_end = write_mean - write_sd,write_mean + write_sd

data_1_sd_deviation = [result for result in write_score if result > write_1_sd_start and result < write_1_sd_end]
percent_for_1_sd = (len(data_1_sd_deviation)*100/len(write_score))
print(str(percent_for_1_sd)+ "% of data lies within 1 standard deviation")

write_2_sd_start,write_2_sd_end = write_mean - (2*write_sd),write_mean + (2*write_sd)

data_2_sd_deviation = [result for result in write_score if result > write_2_sd_start and result < write_2_sd_end]
percent_for_2_sd = (len(data_2_sd_deviation)*100/len(write_score))
print(str(percent_for_2_sd)+ "% of data lies within 2 standard deviation")

write_3_sd_start,write_3_sd_end = write_mean - (3*write_sd),write_mean + (3*write_sd)

data_3_sd_deviation = [result for result in write_score if result > write_3_sd_start and result < write_3_sd_end]
percent_for_3_sd = (len(data_3_sd_deviation)*100/len(write_score))
print(str(percent_for_3_sd)+ "% of data lies within 3 standard deviation")

figure = pff.create_distplot([write_score],["Writing Score"],show_hist= False)
figure.add_trace(go.Scatter(x=[write_mean,write_mean],y=[0,0.03],mode="lines",name="Mean"))
figure.add_trace(go.Scatter(x=[write_1_sd_start,write_1_sd_start], y=[0,0.03],mode="lines", name="Standard Deviation 1"))
figure.add_trace(go.Scatter(x=[write_2_sd_start,write_2_sd_start], y=[0,0.03],mode="lines", name="Standard Deviation 2"))
figure.add_trace(go.Scatter(x=[write_3_sd_start,write_3_sd_start], y=[0,0.03],mode="lines", name="Standard Deviation 3"))
figure.show()