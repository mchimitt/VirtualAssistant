from assistant import Assistant

#   TODO LISTS:
#   Add spot in intents.csv for random gibberish
#       this is because if an input is fudbslbgj then it predicts it as a greeting
#   Test in linux
#   Create a git ignore for the api_keys
#   put on github
#

assistant = Assistant("judy", 130)
assistant.start()
