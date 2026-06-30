import subprocess
import sys
import os

def run_app():
    print("=" * 50)
    print("🤝 Personalized Networking Assistant")
    print("=" * 50)
    print("\n✅ Starting FastAPI Backend...")
    print("✅ Starting Streamlit Frontend...")
    print("\n📌 Backend API Docs: http://127.0.0.1:8000/docs")
    print("📌 Frontend App:     http://localhost:8501")
    print("\n⚠️  Press Ctrl+C to stop both servers")
    print("=" * 50)

    backend = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--reload", "--port", "8000"],
        cwd=os.path.join(os.getcwd(), "backend")
    )

    frontend = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "frontend.py"]
    )

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down servers...")
        backend.terminate()
        frontend.terminate()

if __name__ == "__main__":
    run_app()