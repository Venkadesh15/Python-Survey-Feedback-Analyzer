# SURVEY FEEDBACK ANALYZER

# 1) PRELOADED FEEDBACK DATA
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# 2) ADDING MORE FEEDBACKS

# 2.1) ASKING HOW MANY FEEDBACKS TO ADD
n = int(input("How many more feedbacks do you want to add? "))
# 2.2) COLLECTING NEW FEEDBACKS
for i in range(n):
    print(f"\nEnter details for feedback {i + 1}")
# 2.3) COLLECTING NAME, FEEDBACK AND RATING
    name = input("Enter name: ")
    feedback = input("Enter written feedback: ")
    rating = int(input("Enter rating (1-5): "))
# 2.4) VALIDATING RATING 1 TO 5
    while rating < 1 or rating > 5:
        print("Invalid rating! Please enter a rating between 1 and 5.")
        rating = int(input("Enter rating (1-5): "))
# 2.5) APPENDING DATA FOR NEW FEEDBACK TO THE DICTIONARY
    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# 3) TEXT CLEANING

# 3.1) DEFINING PUNCTUATION TO REMOVE
punctuation = ['.', ',', '!', '?']
# 3.2) LOOPING THROUGH EACH FEEDBACK AND CLEANING IT
for i in range(len(feedback_data['Feedback'])):
    text = feedback_data['Feedback'][i]
# 3.3) REMOVING PUNCTUATION FROM THE FEEDBACK TEXT
    for symbol in punctuation:
        text = text.replace(symbol, '')
# 3.4) CONVERTING TO LOWERCASE
    text = text.lower()
# 3.5) REMOVING EXTRA SPACES AND JOINING WORDS
    text = ' '.join(text.split())
# 3.6) UPDATING CLEANED FEEDBACK
    feedback_data['Feedback'][i] = text


# 4) WORD COUNT INSIGHTS

# 4.1) DEFINING THE FUNCTION
def count_word_in_feedbacks(word):
# 4.2) INITIALIZING THE COUNT VARIABLE
    count = 0
    word = word.lower()
# 4.3) COUNTING OCCURRENCES OF THE WORD IN ALL FEEDBACKS
    for feedback in feedback_data['Feedback']:
        words = feedback.split()
# 4.4) CHECKING IF THE WORD IS PRESENT IN THE FEEDBACK
        if word in words:
            count += 1

    return count
# 4.5) DISPLAYING THE INSIGHTS LIKE GOOD, POOR, EXCELLENT
print("\n--- WORD COUNT INSIGHTS ---")
print("Feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))


# 5) FINAL SURVEY FEEDBACK DATA AFTER CLEANING AND INSIGHTS

# 5.1) DISPLAYING CLEANED FEEDBACK DATA
print("\n--- CLEANED FEEDBACK DATA ---")
print(feedback_data)
# 5.2) CALCULATING AVERAGE RATING
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
# 5.3) DISPLAYING AVERAGE RATING
print("\nAverage Rating:", round(average_rating, 2))
# 5.4) FINDING THE FEEDBACK WITH THE LONGEST WORD COUNT
longest_feedback = max(
    feedback_data['Feedback'],
    key=lambda text: len(text.split())
)
# 5.5) DISPLAYING THE LONGEST FEEDBACK AND ITS WORD COUNT
print("\n--- LONGEST FEEDBACK ---")
print("Feedback:", longest_feedback)
print("Word Count:", len(longest_feedback.split()))
# 5.6) FINDING UNIQUE WORDS IN ALL FEEDBACKS
unique_words = set()
# 5.7) LOOPING THROUGH EACH FEEDBACK TO EXTRACT UNIQUE WORDS
for feedback in feedback_data['Feedback']:
    words = feedback.split()
    unique_words.update(words)
# 5.8) DISPLAYING UNIQUE WORDS AND THEIR COUNT
print("\n--- UNIQUE WORDS ---")
print(sorted(unique_words))
print("Total Unique Words:", len(unique_words))
# 5.9) SORTING FEEDBACK DATA BASED ON RATING IN DESCENDING ORDER
sorted_feedbacks = sorted(
    zip(
        feedback_data['S_No'],
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
# 5.10) SORTING BASED ON RATING IN DESCENDING ORDER
    key=lambda item: item[3],
    reverse=True
)
# 5.11) DISPLAYING SORTED FEEDBACKS BASED ON RATING
print("\n--- FEEDBACKS SORTED BY RATING ---")
# 5.12) LOOPING THROUGH SORTED FEEDBACKS AND PRINTING DETAILS
for s_no, name, feedback, rating in sorted_feedbacks:
    print(s_no, name, feedback, rating)
