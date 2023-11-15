from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate    
from langchain.chains import LLMChain 
from dotenv import load_dotenv

load_dotenv()
def generate_output(input):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['input'],
        template="{input}" # This is the input from what the user put in from index.html page (the main route /)
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="output") #You can name the output data whatever you want. I named it output for simpliciy sake.
    response = name_chain({'input': input})

    return response