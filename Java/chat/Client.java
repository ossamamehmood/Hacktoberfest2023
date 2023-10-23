package network.chatd;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {

    Socket socket;
    BufferedReader bufferedReader;
    PrintWriter printWriter;

    public Client() {
        try {
            System.out.println("Sending request");
            socket = new Socket("216.24.57.3", 8080);
            System.out.println("Connection was made");
            bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            printWriter = new PrintWriter(socket.getOutputStream());
            startReading();
            startWriting();
        } catch (Exception e) {
            System.out.println("Connection failed");
            e.printStackTrace();
            System.exit(0);
        }
    }

    public void startReading() {
        Runnable r1 = () -> {
            while (true) {
                try {
                    String msg = bufferedReader.readLine();
                    if (msg.equals("exit")) {
                        System.out.println("Server terminated the chat");
                        break;
                    }
                    System.out.println("Server: " + msg);
                } catch (Exception e) {
                    e.printStackTrace();
                    System.exit(0);
                }
            }
        };
        new Thread(r1).start();
    }

    public void startWriting() {
        Runnable r2 = () -> {
            System.out.println("Writer start");
            while (true) {
                try {
                    BufferedReader br1 = new BufferedReader(new InputStreamReader(System.in));
                    String content = br1.readLine();
                    printWriter.println(content);
                    printWriter.flush();
                } catch (Exception e) {
                    e.printStackTrace();
                    System.exit(0);
                }
            }
        };
        new Thread(r2).start();
    }

    public static void main(String[] args) {
        new Client();
    }
}
