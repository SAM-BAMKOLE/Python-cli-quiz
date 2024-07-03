import sys
from question import answerQuestions
from question import addQuestion

def askQuestion():
  ready = input('Ready to play  (y/n)?\t').lower()
  correctChoice = False
  if ready == "y" or ready == "n":
      correctChoice = True
  try:
      assert correctChoice == True
  except AssertionError:
      print("Please choose either y or n")
      # askQuestion()
      sys.exit()
  if ready != 'y':
      print("Exitting...")
      return False
  return True

def main():
  response = askQuestion()
  if response != True: return
    
  print('Hello World!')
  action = input("Are you answering questions or adding new questions ? (ans/add)\t")
  
  try:
    result = action.lower() == "ans" or action.lower() == "add"
    assert result == True
  except AssertionError:
    print("Please choose either 'ans' or 'add' !!")
    sys.exit()
  
  if action == 'ans':
    print('Get ready !!!')
    stats = answerQuestions()
    percentage = (stats["total_score"] / stats["total"]) * 100
    print(f"Your total score is {stats['total_score']} out of {stats['total']}, that's {percentage}%")
  else:
    print("Okay, get ready")
    addQuestion()

if __name__ == "__main__":
    main()
     
