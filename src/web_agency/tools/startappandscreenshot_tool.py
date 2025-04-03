from crewai.tools import tool
import subprocess
import time
import requests
from pathlib import Path
from playwright.sync_api import sync_playwright

@tool("Next.js App Screenshot Tool")
def run_nextjs_and_screenshot(project_path: str = "../../fara.ai-frontend", wait_time: int = 30) -> str:
    """
    Starting the Next.js Development Server and to take and safe a Screenshot Image of the Site
    
    Args:
        project_path (str): String-URL with a Link to the generated Image by Dall-E
        wait_time (int): Absolute file path where the image has to be safed
    
    Returns:
        str: Path of the safed image, so it can be analyzed by an other agent
    """
    try:
        project_abs_path = Path(project_path).resolve()

        # ✅ Starting Windows Subrpocess with the shell
        process = subprocess.Popen(
            "npm run dev",
            cwd=project_abs_path,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
            shell=True
        )

        print("⏳ Waiting for local server to start...")
        # Waiting till the server is really online
        timeout = 30  #Seconds
        for _ in range(timeout):
            try:
                res = requests.get("http://localhost:3000")
                if res.status_code == 200:
                    break
            except:
                time.sleep(1)
        else:
            process.terminate()
            return "❌ Server under http://localhost:3000 not accessible."

        screenshot_path = str(project_abs_path / "screenshot.png")
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("http://localhost:3000")
            page.screenshot(path=screenshot_path)
            browser.close()

        process.terminate()
        return f"✅ Screenshot saved under: {screenshot_path}"

    except Exception as e:
        return f"❌ Error while executing this tool: {str(e)}"
