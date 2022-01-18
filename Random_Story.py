import random
when = ['A few years ago', 'Yesterday','Last night','Long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant','a mouse','a turtle','a cat']
name = ['Ali','Miriam','Daniel','Hoouk','Skywalker']
residence = ['Barcelona','India','Germany','Venice','England']
went = ['cinema','university','seminar','school','laundry']
happened = ['a made a lot of friends','Eats a steak','found a secret key','solved a mystery','wrote a book']
print (random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went)+ ' and ' + random.choice(happened))
