public class pattern {
    //* 5 4 3 2 1 * */
    public static void main(String[] args) {


      pattern6_12345mirror(4);
        
    
   
    }
    static void pattern6_12345mirror(int n){

        for(int i=1;i<=n;i++)
        {
            for(int j=0;j<n-i;j++)
                {
                        System.out.print(" ");
                }

        for(int j=0;j<i;j++)
                {
                        System.out.print("*");
                }
              System.out.println();
            
        }

    }
    static void pattern1_54321star(int n){
        for(int  i = 5 ; i>0 ; i--){
                // System.out.println(" ");
                for(int j=0;j<i;j++){
                    System.out.print(" * ");
    
                }
                System.out.println(" ");
                
            }
    }
    static void pattern2_12345star(int n){
        for(int  i = 0 ; i<5 ; i++){

             for(int j=0;j<i;j++){
                 System.out.print(" * ");

             }
             System.out.println(" ");
            
         }
    }

    static void pattern3_12345numeric(int n){
        for(int  i = 1 ; i<=5 ; i++){

             for(int j=1;j<=i;j++){
                 System.out.print(j+"\t");

             }
             System.out.println(" ");
            
         }
    }

    static void pattern4_123454321star(int n){
       for(int i=0;i<2*n;i++){
        int k = i>n ? 2*n-i:i;
        for(int j = 0;j<=k;j++){
            System.out.print("* ");
        }
        System.out.println();
       }
    }

    static void pattern5_543212345numeric(int n){
    
       for(int i=2*n;i>0;i--){
        int k = i>n ? i:2*n-i;
        for(int j = 0;j<=k;j++){
            System.out.print("* ");
        }
        System.out.println();
       }
    }
    }


