import java.util.Scanner;
import java.io.File;  // Import the File class
import java.io.FileWriter;   // Import the FileWriter class
import java.io.IOException;  // Import the IOException class to handle errors

public class GetUserInput {
  public static void main(String args[]) {
    try {
      Scanner in = new Scanner(System.in);
      System.out.print("Who are we talking to? : ");
      String s = in.nextLine();
      File myObj = new File("UserInput.txt");
      myObj.createNewFile();
      FileWriter myWriter = new FileWriter("UserInput.txt");
      myWriter.write(s);
      myWriter.close();
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}
