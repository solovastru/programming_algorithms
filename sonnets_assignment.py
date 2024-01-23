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
        return f"Sonnet {self.id}: {self.title} \n {self.lines}"


    def __repr__(self):
        return f"Sonnet {self.id}: {self.title}\n {self.lines}"


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
            tokenized_lines.extend(tokenized_line)
            for token in tokenized_lines:
                stemmed_token = stemmer.stem(token, 0, len(token) - 1)
                stemmed_tokens.append(stemmed_token)

        return stemmed_tokens







sonnet3 = Sonnet({
        "title": "Sonnet 3: Look in thy glass and tell the face thou viewest",
        "author": "William Shakespeare",
        "lines": [
            "Look in thy glass and tell the face thou viewest",
            "Now is the time that face should form another;",
            "Whose fresh repair if now thou not renewest,",
            "Thou dost beguile the world, unbless some mother.",
            "For where is she so fair whose unear'd womb",
            "Disdains the tillage of thy husbandry?",
            "Or who is he so fond will be the tomb,",
            "Of his self-love to stop posterity?",
            "Thou art thy mother's glass and she in thee",
            "Calls back the lovely April of her prime;",
            "So thou through windows of thine age shalt see,",
            "Despite of wrinkles this thy golden time.",
            "  But if thou live, remember'd not to be,",
            "  Die single and thine image dies with thee."
        ],
        "linecount": "14"
    },)

sonnets_instance_list = []
for sonnet in sonnets:
    sonnet_instance = Sonnet(sonnet["title"], sonnet["lines"])
    sonnets_instance_list.append(sonnet_instance)

print(str(sonnet3))

sonnet3.tokenize()
print(sonnet3.tokenize())


#Part 3


