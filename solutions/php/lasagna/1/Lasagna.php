<?php

class Lasagna
{
    public function expectedCookTime()
    {
        // Implement the expectedCookTime method
        return 40;
    }

    public function remainingCookTime($elapsed_minutes)
    {
        // Implement the remainingCookTime method
        return $this -> expectedCookTime() - $elapsed_minutes;
    }

    public function totalPreparationTime($layers_to_prep)
    {
        // Implement the totalPreparationTime method
        $time_per_layer = 2;
        return $layers_to_prep * $time_per_layer;
    }

    public function totalElapsedTime($layers_to_prep, $elapsed_minutes)
    {
        // Implement the totalElapsedTime method
        return $this -> totalPreparationTime($layers_to_prep) + $elapsed_minutes;
    }

    public function alarm()
    {
        // Implement the alarm method
        return "Ding!";
    }
}
