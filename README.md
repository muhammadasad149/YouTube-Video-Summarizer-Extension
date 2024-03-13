# YouTube Video Summarizer Extension

This Chrome extension allows users to summarize YouTube video content by providing a link to the video. The extension communicates with a FastAPI backend to process the video transcript and generate a summary using Google's Generative AI.

## Features

- Summarize YouTube video content by providing the video URL.
- Customize the length of the summary in words.
- Uses Google's Generative AI to generate the summary.
- Handles errors gracefully.

## Installation

1. Clone this repository to your local machine.
2. Open Chrome and navigate to `chrome://extensions/`.
3. Enable Developer mode (toggle switch usually located in the top-right corner).
4. Click on "Load unpacked" and select the directory where you cloned the repository.

## Usage

1. Click on the extension icon in the Chrome toolbar.
2. Enter the YouTube video URL in the input field.
3. Specify the desired length of the summary (in words) using the number input.
4. Click on the "Summarize" button.
5. Wait for the summary to be generated.
6. The summary will be displayed below the input fields.

## Backend Setup

1. Install Python 3.x if not already installed.
2. Navigate to the `backend` directory.
3. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up a Google API key and add it to a `.env` file in the `backend` directory:
   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```
5. Run the FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
