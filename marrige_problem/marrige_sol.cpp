#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#define fori(a) for(i=0;i<a;i++)
#define forj(a) for(j=0;j<a;j++)
#define fork(a,b) for(k=a;k<b;k++)
int readint()
{
    int t=0;
    char c;
    c=getchar_unlocked();
    while(c<'0' || c>'9')
        c=getchar_unlocked();
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar_unlocked();
    }
    return t;
}
int main()
{
    int i,j,k,t,man,wom,m,n,x;
    t=readint();
    fori(t)
    {
        n=readint();
        int menpref[n+5][n+5],womenpref[n+5][n+5],men[n+5],women[n+5];
        memset(men,0,(n+5)*sizeof(int));
        memset(women,0,(n+5)*sizeof(int));
        forj(n)
        {
            wom=readint();
            fork(1,n+1)
            {
                m=readint();
                womenpref[wom][m]=k;
            }
        }
        forj(n)
        {
            man=readint();
            fork(1,n+1)
            {
                wom=readint();
                menpref[man][k]=wom;
            }
        }
        /*forj(n)
        {
            fork(1,n+1) printf("%d ",womenpref[j+1][k]);
            printf("\n");
        }
        puts("MEN");
        forj(n)
        {
            fork(1,n+1) printf("%d ",menpref[j+1][k]);
            printf("\n");
        }*/
        while(1)
        {
            //puts("Hello\n");
            man=0;
            for (j=1; j<=n; j++)
            {
                if (men[j]==0)
                {
                    man=j;
                    break;
                }
            }
            //printf("man=%d\n",man);
            if (man==0) break;
            else
            {
                x=1;
                while(x<=n)
                {
                    if(women[menpref[man][x]]==0)
                    {
                        women[menpref[man][x]]=man;men[man]=menpref[man][x];
                        break;
                    }
                    else if(womenpref[menpref[man][x]][women[menpref[man][x]]]>womenpref[menpref[man][x]][man])
                    {
                        men[women[menpref[man][x]]]=0;
                        women[menpref[man][x]]=man;
                        men[man]=menpref[man][x];
                        break;
                    }
                    else x++;
                }
            }
            //for (j=1;j<=n;j++) printf("%d %d\n",j,men[j]);
            //puts("");
        }
        for (j=1;j<=n;j++) printf("%d %d\n",j,men[j]);
    }

    return 0;
}