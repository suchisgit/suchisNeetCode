class Solution {
    public int bs(ArrayList<Integer> arr,int target){
        int lo=0;
        int hi=arr.size()-1;
        if(target>arr.get(hi)){
            return hi+1;
        }
        while(lo<hi){
            int m=lo+(hi-lo)/2;
            if (arr.get(m)<target){
                lo=m+1;
            }else{
                hi=m;
            }
        }
        return lo;
    }
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows=matrix.length;
        int cols=matrix[0].length;
        // System.out.println(rows+" "+cols);
        if (target<matrix[0][0] || target>matrix[rows-1][cols-1]){
            return false;
        }
        ArrayList<Integer> firstRow=new ArrayList();
        for(int i=0;i<rows;i++){
            firstRow.add(matrix[i][0]);
            // System.out.println(matrix[i][0]);
        } 
        int actualRow=bs(firstRow,target);
        if(actualRow<firstRow.size() && firstRow.get(actualRow)==target){
            return true;
        }
        // System.out.println("act row"+actualRow);
        ArrayList<Integer> actualRowArr= new ArrayList(); 
        for(int i=0;i<cols;i++){
            actualRowArr.add(matrix[actualRow-1][i]);
        }
        int pos=bs(actualRowArr,target);
        if(actualRowArr.size()>pos && actualRowArr.get(pos)==target){
            return true;
        }else{
            return false;
        }
    }
}