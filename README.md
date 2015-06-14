# Auto completion of sentence by predicting the next two words

#Steps:

#Preprocessing:

The data set consists of 1,00,000 unprocessed real tweets which needs to cleaned to process it for further processing to attain the objects

1 Removed Urls present in the data, exclusion of non-Unicode characters, converting emoticons in to standard tokens using regular expressions.

# What more can be done here?? 

Stemming: Stemming is very much needed to group the words which are similar but in various forms. But the output results of the stemmer are very weak. This in turn involves the process of correcting the spellings of this corpus based on the creating a customized dictionary relevant to the corpus. This involves huge process that checks and corrects each token in document by learning words in dictionary.

Identifying the group of words which have similar meaning:

# Approach tried:

Excluded Nouns in this process. Filtered Adjectives, verbs and adverbs separately and tried grouping the words which are similar by comparing the similarity between their respective wordnets in each of the wordnets. This again involves correcting the spelling to be very effective.

# Prediction of Next two words:

Bigram approach.

Identifying the bigrams, which are present in the document or converting two consecutive words in to bigrams and finding the word that is more probable give the previous word based on the frequency.

The prediction of next word is based on the word that is predicted by the algorithm. Based on the words highest co-occurrence with the other word.
Effective:

This method will be more effective if we can identify the group of words that are having similar meaning. 
Bi gram approach is less effective. Tri gram or n gram where n >3 is more effective in terms of results.

# Other approach for word prediction:

As the whole corpus is talking about one singular subject We can filter NNP ‘s and identify what are the most common adjectives, verbs and adverbs that’s likely to occur given NNP’S based on the conditional probabilities.Tokenizing the data and applying POS tagging on each of the token. Considering each line and their tags as the basis of training to predict the next possible tag that is most likely to occur and filling the word of corresponding tag (predicted) which has got highest occurrence with the respective NNP present in the test data.
