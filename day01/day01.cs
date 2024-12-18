// See https://aka.ms/new-console-template for more information
using System.IO;

var records = File.ReadLines("data.txt")
    .Select(line =>
        {
            string[] parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries|StringSplitOptions.TrimEntries);
            return new
                {
                    column1 = long.Parse(parts[0]),
                    column2 = long.Parse(parts[1])
                };
        }).ToArray();
var a = records.Select(r=>r.column1).OrderBy(r=>r);
var b = records.Select(r=>r.column2).OrderBy(r=>r);
Console.WriteLine(a.Zip(b).Select(t => t.First > t.Second ? t.First-t.Second : t.Second - t.First).Sum());

Console.WriteLine(a.Select(v=>v * b.Where(x=>x == v).Count()).Sum());