# GetToKnow

GetToKnow is an AI-based web application that provides LinkedIn profile information based on a user's name. It uses the `LangChain` library for processing and integrating AI capabilities. This guide will help you set up and run the project locally. It also uses services like Google Custom Search, SerpApi, and Proxycurl to fetch LinkedIn profile information.

## Project Structure

```bash
GetToKnow/
├── .env
├── .gitignore
├── agents/
│ ├── linkedin_lookup_agent.py
│ ├── tools_for_agent/
│ │ ├── tools_search.py
│ │ ├── init.py
├── app.py
├── LICENSE
├── matamata.py
├── output_parser.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── templates/
│ ├── index.html
├── third_party/
│ ├── linkedin.py
```


## Prerequisites

- Python 3.8 or higher
- Pipenv for dependency management

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/hilmiatha/GetToKnow.git
    cd GetToKnow
    ```

2. **Install dependencies:**

    Ensure you have Pipenv installed. If not, install it using:

    ```bash
    pip install pipenv
    ```

    Then, install the project dependencies:

    ```bash
    pipenv install
    ```

3. **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add your environment variables. At a minimum, you need to add these API credentials or any other necessary configurations.

    ```env
    GOOGLE_API_KEY=yourkey
    PROXYCURL_API_KEY=yourkey
    SERPAPI_API_KEY=yourkey
    ```

## Running the Application

1. **Activate the virtual environment:**

    ```bash
    pipenv shell
    ```

2. **Run the Flask application:**

    ```bash
    python app.py
    ```

    The application will start, and you can access it at `http://0.0.0.0:8000`.

## Project Files

- **`app.py`**: Main application file that sets up the Flask server and routes.
- **`matamata.py`**: Contains the `cari_linkedin` function for fetching LinkedIn data.
- **`agents/`**: Contains agents for looking up LinkedIn profiles.
- **`templates/`**: Contains HTML templates for the front end.
- **`third_party/`**: Contains third-party libraries and modules.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
