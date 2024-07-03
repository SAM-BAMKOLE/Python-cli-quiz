import json
import sys
from random import shuffle

def answerQuestions():
  LIMIT = 10
  question_count = input('How many questions are you asking, max is 10\t')
  
  try:
    assert isinstance(int(question_count), int) and int(question_count) <= LIMIT
  except Exception:
    print("Please type only a number and not greater than 10")
    sys.exit()
  
  with open("questions.json", 'r') as file:
    questions = json.load(file)
    shuffle(questions)
    file.close()
    
  question_count = int(question_count) if int(question_count) < len(questions) else len(questions)
  total_score = askQuestions(questions, question_count)
  
  return { "total_score": total_score, "total": question_count }
    
  
  
def askQuestions(questions, limit):
  count = 0
  # print(len(questions[:limit]))
  for question in questions[:limit]:
    ans = input(question["question"] + "\n" + "options: " + ", ".join(question["options"]) + "\n")
    if ans.strip().lower() == question["answer"].lower():
      count += 1
      print("Correct")
    else:
      print("Incorrect")
    
    
  return count
    
    
    
def addQuestion():
  question = input('What is your question ?\t')
  options = input('Write all options separated by a comma.\t')
  correct_answer = input("What is the correct answer ?\t")
  
  new_options = []
  for option in options.split(","):
    new_options.append(option.strip())
    
  new_question = {
    "question": question,
    "options": new_options,
    "answer": correct_answer
  }
  
  with open("questions.json", 'r') as file:
    questions = json.load(file)
    file.close()
  with open("questions.json", "w") as file:
    questions.append(new_question)
    json.dump(questions, file)
    file.close()
    print('Question added')