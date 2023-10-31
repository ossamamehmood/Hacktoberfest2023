public class RemoveAllOccurrence {
    public static void main(String[] args) {
        String str = "baccad";
        char ele = 'x';
        StringBuilder ans = new StringBuilder();
        remove(str, ele,ans);
        System.out.println(ans);
    }
    public static StringBuilder remove(String str, char ele, StringBuilder ans){
        for (int i = 0; i < str.length(); i++) {
//            ans.append(ans);
            if(str.charAt(i) == ele){

            }else{
                ans.append(str.charAt(i));
            }
        }
        return ans;
    }
}
