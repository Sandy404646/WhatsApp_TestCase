package exceptionHandling;

public class TryCatch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(1);
		System.out.println(2);
		System.out.println(3);
		System.out.println(4);
		try{
			System.out.println(1/0);
		}catch(Throwable e) {
			System.out.println("Dont Divide by 0");
		}
		System.out.println(5);
		System.out.println(6);
	}

}
