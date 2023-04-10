import re
def read_template(path):
    with open(path, "r") as file:
        return file.read()


def parse_template(str):
    
    result = re.findall(r'\{([^{}]+)\}', str)
    print(result)
    x = ()
    for item in result:    
     y = list(x)
     y.append( item)
     x = tuple(y)
     str = re.sub(r'\{([^{}]+)\}', '{}', str) 
    return str,x



def merge(stripped_template, parts):
    return stripped_template.format(*parts)


if __name__ == "__main__":
    print("welcom to our game, play by entering what you are asked ;)")
    template = read_template("assets/gameText.txt")
    stripped_template, parts = parse_template(template)

    user_inputs = []
    for part in parts:
        user_inputs.append(input(f"Enter a {part}: "))

    text = merge(stripped_template, user_inputs)
    print(text)
    with open("assets/newText.txt", "w") as file:
        opened_file =file.write(text)
