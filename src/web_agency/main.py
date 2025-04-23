#!/usr/bin/env python
import sys
import warnings
from crew import WebAgency
import os
import agentops

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    print("🚀 Crew startet...")  # Debugging-Print
    session = agentops.init(api_key=os.getenv("AGENTOPS_API_KEY")) # Start AgentOps Session
    
    #Collecting User Input
    def get_input(prompt, default):
        user_input = input(f"{prompt} (Default: {default}): ")
        return user_input.strip() if user_input.strip() != "" else default

    inputs = {
        'feature_description': get_input("📝  Describe the feature you'd like to build", "Login screen with email & password input"),
        'functional_requirements': get_input("⚙️  What are the key functional requirements?", "User authentication, error handling for missing fields"),
        'layout_requirements': get_input("🎨  Any layout or design preferences?", "Image on the left, Form on the right, clean and modern UI"),
        'image_asset': get_input("🖼️  Description of the image if an asset needs to be generated", "No"),
        'edge_cases': get_input("🚧  Any specific edge cases or error scenarios to handle?", "Error message on login failure or empty fields"),
        'url_path': get_input("🔎 Under which URL should be the new page accessible?", "/login"),
        'api_call': get_input("📞  Is there an API Endpoint that need to be called for this page?", "No")
    }

    result = WebAgency().crew().kickoff(inputs=inputs)
    
    print(result)

    session.end_session("✅ AgentOps ended") # End AgentOps Session
    print("✅ Crew finished!") # Debugging-Print

if __name__ == "__main__":
    run()

