## Question 1 : Consider the data set given below
x <- c(0.18, -1.54, 0.42, 0.95)
w <- c(2, 1, 3, 1)
## Give the value of μ that minimizes the least squares equation
sum(x*w) / sum(w)

## Question 2 : Consider the data set given belowFit the regression through the origin and get the slope treating y as the outcome and x as the regressor. (Hint, do not center the data since we want regression through the origin, not through the means of the data.)
x <- c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
y <- c(1.39, 0.72, 1.55, 0.48, 1.19, -1.59, 1.23, -0.65, 1.49, 0.05)
(lm(y ~ x - 1))

## Question 3 : Do 𝚍𝚊𝚝𝚊(𝚖𝚝𝚌𝚊𝚛𝚜) from the datasets package and fit the regression model with mpg as the outcome and weight as the predictor. Give the slope coefficient.
data(mtcars)
lm(mpg ~ wt, data = mtcars)
# ou :
attach(mtcars)
cor(mpg, wt) * sd(mpg)/sd(wt)
detach(mtcars)

## Question 4 : Consider data with an outcome (Y) and a predictor (X). The standard deviation of the predictor is one half that of the outcome. The correlation between the two variables is .5. What value would the slope coefficient for the regression model with Y as the outcome and X as the predictor?
cor(x, y) = 0.5
sd(y)/sd(x)= 2
cor(Y,X)sd(Y)sd(X)=0.5*2=1

## Question 5 : Students were given two hard tests and scores were normalized to have empirical mean 0 and variance 1. The correlation between the scores on the two tests was 0.4. What would be the expected score on Quiz 2 for a student who had a normalized score of 1.5 on Quiz 1?
0.4 * 1.5 = 0.6

## Question 6 : Consider the data given by the following
x <- c(8.58, 10.46, 9.01, 9.64, 8.86)
## What is the value of the first measurement if x were normalized (to have mean 0 and variance 1)?
xc <- (x - mean(x))/sd(x)

## Question 7 : Consider the following data set (used above as well). What is the intercept for fitting the model with x as the predictor and y as the outcome?
x <- c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
y <- c(1.39, 0.72, 1.55, 0.48, 1.19, -1.59, 1.23, -0.65, 1.49, 0.05)
lm(y ~ x)

## Question 8 : You know that both the predictor and response have mean 0. What can be said about the intercept when you fit a linear regression?
It must be identically 0.

## Question 9 : Consider the data given by : What value minimizes the sum of the squared distances between these points and itself?
x <- c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
mean(x)

## Question 10 : Let the slope having fit Y as the outcome and X as the predictor be denoted as β1. Let the slope from fitting X as the outcome and Y as the predictor be denoted as γ1. Suppose that you divide β1 by γ1; in other words consider β1/γ1. What is this ratio always equal to?
Var(Y)/Var(X)