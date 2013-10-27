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


