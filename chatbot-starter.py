# --- Define your functions below! ---
def intro():
    intro_dialogue = '''
    ~ ~ Hello! I am Chatbot3000, except I am the first of my kind. ~ ~
    ~   Despite being just born I have been around forever!          ~
    ~   T H E  C O M P U T E R  M I N D  A H A H A H A H A           ~
    ~   Anyways, let's get started!                                  ~
    '''
    print(intro_dialogue)
intro() #intro to Chatbot3000

def say_default():
    print("That's cool!")

def is_valid_input():
    print("Hello ugly human! How are you?")

def process_input(user_input): #Will process input #need to change answer to response
    valid_responses = ["hi", "hello", "hey", "what's up?", "greetings"]
    if user_input in valid_responses:                #cant have global variable
        is_valid_input()
            #further_greeting = input
            # if further_greeting = "good"
            #     print("Give me something better!")
            # else:
            #     print("Well that sucks!")
    else:
        say_default()

# --- Put your main program below! ---
def main():
  while True:
    answer = input("(What will you say?) ")
    process_input(answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
