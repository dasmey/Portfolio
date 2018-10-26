## Required libraries

library(dplyr)
library(ggplot2)

## data

url <- "https://d396qusza40orc.cloudfront.net/repdata%2Fdata%2FStormData.csv.bz2"
download.file(url, "StormData.csv.bz2",method = "auto")
data <- tbl_df(read.csv("StormData.csv.bz2"))

## Processing data

injuries <- data %>%
        select(EVTYPE, INJURIES) %>%
        group_by(EVTYPE) %>%
        summarize(sum_injuries = sum(INJURIES)) %>%
        arrange(desc(sum_injuries))

fatalities <- data %>%
        select(EVTYPE, FATALITIES) %>%
        group_by(EVTYPE) %>%
        summarize(sum_fatalities = sum(FATALITIES)) %>%
        arrange(desc(sum_fatalities))

Most_injuries <- injuries$sum_injuries[1]
Total_injuries <- sum(injuries$sum_injuries)
mean(Most_injuries / Total_injuries * 100)

top5_most_injuries <- sum(injuries$sum_injuries[1:5])
mean(top5_most_injuries / Total_injuries * 100)

top10_most_injuries <- sum(injuries$sum_injuries[1:10])
mean(top10_most_injuries / Total_injuries * 100)

top20_most_injuries <- sum(injuries$sum_injuries[1:20])
mean(top20_most_injuries / Total_injuries * 100)

Most_fatalities <- fatalities$sum_fatalities[1]
Total_fatalities <- sum(fatalities$sum_fatalities)
mean(Most_fatalities / Total_fatalities * 100)

top5_most_fatalities <- sum(fatalities$sum_fatalities[1:5])
mean(top5_most_fatalities / Total_fatalities * 100)

top10_most_fatalities <- sum(fatalities$sum_fatalities[1:10])
mean(top10_most_fatalities / Total_fatalities * 100)

top20_most_fatalities <- sum(fatalities$sum_fatalities[1:20])
mean(top20_most_fatalities / Total_fatalities * 100)

multiplier <- function(x) {
        if (x %in% c("H", "h"))
                return(100)
        else if (x %in% c("K", "k"))
                return(1000)
        else if (x %in% c("M", "m"))
                return(1000000)
        else if (x %in% c("B", "b"))
                return(1000000000)
        else if (x %in% c("+"))
                return (1)
        else if (x %in% c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
                return (10)
        else
                return(0)
}

data$PROPmultiplier <- sapply(data$PROPDMGEXP, FUN = multiplier)
data$CROPmultiplier <- sapply(data$CROPDMGEXP, FUN = multiplier)

economy <- data %>%
        select(EVTYPE, PROPDMG, PROPmultiplier, CROPDMG, CROPmultiplier) %>%
        filter(PROPmultiplier > 0 | CROPmultiplier > 0) %>%
        mutate(PROPDMG = PROPDMG * PROPmultiplier, CROPDMG = CROPDMG * CROPmultiplier) %>%
        mutate(TOTALDMG = PROPDMG + CROPDMG)

economy2 <- economy %>%
        group_by(EVTYPE) %>%
        summarize(sum_TOTALDMG = sum(TOTALDMG) / 10^9) %>%
        arrange(desc(sum_TOTALDMG))

Most_Economics <- economy2$sum_TOTALDMG[1]
Total_Economics <- sum(economy2$sum_TOTALDMG)
mean(Most_Economics / Total_Economics * 100)

top5_Most_Economics <- sum(economy2$sum_TOTALDMG[1:5])
mean(top5_Most_Economics / Total_Economics * 100)

top10_Most_Economics <- sum(economy2$sum_TOTALDMG[1:10])
mean(top10_Most_Economics / Total_Economics * 100)

top20_Most_Economics <- sum(economy2$sum_TOTALDMG[1:20])
mean(top20_Most_Economics / Total_Economics * 100)

## results

injuries_plot <- ggplot(injuries[1:10, ], aes(x = reorder(EVTYPE, -sum_injuries), y = sum_injuries, fill = EVTYPE)) +
        geom_bar(stat = "identity") + 
        theme(axis.text.x = element_text(angle = 90)) +
        labs(x = "Type of event", y = "Total injuries", title = "Top 10 weather events resulting most injuries in the US ") +
        theme(plot.title = element_text(hjust = 0.5)) +
        scale_fill_hue(c = 50)

fatalities_plot <- ggplot(fatalities[1:10, ], aes(x = reorder(EVTYPE, -sum_fatalities), y = sum_fatalities, fill = EVTYPE)) +
        geom_bar(stat = "identity") + 
        theme(axis.text.x = element_text(angle = 90)) +
        labs(x = "Type of event", y = "Total fatalities", title = "Top 10 weather events resulting most fatalities in the US ") +
        theme(plot.title = element_text(hjust = 0.5)) +
        scale_fill_hue(c = 50)

Economics_plot <- ggplot(economy2[1:10, ], aes(x = reorder(EVTYPE, -sum_TOTALDMG), y = sum_TOTALDMG, fill = EVTYPE)) +
        geom_bar(stat = "identity") +
        theme(axis.text.x = element_text(angle = 90)) +
        labs(x = "Type of event", y = "Total in billion dollars", title = "Top 10 weather events resulting greatest economic damages in the US ") +
        theme(plot.title = element_text(hjust = 0.5)) +
        scale_fill_hue(c = 50)
