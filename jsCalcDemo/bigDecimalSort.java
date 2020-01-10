import java.math.BigDecimal;
import java.util.*;
class Solution{
    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
        sc.close();

        //Write your code here 
        //Bubble Sort the S Array in place
        boolean swap = true;
        while (swap) {
            swap = false;
            for (int i=0; i < n - 1; i++) {
                BigDecimal A = new BigDecimal(s[i]);
                BigDecimal B = new BigDecimal(s[i + 1]);
                if (A.compareTo(B) == -1) {
                    swap = true;
                    String buff = s[i];
                    s[i] = s[i + 1];
                    s[i + 1] = buff;
                }
            }
        }


        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }
}