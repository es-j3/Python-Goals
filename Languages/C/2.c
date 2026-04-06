#include <stdio.h>
#include <stdbool.h>

int main()
{
    int age = 41;
    int year = 2026;
    int quantity = 1;
    
    float gpa = 2.6;
    float price = 19.99;
    float temperature = -10.1;
    double pi = 3.14159265358979;
    double e = 2.7182818284590;
    
    char grade = 'B';
    char symbol = '?';
    char currency = '$';

    char name[] = "Sigma Gigglet";
    char food[] = "Pierogi";
    char email[] = "fake@gigglet.network";

    bool Online = true;
    bool Student = true;
    bool Sale = false;

    if (Online)
    {
      printf("Online.\n");
    }
    else
    {
        printf("Offline.\n");
    }
    if (Student)
    {
      printf("You are a student.\n");
    }
    else
    {
        printf("You aren't a student.\n");
    }
    if (Sale)
    {
      printf("Yo yo yo this item is for sale yo!\n");
    }
    else
    {
        printf("Sorry, come back next time.\n");
    }   

    printf("Your name is: %s\n", name);
    printf("Your favorite food is: %s\n", food);
    printf("Your email is: %s\n", email);

    printf("Your grade's: %c\n", grade);
    printf("Your favorite symbol is: %c\n", symbol);
    printf("The currency used will be: %c\n", currency);

    printf("Your GPA is: %0.1f\n", gpa);
    printf("Price is: $%0.2f\n", price);
    printf("The temperature is: %0.1f*F\n", temperature);
    printf("Pi is: %.14lf\n", pi);
    printf("E is: %.13lf\n", e);

    printf("You are %d\n", age);
    printf("The year is probably %d\n", year);
    printf("You've ordered %d amount of items", quantity);

    return 0;
}