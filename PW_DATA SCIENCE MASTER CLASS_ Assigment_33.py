#!/usr/bin/env python
# coding: utf-8

# #  Assignment_09.03.2023(Advance Statistic-2)

# ## Q1. What are the Probability Mass Function (PMF) and Probability Density Function (PDF)?Explain and example?
# 
# ## Ans:-
#     Both Probability Mass Function (PMF) and Probability Density Function (PDF) are mathematical functions used to describe
#     the probability distribution of a random variable.
# 
#                     1. A probability mass function (PMF) is used to describe the probability distribution of a discrete 
#     random variable. It assigns a probability to each possible value that the random variable can take, and the sum of the 
#     probabilities for all possible values must equal 1. The PMF is defined as:
# 
#     P(X = x) = f(x)
# 
#                     where P(X = x) is the probability that the random variable X takes the value x, and f(x) is the
#                     probability mass function.
# 
#     For example, consider a random variable X that represents the number of heads obtained when flipping a fair coin three
#     times. The possible values of X are 0, 1, 2, or 3, and the probability of each value can be calculated using the PMF as
#     follows:
# 
#                             P(X = 0) = f(0) = (1/2)^3 = 1/8
#                             P(X = 1) = f(1) = 3*(1/2)^3 = 3/8
#                             P(X = 2) = f(2) = 3*(1/2)^3 = 3/8
#                             P(X = 3) = f(3) = (1/2)^3 = 1/8
#                             
#                             The PMF for this example would be:
# 
#                              x	         0	 1	 2	 3
#                             P(X = x)	1/8	3/8	3/8	1/8
#                    2. probability density function (PDF) is used to describe the probability distribution of a continuous
#      random variable. It is a function that describes the relative likelihood of a continuous random variable taking on a
#      certain value, and it integrates to 1 over the entire range of possible values.
# 
#             The PDF is defined as:
# 
#                 f(x) = dF(x) / dx
# 
#                                 where f(x) is the PDF of the random variable X, and F(x) is its cumulative distribution
#                                 function.
# 
#     For example, consider a continuous random variable X that represents the height of a randomly selected adult male in a
#     population. The PDF of X could be a normal distribution with mean μ and standard deviation σ. The PDF for a normal 
#     distribution is given by:
# 
#     f(x) = (1 / (σ * sqrt(2π))) * exp(-(x-μ)^2 / (2σ^2))
# 
#                                 where exp is the exponential function, π is the mathematical constant pi, sqrt is the square
#                                 root function, and μ and σ are the mean and standard deviation of the normal distribution.
# 
#            The PDF for this example would be a normal distribution curve with peak at μ and width determined by the standard
#             deviation σ.

# ## Q2.What is Cumulative Density Function (CDF)?Explain with an example.Why CDF is used?
# 
# ## Ans:-
#     A cumulative distribution function (CDF) is a function that describes the probability that a random variable X takes a
#     value less than or equal to a given value x. It is defined as the integral of the probability density function (PDF) for 
#     a continuous random variable or the sum of the probability mass function (PMF) for a discrete random variable, up to a
#     certain point x.
#     
#     For a discrete random variable X, the CDF is defined as:
# 
#     F(x) = P(X ≤ x) = Σ P(X = k) for all k ≤ x
# 
#                                     where Σ is the sum symbol, P(X = k) is the PMF for X, and k is the possible values of X.
#     For example, Consider a random variable X that represents the number of SIX obtained when rolling a dice 6 times.The 
#     possibility values of X are 0,1,2,3,4,5 or 6. The CDF of X would be:
#      
#       first you calculate the PMF of X:-
#                                       formula is P(X = x) = nCx * p^x * (1-p)^(n-x)
#                                       
#                                                            Where n is the number of trails,p is the probability of sucesses
#                                                            x is the number of sucesses and nCx is the binomial coefficient
#                                                            that gives the number of ways to choose x sucesses out of n trais
#                                                            
#                                                            where in this case,n=6(since we are rolling the dise 6 time)
#                                                            p=1/6(since the probability of getting a six on a single roll
#                                                            is 1/6),and x can take values from 0 to 6.
#                                                            
#       P(X = 0) = (6 choose 0) * (1/6)^0 * (5/6)^6 = 0.3349 -- i.e(6 choose 0)mean= 6!/(0!*(6-0)!)                               
#       P(X = 1) = (6 choose 1) * (1/6)^1 * (5/6)^5 = 0.4018 -- i.e(6 choose 1)mean= 6!/(1!*(6-1)!)=720/(1*120)=6
#       P(X = 2) = (6 choose 2) * (1/6)^2 * (5/6)^4 = 0.2009 -- i.e(6 choose 2)mean= 6!/(2!*(6-2)!)=720/(2*24) =15
#       P(X = 3) = (6 choose 3) * (1/6)^3 * (5/6)^3 = 0.0530 -- i.e(6 choose 3)mean= 6!/(3!*(6-3)!)=720/(6*6)  =21.1
#       P(X = 4) = (6 choose 4) * (1/6)^4 * (5/6)^2 = 0.0082 -- i.e(6 choose 4)mean= 6!/(4!*(6-4)!)=720/(24*2) =15
#       P(X = 5) = (6 choose 5) * (1/6)^5 * (5/6)^1 = 0.0008 -- i.e(6 choose 5)mean= 6!/(5!*(6-5)!)=720/(120*1)=6
#       P(X = 6) = (6 choose 6) * (1/6)^6 * (5/6)^0 = 0.00003 - i.e(6 choose 6)mean= 6!/(6!*(6-6)!)=720/(720*1)=1
#       
#       
#       Then The CDF of X  is defined as the sum of the PMF upto the certain value of X.Therefore, to calculate the CDF of X,
#       we can sum up the probabilities of all values of X less than or equal to a given value of x. 
#       
#       x = P(X<=x)
#        so, x=0 = 0.3349
#            x=1 = (0.3349+0.4018)= 0.7368
#            x=2 = (0.7368+0.2009)= 0.9377
#            x=3 = (0.9377+0.0530)= 0.9907
#            x=4 = (0.9907+0.0082)= 0.9989
#            x=5 = (0.9989+0.0008)= 0.9996
#            x=6 = (0.9996+0.0003)= 0.9999 ~ 1
#            
#       
#     The CDF is used to calculate probabilities for specific values or ranges of values of a random variable X. For example,
#     if we want to find the probability that a randomly selected the probability that the number of SIX obtained is less than
#     or equal to 3
#                                        
#     we can use the CDF and calculate:
# 
#     P(X ≤ 3) = F(3) = 0.9907
# 
#     Therefore, there is a probability of 0.9907 that the number of SIX obtained is less than or equal to 3 when rolling
#     a dice 6 times.
#  

# ## Q3. what are some example of situation where the normal distribution might be used as a model? Explain how the parameters of the normal distribution relate to the shape of the distribution.
# 
# ## Ans:-
#         The normal distribution is widely used as a model in various fields, particularly in statistics, engineering, 
#         finance, and social sciences. Here are some examples of situations where the normal distribution might be used as
#         a model:
#         
#         1.Heights and weights of individuals: The normal distribution can be used to model the distribution of heights
#           and weights of individuals in a population.
#           
#        2.IQ scores: IQ scores are often assumed to follow a normal distribution, with a mean of 100 and a standard deviation
#          of 15.
#          
#        3.Errors in measurements: The normal distribution can be used to model the distribution of errors in measurements, 
#          such as errors in temperature, pressure, or other physical quantities.
#          
#       4.Stock prices: Stock prices are often modeled using the normal distribution, with the mean representing the expected
#         value of the stock price and the standard deviation representing the volatility of the stock price.
#         
#       The parameters of the normal distribution are the mean (μ) and the standard deviation (σ). The mean represents the
#       central tendency of the distribution, while the standard deviation represents the spread of the distribution around 
#       the mean.
# 
#                                            The mean parameter determines the location of the peak of the distribution, and 
#       the standard deviation parameter determines the width of the distribution. A larger standard deviation indicates a 
#       wider spread of data points around the mean, while a smaller standard deviation indicates a narrower spread.
# 
#       In summary, the parameters of the normal distribution play a crucial role in defining the shape of the distribution.

# ## Q4. Explain the importance of Normal distribution.Give a few real-life example of Normal Distribution.
# 
# ## Ans:-
# 
#        Normal distribution, also known as Gaussian distribution, is one of the most important probability distributions in
#        statistics and mathematics. It is widely used in many fields of science, engineering, social sciences, and business 
#        due to its simplicity, versatility, and usefulness. Normal distribution has several important properties that make 
#        it particularly important and widely used, including:
# 
#     1.Symmetry: The normal distribution is symmetric around its mean, which means that the probabilities of values to the 
#     left and right of the mean are equal. This property makes it easy to calculate probabilities and to make inferences 
#     about data.
# 
#     2.Central Limit Theorem: The normal distribution is a key component of the central limit theorem, which states that the
#     sum of many independent and identically distributed random variables tends to be normally distributed, regardless of the
#     underlying distribution of the individual variables. This theorem is crucial for many statistical applications, such as
#     hypothesis testing and confidence intervals.
# 
#     3.Wide Applicability: Normal distribution is often used as an approximation for many real-world phenomena, even when the
#     data does not follow a perfectly normal distribution. This is because many natural phenomena and processes tend to 
#     exhibit a bell-shaped distribution, which can be modeled with the normal distribution.
# 
# Some examples of real-life phenomena that follow a normal distribution include:
# 
#         a)Heights and weights of people: In general, heights and weights of a population follow a normal distribution, with
#         a few outliers at the extremes.
# 
#         b)Test scores: The scores of many standardized tests, such as the SAT, ACT, or GRE, tend to be normally distributed.
#         This makes it easy to compare scores and to set cutoffs for admissions or hiring.
# 
#         c)Financial markets: The returns of stocks, bonds, and other financial assets often follow a normal distribution, 
#         which is useful for modeling risk and constructing portfolios.
# 
#         d)Quality control: Many manufacturing processes, such as the production of computer chips, follow a normal 
#         distribution, which is useful for monitoring and improving quality control.
# 
#         e)Natural phenomena: Many natural phenomena, such as the distribution of temperatures or rainfall over time or 
#         geographic areas, tend to follow a normal distribution, which can be useful for predicting and planning for future
#         events.
# 
#                                 Overall, normal distribution is a crucial tool in many areas of science, engineering, and 
#        business, and understanding its properties and applications is essential for making informed decisions based on data.
# 
# 

# ## Q5.What is Bernoulli Distribution? Give an example. What is the difference between Bernoulli Distribution and Binomial Distribution?
# 
# ## Ans:-
#     Bernoulli distribution named after swiss mathematician Jacob Burnoulli, it is a discrete probability distribution that
#     describes the probability of getting a success or a failure in a single Bernoulli trial, where a success has probability
#     p and a failure has probability 1-p. In other words, it models a single experiment with two possible outcomes, usually
#     labeled as success (1) or failure (0), where the probability of success is p and the probability of failure is 1-p.
# 
#         The probability mass function (PMF) of a Bernoulli distribution is given by:
#                                         P(X = 1) = p
#                                         P(X = 0) = 1 - p
#                                         
#                       Where 'X' is the random variable that represents the outcome of a single Bernoulli trial.
#    
#        Example: A fair coin toss can be modeled as a Bernoulli trial, where the outcome of the trial is heads (success)
#        with probability 0.5 and tails (failure) with probability 0.5.
#        
#        The main difference between Bernoulli distribution and Binomial distribution is that 
#        Bernoulli distribution models a single experiment with two possible outcomes,
#        whereas Binomial distribution models the number of successes in n independent Bernoulli trials.
#        
#                                        More precisely, the Binomial distribution describes the probability of getting k
#        successes in n independent Bernoulli trials, where each trial has the same probability p of success. The probability
#        mass function (PMF) of a Binomial distribution is given by:
#        
#                                P(X = k) = (n choose k) * p^k * (1-p)^(n-k)
#                                
#                                where X is the random variable that represents the number of successes in n Bernoulli trials,
#         k is the number of successes, p is the probability of success in each trial, and (n choose k) is the binomial 
#         coefficient, which represents the number of ways to choose k successes from n trials.
# 
# 

# ## Q6.Consider a dataset with a mean of 50 and Standard deviation of 10. if we assume that the dataset is normal distributed,what is the probability that a randomly selected observation will be greater than 60? Use the appropriate formula and show your calculation. 
# 
# ## Ans:-
#     To find the probability that a randomly selected observation from a normal distribution with a mean of 50 and a standard
#     deviation of 10 will be greater than 60, we need to use the standard normal distribution and the z-score.
# 
#     The z-score represents the number of standard deviations an observation is away from the mean, and it is calculated as:
# 
#                                 z = (x - μ) / σ
#                                     
#                                     Where x is the observation,  μ is the mean, and σ is the standard deviation.
#    
#        In this case, we want to find the z-score for x=60:
#        
#        z= (60-50)/10 = 1
#        
#         Using a standard normal distribution table or calculator, we can find the probability of a z-score greater than 1
#         to be approximately 0.1587.
# 
#     Therefore, the probability that a randomly selected observation from this normal distribution will be greater than 60 is
#     approximately 0.1587 or 15.87%                            

# ## Q7.Explain Uniform Distribution with an example?
# 
# ## Ans:-
#        Uniform distribution is a continuous probability distribution that models a situation where all values in a given 
#        interval have an equal probability of being observed. 
#        In other words, 
#        it describes a random variable that is equally likely to take on any value within a specified range.
#        
#        The probability density function (PDF) of a Uniform distribution over the interval [a, b] is given by:
#        
#                         f(x) = 1 / (b - a)   for a <= x <= b
#                                0              otherwise
#                                
#        Example: A lottery game in which a player can choose any number from 1 to 100 has a Uniform distribution, since each
#        number has an equal chance of being chosen. In this case, the interval [a, b] is [1, 100], and the PDF of the Uniform
#        distribution is:
#                        f(x) = 1 / (100 - 1)= 1/99=0.0101   for 1 <= x <= 100
#                               0                             otherwise
#                               
#                               Therefore, the probability of choosing any particular number between 1 and 100 is 1/100, 
#       since all numbers have an equal probability of being chosen.

# ## Q8. What is the Z score?State the importance of the z score.
# 
# ## Ans:-
#         The Z score, also known as the standard score, is a statistical measurement that indicates how many standard 
#         deviations a data point is away from the mean of the distribution. It is calculated by subtracting the mean from
#         the data point and dividing the result by the standard deviation. The formula for calculating the Z score is:
# 
#                 Z = (X - μ) / σ
# 
#                             where Z is the Z score, X is the data point, μ is the mean, and σ is the standard deviation.
# 
#         The Z score is important because it helps us to standardize data across different distributions and scales,
#         making it easier to compare data points from different populations. 
#         

# ## Q9. What is the Central Limit Theorem? State the significance of the Central limit Theorem
# 
# ## Ans:-
# 
#         The Central Limit Theorem (CLT) is a fundamental concept in statistics and probability theory. It states that as
#         the sample size increases, the sampling distribution of the mean of any random variable approaches a normal 
#         distribution, regardless of the distribution of the original variable, provided that the sample size is 
#         sufficiently large(should be >=30).In other words, the Central Limit Theorem describes the behavior of sample 
#         means as sample sizes increase, implying that even if the population distribution is not normal, the distribution 
#         of sample means tends to become normal with a mean equal to the population mean and a variance equal to the 
#         population variance divided by the sample size. The Central Limit Theorem is often used in hypothesis testing, 
#         confidence interval estimation, and other statistical inference techniques.
#         
#         The significance of the Central Limit Theorem is that it provides a way to make accurate inferences about population
#         parameters based on sample statistics. It allows statisticians and researchers to use the normal distribution as a
#         useful approximation for a wide range of real-world phenomena, even when the underlying population distribution is 
#         unknown or non-normal. The CLT is widely applicable in various fields, including finance, engineering, 
#         social sciences, and medicine.  
#         

# ## Q10. State the assumptions of Central Limit Theorem.
# 
# ## Ans:-
# 
#         The Central Limit Theorem (CLT) relies on a few assumptions to hold true. These assumptions are:
# 
#         1.Random sampling: The samples are drawn randomly from the population. Each sample has an equal chance of being 
#         selected.
# 
#         2.Independence: The samples must be independent of each other. That is, the value of one sample should not depend on 
#         the value of another sample.
# 
#         3.Finite variance: The population from which the samples are drawn should have a finite variance. If the variance is
#         infinite, the CLT may not apply.
# 
#         4.Sufficiently large sample size: The sample size should be large enough. Although there is no strict rule for how 
#         large the sample size should be, a general rule of thumb is that the sample size should be at least 30.
# 
#                     If these assumptions are met, the CLT can be used to approximate the distribution of sample means as a 
#                     normal distribution, regardless of the distribution of the population. It is important to note that 
#                     violating these assumptions can lead to inaccurate results, and other methods may need to be used to
#                     analyze the data.
