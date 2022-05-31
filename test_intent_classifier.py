from intent_classification.intent_classifier import IntentClassifier

###########################
# Intent Classifier Testing

classifier = IntentClassifier()

# print(classifier.predict("Hello, how are you?"))
# print(classifier.predict("hi, how is it going?"))

text = 'happy'
print(text)
print(classifier.predict(text))

text = 'juice is cool'
print(text)
print(classifier.predict(text))

text = 'what are you doing'
print(text)
print(classifier.predict(text))

text = 'hello there'
print(text)
print(classifier.predict(text))

text = 'whats the weather?'
print(text)
print(classifier.predict(text))

# print(classifier.predict("what is the weather?"))

text = input("Enter a question: ")
intent = classifier.predict(text)
print(intent)

#############################################################################
# GETTING MORE DATA IN THE CSV FILE (NOT FINISHED)
# i = input("Is this correct? Press Enter if correct otherwise type 'N' : ")
# if(i != 'N'):
#    with open('intents.csv', 'ab') as out:
#        writer = csv.writer(out)
#        writer.writerow(())
#    data = { 'text': [text], 'intent': [intent] }
#    df = pd.DataFrame(data)
#    df.to_csv('intents.csv', mode='a', index=False, header=False)
#    print(f"Added {text},{intent} to the CSV file")
