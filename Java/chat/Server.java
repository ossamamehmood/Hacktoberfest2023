package network.chatd;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    ServerSocket server;
    Socket socket;
    BufferedReader bufferedReader;
    PrintWriter printWriter;

    public Server() {
        try {
            server = new ServerSocket(6666);
            System.out.println("Server is ready to accecpt connection");
            System.out.println("Waiting....");
            socket = server.accept();
            server.setSoTimeout(0);
            bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            printWriter = new PrintWriter(socket.getOutputStream());
            startReading();
            startWriting();
        } catch (Exception e) {
            e.printStackTrace();
            try {
                server.close();
            } catch (Exception ex) {
                ex.printStackTrace();
                e.printStackTrace();
            }
        }
    }

    public void startReading() {
        Runnable r1 = () -> {
            while (true) {
                try {
                    String msg = bufferedReader.readLine();
                    if (msg.equals("exit")) {
                        System.out.println("Client terminated the chat");
                        socket.close();
                        break;
                    }
                    System.out.println("Client: "+msg);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        };
        new Thread(r1).start();
    }

    public void startWriting(){
        Runnable r2 =()->{
            System.out.println("Writer start");
            while (true) {
                try {
                    BufferedReader br1 = new BufferedReader(new InputStreamReader(System.in));
                    String content  = br1.readLine();
                    printWriter.println(content);
                    printWriter.flush();
                    System.out.println("Message: "+content);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        };
        new Thread(r2).start();
    }

    public static void main(String[] args) {
        System.out.println("this is server...going to start");
        new Server();
    }
}
