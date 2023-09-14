# Custom Search Engine

This project is a web search result engine and analysis tool designed to provide users with a refined and relevant list of search results. The motivation behind this project is that Google search results often contain many affiliate links trying to sell products instead of providing relevant information. 

The system starts by utilizing the Flask web framework to create a user-friendly web interface. Users can input search queries, triggering the execution of a search operation. The search is powered by a custom Python module that employs the Google Custom Search API, enabling the retrieval of search results for the specified query. 

To manage and store the search results and related data, the project relies on an SQLite database accessed through the SQLite3 module in Python. The database schema includes tables for storing search results, with fields such as query, rank, link, title, snippet, and HTML content. The Pandas library is used to manipulate and work with DataFrames, facilitating data analysis and operations on the retrieved search results. Additionally, BeautifulSoup is employed to parse and extract information from the HTML content of search results.
