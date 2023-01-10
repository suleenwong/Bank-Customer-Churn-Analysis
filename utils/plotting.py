import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

# Function for formatting subplots
def plot_subplots(ax, fontsize, xlabel_text, title_text, legend=True):
    """Format subplots

    Args:
        ax (object): axis object
        fontsize (int): font size for axis labels 
        xlabel_text (str): x-label text
        title_text (str): title test 
        legend (bool, optional): Flag for legend. Defaults to True.
    """
    plt.xticks(fontsize=fontsize-1)
    plt.yticks(fontsize=fontsize-1)
    plt.xlabel(xlabel_text, fontsize=fontsize)
    plt.ylabel('Percent of customers [%]', fontsize=fontsize)
    plt.title(title_text)
    if legend == True:
        legend_labels, _= ax.get_legend_handles_labels()
        ax.legend(legend_labels, ['Retained','Churned'], fontsize=fontsize)
    else:
        plt.legend([],[], frameon=False)


# Function to plot confusion matrix
def plot_confusion_matrix(cm, classes,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    """
    #cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    sns.set_style('white')
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), 
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
        plt.text(j, i+0.1, "("+format(cm_norm[i, j], '.2f')+")", 
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    