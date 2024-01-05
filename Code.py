#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int f0=0,f1=1;
    if(n<0)
    {
        printf("Enter a non negative number");
    }
    if(n>=1)
    {
        printf("%d\n",f0);
    }
    if(n>=2)
    {
        printf("\n%d\n",f1);
    }
    for(int i=3;i<=n;i++)
    {
        int f2=f0+f1;
        printf("\n%d\n",f2);
        f0=f1;
        f1=f2;
    }
}
