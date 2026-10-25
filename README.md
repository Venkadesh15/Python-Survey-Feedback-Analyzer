# 🐍 Python Survey Feedback Analyzer

A Python project that collects, cleans, and analyzes survey feedback to extract meaningful insights using core Python programming concepts.

## 📌 Project Overview

The **Python Survey Feedback Analyzer** is a Python Module End Assignment developed using Python and Visual Studio Code.

The project processes survey feedback stored in a dictionary and performs text cleaning, keyword analysis, average rating calculation, longest feedback identification, unique word extraction, and rating-based sorting.

## 🎯 Objectives

- Store survey data using dictionaries and lists.
- Collect additional feedback from users.
- Validate ratings between 1 and 5.
- Clean feedback text using string operations.
- Count feedback entries containing specific keywords.
- Calculate the average rating.
- Find the longest feedback message.
- Extract unique words from feedback.
- Sort feedback by rating in descending order.

## ✨ Features

| Feature | Description |
|---|---|
| Feedback Collection | Accepts additional customer names, feedback, and ratings. |
| Rating Validation | Ensures ratings are between 1 and 5. |
| Text Cleaning | Removes selected punctuation, converts text to lowercase, and removes extra spaces. |
| Keyword Analysis | Counts feedback entries containing `good`, `poor`, and `excellent`. |
| Average Rating | Calculates the average of all ratings. |
| Longest Feedback | Identifies the feedback containing the most words. |
| Unique Words | Extracts unique words from the cleaned feedback. |
| Feedback Sorting | Sorts feedback by rating from highest to lowest. |

## 🛠️ Technologies Used

- **Programming Language:** Python
- **IDE:** Visual Studio Code
- **Libraries:** Python standard library

### Python Concepts Practiced

`Dictionary` · `List` · `for` Loop · `while` Loop · `if` Statement · Functions · String Methods · Sets · `split()` · `join()` · `max()` · `sum()` · `zip()` · `sorted()` · Lambda Functions

## 📂 Project Structure

```text
Python-Survey-Feedback-Analyzer/
│
├── Python Survey Feedback Analyzer.py
├── Python Survey Feedback Analyzer.docx
└── README.md
```

## ⚙️ Requirements

- Python 3.x
- Visual Studio Code or another Python editor

No external Python packages are required.

## 🚀 How to Run

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

**2. Open the project folder**

Open the downloaded repository in Visual Studio Code.

**3. Run the Python program**

Open the terminal and execute:

```bash
py "Python Survey Feedback Analyzer.py"
```

**4. Enter feedback details**

Enter the number of additional feedback entries and provide the requested name, feedback text, and rating.

The program will display the analysis results in the terminal.

## 📊 Sample Output

Example output based on the original 10 feedback entries:

```text
--- WORD COUNT INSIGHTS ---
Feedbacks containing 'good': 3
Feedbacks containing 'poor': 2
Feedbacks containing 'excellent': 1

Average Rating: 3.4

--- LONGEST FEEDBACK ---
Feedback: poor response and poor handling of issue
Word Count: 7
```

*Note: Results may vary depending on the additional feedback entered by the user.*

## 🎓 Learning Outcomes

- Practiced fundamental Python programming concepts.
- Learned to collect and clean text-based data.
- Applied loops, functions, and conditional statements.
- Extracted useful information from survey feedback.
- Developed a foundation for data analysis projects.

## 🔮 Future Enhancements

- Add positive, negative, and neutral sentiment analysis.
- Visualize survey ratings using charts.
- Export analysis results to CSV or Excel.
- Identify frequently used words.
- Develop an interactive dashboard using Streamlit.

## 👨‍💻 Author

**Venkadesh K**

B.Tech Graduate in Artificial Intelligence and Data Science

**Interests:** Python | Data Analytics | Data Science | Machine Learning
