"""
Simple script to run the Resume Ranker Pro application.
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="localhost",  # Changed from "0.0.0.0" to "localhost" for better compatibility
        port=8000,
        reload=True
    )