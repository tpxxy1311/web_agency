from crewai.tools import tool
import requests

@tool("SaveImageFromUrlTool")
def save_image_from_url(image_url: str, file_path: str) -> str:
    """
    Downloads and saves an image from a given URL to a local file path.
    
    Args:
        image_url (str): String-URL with a Link to the generated Image by Dall-E
        file_path (str): Absolute file path where the image has to be safed
    
    Returns:
        str: Path of the safed image, so it can be included in the frontend
    """
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return f"Image saved successfully to {file_path}"
    return f"Failed to download image. Status code: {response.status_code}"

