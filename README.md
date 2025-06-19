# Python Technical Assessment (1 Hour)

## Overview
This is a 1-hour technical assessment to evaluate your Python development skills. You will be working with a **Task Management API** that has several intentional issues that need to be identified and fixed.

## Your Mission
You have **1 hour** to identify and fix the following issues in the codebase:

### 🐛 Bug Fixes (3 bugs to find and fix)
- There are 3 intentional bugs in the code that prevent the API from working correctly
- You need to identify and fix them (including one particularly challenging performance bug)

### 🔒 Security Issues (1 security threat)
- There's a security vulnerability in the code
- Find and fix it following security best practices

### 🚀 Performance Issues (1 N+1 query problem)
- There's a database performance issue that causes inefficient queries
- Identify and optimize the database queries

### 📝 Code Quality Issues
- Missing type hints in several functions
- Add proper type annotations where needed

### 🧪 Missing Tests
- Some critical functionality is missing unit tests
- Add the missing tests to ensure proper coverage

## Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL (or SQLite for quick testing)

### Quick Setup
1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Unix) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `env.example` to `.env` and configure your database
6. Run migrations: `alembic upgrade head`
7. Start the server: `uvicorn app.main:app --reload`

## What You Need to Do

### 1. Run the Application
First, try to run the application.

### 2. Identify and Fix Issues
Look for:
- **Bugs**: Code that doesn't work as expected
- **Security Issues**: Hardcoded secrets, missing validation, etc.
- **Performance Issues**: Inefficient database queries (N+1 problem) and memory leaks
- **Missing Type Hints**: Functions without proper type annotations
- **Missing Tests**: Critical functionality without test coverage

### 3. Document Your Findings
Create a brief report explaining:
- What issues you found
- How you fixed them
- Any additional improvements you made

## Evaluation Criteria

### Problem Solving (35%)
- Ability to identify and fix bugs
- Understanding of error messages and debugging

### Security Awareness (20%)
- Recognition of security vulnerabilities
- Implementation of proper security fixes

### Performance Awareness (15%)
- Recognition of database performance issues
- Implementation of proper query optimization

### Code Quality (15%)
- Adding proper type hints
- Following Python best practices

### Testing (15%)
- Writing appropriate unit tests
- Understanding of test coverage

## Submission
After 1 hour, submit:
1. Your fixed code
2. A brief report of issues found and fixes applied
3. Any additional improvements you made

## Tips
- Start by trying to run the application
- Check the logs for error messages
- Look for hardcoded values that should be environment variables
- Examine the test files to see what's missing
- Look for inefficient database queries in loops
- Pay attention to memory usage patterns
- Focus on the most critical issues first

Good luck! ⏰
