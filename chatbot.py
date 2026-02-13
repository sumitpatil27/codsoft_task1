from datetime import datetime


def chat_res():
   print("Chatbot : Hello! I am a rule-based chatbot ")
   print("Chatbot : type 'exit' to end conversation " )
  
   

   while True:
      
      msg=input("You : ").lower()

      
      if "hello" in msg :
         print("Chatbot : Hello , How can I help you ? ")

      elif "how are you" in msg:
         print("Chatbot : I'm doing great, thank you for asking! How about you? ")

      elif "time" in msg:
         current_time = datetime.now().strftime("%H:%M:%S")
         print(f"Chatbot : Current time is {current_time}")
    
      elif "your name" in msg :
         print("Chatbot : I am a simple rule-based chatbot.")

      elif "exit" in msg or "bye" in msg:
         print("Chatbot : Goodbye! Have a nice day ")
         break
      
      elif "date" in msg:
        today = datetime.now().strftime("%d-%m-%Y")
        print(f"Chatbot : Today's date is {today}")

      else:
         print("Chatbot : Sorry, I didn't understand that.") 
        

chat_res()  
    

