using System;

public class Ship
{
    public string Name { get; set; }
    public int Length { get; set; }
    public int CrewSize { get; set; }

    public Ship(string name, int length, int crewSize)
    {
        Name = name;
        Length = length;
        CrewSize = crewSize;
    }

    public virtual void Sail()
    {
        Console.WriteLine($"{Name} типично плывёт.");
    }

    public void Anchor()
    {
        Console.WriteLine($"{Name} на якоре.");
    }
}

public class Steamboat : Ship
{
    public Steamboat(string name, int length, int crewSize) : base(name, length, crewSize) { }

    public override void Sail()
    {
        Console.WriteLine($"{Name} дымит!");
    }
}

public class Sailboat : Ship
{
    public Sailboat(string name, int length, int crewSize) : base(name, length, crewSize) { }

    public override void Sail()
    {
        Console.WriteLine($"{Name} ловит ветер!");
    }
}

public class Corvette : Ship
{
    public Corvette(string name, int length, int crewSize) : base(name, length, crewSize) { }

    public override void Sail()
    {
        Console.WriteLine($"{Name} разбивает волны!");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Ship myShip = new Ship("Супремайтист", 100, 20);
        Ship mySteamboat = new Steamboat("MSC-Сивью", 80, 15);
        Ship mySailboat = new Sailboat("Циклон м/c", 30, 5);
        Ship myCorvette = new Corvette("Корвет-12Т", 90, 10);

        myShip.Sail();
        mySteamboat.Sail();
        mySailboat.Sail();
        myCorvette.Sail();
    }
}
