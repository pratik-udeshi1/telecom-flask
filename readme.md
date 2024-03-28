# Flask - Telecom APP

This Flask application provides APIs for user registration, retrieving user information, and upgrading user plans. It utilizes SQLAlchemy for database operations and provides endpoints for interacting with user data.

## Setup

1. **Installation**: Ensure you have Python and Flask installed. You can install Flask using pip:
   ```
   pip install Flask
   ```

2. **Database Configuration**: This app uses PostgreSQL as the database. Make sure you have PostgreSQL installed and running. Update the database configurations in `config.py` if necessary.

3. **Dependencies**: Install the required dependencies by creating a Conda environment and installing the packages listed in the `requirements.txt` file:

   - **Create Conda Environment**:
     ```
     conda create --name myenv
     ```

   - **Activate Environment**:
     ```
     conda activate myenv
     ```

   - **Install Dependencies**:
     ```
     conda install --file requirements.txt
     ```

4. **Database Initialization**: Initialize the database by running the following commands:
   ```
   flask db upgrade; flask db migrate;
   ```

5. **Custom Plans**: Run the script `add_custom_plans.py` to add custom plans to the database:
   ```
   python add_custom_plans.py
   ```

## Usage

1. **User Registration**: To register a new user, send a POST request to `/user/register` endpoint with JSON data containing user details such as name, date of birth, email, Aadhar number, mobile number, and selected plan.

   Example:
   ```
   POST /user/register
   {
       "name": "John Doe",
       "dob": "01-01-1990",
       "email": "john@example.com",
       "aadhar_number": "123456789012",
       "mobile_number": "9876543210",
       "plan": "Platinum365"
   }
   ```

2. **Get All Users**: Retrieve all users by sending a GET request to `/users` endpoint.

   Example:
   ```
   GET /users
   ```

3. **Upgrade User Plan**: Upgrade a user's plan by sending a PATCH request to `/user/<user_id>/plan_upgrade` endpoint with the user's ID and the new plan.

   Example:
   ```
   PATCH /user/<user_id>/plan
   {
       "plan": "Gold180"
   }
   ```

## Error Handling

- If there are any validation errors during user registration or plan upgrade, appropriate error messages along with error details will be returned.
- In case of any internal server errors, a 500 status code with an error message will be returned.

---