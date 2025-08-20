# AI Resume Scorer

A modern web application that provides instant AI-powered resume analysis and feedback using Google's Gemini AI. Get professional insights on your resume's clarity, grammar, professionalism, and ATS-friendliness with personalized improvement suggestions.

## Features

- **AI-Powered Analysis**: Uses Google Gemini 2.5 Flash for intelligent resume evaluation
- **Multiple Input Methods**: 
  - Paste resume text directly
  - Upload PDF files with drag & drop support
- **Comprehensive Scoring**: Evaluates clarity, grammar, professionalism, and ATS-friendliness
- **Improvement Suggestions**: Optional detailed recommendations for enhancement
- **Role Matching**: Suggests suitable job roles based on resume content
- **Modern UI**: Beautiful gradient design with smooth animations and responsive layout
- **File Validation**: Ensures only PDF files are uploaded
- **Loading States**: Visual feedback during analysis

## Quick Setup

### Prerequisites
- Python 3.7+
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai_resume_scoring.git
   cd ai_resume_scoring
   ```

2. **Run the quick setup script (Windows)**
   ```bash
   quicksetup.bat
   ```
   This will:
   - Create a virtual environment
   - Install required dependencies
   - Create a `.env` file template

3. **Configure your API key**
   - Edit the `.env` file and replace `your_api_key_here` with your actual Google Gemini API key
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

### Manual Setup

If you prefer manual setup:

1. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create environment file**
   ```bash
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

4. **Update your API key** in the `.env` file

## Usage

1. **Access the application** at `http://localhost:5000`
2. **Choose your input method**:
   - **Text Input**: Paste your resume content directly
   - **File Upload**: Drag & drop or click to upload a PDF resume
3. **Optional**: Check "Request Improvements" for detailed suggestions
4. **Click "Analyze Resume"** and wait for AI-powered feedback
5. **Review results** including:
   - Overall score (1-10)
   - Individual category scores
   - Improvement suggestions (if requested)
   - Suitable job roles

## Technology Stack

- **Backend**: Flask (Python web framework)
- **AI Engine**: Google Gemini 2.5 Flash API
- **PDF Processing**: PyPDF2
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Modern gradient design with glassmorphism effects
- **Environment**: python-dotenv for configuration

## Project Structure

```
ai_resume_scoring/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── quicksetup.bat     # Windows setup script
├── README.md          # Project documentation
├── .env              # Environment variables (create this)
├── templates/
│   └── index.html    # Main web interface (includes embedded CSS/JS)
├── static/
│   └── style.css     # Additional stylesheet (optional)
└── venv/            # Virtual environment (created by setup)
```

## Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Getting a Gemini API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file

## UI Features

- **Responsive Design**: Works on desktop and mobile devices
- **Drag & Drop**: Modern file upload with visual feedback
- **Loading States**: Animated spinner during analysis
- **Error Handling**: User-friendly error messages
- **Smooth Animations**: Hover effects and transitions
- **Glassmorphism**: Modern translucent design elements

## Security Features

- **Input Validation**: Ensures only PDF files are processed
- **Content Filtering**: AI system prompt prevents processing non-resume content
- **Error Handling**: Graceful handling of API failures and invalid inputs
- **Environment Variables**: Secure API key storage

## Troubleshooting

### Common Issues

1. **"GEMINI_API_KEY not set" error**
   - Ensure you've created the `.env` file
   - Verify your API key is correctly set in the `.env` file
   - Make sure there are no spaces around the equals sign

2. **PDF upload not working**
   - Ensure the file is a valid PDF
   - Check file size (very large files may timeout)
   - Try refreshing the page and uploading again

3. **No response from Gemini**
   - Verify your API key is valid and has quota remaining
   - Check your internet connection
   - Try again after a few moments

4. **Application won't start**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

## Development

To contribute or modify the application:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### Code Structure
- `app.py`: Main Flask routes and AI integration
- `templates/index.html`: Frontend interface with embedded CSS/JS
- `requirements.txt`: Python package dependencies

## License

This project is open source. Feel free to use, modify, and distribute according to your needs.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## Future Enhancements

- [ ] Support for more file formats (DOCX, TXT)
- [ ] Resume template suggestions
- [ ] Export analysis results as PDF
- [ ] User accounts and history
- [ ] Batch processing for multiple resumes
- [ ] Integration with job boards for role matching
- [ ] Dark mode toggle
- [ ] Multi-language support

---

Built with ❤️ using Flask and Google Gemini AI