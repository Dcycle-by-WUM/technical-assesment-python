#!/usr/bin/env python3
"""
Quick setup script for the Python Technical Assessment
"""

import os
import subprocess
import sys


def run_command(command, description):
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False


def main():
    print("🚀 Setting up Python Technical Assessment...")

    # Check if virtual environment exists
    if not os.path.exists("venv"):
        print("📦 Creating virtual environment...")
        if not run_command("python -m venv venv", "Creating virtual environment"):
            return False

    # Activate virtual environment and install dependencies
    if os.name == "nt":  # Windows
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/MacOS
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"

    # Install dependencies
    if not run_command(
        f"{pip_cmd} install -r requirements.txt", "Installing dependencies"
    ):
        return False

    # Create .env file if it doesn't exist
    if not os.path.exists(".env"):
        print("📝 Creating .env file...")
        with open(".env", "w") as f:
            f.write("DATABASE_URL=sqlite:///./test.db\n")
            f.write("SECRET_KEY=your-secret-key-here\n")
            f.write("ALGORITHM=HS256\n")
            f.write("ACCESS_TOKEN_EXPIRE_MINUTES=30\n")
        print("✅ .env file created")

    # Initialize Alembic
    if not os.path.exists("alembic/versions"):
        print("🗄️ Initializing database migrations...")
        if not run_command("alembic init alembic", "Initializing Alembic"):
            return False

    # Run migrations
    if not run_command("alembic upgrade head", "Running database migrations"):
        return False

    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate virtual environment:")
    if os.name == "nt":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Start the server: uvicorn app.main:app --reload")
    print("3. Open http://localhost:8000/docs to see the API documentation")
    print("4. Run tests: pytest")
    print("\n🔍 Remember to look for bugs, security issues, and missing tests!")


if __name__ == "__main__":
    main()
