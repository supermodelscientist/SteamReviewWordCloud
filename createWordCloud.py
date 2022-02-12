import grabReviewJSON
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

reviewList = grabReviewJSON.getList()
collapsedList = ' '.join(reviewList)
STOPWORDS.update(['game','cookie','cookies','clicker','play','idle'])
wordcloud = WordCloud().generate(text=collapsedList)
wordcloud.to_file('first_100_neg.png')