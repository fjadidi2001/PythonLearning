print("welcome")

name = input("Name: ")
playing = input("Do u wanna play: ")
if playing.lower() != "yes":
    quit()

print('Lets Go')
score = 0
answer = input("List out components of a computer system. ")
if answer.lower() == "cpu and memory and input and output device":
    print('correct!')
    score += 1
else:
    print("incorrect")
answer = input("List out some popular operating system. ")
if answer.lower() == "windows and linux and osx":
    print('correct!')
    score += 1
else:
    print("incorrect")
answer = input("List out some computer processors. ")
if answer.lower() == "intel and amd":
    print('correct!')
    score += 1
else:
    print("incorrect")
answer = input("What is the full form of SDLC?. ")
if answer.lower() == "software development life cycle":
    print('correct!')
    score += 1
else:
    print("incorrect")
print(name + ' got ' + str(score) + " questions correct!")
print(name+" got " + str((score/4)*100) + "%.")




'''
This code is a simple quiz game that tests the user's knowledge about computer systems, operating systems, processors, and software development life cycle (SDLC). Here’s a breakdown of the code:

1. **Welcome Message**: It first prints a welcome message.
   ```python
   print("welcome")
   ```

2. **User Input for Name**: The program prompts the user to enter their name.
   ```python
   name = input("Name: ")
   ```

3. **Play Confirmation**: It asks the user if they want to play the game. If the user inputs anything other than "yes" (case insensitive), the program quits.
   ```python
   playing = input("Do u wanna play: ")
   if playing.lower() != "yes":
       quit()
   ```

4. **Game Start Message**: If the user wants to play, it prints a message indicating the game is starting.
   ```python
   print('Lets Go')
   ```

5. **Score Initialization**: A variable `score` is initialized to 0 to keep track of the number of correct answers.
   ```python
   score = 0
   ```

6. **Quiz Questions**: The program then asks a series of questions one by one, checking the user's input against the correct answers:
   - **Components of a Computer System**: The user must list the components, and the correct answer is "CPU and memory and input and output device." 
     ```python
     answer = input("List out components of a computer system. ")
     if answer.lower() == "cpu and memory and input and output device":
         print('correct!')
         score += 1
     else:
         print("incorrect")
     ```

   - **Popular Operating Systems**: The expected answer is "windows and linux and osx." 
     ```python
     answer = input("List out some popular operating system. ")
     ```

   - **Computer Processors**: The correct answer is "intel and amd."
     ```python
     answer = input("List out some computer processors. ")
     ```

   - **Full Form of SDLC**: The expected answer is "software development life cycle."
     ```python
     answer = input("What is the full form of SDLC?. ")
     ```

7. **Score Summary**: After all questions, the program informs the user of their score by outputting the number of correct answers and the percentage score out of 100.
   ```python
   print(name + ' got ' + str(score) + " questions correct!")
   print(name+" got " + str((score/4)*100) + "%.")
   ```

### Summary:
- The program welcomes the user and asks if they want to play a quiz.
- If they agree, it asks four questions and checks the user's answers.
- It keeps track of the score and displays the number of correct answers and the corresponding percentage at the end.


'''
