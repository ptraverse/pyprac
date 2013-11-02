product review system
get points for doing reviews
reviews have user selected ads (exact/nonexact)
get points for 
	making posts
	commenting/liking posts 
	getting adclicks (later)

users
-name
-datecreated
-currentpoints
-pointmultiplier
-cash

posts
-title
-description
-price
-usercreated

comments
-post_id
-text
-usercreated
-time

likes
-post_id
-usercreated
-time

lottery
-currentpoints
-currentcash

user.createpost(self,title,description,price):
	post = new post(self,title,description,price)
	self.currentpoints += self.determinepoints(post)
	
user.commentpost(self,post_id,comment):
	comment = new comment(self, post_id)
	self.currentpoints += self.determinepoints(comment)

user.likepost():
	...

user.determinepoints():
	...

user.determinelotterypoints():
user.determinelotterycash():
	...

lottery.draw()
	...



