# Udacity-Projects

## Intro

Quantitative Finace and Machine Learning for Finance Projects.

## Parts

There are two terms that projects were based on different focus.

- First term is about __quantitative finance__. The projects include traditional trading strategies, Alpha and Beta generation and multi-factor models that combine different trading signals. In this term, the focus is to get a basic understanding of portfolio structure and management.

- In second term is more focused on __Artificial Intelligence for Finance__. We introduce Machine Learning, NLP and Deep Learning techniques to boost signal performance for our research. The projects include Natural Language Processing on financial statements, sentiment analysis with neural network techniques(tweets etc.), feature selection techniques and model explainability with SHapley (a game theory approach). We finally, perform backtesting on our research theory to ensure that our strategy is fully tested and ready to be implemented in real time.

### Term 1

1. **Trading with Momentum**

    In this project, we implement a trading strategy, and test to see if it has the potential to be profitable. We will be supplied with a universe of stocks and time range. We will also be provided with a textual description of how to generate a trading signal based on a momentum indicator. We will then compute the signal for the time range given and apply it to the dataset to produce projected returns. Finally, we will perform a statistical test on the mean of the returns to conclude if there is alpha in the signal. For the dataset, we'll be using the end of day from Quotemedia.

2. **Breakout Strategy**

    In this project, we will implement the breakout strategy. We'll find and remove any outliers. We'll test to see if it has the potential to be profitable using a Histogram and P-Value. For the dataset, we'll be using the end of day from Quotemedia.

3. **Smart Beta and Portfolio Optimisation**

    In this Project we utilise Smart Beta trading strategy and also try to optimise the Portfolio to track an Index. We search for the minimum of a convex function with contraints that will help to minimise the tracking errror of the ETF against the Index.

4. **Multi-factor Model**

    In this project, we will build a statistical risk model using PCA. We'll use this model to build a portfolio along with 5 alpha factors. We'll create these factors, then evaluate them using factor-weighted returns, quantile analysis, sharpe ratio, and turnover analysis. At the end of the project, we'll optimize the portfolio using the risk model and factors using multiple optimization formulations. For the dataset, we'll be using the end of day from Quotemedia and sector data from Sharadar.

### Term 2

5. **NLP on Financial Statements**

    In this project, we'll do NLP Analysis on 10-k financial statements to generate an alpha factor. For the dataset, we'll be using the end of day from Quotemedia and Loughran-McDonald sentiment word lists.

6. **Sentiment Analysis with Neural Networks**

    In this project, we'll build our own deep learning model to classify the sentiment of messages from StockTwits, a social network for investors and traders. Our model will be able to predict if any particular message is positive or negative. From this, we'll be able to generate a signal of the public sentiment for various ticker symbols.

7. **Combining Signals for Enhanced Alpha**

    In this project, we'll combine signals on a random forest for enhanced alpha. While implementing this, we'll have to solve the problem of overlapping samples. For the dataset, we'll be using the end of day from Quotemedia and sector data from Sharadar.

8. **Backtesting**

    In this project, we will build a fairly realistic backtester that uses the __Barra__ data. The backtester will perform portfolio optimization that includes transaction costs, and we'll implement it with computational efficiency in mind, to allow for a reasonably fast backtest. We'll also use performance attribution to identify the major drivers of our portfolio's profit-and-loss (PnL). We will have the option to modify and customize the backtest as well.

## Others

There is also a Monte Carlo Simulation script for _Value at Risk Model (VaR)_.

-------

__NOTES__

The data samples for some of the quiz sections are stored on the Google and OneDrive drives (eg. `.csv`, `.zip`).
