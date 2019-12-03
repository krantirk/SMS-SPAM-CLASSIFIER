from filter import Filter
import sys

def text(inputText):

   messages= open("messages.txt","w+")
   messages.write('inputText')
   train='C:/spamfilter-master/Bayes1/src/train.txt'
   do_stuff(train,messages)

def do_stuff(train, messages):
# Open files for reading and writing
      train_file = open(train, "rb")
      messages_file = open(messages, "rb")
      predictions_file = open("predictions.txt", "w")

      # Create new filter and train it using the train-file
      f = Filter()
      f.train(train_file)

      #filter the messages in messages_file, write results to predictions_file
      f.filter(messages_file, predictions_file)

      # Close all the files
      train_file.close()
      messages_file.close()
      p=predictions.read()
      print(p)
      predictions_file.close()

if __name__ == '__main__':
    # Get arguments from user
    
    text(inputText)