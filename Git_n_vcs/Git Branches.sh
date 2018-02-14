## 1. Introduction to Git Branches ##

/home/dq/chatbot$ git clone /dataquest/user/giit/chatbot chatbot

## 2. Switching Branches ##

/home/dq/chatbot$ nano bot.py

## 3. Pushing a Branch to a Remote ##

/home/dq/chatbot$ git push origin

## 4. Merging Branches ##

/home/dq/chatbot$ git push origin master

## 5. Deleting Branches ##

/home/dq/chatbot$ git branch -d more-speech

## 6. Checking Out Branches From the Remote ##

/home/dq/chatbot2$ git push origin happy-bot

## 7. Finding Differences Across Branches ##

/home/dq/chatbot$ git diff happy-bot master

## 8. Branch Naming Conventions ##

/home/dq/chatbot$ git push origin feature/random-messages

## 9. Branch History ##

/home/dq/chatbot$ git checkout -b feature/spam-messages