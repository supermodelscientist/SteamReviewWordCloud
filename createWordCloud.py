import grabReviewJSON
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

reviews = grabReviewJSON.get_n_reviews('1454400',5000)
reviewList = [x['review'] for x in reviews.json()]
collapsedList = ' '.join(reviewList)
STOPWORDS.update(['game','cookie','cookies','clicker','play','idle'])
wordcloud = WordCloud(collocation_threshold = 3, width=1600, height=800).generate(text=collapsedList)
wordcloud.to_file('first_100.png')