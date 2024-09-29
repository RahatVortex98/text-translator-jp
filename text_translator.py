from translate import Translator




# Initialize the Translator for Japanese
translator = Translator(to_lang="ja")

# Open the file and read its content
with open('hello.txt', mode='r', encoding='utf-8') as my_file:
    text = my_file.read()

    # Translate the content
    translation = translator.translate(text)  # Use the variable text, not the string "text"

    # Print the translated text
    print(translation)
