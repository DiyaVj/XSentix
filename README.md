# XSentix

## Overview

XSentimentAnalyzer is a powerful sentiment analysis and content recommendation system designed to analyze and interpret sentiments expressed in tweets on the "X" platform (formerly known as Twitter).

## Key Features

- **Sentiment Analysis**: XSentimentAnalyzer utilizes state-of-the-art NLP models to perform in-depth sentiment analysis on tweets, categorizing them as positive, negative, or neutral.

- **Emotion Classification**: Beyond sentiment, our system classifies tweets into various emotions, including joy, sadness, anger, and more, offering a richer understanding of user sentiments.

- **Sensitive Content Detection**: XSentimentAnalyzer actively scans tweets for sensitive information such as mentions of critical events (e.g., death) and, when detected, initiates notifications to appropriate individuals or groups.

- **Personalized Content Recommendations**: Based on a user's current sentiment or emotional state, XSentimentAnalyzer recommends tailored content, including news articles, videos, and user profiles to follow, enhancing the user experience.

- **Real-time Updates**: The system continuously updates sentiment scores, emotion classifications, and content recommendations, ensuring users receive the most relevant information as it happens.

- **Interactive Dashboard**: XSentimentAnalyzer provides a comprehensive, user-friendly dashboard with interactive visualizations, including graphs and charts, to present tweet data in an easily digestible format.

## Usage

- Access the web-based interface or use API endpoints to input a user's "X" platform username or a specific hashtag.
- XSentimentAnalyzer will perform sentiment analysis on recent tweets associated with the user or hashtag.
- The system will provide sentiment scores, emotion classifications, and sensitive content detection.
- If sensitive information is detected, notifications will be sent to designated contacts or well-wishers.
- Explore the interactive dashboard to gain insights through visually appealing graphs and charts.

## Getting Started

These instructions will help you set up a virtual environment and install the required dependencies for this project.

### Prerequisites

- Python (>=3.6) installed on your system.
- Git (optional, if you plan to clone the repository).

### Setting up a Virtual Environment

It's a good practice to create a virtual environment to manage project dependencies. You can use `venv` or `virtualenv` depending on your preference.

#### Using `venv` (Python 3.3+)

```bash
python -m venv myenv  # Replace 'myenv' with your preferred environment name
source myenv/bin/activate  # Use 'activate' on Windows
```
```
pip install virtualenv
virtualenv myenv  # Replace 'myenv' with your preferred environment name
source myenv/bin/activate  # Use 'activate' on Windows
```
## Installing Dependencies
Once you have activated your virtual environment, you can install the project dependencies using the requirements.txt file.

```
pip install -r requirements.txt
```
This will install all the required packages for the project.

## Contributors 
- [Ashish Meena]()
- [Deepak Goyal]()
- [Divyanshi Rajpurohit]()
- [Diya Vijay](https://github.com/DiyaVj)

## License
This project is open-source and licensed under the [MIT License](https://github.com/DiyaVj/X-sentimental/blob/main/LICENSE).
