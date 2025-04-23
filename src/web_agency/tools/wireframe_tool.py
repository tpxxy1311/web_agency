from crewai.tools import tool
from PIL import Image, ImageDraw, ImageFont
import json
import os

@tool("RenderWireframrTool")
def render_wireframe(json_data: str) -> str:
    """
    Erstellt ein Wireframe-Bild aus einer JSON-Beschreibung der UI-Komponenten.
    
    Args:
        json_data (str): JSON-String mit UI-Komponenten und ihren Bounding-Box-Daten.
    
    Returns:
        str: Pfad zur gerenderten PNG-Datei.
    """
    try:
        # JSON-Daten laden
        data = json.loads(json_data)
        components = data.get("components", [])
        
        # Bild erstellen
        width, height = 1024, 720
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)

        # Schriftart für Labels (Standard-Font von PIL nutzen)
        font = None  # Falls PIL keine Standard-Schriftart hat
        
        try:
            font = ImageFont.truetype("arial.ttf", 14)  # Arial nutzen, falls vorhanden
        except IOError:
            pass  # Falls nicht verfügbar, werden Labels ohne spezielle Schriftart gezeichnet

        # UI-Komponenten zeichnen
        for component in components:
            x, y, w, h = component["x"], component["y"], component["width"], component["height"]
            draw.rectangle([x, y, x + w, y + h], outline="black", width=2)

            # Label hinzufügen
            label = component["type"]
            text_x, text_y = x + 5, y + 5
            draw.text((text_x, text_y), label, fill="black", font=font)

        # Bild speichern
        output_path = "wireframes/wireframe_output.png"
        image.save(output_path)

        return f"Wireframe gespeichert unter: {os.path.abspath(output_path)}"

    except Exception as e:
        return f"Fehler beim Rendern des Wireframes: {str(e)}"