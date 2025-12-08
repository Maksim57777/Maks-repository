using System;

namespace project
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine ("Нажмите X для выхода");
            ConsoleKeyInfo key = Console.ReadKey ();
            while (key.Key != ConsoleKey.X)
            {
            
            }
        }
    }
}