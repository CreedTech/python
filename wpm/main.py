import random
import threading
import time
from datetime import datetime as dt

#
# def wpm():
#     words_list = ["name", "elephant", "array", "pupil", "everything"]
#     typed_words = []
#     is_playing = True
#     start = dt.now()
#     for x in range(3):
#         rands = random.choice(words_list)
#         print(rands)
#         # start = time.time()
#         input_text = input("Type the words above here: ")
#
#         typed_words.append(input_text)
#     print("Total words")
#     print(typed_words)
#     # end = time.time()
#     end  = dt.now()
#     time_taken = end - start
#     # secs = time_taken / 1000000000.0
#     # minutes_diff = (datetime_end - datetime_start).total_seconds() / 60.0
#     for single_word in typed_words:
#         word_count = len(single_word)
#
#     num_length = 0
#     for w in typed_words:
#         num_length += len(w)
#     print(num_length)
#     # num_chars = len(typed_words)
#     secs = time_taken.seconds
#     print(secs)
#     # difference = (((num_length / 5) // time_taken) * 60)
#     # print(difference)
#     words_per_minute = (word_count / secs)
#     print(words_per_minute)
#
#
# wpm()

string = "The quick brown fox jumps over the lazy dog"
print(string)
word_count = len(string)

while str(input('Enter "yes" when you are ready')) != 'yes':
    str(input('Enter "yes" when you are ready'))
start = dt.now()
inputText = str(input('Enter the phrase as fast as possible'))
end = dt.now()
timeTaken = start - end
secs = timeTaken.seconds
print(secs)
wordPM = (word_count/secs)
print(wordPM)
