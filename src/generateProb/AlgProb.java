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
		String[] temp  = new String[4];
		temp[0] = a + "x + " + b + "y = " + c;
		temp[1] = d + "x + " + e + "y = " + f;
		double t = (double)(c*e - b*f)/a*e-b*d;
		temp[2] = ((Double) t).toString();
		double u = (double)(c - a*t)/b;
		temp[2] = ((Double) u).toString();
		return temp;
		
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
		int j = (int) (Math.random()*25 + 1);
		int k = (int) (Math.random()*25 + 1);
		int l = (int) (Math.random()*25 + 1);
		String[] temp  = new String[6];
		temp[0] = a + "x + " + b + "y + " + c +"z = "+ d;
		temp[1] = e + "x + " + f + "y + " + g +"z = "+ h;
		temp[2] = i + "x + " + j + "y + " + k +"z = "+ l;
		int[][] det = new int[3][3];
		int[][] detx = new int[3][3];
		int[][] dety = new int[3][3];
		int[][] detz = new int[3][3];
		det[0] = new int[]{a,b,c};
		det[1] = new int[]{e,f,g};
		det[2] = new int[]{i,j,k};
		detx[0] = new int[]{d,b,c};
		detx[1] = new int[]{h,f,g};
		detx[2] = new int[]{l,j,k};
		dety[0] = new int[]{a,d,c};
		dety[1] = new int[]{e,h,g};
		dety[2] = new int[]{i,l,k};
		detz[0] = new int[]{a,b,d};
		detz[1] = new int[]{e,f,h};
		detz[2] = new int[]{i,j,l};
		double x1 = (double) determinant(detx, 3,3) / determinant(det, 3,3);
		double y1 = (double) determinant(dety, 3,3) / determinant(det, 3,3);
		double z1 = (double) determinant(detz, 3,3) / determinant(det, 3,3);
		temp[3] = ((Double) x1).toString();
		temp[4] = ((Double) y1).toString();
		temp[5] = ((Double) z1).toString();
		
	}
	return null;
		
		
}
	public static int determinant(int[][] result, int rows, int cols) {
	    if (rows == 2)
	        return result[0][0] * result[1][1] - result[0][1] * result[1][0];

	    int determinant1 = 0, determinant2 = 0;
	    for (int i = 0; i < rows; i++) {
	        int temp = 1, temp2 = 1;
	        for (int j = 0; j < cols; j++) {
	            temp *= result[(i + j) % cols][j];
	            temp2 *= result[(i + j) % cols][rows - 1 - j];
	        }

	        determinant1 += temp;
	        determinant2 += temp2;
	    }

	    return determinant1 - determinant2;
	}
}

