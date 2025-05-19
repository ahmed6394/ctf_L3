#include <stdio.h>
#include <unistd.h>

int main(int ac, char **av)
{
    char buf[4];
    // printf("1145258561x%1$n", buf);
    printf("%65x%1$hhn%c%2$hhn%c%3$hhn%c%4$hhn", buf, buf+1, buf+2, buf+3);

    printf("\n\n\n");
    write(1, buf, 4);
}

/* 
1. 65 is A, here we are increasing the value 4 time, and store in in buf, so We 
    get ABCD with less noise or time than the 1st printf way. here "hhn" leak i byte, 
    "%c" formate of char

*/