using System;

public class Transport
{
    public string Name { get; set; }
    public int Capacity { get; set; }
    public double Speed { get; set; }

    public virtual void Start()
    {
        Console.WriteLine($"{Name} начинает движение.");
    }

    public virtual void Stop()
    {
        Console.WriteLine($"{Name} останавливается.");
    }
}

public class Car : Transport
{
    public string FuelType { get; set; }

    public override void Start()
    {
        Console.WriteLine($"{Name} (автомобиль) начинает движение.");
    }

    public override void Stop()
    {
        Console.WriteLine($"{Name} (автомобиль) останавливается.");
    }
}

public class Train : Transport
{
    public int NumberOfCars { get; set; }

    public override void Start()
    {
        Console.WriteLine($"{Name} (поезд) начинает движение.");
    }

    public override void Stop()
    {
        Console.WriteLine($"{Name} (поезд) останавливается.");
    }
}

public class Express : Train
{
    public int TravelTime { get; set; }

    public override void Start()
    {
        Console.WriteLine($"{Name} (экспресс) начинает движение.");
    }

    public override void Stop()
    {
        Console.WriteLine($"{Name} (экспресс) останавливается.");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Car myCar = new Car { Name = "Мой автомобиль", Capacity = 5, Speed = 120, FuelType = "Бензин" };
        myCar.Start();
        myCar.Stop();

        Express myExpress = new Express { Name = "Скорый поезд", Capacity = 200, Speed = 300, NumberOfCars = 10, TravelTime = 120 };
        myExpress.Start();
        myExpress.Stop();
    }
}


