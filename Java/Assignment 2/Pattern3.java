//         *
//      *     *
//    *    *    *
//      *     *
//         *


public class Pattern3 {
    public static void main(String[] args) {
        int n=3;
        for(int i=0;i<3;i++){
           for(int j=0;j<n-i-1;j++){
            System.out.print("\t");
           }
           for(int j=0;j<=i;j++)
           System.out.print("*\t");
        System.out.println();
        }
    }
}