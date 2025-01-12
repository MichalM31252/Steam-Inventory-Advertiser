# Counter-Strike Item Advertiser

A Python-based automation project for advertising Counter-Strike items on websites such as Reddit, Steam Community forums, and multiple Steam groups. This tool utilizes modern Python libraries such as `asyncio`, `selenium`, `requests`, and `threading` for efficient, multi-platform advertising. A MySQL database is used to store and manage all the relevant data.

---

## 🚀 Features

- **Automated Posting**: Seamlessly advertise your Counter-Strike items on multiple platforms, including Reddit, Steam Community forums, and Steam groups.
- **Concurrency and Performance**: Powered by `asyncio` and threading to handle multiple tasks concurrently.
- **Selenium Integration**: Interact with web pages for posting in discussions and groups automatically.
- **MySQL Database**: Store data about items, platform details, and posting history for better management and tracking.
- **Customizable Configuration**: Define platforms, messages, and schedules via config files or command-line arguments.
- **Error Handling**: Robust error-handling mechanisms to ensure smooth operation.
- **Multi-Account Support**: Manage multiple Steam and Reddit accounts for posting rotation.

---

## 📦 Tech Stack

- **Python 3.9+**
  - `asyncio` for asynchronous operations
  - `selenium` for browser automation
  - `requests` for making HTTP requests
  - `threading` for concurrent processes
- **MySQL** for data storage and management

---

## 📋 Requirements

1. Python 3.9+
2. MySQL server
3. Browser driver for Selenium (e.g., ChromeDriver or GeckoDriver)
4. API keys (if required for Reddit or Steam integrations)

---

## 🛠 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cs-item-advertiser.git
   cd cs-item-advertiser
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:

   - Create a database and import the schema from `database/schema.sql`.
   - Configure the database connection in `config.py`.

4. Download the appropriate browser driver for Selenium and add it to your PATH.

---

## ⚙️ Configuration

Modify the `config.py` file to customize:

- **Database Connection**: Set MySQL host, user, password, and database name.
- **Platform Credentials**: Add account credentials for Reddit and Steam.
- **Posting Messages**: Define item descriptions and advertising messages.
- **Schedule**: Set intervals for posting.

Example `config.py`:

```python
DATABASE = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "cs_items"
}

REDDIT_CREDENTIALS = {
    "username": "your_reddit_username",
    "password": "your_reddit_password"
}

STEAM_CREDENTIALS = {
    "username": "your_steam_username",
    "password": "your_steam_password"
}

POSTING_MESSAGE = "Check out this awesome CS:GO item! [Your Item Link Here]"
```

---

## 🖥️ Usage

1. Start the application:

   ```bash
   python main.py
   ```

2. Logs will show the status of posting, errors, and database updates.

---

## 📊 Database Schema

The project uses a MySQL database with the following schema:

- **items**: Stores details about Counter-Strike items (name, link, description).
- **platforms**: Stores platform details (name, URL, login credentials).
- **posting_history**: Tracks where and when each item was posted.

Refer to the `database/schema.sql` file for details.

---

## 🛡️ Safety and Ethics

- Ensure compliance with the terms of service for platforms like Reddit and Steam.
- Use the tool responsibly and avoid spamming or abusing platform rules.

---

## 🤝 Contributions

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request with a detailed description of your changes.

---

## 🐛 Issues

If you encounter any issues or bugs, please [open an issue](https://github.com/yourusername/cs-item-advertiser/issues).

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💡 Future Enhancements

- Add support for additional platforms.
- Implement advanced analytics for tracking post engagement.
- Integrate CAPTCHA-solving tools for platforms requiring user verification.

---

## 🙌 Acknowledgments

Special thanks to the developers and maintainers of Python, Selenium, and MySQL for making this project possible.
