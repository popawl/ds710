library(wordcloud)

#==============================================================================
# For the 2 samples T-test
#==============================================================================
df <- read.csv('data_sentiment.csv')
boxplot(df$compound ~ df$ToD)
t.test(df$compound ~ df$ToD)

#==============================================================================
# Word cloud
#==============================================================================
wc_morn <- scan('data_wc_morn.csv', what="", sep=',', skip=1)
wordcloud(wc_morn, max.words=100, col=rainbow(12))
wc_night <- scan('data_wc_night.csv', what="", sep=',', skip=1)
wordcloud(wc_night, max.words=100, col=rainbow(12))
