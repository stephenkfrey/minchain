from helpers import create_simple_openai_chat_completion


def generate_search_terms(prompt):
    search_term_list = create_simple_openai_chat_completion(
        system_message="You are helping the user to generate search terms that are relevant to their problem or query. Please generate a creative, useful, mutually-exclusive, and collectively-exhaustive list of search terms that the user can use to find relevant tools and repositories. Think about synonyms for the terms, as well as even more general tools that could be involved. For example, if the user searches for 'frontend code generation', you may search for 'automated code generation agents', since these tools may be applied to frontend. Respond with a list of 10 search terms, single line, sepearted by commas",
        user_message=f"Generate search terms to find tools and repositories to help with: {prompt}"
    )
    search_term_list = [term.strip().replace('"', '') for term in search_term_list.split(",")]
    return search_term_list

# print (generate_search_terms("I want to find a tool that helps me with data cleaning"))

def analyze_results(prompt, results):

    processed_results_string = create_simple_openai_chat_completion(
        system_message="""You are helping the user to find tools and repositories relevant to their query. Here is a list of GitHub repositories that may have been relevant. Drawing DIRECTLY and ONLY from this list of repositories, please respond with the 10 repositories that are most relevant: determinine relevance based on the quality and content of the README, number of stars, and your interpretation of the relevance of the repo description to the user's problem. Only include English-language repositories.      
        Respond with a list of 10 repositories, each one in this format: 
        == 1. Title: <title>, URL: <url> == 
        <Specific list of steps the user could take to use repository to address their query, based on the readme and their original query>
        """,

        user_message="""Here is the issue or problem the user is trying to address: {prompt}. 
        
        Here is the list of GitHub repositories and data that you found: {results}""".format(prompt=prompt, results=results),

        model="gpt-3.5-turbo-16k"
    )
    print ("Processed results string: ", processed_results_string)
    
    # Placeholder function for LLM call
    # Returns categorized results and top relevant ones
    return processed_results_string, processed_results_string
