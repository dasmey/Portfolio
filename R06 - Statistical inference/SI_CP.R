## simulation rules
set.seed(13053312)
lambda <- 0.2
n <- 40
sim <- 1000

## simulating
sim_test <- matrix(data=rexp(n * sim, lambda), sim)
sim_test_Means <- apply(sim_test, 1, mean)

## range & histogram
range(sim_test_Means)
hist(sim_test_Means , breaks=40 , col="lightblue", border=F , main="Rexp mean distribution", xlab = "mean", xlim = c(2.5,8.5))

## mean vs theorical mean
rexp_sim_mean <- mean(sim_test_Means)
theoretical_mean <- 1/0.2

## visualize mean & theorical mean
abline(v = rexp_sim_mean, lwd="2", col="blue")
abline(v = theoretical_mean, lwd="2", col = "red")
legend('topright', c("simulation", "theoretical"), lty=c(1,1), col=c("blue", "red"))

## variance vs theorical variance
rexp_sim_var <- var(sim_test_Means)
theoretical_var <- (1/lambda)^2/n

## distribution
hist(sim_test_Means , prob = TRUE, breaks=40 , col="lightblue", border=F , main="rexp mean distribution", xlab = "mean", xlim = c(2.5,8.5))
curve(dnorm(x, mean=theoretical_mean, sd=sqrt(theoretical_var)), add = TRUE, lwd = 2, col = "red")
lines(density(sim_test_Means), lwd = 2, col = "blue")
legend('topright', c("simulation distribution", "theoretical distribution"), lty=c(1,1), col=c("blue", "red"))

