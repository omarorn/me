"""
Main entry point for Railway deployment.
This file imports and runs the Flask application from lpm_kernel/app.py
"""

import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the app from lpm_kernel
from lpm_kernel.app import app

# This file will be detected by Railway's Railpack
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)