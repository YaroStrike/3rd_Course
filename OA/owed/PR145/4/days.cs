using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите номер дня недели (1-7):");
        int dayNumber = Convert.ToInt16(Console.ReadLine());

        switch (dayNumber)
        {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                Console.WriteLine("Рабочий день");
                break;
            case 6:
                Console.WriteLine("Суббота");
                break;
            case 7:
                Console.WriteLine("Воскресенье");
                break;
            default:
                Console.WriteLine("Некорректный номер дня. Пожалуйста, введите число от 1 до 7.");
                break;
        }
    }
}
