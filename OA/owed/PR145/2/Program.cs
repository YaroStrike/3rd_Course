using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Заправка");
        Console.WriteLine("Тип топлива:");
        Console.WriteLine("1 - 92");
        Console.WriteLine("2 - 95");
        Console.WriteLine("3 - 98");
        Console.WriteLine("4 - ДТ");
        Console.Write("Ваш выбор -> ");
        double fuelType = Convert.ToInt16(Console.ReadLine());

        Console.Write("Литров -> ");
        double liters = Convert.ToInt16(Console.ReadLine());

        double price92 = 68.43;
        double price95 = 69.94;
        double price98 = 1000;
        double priceDF = 86.55;  
        double totalPrice = 0;
        double pricePerLiter;

        switch (fuelType)
        {
            case 1:
                totalPrice = price92 * liters;
                break;
            case 2:
                totalPrice = price95 * liters;
                break;
            case 3:
                totalPrice = price98 * liters;
                break;
            case 4:
                totalPrice = priceDF * liters;
                break;
            default:
                Console.WriteLine("Неверный тип топлива.");
                return;
        }

        Console.WriteLine("-----------------------------");
        if (fuelType == 1){
            pricePerLiter = price92;
        }
        else if (fuelType == 2){
            pricePerLiter = price95;
        }
        else if (fuelType == 3){
            pricePerLiter = price98;
        }
        else if (fuelType == 4){
            pricePerLiter = priceDF;
        }
        else {
            pricePerLiter = 0;
        }
        Console.WriteLine($"Цена за литр: {pricePerLiter} rub");
        Console.WriteLine($"Литров: {liters}");
        Console.WriteLine($"К оплате: {totalPrice} rub");
    }
}
