from langchain_classic.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class TextValidator:
    def __init__(self, category):
        # Initialize the class with a category name
        self.category = category

    def is_too_long(self, content, max_length):
    returns True if the content exceeds the max_length, else False.
        if len(content) > max_length:
            return True
        else:
            return False

# --- Example Usage ---

# 1. Create an instance of the class
validator = TextValidator("Document Processing")

# 2. Define some data to check
sample_text = "Space exploration continues to push the boundaries of what's possible."
threshold = 50

# 3. Use an if-else statement to handle the method's result
if validator.is_too_long(sample_text, threshold):
    print(f"[{validator.category}] Alert: The text is too long for the current chunk size.")
else:
    print(f"[{validator.category}] Success: The text fits within the limits.")
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 0
)

result = splitter.split_text(text)

print(result)