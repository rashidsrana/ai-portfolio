import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# The intercepted message
text = "Hey, I think peter Parker is actually Spider Man, and he lives in New York."

# Process text with spaCy
doc = nlp(text)

# Find PERSON entities
person_names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

print("Detected PERSON names:", person_names)

# Replace each detected name with "xxxx"
cleaned_text = text
for name in person_names:
    cleaned_text = cleaned_text.replace(name, "xxxx")

print("Cleaned text:", cleaned_text)
