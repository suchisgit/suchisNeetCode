class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> cntAr1(26,0),cntAr2(26,0);
        for(auto ch:s){
            cntAr1[ (int)ch - (int)'a' ]++;
        }
        for(auto ch:t){
            cntAr2[ (int)ch - (int)'a' ]++;
        }
        for( int i=0; i<26;i++){
            if( cntAr1[i] != cntAr2[i]){
                return false;
            }
        }
        return true;
    }
};
