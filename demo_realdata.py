# Standard library
import random
import pandas as pd

# Third-party libraries
from matplotlib import pyplot as plt
from matplotlib.cm import Dark2

# Custom modules
from thread_plot import thread_plot



df=pd.read_csv('cluster_ids_jaccard_exp0_k3_simulated_set6_seed1.csv')
print(df.head())

df_clust0=df.loc[df['cluster']==0]
print(len(df_clust0))

choice=list(df_clust0['String'].unique())
choices=''.join(choice)
#print(choices)

choices2=[]

for i in choices:
    if i not in set(choices2):
        choices2.append(i)

choices3=''.join(choices2)
print(choices3)

if __name__ == '__main__':
    choices = choices3
    data = list(df_clust0['String'])

    # We need to make a color choice for each letter in the sequence
    cm = plt.get_cmap('tab20')
    colors = dict([(choices[i], cm(1.*i/len(choices))) for i in range(len(choices))])

    # Make the plot
    fig, ax = plt.subplots(1)
    thread_plot(ax, colors, data)

    # Since we're using patches (rectangles), Matplotlib doesn't know about our legend, so we have
    # to generate some fake data to force the legend to appear properly
    markers = [plt.Line2D([0,0],[0,0],color=color, marker='o', linestyle='') for color in colors.values()]
    plt.legend(markers, colors.keys(), numpoints=1, bbox_to_anchor=(1.05, 1))
    plt.tight_layout()

    plt.show()

