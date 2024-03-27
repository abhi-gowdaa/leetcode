class Solution {
public:
    bool isValid(string s) {
    stack<char> stk;
 
    for(int i=0;i<s.size();i++)
    {
      if (s[i] == '(' || s[i] == '{' || s[i] == '[')
      {
        stk.push(s[i]);
        } 
      else if (s[i] == ')' || s[i] == '}' || s[i] == ']')
      {
        if (stk.empty()) {
                return false; // If the stack is empty, there's no corresponding opening   parenthesis
            }
        char ele=stk.top();
        stk.pop();
        if ((s[i] == ')' && ele != '(' ) ||  
            ( s[i] == '}' && ele != '{') || 
             ( s[i] == ']' && ele != '[')) {
              return false;
            }
      }
    }

   return stk.empty();
    }
};