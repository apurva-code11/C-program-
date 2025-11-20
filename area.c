
#include <stdio.h>
int main() {
//area of sqare
        int side,area;
        printf("\nEnter side of square :  ");
        scanf("%d", &side);
        area=side*side;
        printf("area of square = %d",area);

    //radius of circle
        float radius,area1;
        printf("\nEnter radius of circle :  ");
        scanf("%f", &radius);
        area1=3.14*radius*radius;
        printf("area of circle = %f",area1);

    // area of rectangle
        int length,breadth,area2;
        printf("\nEnter length & breadth of rectangle :  ");
        scanf("%d%d", &length,&breadth);
        area2=length*breadth;
        printf("area of rectangle = %d",area2);

    // area of triangle
        float base,height,area3;
        printf("\nEnter base & height of triangle :  ");
        scanf("%f%f", &base,&height);
        area3=0.5*base*height;
        printf("area of triangle = %f",area3);
    return 0;
}
