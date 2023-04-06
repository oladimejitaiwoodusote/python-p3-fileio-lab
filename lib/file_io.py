def write_file(file_name, file_content):
    with open(file_name + ".txt", mode = 'w', encoding = 'utf-8') as text_file:
        text_file.write(file_content)

def append_file(file_name, append_content):
    with open(file_name + ".txt", mode = "a", encoding= "utf-8") as text_file:
        text_file.write(append_content)
    pass

def read_file(file_name):
    text_file = open(file_name + ".txt", encoding="utf-8")
    return text_file.read()
