import java.util.Scanner;

/*
 * Team 13
 */
public class triangleTest {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        
        System.out.print("Enter x-side length of the triangle: ");
        int xSideLength = keyboard.nextInt();
    
        System.out.print("Enter y-side length of the triangle: ");
        int ySideLength = keyboard.nextInt();
        
        System.out.print("Enter z-side length of the triangle: ");
        int zSideLength = keyboard.nextInt();
        
        conditionsOfTriangle(xSideLength, ySideLength, zSideLength);
        
    
    }
    
    private static void conditionsOfTriangle(int x, int y, int z) {
        if (x <= 0 || y <= 0 || z <= 0) {
            throw new IllegalArgumentException("Length of sides cannot be equal to or less than zero");
        }else if (x > (y + z) || y > (x + z) || z > (x + y)) {
            throw new IllegalArgumentException("Sum of any two sides must be larger than the remaining side");
        }
        
        if(x == y && y == z){
            System.out.println("This is an Equilateral Triangle.");
        }else if(x == y || x == z || y == z) {
            System.out.println("This is an Isosceles Triangle.");
        }else{
            System.out.println("This is a Scalene Triangle.");
        }
        
    }    
    

}
