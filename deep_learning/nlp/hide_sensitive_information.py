import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(text):
    doc = nlp(text)
    redacted_text = text

    for ent in reversed(doc.ents):
        if ent.label_ in ["PERSON", "GPE", "DATE"]:  # Person, Location, Date
            start = ent.start_char
            end = ent.end_char
            # Replace the sensitive text with its category label
            redacted_text = redacted_text[:start] + f"[{ent.label_}]" + redacted_text[end:]

    return redacted_text

# Test it out
raw_email = "Hi team, Alice Smith from Toronto called to confirm her interview on July 15th."
print(anonymize_text(raw_email))
