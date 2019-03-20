import java.util.*;

public class InfixToPostfix
{
	public static void main(String args[])
	{
		Scanner in = new Scanner(System.in);
		String exp;
		System.out.println("enter the expression with proper parenthesis");
		exp=in.next();
		System.out.println(IToP(exp));
	}
	
	static int PrecedenceManager(char ch)
    {
        switch (ch)
        {
        case '+':
        case '-':
            return 1;
      
        case '*':
        case '/':
            return 2;
      
        case '^':
            return 3;
        case ',':
        	return 4;
        }
        return -1;
    }
      
    static String IToP(String exp)
    {
        String result = new String("");
        Stack<Character> stack = new Stack<>();
         
        for (int i=0;i<exp.length();i++)
        {
        	//System.out.println(i);
            char c = exp.charAt(i);
            
            if (Character.isLetterOrDigit(c))
            {
                result += c;
                //System.out.println(result);
            }
            /*else if(c=='+'||c=='-'||c=='*'||c=='/')
            {
            	result+=",";
            }*/
            
            else if (c=='(')
            	 stack.push(c);
            else if (c==')')
            {
                while (!stack.isEmpty()&&stack.peek()!='(')
                    result += stack.pop();
                 
                if (!stack.isEmpty()&&stack.peek()!='(')
                    return "Invalid Expression";               
                else
                	stack.pop();
            }
            /*else if (c==',')
            {
               stack.push(c);
            }*/
            else 
            {
            	int l=result.length();
            	char ch=result.charAt(l-1);
            	if(Character.isDigit(ch))
            	{
            		result +=",";
            		//System.out.println("lol");
            		while (!stack.isEmpty()&&PrecedenceManager(c)<=PrecedenceManager(stack.peek()))
                        result =result+stack.pop();
                        stack.push(c);
            	}
            	else
            	{
            	//result +=",";
                while (!stack.isEmpty()&&PrecedenceManager(c)<=PrecedenceManager(stack.peek()))
                    result =result+stack.pop();
                    stack.push(c);
            	}
            	l=0;
            	ch=' ';
            }
      
        }
      
        while (!stack.isEmpty())
            result=result+stack.pop();
      
        return result;
    }

}
