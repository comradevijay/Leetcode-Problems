class Solution {
    public boolean isValid(String s) {
        Stack<Character> cstack = new Stack<>();

        for(char c : s.toCharArray()){
            if(c == '(')
                cstack.push(')');
            else if(c == '{')
                cstack.push('}');
            else if(c == '[')
                cstack.push(']');

            else if(cstack.isEmpty() || cstack.pop() != c)
                return false;
        }
        return cstack.isEmpty();

        
    }
}