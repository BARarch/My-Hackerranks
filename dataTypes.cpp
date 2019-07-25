#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int i;
    long lg;
    char cr;
    float ft;
    double dle;
    
    scanf("%d %ld %c %f %lf", &i, &lg, &cr, &ft, &dle);
    printf("%d\n%ld\n%c\n%f\n%lf", i, lg, cr, ft, dle);
    return 0;
}