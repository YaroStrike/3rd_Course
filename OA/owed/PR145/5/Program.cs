using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите длительность разговора (в минутах): ");
        int duration = Convert.ToInt16(Console.ReadLine());

        Console.Write("Введите номер дня недели (1-7): ");
        int dayOfWeek = Convert.ToInt16(Console.ReadLine());

        double pricePerMinute = 6.46;
        double totalPrice = duration * pricePerMinute;

        if (dayOfWeek == 6 || dayOfWeek == 7)
        {
            totalPrice *= 0.8; // Применяем скидку 20%
            Console.WriteLine("Предоставляется скидка 20%");
        }

        Console.WriteLine($"Цена разговора: {totalPrice:F2} rub");
    }
}
