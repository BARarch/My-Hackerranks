    //Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
	public static void main(String []argh)
	{
		Scanner in = new Scanner(System.in);
		int n=in.nextInt();
		in.nextLine();
        Map<String, Integer> m = new HashMap<String, Integer>();
		for(int i=0;i<n;i++)
		{
			String name=in.nextLine();
			Integer phone=new Integer(in.nextInt());
			in.nextLine();
            m.put(name, phone);
		}
		while(in.hasNext())
		{
			String s=in.nextLine();
            if (m.containsKey(s)) {
                System.out.println(s + "=" + m.get(s).toString());
            } else {
                System.out.println("Not found");
            }
		}
	}
}



