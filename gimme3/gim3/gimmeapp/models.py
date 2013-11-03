from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=12)
	date_created = models.DateTimeField()
	current_points = models.IntegerField()
	cash = models.FloatField()
	point_multiplier = models.FloatField()
	def ___repr__(self):
		return self.name
	def create_post(self,title,description,price):
		p = Post(name = title,description = description,price = price,user_created = self)
		p.save()
		self.current_points += self.determine_points(p)
		self.save()
	def comment_post(self,post,comment):
		c = Comment(parent_post = post, text = comment, user_created = self, date_created=now() )
		c.save()
		self.current_points += self.determine_points(c)
		self.save()
	def like_post(self,post):
		l = Like(parent_post = post, user_created = self, date_created = now() )
		l.save()		
	def determine_points(self,post):
		return self.point_multiplier*strlen(post.description)
		# TODO Finish this 

class Post(models.Model):
	name = models.CharField(max_length=12)
	description = models.TextField
	price = models.FloatField
	user_created = models.ForeignKey(User)
	def __repr__(self):
		return self.name+" by "+self.user_created.repr()


class Comment(models.Model):
	parent_post = models.ForeignKey(Post)
	text = models.TextField()
	user_created = models.ForeignKey(User)
	date_created = models.DateTimeField()
	def __repr__(self):
                return self.user_created.repr()+" on "+self.date_created

class Like(models.Model):
	parent_post = models.ForeignKey(Post)
	user_created = models.ForeignKey(User)
	date_created = models.DateTimeField()
	def __repr__(self):
                return self.user_created.repr()+" on "+self.date_created

class Lottery(models.Model):
	current_points = models.IntegerField()
	current_cash = models.FloatField
	def __str__(self):
                return self.pool_total
	def draw(self,users):
		# TODO - Use the points sytem in random choosing
		u = random.choice(users)
		u.cash += self.current_cash
		self.current_cash = 0
		u.save()
		self.save()
		return "Congrats "+str(u)+"!"

