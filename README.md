# Cold Email Generator

## Overview
The Cold Email Generator is a Streamlit application designed to generate personalized cold emails based on job descriptions extracted from URLs. It leverages a language model to analyze job postings and create tailored emails that highlight the capabilities of a client.

## Features
- **URL Input**: Users can input a URL pointing to a job listing.
- **Job Extraction**: The application extracts job details such as role, experience, skills, and description from the provided URL.
- **Portfolio Integration**: Queries a portfolio to find relevant links based on the skills required for the job.
- **Email Generation**: Generates a cold email tailored to the job description, showcasing AtliQ's expertise and relevant portfolio links.

## Setup Instructions
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Ensure you have Python installed, and install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Environment Variables**: Create a `.env` file in the `app` directory and set the necessary environment variables, including `GROQ_API_KEY`.
4. **Run the Application**: Start the Streamlit application by running:
   ```bash
   streamlit run app/main.py
   ```

## Usage
- Open the application in your browser.
- Enter a URL to a job listing and click "Submit".
- View the generated cold email, which will be displayed in markdown format.

## File Structure
- `app/main.py`: Entry point of the application.
- `app/chains.py`: Contains the `Chain` class for job extraction and email generation.
- `app/portfolio.py`: Manages and queries the portfolio of projects or skills.
- `app/utils.py`: Utility functions for text cleaning.
- `vectorstore/`: Directory for storing persistent data using ChromaDB.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or support, please contact at joshiaj33@gmail.com
