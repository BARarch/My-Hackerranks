import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        ArrayList<Integer> nums = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            nums.add(scan.nextInt());
        }
        //System.out.println(nums.size());
        int q = scan.nextInt();
        scan.nextLine();
        for (int j = 0; j < q; j++) {
            String cmd = scan.nextLine();
            //System.out.println(cmd);
            if (cmd.equals("Insert")) {
                nums.add(scan.nextInt(), scan.nextInt());
                if (scan.hasNext()) {   
                    scan.nextLine();
                }
            }
            if (cmd.equals("Delete")) {
                //System.out.println("Deleting");
                nums.remove(scan.nextInt());
                if (scan.hasNext()) {   
                    scan.nextLine();
                }
            }
        }
        //System.out.println(nums.size());
        //System.out.println(nums);
        for (int i = 0; i < nums.size(); i++){
            if (i == nums.size() - 1) {
                System.out.print(nums.get(i));    
            } else {
            System.out.print(nums.get(i) + " ");
            }
        }
    }
}

