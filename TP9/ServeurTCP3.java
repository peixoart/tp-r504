import java.io.*;
import java.net.*;

public class ServeurTCP3 {
    public static void main(String[] args) throws Exception {
        ServerSocket socketserver = new ServerSocket(2016);
        System.out.println("Serveur en attente");

        while (true) {
            Socket socket = socketserver.accept();
            System.out.println("Connexion d'un client");

            DataInputStream dIn = new DataInputStream(socket.getInputStream());
            DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());

            String msg = dIn.readUTF();
            System.out.println("Message reçu : " + msg);

            String rev = new StringBuilder(msg).reverse().toString();

            dOut.writeUTF(rev);

            socket.close();
        }
    }
}

