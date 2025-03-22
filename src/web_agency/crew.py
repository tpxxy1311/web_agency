from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.wireframe_tool import render_wireframe
from crewai_tools import FileWriterTool, CodeDocsSearchTool, DirectoryReadTool, FileReadTool
from dotenv import load_dotenv

load_dotenv()

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

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def requirement_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['requirement_analyst'],
			verbose=True,
			memory=True,
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
		)

	@agent
	def wireframe_file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['wireframe_file_writer'],
			verbose=True,
			tools=[FileWriterTool()],
		)

	@agent
	def wireframe_validator(self) -> Agent:
		return Agent(
			config=self.agents_config['wireframe_validator'],
			verbose=True,
			tools=[FileWriterTool()],
		)
	
	@agent
	def frontend_software_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['frontend_software_engineer'],
			verbose=True,
			tools=[DirectoryReadTool(directory_path='../../fara.ai-frontend/src')],
			memory=True
		)

	@agent
	def nextjs_frontend_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['nextjs_frontend_developer'],
			verbose=True,
			memory=True,
			tools=[CodeDocsSearchTool()]
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task

	@task
	def requirement_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['requirement_analysis_task'],
		)

	@task
	def define_components_task(self) -> Task:
		return Task(
			config=self.tasks_config['define_components_task'],
		)
	
	@task
	def generate_wireframe_description_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_wireframe_description_task'],
		)

	@task
	def parse_wireframe_components_task(self) -> Task:
		return Task(
			config=self.tasks_config['parse_wireframe_components_task'],
		)
	
	@task
	def render_wireframe_task(self) -> Task:
		return Task(
			config=self.tasks_config['render_wireframe_task'],
			tools=[render_wireframe]
		)

	@task
	def wireframe_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['wireframe_generation_task'],
		)
	
	@task
	def wireframe_file_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['wireframe_file_write_task'],
		)

	@task
	def wireframe_validation_task(self) -> Task:
		return Task(
			config=self.tasks_config['wireframe_validation_task'],
		)

	@task
	def plan_component_structure_task(self) -> Task:
		return Task(
			config=self.tasks_config['plan_component_structure_task'],
		)
	
	@task
	def implement_nextjs_components_task(self) -> Task:
		return Task(
			config=self.tasks_config['implement_nextjs_components_task'],
		)

	

	@crew
	def crew(self) -> Crew:
		"""Creates the WebAgency crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
