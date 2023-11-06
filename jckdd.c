#include <stdio.h>
struct Soo{
    char name[20];
    int os, db, hab1, hab2;
}

void main(){
    struct Soo s[3] = {{"데이터1", 95, 88},{"데이터2", 84, 91},{"데이터3", 86, 75}};
    struct Soo *p;
    p = &s[0];
    (p+1)->hab1 = (p+1)->os+(p+2)->db;
    (p+1)->hab2 = (p+1)->had1 + p->os + p->db;
    printf("%d\n", (p+1)->hab1 + (p+1)->hab2);

}


