public class IntegerToRoman   
{  
public static void intToRoman(int num)   
{  
System.out.println("Integer: " + num);  
int[] values = {1000,900,500,400,100,90,50,40,10,9,5,4,1};  
String[] romanLetters = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};  
StringBuilder roman = new StringBuilder();  
for(int i=0;i<values.length;i++)   
{  
while(num >= values[i])   
{  
num = num - values[i];  
roman.append(romanLetters[i]);  
}  
}  
System.out.println("Corresponding Roman Numerals is: " + roman.toString());  
}  
public static void main(String args[])   
{  
intToRoman(125);  
intToRoman(252);  
intToRoman(1000);  
intToRoman(1010);  
}  
}  
Output:

Convert Integer to Roman Numerals in Java
Another way to print roman numeral is to create four arrays of place values. For example, unit, tens, hundred, and thousand. After that, calculates its place value and convert into roman numerals.

IntegerToRoman.java

public class IntegerToRoman   
{  
//method to convert integer to roman  
//function that converts integer to roman  
public static String intToRoman(int number)   
{  
//creating array of place values      
String[] thousands = {"", "M", "MM", "MMM"};  
String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};  
String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};  
String[] units = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};  
return thousands[number / 1000] + hundreds[(number % 1000) / 100] + tens[(number % 100) / 10] + units[number % 10];  
}  
public static void main(String args[])   
{  
//creating an array of integers to be convert into roman      
int[] numbers = {13, 21, 38, 50, 190, 141, 117, 120, 125, 138, 149, 6, 712, 181, 197, 918, 199, 1100, 1101, 1248, 1253};  
for (int number : numbers)   
{  
System.out.printf("%4d -> %8s\n", number, intToRoman(number));  
}  
}  
}  
