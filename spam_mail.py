import pickle
count_vactorizer = pickle.load(open('count_vactor_email.pickle','rb'))
spam_mail = pickle.load((open('spam_email_detactor.pickle','rb')))
tra = count_vactorizer.transform([input("Email : ")])
ans = spam_mail.predict(tra)
if ans == 0:print(f"It's spam Mail. Be careful.")
else: print(f"It's not spam Mail :) ")