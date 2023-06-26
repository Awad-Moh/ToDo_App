import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo_local = st.session_state["new_todo"]
    # if todo_local not in todos and todo_local:
    todos.append(todo_local + '\n')
    functions.write_todos(todos)
    st.session_state["new_todo"] = ''

st.title("My Todo App")
st.title("This is my todo app")
st.write("This app is to increase your productivity")


for i,todo in enumerate(todos):
    check = st.checkbox(todo, key = todo)
    if(check):
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Add a todo", placeholder = "Add a new todo...", on_change=add_todo, key= 'new_todo', label_visibility="collapsed")

