package othello;

import java.util.Scanner;

public class Othello {
    Player player1,player2;
    Board board;

    public static void main(String args[]){
        Othello o = new Othello();
        o.startGame();

    }

    public void startGame(){
        Scanner s = new Scanner(System.in);

        //Setting player1 and player2
        player1 = takePlayerInput(1);
        player2 = takePlayerInput(2);
        while(player1.getSymbol() == player2.getSymbol()){
            System.out.println("Please enter another symbol!");
            char symbol = s.next().charAt(0);
            player2.setSymbol(symbol);
        }

        //Creating new board
        board = new Board(player1.getSymbol(),player2.getSymbol());
        
        int status = Board.INCOMPLETE;
        boolean p1Turn = true;
        while(status == Board.INCOMPLETE || status == Board.INVALID){
            if(p1Turn){

                //Taking player1 turn input
                System.out.println("Player1 " + player1.getName() + "'s turn!");
                System.out.println("Please enter X coordinate");
                int x = s.nextInt();
                System.out.println("Please enter Y coordinate");
                int y = s.nextInt();

                //checking player1 move
                status = board.move(x,y,player1.getSymbol());
                
                if(status != Board.INVALID){
                    p1Turn = false;
                    board.print();

                }else{
                    System.out.println("Invalid input!");
                }


            }else{

                 //Taking player1 turn input
                System.out.println("Player2 " + player2.getName() + "'s turn!");
                System.out.println("Please enter X coordinate");
                int x = s.nextInt();
                System.out.println("Please enter Y coordinate");
                int y = s.nextInt();

                //checking player1 move
                status = board.move(x,y,player2.getSymbol());

                if(status != Board.INVALID){
                    p1Turn = true;
                    board.print();

                }else{
                    System.out.println("Invalid input!");
                }

            }
        }
        if(status == Board.PLAYER1_WINS){
            System.out.println("Congratulations! Player1 " + player1.getName() + " wins." );
        }else if(status == Board.PLAYER2_WINS){
            System.out.println("Congratulations! Player2 " + player2.getName() + " wins." );
        }else{
            System.out.println("Congratulations! It was a draw --");
        }
    }

    public Player takePlayerInput(int num){
        Scanner s = new Scanner(System.in);

        //Taking player input
        System.out.println("Please enter player" + num + " name!");
        String name = s.nextLine();
        System.out.println("Please enter player" + num + " symbol");
        char symbol = s.next().charAt(0);

        //Creating new player
        Player p = new Player(name,symbol);
        return p;


    }
    
    
}
