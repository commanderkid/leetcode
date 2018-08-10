using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Morzecode
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution sol = new Solution();
            string[] words = new string[] { "gin", "zen", "gig", "msg" };
            int a = sol.UniqueMorseRepresentations(words);
            Console.WriteLine(a);
        }
    }

    public class Solution
    {
        public int UniqueMorseRepresentations(string[] words)
        {
            List<string> ListOfStrings = MorzeCodeConverter(words, MorzeAlpha()).Distinct().ToList();
            return ListOfStrings.Count;
        }

        public Dictionary<char, string> MorzeAlpha()
        {
            string[] MorzeCode = new string[] { ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.." };
            Dictionary<char, string> MorzeAlphabet = new Dictionary<char, string>();

            for (int i = 0; i < 26; i++)
                MorzeAlphabet.Add((char)(97 + i), MorzeCode[i]);
            return MorzeAlphabet;
        }

        public List<string> MorzeCodeConverter(string[] words, Dictionary<char, string> DictionaryOfwords) //return list of strings
        {
            List<string> ConvertedStringArray = new List<string>();
            string adder;
            foreach (string str in words)
            {
                adder = null;
                foreach (char chr in str)
                    adder += DictionaryOfwords[chr];
                ConvertedStringArray.Add(adder);
            }
            return ConvertedStringArray;
        }
    }
}
