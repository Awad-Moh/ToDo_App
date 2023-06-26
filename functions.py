FILEPATH = "todos.txt"
def get_todos(filepath_local = FILEPATH):
    with open(filepath_local, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_local, filepath_local = FILEPATH):
    with open(filepath_local, 'w') as file:
        file.writelines(todos_local)

# if you simply addded a print, the strings will be printed when u import the functions in another a code
# to avoid this add the conditional statement

if __name__ == "__main__":
    print("hello from functions")