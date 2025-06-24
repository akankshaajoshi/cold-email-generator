from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
os.environ.get("GROQ_API_KEY")

class Chain:
    def __init__(self):
        self.llm = init_chat_model("llama3-8b-8192", model_provider="groq")

    def extract_jobs(self, data):
        parser = JsonOutputParser()

        job_template = """
            SCRAPED TEXT FROM WEBSITE:
            {page_content}

            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the 
            following keys: `role`, `experience`, `skills`, and `description` with string values.
            ONLY RETURN VALID JSON OBJECT, NOTHING ELSE OR I WILL SHUT YOU DOWN!!!
        """

        prompt_template = ChatPromptTemplate.from_template(job_template)
        prompt = prompt_template.invoke({"page_content": data})

        try:
            result = self.llm.invoke(prompt)
            result = parser.parse(result.content)
            return result
        except Exception as e:
            print(f"Error parsing response: {e}")
            return []

    def write_mail(self, job, links):
        mail_template =   """
            ### JOB DESCRIPTION:
            {job}
            
            ### INSTRUCTION:
            You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a human like cold email to the client regarding the job mentioned above describing the capability of AtliQ 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Atliq's portfolio to the message: {link_list}
            Remember you are Mohan, BDE at AtliQ. 
            Do not provide a preamble.
            ### NO OTHER TEXT, JUST THE SENDABLE EMAIL OR I WILL SHUT YOU DOWN!!!
        """

        prompt_template = ChatPromptTemplate.from_messages(
            [("system", mail_template)]
        )
        prompt = prompt_template.invoke({"job": str(job), "link_list": links})
        response = self.llm.invoke(prompt)
        return response.content