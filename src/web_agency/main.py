#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
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
    session = agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))
    
    inputs = {
        'user_description' : "A login screen with two input fields mail an password and sumbit button, there should be an error when the login failed or the user sends the form and one input field is missing. There should also be a visual image element on the left"
    }

    result = WebAgency().crew().kickoff(inputs=inputs)
    print(result)
    session.end_session("AgentOps ended")

if __name__ == "__main__":
    run()

