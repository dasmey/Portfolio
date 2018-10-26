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

## it's time to plot
hist(sub_power$Global_active_power, main = "Global Active Power", col = "red", xlab = "Global Active Power (kilowatts)", ylab = "Frequency")
# and to create a PNG file
dev.copy(png, filename = "plot1.png", width = 480, height = 480)
dev.off()