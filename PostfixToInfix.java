package ptoI;

import java.io.*;
import java.util.*;

class ConsoleCalculator
{
	 
	String postfix_evaluation(String st)
	{
 
		Stack<String> stack = new Stack<String>();
		StringTokenizer str = new StringTokenizer(st);
 
		ArrayList<String> operators= new ArrayList<>(Arrays.asList("+" ,"-" ,"*" ,"/" ,"^"));
 
		while(str.hasMoreTokens())
		{		
 
			String data = str.nextToken().trim();
 
			if(!operators.contains(data))		
				stack.push(data.trim());
			else {
 
				int val1 = Integer.parseInt(stack.pop());		
				int val2 = Integer.parseInt(stack.pop());
 
				int res = operation(val2 , val1, data.charAt(0));
 
				stack.push(Integer.toString(res)); 		
			}	
		}
		return stack.pop();
	}
 
	int operation(int a , int b, char operator)  {
 
		int res = 0;
 
		switch(operator) {
			case '+' :
				res = a + b;
				break;
			case '-' :
				res = a - b;
				break;
			case '*' :
				res = a * b;
				break;
			case '/' :
				res = a / b;
				break;
			case '^' :
				res = (int)Math.pow(a,b);
				break;
			default :	
		}
		return res;
	}
 
	public static void main(String args[]) throws IOException {
 
		ConsoleCalculator obj = new ConsoleCalculator();

		BufferedReader in = new BufferedReader (new InputStreamReader(System.in));
		String postfix ;
		System.out.print("enter postfix:");
		postfix = in.readLine();
		
		String evaluation = obj.postfix_evaluation(postfix);
		System.out.println("Postfix Expresion : " +postfix);
		System.out.println("Postfix Evaluation : " +evaluation);
 
	}
}
