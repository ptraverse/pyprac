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
