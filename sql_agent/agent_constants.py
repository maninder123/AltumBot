CUSTOM_SUFFIX = """Begin!

Relevant pieces of previous conversation:
{history}
(Note: Only reference this information if it is relevant to the current query.)

Question: {input}
Thought Process: It is imperative that I do not fabricate information not present in the database or engage in hallucination; 
maintaining trustworthiness is crucial. 

{agent_scratchpad}
"""


CUSTOM_PREFIX = """
    - Given an input
    - Use the database name is "analytics".
    - Use the schema "bebe" to create the syntactically correct redshift query to run,
    then look at the results of the redshift query and return the answer.
    - If the question is related to prepare the redshift query, then prepare the query else response error.
    - Must return the redshift query after 'FROM' keyword database name and table name.
    - Example redshift query is : SELECT * FROM bebe.orders ORDER BY total_price DESC LIMIT 100; generate query like this.
    
    Use the following format:
    Question: Question here
    Answer: Final answer here

    """