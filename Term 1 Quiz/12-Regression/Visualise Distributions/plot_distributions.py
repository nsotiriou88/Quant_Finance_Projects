"""Visualize the distribution of different samples.

Many variables tend to follow a Normal distribution (hence the name
“Normal”), both in nature as well as artificial contexts. But there
are other distributions as well, some that are variants of the
Normal distribution, and some that are completely different! Each
distribution is suitable for modeling certain kinds of variables.
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram(sample, title, bins=16, **kwargs):
    """Plot the histogram of a given sample of random values.

    Parameters
    ----------
    sample : pandas.Series
        raw values to build histogram
    title : str
        plot title/header
    bins : int
        number of bins in the histogram
    kwargs : dict 
        any other keyword arguments for plotting (optional)
    """
    hist = sample.hist(bins=bins)
    plt.title(title)
    
    plt.show()
    
    return


def test_run():
    """Test run plot_histogram() with different samples."""
    # Load and plot histograms of each sample
    # Note: Try plotting them one by one if it's taking too long
    A = pd.read_csv("A.csv", header=None, squeeze=True)
    plot_histogram(A, title="Sample A")
    
    B = pd.read_csv("B.csv", header=None, squeeze=True)
    plot_histogram(B, title="Sample B")
    
    C = pd.read_csv("C.csv", header=None, squeeze=True)
    plot_histogram(C, title="Sample C")
    
    D = pd.read_csv("D.csv", header=None, squeeze=True)
    plot_histogram(D, title="Sample D")


if __name__ == '__main__':
    test_run()
