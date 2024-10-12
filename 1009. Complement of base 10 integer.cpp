class Solution {
public:
    int bitwiseComplement(int n) {
        int a = n;
        int b = 0;
        if(n == 0)
            return 1;
        while(a != 0){
            b = (b << 1) | 1;
            a = a >> 1;
        }
        int c = (~n) & b;
        return c;
    }
};