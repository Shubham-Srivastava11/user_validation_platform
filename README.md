# User Validation Platform

A Python-based user validation platform that validates user data from CSV files and stores it in a database. Supports both email and phone number validation with both synchronous and asynchronous processing modes.

**NOTE: few files are also included just for the mocking purpose. It's not a good practice to push sensitive information**

## Features

- CSV data provider for user import
- Email validation
- Phone number validation
- SQLite and MySQL database support
- Synchronous and asynchronous pipeline execution
- Typer CLI interface

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- MySQL (optional, for MySQL database support)

## Installation

1. **Clone the repository** :
   ```bash
   git clone <repository-url>
   cd user_validation_platform
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   
   Create a `.env` file in the project root with the following variables:
   
   ```env
   # Database Configuration
   DB_TYPE=sqlite  # Use 'mysql' for MySQL database
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=password
   DB_NAME=user_validation
   ```

## Configuration

### Database Options

#### SQLite (Default)
```env
DB_TYPE=sqlite
```
- No additional setup required
- Database file: `user_validation.db`

#### MySQL
```env
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=user_validation
```

## Usage

### Basic Usage

Run the validation pipeline with a LinkedIn profile:

```bash
python -m app.main run "linkedin-profile-url"
```

Example:
```bash
python -m app.main run "shubham-srivastava"
```

### Command Line Interface

The application uses Typer for CLI commands. Available commands:

```bash
# Run validation with LinkedIn profile
python -m app.main run <linkedin_profile> / python -m app.main <linkedin_profile>

# Get help
python -m app.main --help
```

## Running the Application

### Option 1: Using Python module
```bash
python -m app.main run "shubham-srivastava"
```

### Option 2: Using the main script
```bash
python app/main.py run "shubham-srivastava"
```

### Option 3: With Typer CLI
```bash
typer app/main.py run "shubham-srivastava"
```

## Sample Data

The project includes a sample CSV file at `data/users.csv` with the following structure:

```csv
linkedin,name,emails,phones
shubham-srivastava,Shubham Srivastava,shubham@gmail.com;shubham.s@company.com,9876543210;9123456789
himanshu-dubey,Himanshu Dubey,hd@gmail.com,9988776655;7896786534
ridhiman-singh,Ridhiman Singh,bunny@gmail.com:r.singh@company.com,9873456321
```

## Development

### Adding New Validators

1. Create a new validator class in `app/infrastructure/validators/`
2. Implement the validation logic
3. Register the validator in the pipeline service

