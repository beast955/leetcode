// Title: Remove Duplicates from Sorted Array
            // Difficulty: Easy
            // Language: Java
            // Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
    public int removeDuplicates(int[] nums) {
        int n= nums.length;
        int k=1;
        for(int i=0;i<n;i++){
            if(nums[i]!=nums[k-1]){
                nums[k]=nums[i];
                k++;
            }
        }
        return(k);
    }
