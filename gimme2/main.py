import random

class Company(object):
	def __init__(self, name, rake, rev=0):
		self.name = name
		self.rake = rake
		self.rev = rev
	def __str__(self):
		return "Company "+self.name+" takes rake "+str(self.rake)+" and has balance "+str(self.rev)

class Lottery(object):
	def __init__(self):
		self.currentpoints = 0
		self.currentrev = 0
	def draw(self,users):
		u = self.pick_random_user(users)
		u.winnings += self.currentrev
		self.currentpoints = 0
		self.currentrev = 0
		return u.name+" just won "+str(u.winnings)+"!"
	def pick_random_user(self, users):
		return users[random.randrange(0,len(users))]

class Star(object):
        def  __init__(self,cost,points):
                self.cost = cost;
                self.points = points;
	
class User(object):        
        def __init__(self,name,currentpoints = 0,use_count = 0,winnings  = 0):
                self.name = name
                self.currentpoints = currentpoints
                self.use_count = use_count
                self.winnings = winnings
        def __unicode__(self):
                return self.name+" currently has "+str(self.currentpoints)+" and has viewed "+str(self.use_count)+" times and has won "+str(self.winnings)
        def use_star(self, star, lottery, company):
                self.use_count += 1
                self.currentpoints += star.points
                lottery.currentrev += star.cost*(1-company.rake)
		company.rev += star.cost*(company.rake)
                return self.name+" used star("+str(star.cost)+","+str(star.points)+")"

# ----- MAIN ----- #

c = Company("Gimme2",0.5)
l = Lottery()

num_users = 100;

users = []
#users.append(User("Cliff"))
#users.append(User("Cole"))
#users.append(User("Catherine"))
#users.append(User("Carson"))

for count in range(0,100):
	users.append(User(str(count)))

stars = []
minpoints = 5
maxpoints = 1 
mincost = 0.05
maxcost = 0.01
for count in range(0,10):
	randpoints = random.uniform(1,5)
	if (randpoints>maxpoints):
		maxpoints = randpoints
	if (randpoints<minpoints):
		minpoints = randpoints
	randcost = random.uniform(1,5)/100
	if (randcost>maxcost):
		maxcost = randcost
	if (randcost<mincost):
		mincost = randcost
	stars.append(Star(randcost,randpoints))

# -------- Done Initializing ---- #

num_events_per_user = 50;
events = []
for user in users:
	if (user.use_count<num_events_per_user):
		randstar = stars[random.randrange(0,len(stars))]
		events.append(user.use_star(randstar,l,c))
	
print l.draw(users)

print "maximum cost was "+str(maxcost)
print "minimum cost was "+str(mincost)
print "max points was "+str(maxpoints)
print "min points was "+str(minpoints)

print "number of events: "+str(len(events))

print c
