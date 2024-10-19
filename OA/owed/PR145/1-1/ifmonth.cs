using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите номер месяца (от 1 до 12) -> ");
        int month = Convert.ToInt16(Console.ReadLine());

        if (month == 12 || month == 1 || month == 2)
        {
            Console.WriteLine("Зима");
        }
        else if (month >= 3 && month <= 5)
        {
            Console.WriteLine("Весна");
        }
        else if (month >= 6 && month <= 8)
        {
            Console.WriteLine("Лето");
        }
        else if (month >= 9 && month <= 11)
        {
            Console.WriteLine("Осень");
        }
        else
        {
            Console.WriteLine("Некорректный номер месяца. Пожалуйста, введите число от 1 до 12.");
        }
    }
}
