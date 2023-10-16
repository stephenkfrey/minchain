from llm_functions import generate_search_terms, analyze_results
from github_api_handler import search_github, extract_repo_details

def main():
    # Step 1: Get problem statement
    prompt = input("Enter the problem you are trying to solve: ")

    # Step 2: Generate search terms
    search_terms = generate_search_terms(prompt)
    print (f"\n\n-------------- Generated search terms:\n {search_terms}")

    all_results = []

    # Step 3: Search GitHub
    for term in search_terms:
        print (f"Searching GitHub for {term}")
        repos = search_github(term)
        for repo in repos:
            details = extract_repo_details(repo)
            print (f"Found {details['title'], details['readme']}")
            # truncate the readme to 500 characters
            details['readme'] = details['readme'][:500]
            all_results.append(details)
        print (f"Found {len(repos)} results for {term}")

    print (f"Found {len(all_results)} TOTAL results")

    # Step 4: Analyze results using LLM
    categorized_results, most_relevant = analyze_results(prompt, all_results)

    print (f"\n\n--------------GitHub Repos most likely to help you-------------- \n query: {prompt}\n searched for: {search_terms} \n\n {categorized_results}")

    # # Step 5: Display results
    # print("Most Relevant Repositories:")
    # for repo in most_relevant:
    #     print(f"Title: {repo['title']}, URL: {repo['url']}")

if __name__ == "__main__":
    main()
