#include<string>
#include<stack>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        set<char> op={'(','{','['};
        int l=s.length();
        int i=0;
        while(i<l){
            if(op.find(s[i]) != op.end()){
                st.push(s[i]);
            }else{
                if(st.empty()){
                    return false;
                }
                char t=st.top();
                if( (s[i] == '}' and t== '{') or (s[i] == ']' and t== '[') or (s[i] == ')' and t== '(') ) {
                    st.pop();
                }else{
                    return false;
                }
            }
            i++;
        }
        return st.empty();
    }
};