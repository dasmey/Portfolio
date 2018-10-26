library(dplyr)
library(lubridate)

## Download and extract data
url <- "https://d396qusza40orc.cloudfront.net/exdata%2Fdata%2Fhousehold_power_consumption.zip"
download.file(url, "power.zip", method = "auto")
unzip("power.zip")

## Locating data file and creating our power data with read.table.
list.files()
power <- read.table("household_power_consumption.txt", sep = ";", dec = ".", stringsAsFactors = FALSE, header = TRUE)
# Creating a more compact and usefull data to explore
power <- tbl_df(power)
## To subset, we first need to change our date column to the right class
power$Date <- as.Date(power$Date, format="%d/%m/%Y")
# Now we can subset
sub_power <- filter(power, Date >= "2007-02-01" & Date <= "2007-02-02")
# and remove our previous power data
rm("power")

## Before creating the plot, we need to convert some columns to numeric instead of character
sub_power$Global_active_power <- as.numeric(as.character(sub_power$Global_active_power))
sub_power$Global_reactive_power <- as.numeric(as.character(sub_power$Global_reactive_power))
sub_power$Voltage <- as.numeric(as.character(sub_power$Voltage))
sub_power$Global_intensity <- as.numeric(as.character(sub_power$Global_intensity))
sub_power$Sub_metering_1 <- as.numeric(as.character(sub_power$Sub_metering_1))
sub_power$Sub_metering_2 <- as.numeric(as.character(sub_power$Sub_metering_2))
# Key part of the second plot,We need to convert our Date & Time to Date/time variable
fulldate <- paste(sub_power$Date, sub_power$Time)
sub_power$Full_Date <- as.POSIXct(fulldate)

## Time to create a plot
par(mfrow = c(2, 2), mar = c(4,4,2,1), oma = c(0,0,2,0))
with(sub_power, {
        plot(Global_active_power ~ Full_Date, type = "l", xlab = "", ylab = "Global Active Power (kilowatts)")
        plot(Voltage ~ Full_Date, type = "l", xlab = "datetime", ylab = "Voltage")
        plot(Sub_metering_1~Full_Date, type="l", ylab="Energy sub metering", xlab="")
        lines(Sub_metering_2~Full_Date, col='Red')
        lines(Sub_metering_3~Full_Date, col='Blue')
        legend("topright",col=c("black", "red", "blue"),lty=1,lwd=2,legend=c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"))
        plot(Global_reactive_power ~ Full_Date, type = "l", xlab = "datetime")
})

## And finally save our png
dev.copy(png, file="plot4.png", height=480, width=480)
dev.off()