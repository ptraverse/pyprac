
<?php

class Company 
{

	public $name;
	public $rev;
	public $rake;

	public function __construct($name,$rake)
	{
		$this->name = $name;
		$this->rake = $rake;
		$this->rev = 0;
	}

	public function __toString()
	{
		return "Company '$this->name' has total revenue of $this->rev. \n"; 
	}
}

?>


<?php

class Lottery 
{

	public $currentpoints;
	public $currentrev;

	public function __construct()
	{
		$this->currentpoints = 0;
		$this->currentrev = 0;
	}

	public function draw($users)
	{
		$u = $this->pick_random_user($users);
		$u->winnings += $this->currentrev;
		echo "$u->name just won $this->currentrev!! \n";
		$this->currentrev = 0;
		$this->currentpoints = 0;
	}

	public function pick_random_user($users)
	{
		$key = floor(rand(1,count($users)))-1;
		return $users[$key];
	}
}

?>
<?php

class Star
{

	public $cost;
	public $points;

	public function __construct($cost,$points)
	{
		$this->cost = $cost;
		$this->points = $points;
	}
}

?>
<?php

class User  
{

	public $name;
	public $currentpoints;
	public $winnings;
	public $use_count;

	public function __construct($name)
	{
		$this->name = $name;
		$this->currentpoints = 0;
		$this->use_count = 0;
		$this->winnings = 0;
	}

	public function __toString()
	{
		return "$this->name currently has $this->currentpoints and has viewd $this->use_count times and has won $this->winnings. \n";
	}

	public function use_star($star, $lottery, $company)
	{
		$this->use_count++;
		$this->currentpoints += $star->points;
		$lottery->currentrev += $star->cost*(1-$company->rake);
		$company->rev += $star->cost*($company->rake);
		return "$this->name used star($star->cost,$star->points)\n"; 
	}
}

?>
