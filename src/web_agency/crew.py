from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.wireframe_tool import render_wireframe
from tools.saveimage_tool import save_image_from_url
from tools.startappandscreenshot_tool import run_nextjs_and_screenshot
from crewai_tools import FileWriterTool, CodeDocsSearchTool, DirectoryReadTool, FileReadTool, DallETool, VisionTool
from dotenv import load_dotenv

#Load Environment Variables such as API Keys
load_dotenv()

vision_tool = VisionTool(image_path_url="quality_assurance/screen.png")
# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase

class WebAgency():
	"""WebAgency crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def requirement_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['requirement_analyst'],
			verbose=True,
			memory=True,
			llm='gpt-4o'
		)
	
	@task
	def requirement_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['requirement_analysis_task'],
		)
	
	@agent
	def wireframe_parser(self) -> Agent:
		return Agent(
			config=self.agents_config['wireframe_parser'],
			verbose=True,
			memory=True,
		)
	
	@agent
	def wireframe_visualizer(self) -> Agent:
		return Agent(
			config=self.agents_config['wireframe_visualizer'],
			verbose=True,
		)
	
	@agent
	def wireframe_designer(self) -> Agent:
		return Agent(
			config=self.agents_config['wireframe_designer'],
			verbose=True,
			memory=True,
			max_retry_limit=3,
			llm='gpt-4o'
		)

	@agent
	def wireframe_validator(self) -> Agent:
		return Agent(
			config=self.agents_config['wireframe_validator'],
			verbose=True,
			tools=[FileWriterTool()],
			llm='gemini/gemini-1.5-flash'
		)

	@agent
	def wireframe_file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['wireframe_file_writer'],
			verbose=True,
			tools=[FileWriterTool()],
		)
	
	@agent
	def frontend_software_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['frontend_software_engineer'],
			verbose=True,
			tools=[DirectoryReadTool(directory_path='../../fara.ai-frontend/src')],
			memory=True,
			llm='gpt-4o',
		)
	
	@agent
	def image_asset_designer(self) -> Agent:
		return Agent(
			config=self.agents_config['image_asset_designer'],
			verbose=True,
			tools=[DallETool()],
			llm='gpt-4o',
		)

	@agent
	def nextjs_frontend_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['nextjs_frontend_developer'],
			verbose=True,
			memory=True,
			llm='gpt-4o',
			tools=[
				CodeDocsSearchTool(),
				FileReadTool(file_path='../../knowledge/api_documentation.json')
			],
		)
	
	# @agent
	# def frontend_code_reviewer(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['frontend_code_reviewer'],
	# 		verbose=True,
	# 		memory=True,
	# 		tools=[CodeDocsSearchTool()],
	# 		llm='gemini/gemini-1.5-pro'
	# 	)

	# @agent
	# def frontend_ui_designer(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['frontend_ui_designer'],
	# 		verbose=True,
	#     	memory=True,
	# 		tools=[FileReadTool(file_path='../../fara.ai-frontend/src/app/globals.css')],
	# 		llm='gpt-4o'
	# 	)
	
	# @agent
	# def frontend_file_writer(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['frontend_file_writer'],
	# 		verbose=True,
	# 		tools=[FileWriterTool()],
	# 	)

	# @agent
	# def screenshot_provider(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['screenshot_provider'],
	# 		verbose=True,
	# 		tools=[run_nextjs_and_screenshot]
	# 	)

	@agent
	def ux_qa_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['ux_qa_analyst'],
			verbose=True,
			multimodal=True,
			llm='gpt-4o',
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task

	# @task
	# def requirement_analysis_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['requirement_analysis_task'],
	# 	)

	# @task
	# def define_components_stask(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['define_components_task'],
	# 	)
	
	# @task
	# def generate_wireframe_description_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['generate_wireframe_description_task'],
	# 	)

	# @task
	# def parse_wireframe_components_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['parse_wireframe_components_task'],
	# 	)
	
	# @task
	# def render_wireframe_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['render_wireframe_task'],
	# 		tools=[render_wireframe]
	# 	)

	# @task
	# def wireframe_generation_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['wireframe_generation_task'],
	# 	)
	
	# @task
	# def wireframe_validation_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['wireframe_validation_task'],
	# 	)
	
	# @task
	# def wireframe_file_write_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['wireframe_file_write_task'],
	# 	)

	# @task
	# def plan_component_structure_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['plan_component_structure_task'],
	# 	)
	
	# @task
	# def generate_page_assets_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['generate_page_assets_task'],
	# 	)

	# @task
	# def save_image_asset_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['save_image_asset_task'],
	# 		tools=[save_image_from_url]
	# 	)
	
	# @task
	# def implement_nextjs_components_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['implement_nextjs_components_task'],
	# 	)
	
	# @task
	# def implement_api_calls_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['implement_api_calls_task'],
	# 		tools=[FileReadTool(file_path='../../knowledge/api_documentation.json')]
	# 	)
	
	# @task
	# def validate_nextjs_code_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['validate_nextjs_code_task'],
	# 	)

	# @task
	# def write_nextjs_code_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['write_nextjs_code_task'],
	# 	)
	
	# @task
	# def style_components_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['style_components_task'],
	# 	)
	
	# @task
	# def style_page_layout_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['style_page_layout_task'],
	# 	)

	# @task
	# def write_scss_styles_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['write_scss_styles_task'],
	# 	)
	
	# @task
	# def bind_scss_imports_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['bind_scss_imports_task'],
	# 	)
	
	# @task
	# def take_screenshot_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['screenshot_and_analyze_task'],
	# 	)

	@task
	def analyze_screenshot_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_screenshot_task'],
			tools=[VisionTool()]
		)

	
	@crew
	def crew(self) -> Crew:
		"""Creates the WebAgency crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)

