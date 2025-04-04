from crewai.tools import tool
import subprocess
import time
import requests
from pathlib import Path
from playwright.sync_api import sync_playwright

@tool("Next.js App Screenshot Tool")
def run_nextjs_and_screenshot(
    project_path: str = "../../fara.ai-frontend",
    url_path: str = "/",
    wait_time: int = 30
) -> str:
    """
    Starts the Next.js development server, navigates to a specified route, captures a screenshot,
    and saves it into the CrewAI project's 'Quality Assurance' directory.

    Args:
        project_path (str): Absolute or relative path to the Next.js project directory.
        url_path (str): Path of the page to screenshot (e.g. "/login", "/dashboard").
        wait_time (int): Time in seconds to wait for the dev server to be available.

    Returns:
        str: A success message with screenshot path or an error message if something fails.
    """
    try:
        project_abs_path = Path(project_path).resolve()
        crew_root_path = Path.cwd().resolve()
        qa_dir = crew_root_path / "quality assurance"
        qa_dir.mkdir(parents=True, exist_ok=True)  # ✅ Ensure the QA folder exists

        # Start the Next.js dev server using Windows-compatible shell command
        process = subprocess.Popen(
            "npm run dev",
            cwd=project_abs_path,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
            shell=True
        )

        print("⏳ Waiting for the dev server to become available...")
        for _ in range(wait_time):
            try:
                res = requests.get("http://localhost:3000")
                if res.status_code == 200:
                    break
            except:
                time.sleep(1)
        else:
            process.terminate()
            return "❌ Could not reach http://localhost:3000 after waiting."

        # Create a clean filename based on the requested URL path
        clean_path = url_path.strip("/").replace("/", "_") or "homepage"
        screenshot_path = qa_dir / f"screenshot_{clean_path}.png"

        # Take the screenshot using Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            full_url = f"http://localhost:3000{url_path}"
            page.goto(full_url)
            page.screenshot(path=str(screenshot_path))
            browser.close()

        process.terminate()
        return f"✅ Screenshot of '{url_path}' saved at: {screenshot_path}"

    except Exception as e:
        return f"❌ Error while executing the screenshot tool: {str(e)}"
