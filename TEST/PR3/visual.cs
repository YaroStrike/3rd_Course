using System;

class visual
{
    static void Main()
    {
        Console.WriteLine("Enter the first non-zero number:");
        double num1 = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Enter the second non-zero number:");
        double num2 = Convert.ToDouble(Console.ReadLine());

        if (num1 != 0 && num2 != 0)
        {
            double sum = num1 + num2;
            double difference = num1 - num2;
            double product = num1 * num2;
            double quotient = num1 / num2;

            Console.WriteLine($"Sum: {sum}");
            Console.WriteLine($"Difference: {difference}");
            Console.WriteLine($"Product: {product}");
            Console.WriteLine($"Quotient: {quotient}");
        }
        else
        {
            Console.WriteLine("Both numbers must be non-zero.");
        }
    }
}
