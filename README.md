# Zootopia

## 📌 Overview

Zootopia is a web-based application designed to display animal-related data. The project involves:

- A web application for visualizing animal data.
- Dependencies on Python libraries, including:
  - `python-dotenv` (for environment variable management)
  - `pydantic` (for data validation)
  - `requests` (for making API calls)

## 🚀 Getting Started

### 📥 Clone the Repository
```bash
git clone https://github.com/AteetVatan/Zootopia.git
cd Zootopia
```

### 📦 Install Dependencies
```bash
pip install python-dotenv
pip install -U pydantic  # Pydantic module for data validation
pip install requests
```

## Configration
For configration go to config.py and here two constants can be edited.
* [AllOW_USER_INPUT] : Allows user console for search input otherwise [ANIMAL_DEFAULT_SEARCH] 
variable will be used.
* [LOAD_DATA_FROM_API] : To Load data form API calls if False then default [ANIMALS_JSON_DATA_FILE] 
json data will be used.



## Usage

To use this project, run the following command - `python3 zootopia.py`.


## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 📧 Contact

For any inquiries, reach out via [GitHub Issues](https://github.com/AteetVatan/Zootopia/issues).
