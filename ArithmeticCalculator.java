import java.util.Scanner

class Main {
  public static void main(String[] args){
    Scanner stinky = new Scanner(System.in);
    System.out.println("Enter first number for math problem");
    int firstNum = stinky.nextInt();
    Scanner poopoo = new Scanner(System.in);
    System.out.println("What type of problem: Addition, Subtraction, Multiplication, or Division? (Type Exactly!)")
    String typeOfProblem = poopoo.nextString;
    Scanner haha = new Scanner(System.in);
    System.out.println("Enter second number for math problem");
    int secondNum = haha.nextInt();
    
    if(typeOfProblem == "Addition"){
      System.out.println(firstNum + secondNum);
     }elseif(typeOfProblem == "Subtraction"){
      System.out.println(firstNum - secondNum);
     }elseif(typeOfProblem == "Multiplication"){
      System.out.println(firstNum * secondNum);
     }elseif(typeOfProblem == "Division"){
      System.out.println(firstNum / secondNum);
     } else{
      System.out.println("That is not an acceptable problem type, restart the program and retype the problem type");
     }
    }
   }
    
    
   
