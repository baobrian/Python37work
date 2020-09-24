from nltk.translate import bleu


referrence=[['the','cat','is','now','on','the','mat']]
candidate=['the','cat','the','the','the','the']


print ('bigram:',bleu(referrence,candidate,weights=(0,1,0,0)))
# print ('bleu:',bleu(referrence1,candidate1))