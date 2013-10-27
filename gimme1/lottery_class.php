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
