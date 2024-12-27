# 🛢 GenAI App - Chat With SQL DB



A Streamlit web application that enables users to chat with their SQL databases using LangChain's SQLKit and agent types. This app provides a seamless interface to interact with your database, ask questions, and retrieve meaningful insights. It also maintains a chat history for better context and user experience.


## 🚀 Features

- **Chat with SQL Databases**: Supports both local databases and remote connections.
- **Flexible Database Selection**: Users can either:
  - Select a local database file.
  - Provide connection details (host, user, password, and database name).
- **AI-Powered Querying**: Uses LangChain SQLKit and agent types to process natural language queries and fetch relevant data from the database.
- **Chat History**: Keeps track of the conversation for improved context and user engagement.
- **Streamlit Interface**: User-friendly and interactive web application for quick setup and usage.


## 🛠️ Tech Stack

- **Streamlit**: Framework for building the web application.
- **LangChain**: Framework for integrating large language models with SQL databases.
- **Python**: Core programming language for the app.
- **SQL Databases**: Compatible with SQLite, MySQL, PostgreSQL, and more.


## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/chat-with-sql-db.git
cd chat-with-sql-db
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```


## 🧩 How It Works

1. **Database Connection**:
   - Select a local database file (e.g., `.db` for SQLite).
   - OR, provide host, username, password, and database name for remote SQL servers.

2. **Natural Language Query**:
   - Ask questions in plain English (e.g., "What are the top 10 customers by sales?").
   - The app converts your question into SQL queries and executes them on the database.

3. **Chat History**:
   - All user queries and responses are saved in a chat history panel for reference.


## 🔧 Configuration

### Environment Variables (Optional)
Create a `.env` file to store your database credentials securely:
```env
DB_HOST=your-host
DB_USER=your-username
DB_PASSWORD=your-password
DB_NAME=your-database
```

The app will use these credentials when no input is provided manually.


## ⚡ Benefits

- Simplifies database querying with natural language.
- Supports multiple database types and configurations.
- Maintains a context-rich chat history for user convenience.
- Quick setup with minimal configuration.


## 🚧 Future Enhancements

- Add support for NoSQL databases (e.g., MongoDB).
- Integrate advanced visualizations for query results.
- Improve chat history with export options (e.g., download as `.txt` or `.csv`).
- Support multiple concurrent database connections.



## 🤝 Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements or suggestions.


## 🌟 Acknowledgments

- **Streamlit** for enabling rapid development of interactive web apps.
- **LangChain** for its robust integration of language models with SQL databases.
- **SQL Databases** for being the backbone of data-driven applications.
