using System;
using System.Collections.Generic;
Console.WriteLine("引数を入力してください.");

string var = Console.ReadLine();

string[] GGG; ;

GGG = var.Split(' ');

int a = Int32.Parse( GGG[0]);
int b = Int32.Parse( GGG[1]);

int anser = a + b;

Console.WriteLine(anser);
Console.WriteLine("やったね");
Console.WriteLine("成功");
Console.WriteLine("成功");

Console.Read();