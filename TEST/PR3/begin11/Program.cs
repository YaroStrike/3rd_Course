using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите первое ненулевое число:");
        double num1 = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Введите второе:");
        double num2 = Convert.ToDouble(Console.ReadLine());

        if (num1 != 0 && num2 != 0)
        {
            double sum = num1 + num2;
            double difference = num1 - num2;
            double product = num1 * num2;
            double quotient = num1 / num2;

            Console.WriteLine($"Сумма: {sum}");
            Console.WriteLine($"Разность: {difference}");
            Console.WriteLine($"Произведение: {product}");
            Console.WriteLine($"Частное: {quotient}");
        }
        else
        {
            Console.WriteLine("Оба числа должны быть не нуль.");
        }
    }
}
