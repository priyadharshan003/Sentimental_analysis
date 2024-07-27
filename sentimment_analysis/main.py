import string
from collections import Counter
import matplotlib.pyplot as plt

# reading text file
text = open("read.txt", encoding="utf-8").read()

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()

stop_words = [
    'into', 'very', 're', 'are', 'while', 'my', 'just', 'needn', 'few', 'no', 's', 'which', 'about', 'the', 'and',
    'some', 'isn', 'its', 'couldn', 'does', 'than', 'through', 'myself', 'not', "that'll", 'should', 'after', 'only',
    'of', 'this', 'o', 'has', 'own', 'most', 'below', 'by', 'under', 'her', 'they', 'itself', 'both', 'same', 'd',
    'there', 'ma', "isn't", 'above', "didn't", 'here', 'yours', "wouldn't", 'yourselves', 'with', 'what', "wasn't",
    'from', 'other', 'do', 'on', 'yourself', 'be', "hasn't", 'so', "mustn't", 'each', "won't", 'between', 'wouldn',
    'those', 'more', 'a', 'doesn', 'further', "she's", 'then', 'hadn', 'him', 'whom', 'where', 'too', "aren't",
    'these', 'because', 'himself', 'herself', "doesn't", 'wasn', 'your', 'been', "hadn't", 'down', 'themselves',
    'will', "you've", 'until', 'aren', 'being', "shouldn't", 'did', "haven't", 'mustn', 'now', 'our', 'such',
    "should've", 'but', 'll', 'she', 'don', 'if', 'hers', 'at', 'all', 'before', 'his', 'didn', 'out', 'or', 'is',
    'i', 'me', 'having', 'were', 'theirs', 'any', 'haven', "needn't", 'shouldn', "mightn't", 'their', 'against',
    "don't", 'was', 'doing', 'won', 'as', 'when', "it's", 'to', 'shan', 'that', 'them', 'it', 'ours', "shan't",
    'can', 'he', 've', "you'll", 't', 'for', 'y', 'ain', 'we', 'ourselves', 'hasn', 'nor', 'had', 'over', 'again',
    'once', 'm', 'weren', "weren't", 'why', 'in', 'off', 'how', "couldn't", "you're", 'you', 'during', "you'd",
    'an', 'up', 'mightn', 'am', 'who', 'have'
]

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

# Counting occurrences of each emotion
emotion_counter = Counter(emotion_list)

# Positive and Negative colors
positive_color = 'lightgreen'
negative_color = 'lightcoral'

# Plotting the emotions on the bar graph with enhanced styling
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Bar graph
bars = ax1.barh(list(emotion_counter.keys()), list(emotion_counter.values()), color=[positive_color if val >= 0 else negative_color for val in emotion_counter.values()])
for bar in bars:
    yval = bar.get_width()
    ax1.text(yval, bar.get_y() + bar.get_height() / 2, round(yval, 1), ha='left', va='center', color='black', fontsize=10)

ax1.set_xlabel('Occurrences')
ax1.set_ylabel('Emotion')
ax1.set_title('Emotion Analysis', fontsize=16, fontweight='bold')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

# Styling the bar graph
ax1.invert_yaxis()  # Invert the y-axis for better readability
ax1.xaxis.set_tick_params(width=0)  # Hide x-axis ticks

# Pie chart
labels = list(emotion_counter.keys())
sizes = list(emotion_counter.values())
colors = [positive_color, negative_color, 'lightskyblue', 'lightpink', 'lightyellow', 'lightgrey']
explode = (0.1,) * len(emotion_counter)  # Set explode length to match the number of emotions

ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Adding title
ax2.set_title('Distribution of Emotions', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('combined_graphs.png')
plt.show()