using System;

namespace project
{
    class Program
    {
        static void Main()
        {
            int Name;
            Console.Write ("Введи ваше имя: ");
            Name = Convert.ToInt32 (Console.ReadLine ());
            Console.WriteLine ("Тебя зовут " + Name + "?");
        }
    }
}