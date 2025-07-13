# KPA Forms API - Assignment Submission
**Technologies:** FastAPI, PostgreSQL, SQLAlchemy, Pydantic

## Assignment Overview

This project implements **2 APIs** from the provided KPA_form_data Postman collection:

1. **POST /api/forms/wheel-specifications** - Submit wheel specification forms
2. **GET /api/forms/wheel-specifications** - Retrieve wheel specifications with filtering

The implementation provides exact response formats matching the original Postman collection specifications.

## Tech Stack

- **Backend Framework:** FastAPI 0.104.1
- **Database:** PostgreSQL 15 (Docker container on EC2)
- **ORM:** SQLAlchemy 2.0.23 (with automatic table creation)
- **Validation:** Pydantic 2.5.0
- **Python Version:** 3.8+

## How to Set Up the Project

### Prerequisites
- Python 3.8 or higher
- Access to PostgreSQL Docker container on EC2
- Your EC2 public IP or hostname

### Step 1: Clone and Setup Environment
```bash
# Clone the repository
git clone <repository-url>
cd kpa_assignment

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Database Configuration

**Your PostgreSQL Database Setup:**
1. DATABASE_URL= YOUR_DATABASE_URL

### Step 3: Verify Database Connection
```bash
# Test database connectivity (optional)
python -c "from app.database import test_connection; test_connection()"

# Should output: "Database connection successful!"
```

**Note:** Database tables are created automatically when the application starts for the first time.

### Step 4: Run the Application
```bash
# Start the FastAPI server (tables will be created automatically)
python -m app.main
```

**The application will:**
1. Test database connection
2. Create tables automatically if they don't exist
3. Start the FastAPI server
4. Display success messages and documentation URLs

### Step 5: Access the API
- **API Base URL:** http://localhost:8000
- **Swagger Documentation:** http://localhost:8000/docs
- **ReDoc Documentation:** http://localhost:8000/redoc

## Key Features Implemented

### 1. Exact API Response Format
- Implements precise response structure from Postman collection
- Standard format: `{success: boolean, message: string, data: object}`
- Correct HTTP status codes (201 for POST, 200 for GET)

### 2. Complete Wheel Specification Management
- **POST API:** Accepts 15 technical specification fields
- **GET API:** Retrieves records with optional filtering
- **Field Validation:** Pydantic schemas ensure data integrity
- **Unique Constraints:** Prevents duplicate form numbers

### 3. Advanced Filtering Capabilities
- Filter by `formNumber`, `submittedBy`, `submittedDate`
- Support for multiple simultaneous filters
- Returns empty array for no matches (not error)

### 4. Professional Data Examples
- Realistic dummy data in Swagger UI for easy testing
- Authentic railway terminology and specifications
- Professional user IDs and form numbering

### 5. Robust Error Handling
- Duplicate form number validation
- Database connection error handling
- Comprehensive input validation
- Meaningful error messages

### 6. Database Design
- Optimized PostgreSQL schema for railway data
- Separate storage for all 15 technical fields
- Audit trails with created/updated timestamps
- Proper indexing for performance

### 7. API Documentation
- Auto-generated Swagger/OpenAPI documentation
- Interactive testing interface
- Complete request/response examples
- Professional API descriptions

## API Endpoints Details

### POST /api/forms/wheel-specifications
**Purpose:** Submit new wheel specification form

**Request Body:**
```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "inspector_raj_001",
  "submittedDate": "2025-07-13",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)",
    ... // 11 more technical fields
  }
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "inspector_raj_001",
    "submittedDate": "2025-07-13",
    "status": "Saved"
  }
}
```

### GET /api/forms/wheel-specifications
**Purpose:** Retrieve wheel specifications with optional filtering

**Query Parameters:**
- `formNumber` (optional): Filter by specific form number
- `submittedBy` (optional): Filter by submitter user ID
- `submittedDate` (optional): Filter by submission date

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "inspector_raj_001",
      "submittedDate": "2025-07-13",
      "fields": {
        "treadDiameterNew": "915 (900-1000)",
        "lastShopIssueSize": "837 (800-900)",
        "condemningDia": "825 (800-900)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ]
}
```

## Testing the APIs

### Using Swagger UI (Recommended)
1. Start the application: `python -m app.main`
2. Open http://localhost:8000/docs
3. Use "Try it out" with pre-filled professional examples
4. Test both POST and GET endpoints

### Using Postman
1. Import the provided `postman_collection.json`
2. Set base URL to `http://localhost:8000`
3. Run test requests with example data

### Using curl
```bash
# Test POST
curl -X POST "http://localhost:8000/api/forms/wheel-specifications" \
  -H "Content-Type: application/json" \
  -d '{"formNumber": "WHEEL-2025-001", "submittedBy": "inspector_raj_001", "submittedDate": "2025-07-13", "fields": {"treadDiameterNew": "915 (900-1000)"}}'

# Test GET
curl "http://localhost:8000/api/forms/wheel-specifications?formNumber=WHEEL-2025-001"
```

## Limitations and Assumptions

### Limitations
1. **Partial GET Response:** GET endpoint returns only 4 fields (treadDiameterNew, lastShopIssueSize, condemningDia, wheelGauge) as per original API specification, not all 15 fields
2. **No Authentication:** APIs are public endpoints without authentication mechanism
3. **String Storage:** All technical fields stored as strings to match API specification format
4. **No File Upload:** Current implementation doesn't support document attachments
5. **Basic Error Responses:** Limited error detail for security reasons

### Assumptions Made
1. **Date Format:** Assumed string format for dates (e.g., "2025-07-13") as per Postman examples
2. **Form Number Uniqueness:** Assumed form numbers must be unique across all submissions
3. **Field Optionality:** All technical specification fields are optional in POST request
4. **Filter Logic:** GET filters use exact string matching (case-sensitive)
5. **Database Location:** Assumed PostgreSQL container is accessible from local machine
6. **Numeric Ranges:** Technical values stored as strings with ranges (e.g., "915 (900-1000)") as per specification

### Design Decisions
1. **SQLAlchemy ORM:** Chosen for better maintainability over raw SQL
2. **Pydantic Validation:** Ensures type safety and automatic API documentation
3. **Separate Models:** Used distinct models for database and API schemas
4. **Environment Configuration:** All sensitive data in .env file for security
5. **Professional Examples:** Used realistic Indian Railways terminology for credibility

## Database Schema

The application automatically creates the required database tables on startup.

### wheel_specifications Table
- **Primary Key:** `id` (auto-increment)
- **Unique Constraint:** `form_number`
- **Indexes:** `form_number`, `submitted_by`, `submitted_date`
- **Technical Fields:** All 15 specification fields stored as VARCHAR columns
- **Audit Fields:** `created_at`, `updated_at` timestamps

### Automatic Table Creation
- Tables are created automatically when the application starts
- Uses SQLAlchemy `Base.metadata.create_all()` method
- Only creates tables if they don't already exist
- No manual database setup required

## 🎉 Assignment Completion Status

**Requirement 1:** Implemented 2 APIs from Postman collection  
**Requirement 2:** Exact request/response structure matching  
**Requirement 3:** PostgreSQL database integration  
**Requirement 4:** FastAPI framework with proper documentation  
**Requirement 5:** Input validation and error handling  
**Requirement 6:** Environment-based configuration  
**Requirement 7:** Working Postman collection provided  
**Requirement 8:** Comprehensive README with setup instructions  
