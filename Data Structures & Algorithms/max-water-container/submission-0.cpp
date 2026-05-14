class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l=0;
        int r=heights.size()-1;
        int area=0;
        while (l<r) {
            int mnh=min(heights[l],heights[r]);
            area=max(area,mnh*(r-l));
            if(heights[l]<heights[r]){
                l++;
            }else{
                r--;
            }
        }
        return area;
    }
};
