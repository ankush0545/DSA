class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        vector<int> vec3;

        for (int x : nums1)
            vec3.push_back(x);

        for (int x : nums2)
            vec3.push_back(x);

        sort(vec3.begin(), vec3.end());

        int n = vec3.size();

        if (n % 2 == 0) {
            return (vec3[n/2] + vec3[n/2 - 1]) / 2.0;
        } else {
            return vec3[n/2];
        }
    }
};
