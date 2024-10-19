using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Выберите размер фотографии:");
        Console.WriteLine("1 - 9x12");
        Console.WriteLine("2 - 10x15");
        Console.WriteLine("3 - 18x24");
        Console.Write("Ваш выбор -> ");
        int sizeChoice = Convert.ToInt16(Console.ReadLine());

        Console.Write("Количество -> ");
        int quantity = Convert.ToInt16(Console.ReadLine());

        double pricePerPhoto;

        switch (sizeChoice)
        {
            case 1:
                pricePerPhoto = 3.5;
                break;
            case 2:
                pricePerPhoto = 4.0;
                break;
            case 3:
                pricePerPhoto = 5.0;
                break;
            default:
                Console.WriteLine("Неверный выбор размера.");
                return;
        }

        double totalPrice = pricePerPhoto * quantity;
        double discount = 0;

        if (quantity > 50)
        {
            discount = totalPrice * 0.15;
        }
        else if (quantity > 10)
        {
            discount = totalPrice * 0.10;
        }

        double finalPrice = totalPrice - discount;

        Console.WriteLine("-----------------------------");
        Console.WriteLine($"Цена: {pricePerPhoto} rub");
        Console.WriteLine($"Количество: {quantity} шт.");
        Console.WriteLine($"Сумма: {totalPrice} rub");
        Console.WriteLine($"Скидка: -{discount} rub");
        Console.WriteLine($"К оплате: {finalPrice} rub");
    }
}
