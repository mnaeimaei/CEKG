from neo4j import GraphDatabase

uri = "neo4j+s://a6f90080.databases.neo4j.io"
username = "neo4j"  # Replace with your actual username
password = "tb9tVAiwc7rBvJCjHcXUJAL7-Fpm32_Fa-ONV0SPgBU"  # Replace with your actual password

driver = GraphDatabase.driver(uri, auth=(username, password))

def run_query():
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n")
        for record in result:
            print(record["n"])

run_query()
driver.close()