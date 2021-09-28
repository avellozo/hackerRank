'''
For those who're confused with problem statement. Here's an outline of how to get solution.

"You have a sample of n values from a population with mean m and with standard deviation s."

Means you have sample: x1, ..., xn of random variable with some unknown distribution with known mean m and standard deviation s.

Sample mean is defined as the function of sample, there fore itself being a random variable: avg = 1/n * (x1 + ... + xn)

Task is: "compute the interval that covers the middle p of the distribution of the sample mean. i.e. a and b such that Pr[a < avg < b] = p"

So, we need to determine distribution of sample mean (as random variable) first.

According to central limit theorem, distribution of sample mean approaches normal distribution, as sample size approaches infinity.

So, if we assume n is large enough for error to be negligable, we now know that distribution of sample mean is normal with mean m_avg and standard deviation s_avg.

Properties of mean:

E[a*X] = a*E[X]

E[X + Y] = E[X] + E[Y]

We can calculate mean of sample mean:

m_avg = E[avg] = E[1/n * (x1 + ... + xn)] = 1/n * (E[x1] + ... + E[xn]) = 1/n * n*m = m

Properties of variance (square of standard error):

D[X + Y] = D[X] + D[Y], if X and Y are independant

D[a*X] = a^2 * D[X]

We can compute sample mean standard error:

s_avg^2 = D[avg] = D[1/n * (x1 + ... + xn)] = 1/n^2 * (D[x1] + ... + D[xn]) = 1/n^2 *n*s^2 = s^2 / n

s_avg = s / sqrt(n)

Now we have avg distribution: Normal(m, s/sqrt(n))

We need to find middle interval a = m - delta, b = m + delta such that Pr[a < x- < b] = p

Quantile function is the 'inverse' of cummulative distribution function in a sense that you go from probability to variable range instead of the opposite. For normal distribution there's a table of "z-values" that satisfy Pr[m-z*s < x < m+z*s] = p for given p.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mean = 500
std = 80
n = 100

mean2 = mean
std2 = std/math.sqrt(n)

dif = std2*1.96
print(round(mean2-dif,2))
print(round(mean2+dif,2))
