#!/usr/bin/env python3
import speech_recognition as sr
commandsList = ["forward","right","left","backward"]

text = 'move forward then rotate right 60 degree'
def cmd_resolver(speech):
      try:
        print(str(speech))
        x = speech.split()
        result = []
        for index in range(len(x)):
            if((any(ele in x[index] for ele in commandsList)) or (x[index].isnumeric())):
                result.append(x[index])

      except:
        print('sorry')
        return []
      return result
