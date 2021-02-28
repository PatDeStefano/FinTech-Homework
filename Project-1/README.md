# PORTFOLIO FORECASTING
 *by Arzu Isik Topbas, Hope Forrester, Terry Fry, Patrick DeStefano, Freddie Eisa, Ali Jaber*
 
 <img src="https://previews.123rf.com/images/peshkov/peshkov1905/peshkov190500213/121955022-abstract-glowing-forex-chart-backdrop-with-grid-invest-and-trade-concept-3d-rendering.jpg" width="900" height="250" />

[image source](https://www.123rf.com/photo_121955022_abstract-glowing-forex-chart-backdrop-with-grid-invest-and-trade-concept-3d-rendering.html?vti=of6pb64qajdoj322t4-1-36)

In this project,  we built a notebook to forecast **portfolio based on stock earnings**. Accordingly, we explored *what factors have the greatest influence on returns based on earnings?*  We also designed a **Portfolio Forecaster Dashboard** by using Python visualizations.

![image source](https://github.com/arzuisiktopbas/Project-1/blob/main/Images/Project_Dashboard.gif)

**Question #1 - Are dividends and earnings enough to construct an optimal portfolio of stocks?**

This is enough to construct a portfolio, but we found we needed to include particular variables to optimize it, such as “initial investment”, “days in the market”, “weights”, and “number of stocks”.

**Question #2 - Would weighting stocks differently result in higher returns?**

After running a Monte Carlo Simulation, we found that we were likely to lose our initial investment.
We want to create a weighting calculator to test this theory and found.. the number of stocks played more into the results than the varied weights. We found the  more stocks we had, the worse the returns were. 
Weighting does present the opportunity for higher returns. 

**Question #3 - Is Monte Carlo an optimal method for forecasting our portfolio?**

Machine Learning will be more efficient as Monte Carlo Simulations are static.
We wanted to see if there was a more efficient way of pinpointing a time in the future to buy or sell a particular stock. 

**Question #4 - Where can we obtain data to accomplish this task?**

We utilized the Yahoo Finance Calendar and Alpaca API’s to pull real time stock data.
While we were able to obtain sufficient data, the data was robust, and created issues with narrowing it down and completing further cleaning.

### SUMMARY
We initially planned to forecast at what point we should buy or sell a particular stock, and found we were limited in determining this as it would require machine learning to make effective predictions. 
We discovered that we would need to build an optimal portfolio to determine returns based on the following factors: Initial Investment, number of days left in the market, weighting, and number of stocks, to begin phase two of prediction.
* We found that Initial Investment affected returns only to the extent that it heightened the difference between 95% Confidence Intervals. 
* More days left in the market decreased the opportunity for high returns and created a large gap between Confidence Intervals.
* Weighting
   -  Equal Weighting: The more stocks we added at equal weights increased the risk to lose entirety of initial investment.
   -  Random Weighting: If choosing more than 3 stocks, varied weights are required to ensure gains.
* The more stocks included in the portfolio, the greater risk of losing the entirety of our initial investment, and conversely, the greater opportunity for reward in reaping significant gains.  
