<?php

include('./company_class.php');
include('./lottery_class.php');
include('./user_class.php');
include('./star_class.php');

//echo __FILE__."\n";

$c = new Company("Gimme1","0.5");
$l = new Lottery();

$users = array();
$users[] = new User("Bob");
$users[] = new User("Bill");
$users[] = new User("Bo");
$users[] = new User("Barry");

$stars = array();
$num_stars = 50;
while ($num_stars > count($stars))
{
	$randPoints = rand(1,5); //points range from 1 to 5 per star use
	$randCost = $randPoints * (1/rand(50,550)); //cost ranges from 0.02 to 0.00002 of a point (ie max cost = 0.1, min cost = 0.00002)
	$stars[] = new Star($randCost, $randPoints);
}


$num_events = 1000;
$events = array();
while ($num_events > count($events))
{
	$randStar = $stars[floor(rand(1,count($stars))-1)];
	$randUser = $users[floor(rand(1,count($users))-1)];
	$events[] = $randUser->use_star($randStar,$l,$c);
}

echo $l->draw($users);

foreach ($users as $user)
{
	echo $user;
}

echo "\n".$c;


?>
