from llm_functions import generate_search_terms, analyze_results
from github_api_handler import search_github, extract_repo_details

def main():
    # Step 1: Get problem statement
    prompt = input("Enter the problem you are trying to solve: ")

    # Step 2: Generate search terms
    search_terms = generate_search_terms(prompt)
    print (f"\n\n-------------- Generated search terms: {search_terms}")

    all_results = []

    # Step 3: Search GitHub
    for term in search_terms:
        repos = search_github(term)
        for repo in repos:
            details = extract_repo_details(repo)
            all_results.append(details)

    print (f"Found {len(all_results)} results")

    # Step 4: Analyze results using LLM
    categorized_results, most_relevant = analyze_results(prompt, all_results)

    print (f"\n\n--------------Categorized results: {categorized_results}")

    # Step 5: Display results
    print("Most Relevant Repositories:")
    for repo in most_relevant:
        print(f"Title: {repo['title']}, URL: {repo['url']}")

if __name__ == "__main__":
    main()
