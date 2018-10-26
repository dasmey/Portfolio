library(datasets)
data("ToothGrowth")

library(ggplot2)
head(ToothGrowth)
summary(ToothGrowth)
str(ToothGrowth)
sum(is.na(ToothGrowth))

unique(ToothGrowth$supp)
unique(ToothGrowth$dose)

g + geom_point(aes(fill = factor(dose), colour = supp)) + facet_grid(~supp)
g + geom_boxplot(aes(fill = factor(dose))) + facet_grid(~supp)

