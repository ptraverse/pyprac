gimme1: sample test run for model demo in barebones php

Company
	-rev
	-rake

Lottery
	-currentpoints
	-currentrev

Lottery.draw(Users)
	U = This.pickRandomUser(Users)
	U.winnings += This.currentrev
	This.rev = 0
	This.currentpoints = 0
	

User
	-name
	-currentpoints
	-winnings

User.use(Star,Lottery,Company):
	This.currentpoints += Star.points
	Lottery.currerev += Star.cost*(1-Company.rake)
	Company.rev += Start.cost*Company.rake)
	

Star
	-cost
	-points


