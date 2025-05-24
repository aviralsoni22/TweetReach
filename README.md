# TweetReach
This project implements a Twitter bot that sends email notifications to users when tweets containing specified keywords are posted. Users can subscribe to certain keywords, and the bot will monitor Twitter in real-time to alert them whenever matching tweets appear.

## Prerequisites
- Python 3.10
- Anaconda or Miniconda
- Git (optional, if you plan to clone via Git)
- NPM

## Setup Instructions

Follow these steps to set up the project locally on your machine.

### Step 1: Clone the Repository
Open new cmd

Clone the repository using Git:

```bash
git clone https://github.com/aviralsoni22/TweetReach.git
cd TweetReach
```

### Step 2: Create a Virtual Environment
For Windows cmd, use the following command to create a virtual environment
```bash
conda create -p venv python==3.10 -y
```

### Step 3: Activate the virtual environment
```bash
conda activate <Path of venv>
```

### Step 4: Install the required dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Create a .env file in TweetReach folder
Create a .env file and paste the following details: \
```env
EMAIL_SENDER = "" 
EMAIL_PASSWORD = "" 
EMAIL_RECIPIENT = "" 
APP_PASSWORD = "" 
```
NOTE: Make sure to replace the empty strings with your actual credentials.

### Step 6: Open a new command prompt and run the following commands
Don't close the 1st cmd, create a 2nd cmd to run the Twitter API (mock) server.
Navigate to TweetReach folder and run the following commands.
```bash
conda activate <the path of venv>
```
```bash
npm install -g @mockoon/cli
```
```bash
mockoon-cli start --data https://raw.githubusercontent.com/mockoon/mock-samples/main/mock-apis/data/twittercom-current.json
```

### Step 7: Run the application
Navigate to the directory where main.py is located and run the application in the 1st cmd:

```bash
python main.py
```

The code should execute successfully if all configurations are correct. If you encounter any errors, please double-check the details in your .env file to ensure all required environment variables are properly set.




