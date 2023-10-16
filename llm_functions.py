from helpers import create_simple_openai_chat_completion


def generate_search_terms(prompt):
    search_term_list = create_simple_openai_chat_completion(
        system_message="You are helping the user to generate search terms that are relevant to their problem or query. Please generate a creative, useful, mutually-exclusive, and collectively-exhaustive list of search terms that the user can use to find relevant tools and repositories. Respond with a list of search terms, single line, sepearted by commas",
        user_message=f"Generate search terms to find tools and repositories to help with: {prompt}"
    ).split(",")
    return search_term_list

print (generate_search_terms("I want to find a tool that helps me with data cleaning"))

def analyze_results(prompt, results):
    processed_results_string = create_simple_openai_chat_completion(
        system_message="""You are helping the user to find tools and repositories relevant to their query. Here is a list of GitHub repositories that may be relevant. From this list, please respond with a list of the 10 most relevant repositories, based on the quality of the README, number of stars, and your interpretation of the relevance to the user's query. 
        
        Respond with a list of 10 repositories, each one in this format: 
        Title: <title>, URL: <url>
        <Your of how the user could use this repository to address their query, based on the readme and their original query>
        """,

        user_message="""Here is the issue or problem the user is trying to address: {prompt}. 
        
        Here is the list of GitHub repositories and data that you found: {results}""",

        model="gpt-3.5-turbo-16k"
    )
    
    # Placeholder function for LLM call
    # Returns categorized results and top relevant ones
    return processed_results_string
