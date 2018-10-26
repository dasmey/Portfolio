## Question 3 : Consider the 𝚖𝚝𝚌𝚊𝚛𝚜 data set. Fit a model with mpg as the outcome that includes number of cylinders as a factor variable and weight as confounder. Give the adjusted estimate for the expected change in mpg comparing 8 cylinders to 4.

fit <- lm(mpg ~ factor(cyl) + wt, data = mtcars)
summary(fit)$coef

## Question 2 : Consider the 𝚖𝚝𝚌𝚊𝚛𝚜 data set. Fit a model with mpg as the outcome that includes number of cylinders as a factor variable and weight as a possible confounding variable. Compare the effect of 8 versus 4 cylinders on mpg for the adjusted and unadjusted by weight models. Here, adjusted means including the weight variable as a term in the regression model and unadjusted means the model without weight included. What can be said about the effect comparing 8 and 4 cylinders after looking at models with and without weight included?.

Holding weight constant, cylinder appears to have less of an impact on mpg than if weight is disregarded.
summary(fit)$coef[3] 
summary(fit2)$coef[3] 
Note that 11.564 > 6.071, and so holding weight constant, cylinder appears to have less of an impact on mpg than if weight is disregarded.

## Question 3 : Consider the 𝚖𝚝𝚌𝚊𝚛𝚜 data set. Fit a model with mpg as the outcome that considers number of cylinders as a factor variable and weight as confounder. Now fit a second model with mpg as the outcome model that considers the interaction between number of cylinders (as a factor variable) and weight. Give the P-value for the likelihood ratio test comparing the two models and suggest a model using 0.05 as a type I error rate significance benchmark.
fit <- lm(mpg ~ cyl + wt, mtcars)
fit3 <- lm(mpg ~ cyl*wt, mtcars)
anova(fit, fit3)

## Question 4 : Consider the 𝚖𝚝𝚌𝚊𝚛𝚜 data set. Fit a model with mpg as the outcome that includes number of cylinders as a factor variable and weight inlcuded in the model as

lm(mpg ~ I(wt * 0.5) + factor(cyl), data = mtcars)
Since the unit of (wt * 0.5) is (lb/2000), and one (short) ton is 2000 lbs, the wt coefficient is interpretted as the estimated expected change in MPG per one ton increase in weight for a specific number of cylinders (4, 6, 8).

## Question 5 : Consider the following data set

x <- c(0.586, 0.166, -0.042, -0.614, 11.72)
y <- c(0.549, -0.026, -0.127, -0.751, 1.344)

influence(lm(y ~ x))$hat (professor solution)

my solution : hatvalues(fit6) (simpler)

## Question 6 : Consider the following data set, Give the slope dfbeta for the point with the highest hat value.

x <- c(0.586, 0.166, -0.042, -0.614, 11.72)
y <- c(0.549, -0.026, -0.127, -0.751, 1.344)

dfbetas(fit6)
Note : Be careful, dfbeta and dfbetas are very different.

## Question 7 : Consider a regression relationship between Y and X with and without adjustment for a third variable Z. Which of the following is true about comparing the regression coefficient between Y and X with and without adjustment for Z.

It is possible for the coefficient to reverse sign after adjustment. For example, it can be strongly significant and positive before adjustment and strongly significant and negative after adjustment.



