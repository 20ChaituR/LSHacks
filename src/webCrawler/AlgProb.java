package webCrawler;


public class AlgProb {
public static String[] generatorQuad()
{
	int a = (int) (Math.random()*3 + 1);
	int b = (int) (Math.random()*20 + 1);
	int c = (int) (Math.random()*20 + 1);
	String[] temp  = new String[3];
	temp[0] = a+ "x^2 + " +  b + "x + " + c; 
	if(Math.pow(b, 2)-4*a*c<0){
		temp[1]="none";
		temp[2] = null;
		return temp;
	}
	double answer1 = (-b + Math.sqrt(Math.pow(b, 2)-4*a*c))/2*a;
	double answer2 = (-b - Math.sqrt(Math.pow(b, 2)-4*a*c))/2*a;
	if(answer1==answer2){
		temp[1] = null;
		temp[2] = ((Double) answer1).toString();
	}
	else{
		temp[1] = ((Double) answer1).toString();
		temp[2] = ((Double) answer2).toString();
	}
		
	
	return temp;
}
public static String[] generatorLinear(){
	int a = (int) (Math.random()*25 + 1);
	int b = (int) (Math.random()*25 + 1);
	String[] temp  = new String[2];
	temp[0] = a+ "x + " +  b ; 
	double t = (double) -b/a;
	temp[1] = ((Double)t).toString();
	return temp;
}
public static String[] generatorSystem(){
	int number = (int) (Math.random()*2 + 2);
	if(number==2){
		int a = (int) (Math.random()*25 + 1);
		int b = (int) (Math.random()*25 + 1);
		int c = (int) (Math.random()*25 + 1);
		int d = (int) (Math.random()*25 + 1);
		int e = (int) (Math.random()*25 + 1);
		int f = (int) (Math.random()*25 + 1);
		String[] temp  = new String[3];
		temp[0] = a + "x + " + b + "y = " + c;
		temp[1] = d + "x + " + e + "y = " + f;
		
	}
	if(number==3){
		int a = (int) (Math.random()*25 + 1);
		int b = (int) (Math.random()*25 + 1);
		int c = (int) (Math.random()*25 + 1);
		int d = (int) (Math.random()*25 + 1);
		int e = (int) (Math.random()*25 + 1);
		int f = (int) (Math.random()*25 + 1);
		int g = (int) (Math.random()*25 + 1);
		int h = (int) (Math.random()*25 + 1);
		int i = (int) (Math.random()*25 + 1);
		String[] temp  = new String[4];
		temp[0] = a + "x + " + b + "y = " + c;
		temp[1] = d + "x + " + e + "y = " + f;
		temp[2] = g + "x + " + h + "y = " + i;
}

}

