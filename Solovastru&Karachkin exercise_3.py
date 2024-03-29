
import requests
import json
from porter_stemmer import PorterStemmer

#Part 1
sonnets_url= "https://poetrydb.org/author,title/Shakespeare;Sonnet"

response = requests.get(sonnets_url)

sonnets = json.loads(response.text)

#print(sonnets,"\n"[0:1])
#print(type(sonnets))

#Part 2

class Sonnet:
    def __init__(self, sonnet_data):
        title_parts = sonnet_data['title'].split(':')
        self.id = int(title_parts[0].split()[-1])
        self.title = title_parts[1]
        self.lines = sonnet_data['lines']

    def __str__(self):
        lines_str = '\n'.join(self.lines)
        return f"Sonnet {self.id}: {self.title}\n{lines_str}"


    def __repr__(self):
        return f"Sonnet {self.id}: {self.title}\n {self.lines}"

#Part 3 & 4


    def tokenize(self) -> list[str]:
        tokenized_lines = []
        punct_to_remove = [",", "'", ":", ";", "!", "?"]
        stemmer = PorterStemmer()
        stemmed_tokens = []

        for line in self.lines:
            line = line.lower()
            for word in punct_to_remove:
                line = line.replace(word, " ")
            tokenized_line = line.split()


            for token in tokenized_line:
                stemmed_token = stemmer.stem(token, 0, len(token) - 1)
                stemmed_tokens.append(stemmed_token)
            tokenized_lines.extend(tokenized_line)

        return stemmed_tokens



#Part2 create instances

sonnets_instance_list = []

for sonnet in sonnets:
    sonnet_instance = Sonnet(sonnet)
    sonnets_instance_list.append(sonnet_instance)


print(sonnets_instance_list[3].tokenize())
print(str(sonnets_instance_list[3]))

#Part 5

class Index(dict[str, set[int]]):
    def __init__(self, documents: list[Sonnet]):
        super().__init__()
        self.documents = documents
        for document in documents:
            self.add(document)

    def add(self, document: Sonnet):
        tokens = document.tokenize()

        for token in tokens:
            if token not in self:
                self[token] = set()
            self[token].add(document.id)

for s in sonnets_instance_list[:2]:
    print(type(s))


sonnets_index = Index(sonnets_instance_list)
for token, ids in sonnets_index.items():
    print(f"Token: {token} -> Documents: {ids}")

"""Part 6"""

#Part 6 & 7

class Document:
    def __init__(self, lines):
        self.lines = lines

    def tokenize(self) -> list[str]:
        tokenized_lines = []
        punct_to_remove = [",", "'", ":", ";", "!", "?"]
        stemmer = PorterStemmer()
        stemmed_tokens = []

        for line in self.lines:
            line = line.lower()
            for word in punct_to_remove:
                line = line.replace(word, " ")
            tokenized_line = line.split()


            for token in tokenized_line:
                stemmed_token = stemmer.stem(token, 0, len(token) - 1)
                stemmed_tokens.append(stemmed_token)
            tokenized_lines.extend(tokenized_line)

        return stemmed_tokens

class Sonnet(Document):
    def __init__(self, sonnet_data):
        title_parts = sonnet_data['title'].split(':')
        self.id = int(title_parts[0].split()[-1])
        self.title = title_parts[1]
        self.lines = sonnet_data['lines']

    def __str__(self):
        lines_str = '\n'.join(self.lines)
        return f"Sonnet {self.id}: {self.title}\n{lines_str}"


    def __repr__(self):
        return f"Sonnet {self.id}: {self.title}\n {self.lines}"

class Query(Document):
    def __init__(self, query):
        super().__init__([query])

class Index(dict[str, set[int]]):

    def __init__(self, documents: list[Sonnet]):
        super().__init__()
        self.documents = documents
        for document in documents:
            self.add(document)

    def add(self, document: Sonnet):
        tokens = document.tokenize()

        for token in tokens:
            if token not in self:
                self[token] = set()
            self[token].add(document.id)

    def search(self, query: Query) -> list[Sonnet]:
        tokens = query.tokenize()
        ids = set.intersection(*(self[token] for token in tokens if token in self))
        return [self.documents[id] for id in ids]

index = Index(sonnets_instance_list)  # Build the index
query = Query("love hate")  # Build the query
matching_sonnets = index.search(query)  # Search the index with the query

# Print the results
for matching_sonnet in matching_sonnets:
  print(matching_sonnet)

# Part 8

def main():
    sonnets = [...]  # Load or define your sonnets here

    # Create Sonnet instances from the sonnets data
    sonnet_instances = [Sonnet(sonnet_data) for sonnet_data in sonnets]

    # Create an Index instance with the list of Sonnet instances
    sonnets_index = Index(sonnet_instances)

    while True:
        query_str = input("Search for sonnets ('q' to quit)> ")
        if query_str.lower() == 'q':
            break

        query = Query(query_str)

        matching_sonnets = sonnets_index.search(query)

        if matching_sonnets:
            print(f"--> Your search for '{query_str}' matched {len(matching_sonnets)} sonnets:")
            for sonnet in matching_sonnets:
                print(sonnet)
        else:
            print(f"No sonnets matched your query '{query_str}'.")

if __name__ == "__main__":
    main()
