from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# from langchain.agents import load_tools
from langchain_community.agent_toolkits.load_tools import load_tools

from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv


load_dotenv()


def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)

    # Перший ланцюг: Генерація імені
    propmpt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} pet, it is {pet_color} in color. Suggest me five cool names for my pet.",
    )
    name_chain = LLMChain(llm=llm, prompt=propmpt_template_name)
    name_response = name_chain.invoke(
        {"animal_type": animal_type, "pet_color": pet_color}
    )

    # Виведення сирого результату для перевірки
    print("Raw names response:\n", name_response["text"])

    # Очищення та розділення імен, якщо вони повертаються в одному рядку
    names = name_response["text"].strip().split("\n")

    if (
        len(names) == 1
    ):  # Якщо всі імена в одному рядку, спробуємо розділити за іншими розділювачами
        names = names[0].split(" ")

    formatted_names = "\n".join([name.strip() for name in names if name])

    # Другий ланцюг: Генерація характеру тварини
    prompt_template_character = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} that is {pet_color} in color. Describe its personality in one sentence.",
    )
    character_chain = LLMChain(llm=llm, prompt=prompt_template_character)
    character_response = character_chain.invoke(
        {"animal_type": animal_type, "pet_color": pet_color}
    )
    character_description = character_response["text"].strip()

    # Третій ланцюг: Опис імені та характеру тварини
    prompt_template_description = PromptTemplate(
        input_variables=["name", "character"],
        template="The pet's name is {name}. {character}. Create a cool tagline for this pet.",
    )
    description_chain = LLMChain(llm=llm, prompt=prompt_template_description)
    description_response = description_chain.invoke(
        {"name": names[0].strip(), "character": character_description}
    )
    final_description = description_response["text"].strip()

    return formatted_names, character_description, final_description


def langchain_agent():
    llm = OpenAI(temperature=0.7)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agent.run("What is the average age of a cat? Multiply the age by 3")

    print(result)


if __name__ == "__main__":
    pet_type = "cat"
    pet_color = "black"

    names, character, final_tagline = generate_pet_name(pet_type, pet_color)

    # Виведення результату у читабельній формі
    print("Here are some cool names for your pet:\n")
    print(names)
    print("\nPersonality of your pet:\n")
    print(character)
    print("\nCool tagline for your pet:\n")
    print(final_tagline)

    langchain_agent()
