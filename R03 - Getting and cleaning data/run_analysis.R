## Hi, first we need to download the data set

project_url <- "https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip"
download.file(project_url, "project.zip", method="curl")
unzip("project.zip")

## Once it's done, we can now read the data :
## test
subject_test <- read.table("UCI HAR Dataset/test/subject_test.txt")
X_test <- read.table("UCI HAR Dataset/test/X_test.txt")
Y_test <- read.table("UCI HAR Dataset/test/Y_test.txt")
## train
subject_train <- read.table("UCI HAR Dataset/train/subject_train.txt")
X_train <- read.table("UCI HAR Dataset/train/X_train.txt")
Y_train <- read.table("UCI HAR Dataset/train/Y_train.txt")

## Now we can create our data and merge it :
## create test
test <- cbind(subject_test, Y_test, X_test)
## create train
train <- cbind(subject_train, Y_train, X_train)
## and merge them
human_activity <- rbind(test, train)

## As columns are not yet named in our dataset, we need to name them
## columns names actually appears in the features.txt
features <- read.table("UCI HAR Dataset/features.txt", colClasses = "character")
## subject = "subject", activity = "Y", features[, 2] = "X"
colnames(human_activity) <- c("subject", "activity", features[, 2])

## Extracts only the measurements on the mean and standard deviation for each measurement.
columnsWeWant <- grepl("subject|activity|mean|std", colnames(human_activity))
human_activity <- human_activity[, columnsWeWant]
## Tried to do the previous line with select() but it didn't succeed... If anyone knows, i'd be very interested...

## Uses descriptive activity names to name the activities in the data set
activity_labels <- read.table("UCI HAR Dataset/activity_labels.txt", colClasses = "character")
# In order to use mutate(), We need to load the dplyr library :
library(dplyr)
human_activity <- mutate(human_activity, activity = factor(human_activity[, 2], levels=c(1,2,3,4,5,6), labels=activity_labels[, 2]))

## let's clean our workspace
rm("subject_test", "subject_train", "test", "train", "X_test", "X_train", "Y_test", "Y_train")
## Appropriately labels the data set with descriptive variable names.
# Done at the line 29

## From the data set in step 4, creates a second, independent tidy data set with the average of each variable for each activity and each subject
# group by subject and activity and summarise_all
human_activity_data <- human_activity %>% 
                        group_by(subject, activity) %>%
                        summarise_all(funs(mean))
# creating data table
final_data <- tbl_df(human_activity_data)
# Writing txt file
write.table(final_data, "final_data.txt", row.name=FALSE)

