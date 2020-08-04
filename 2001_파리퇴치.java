import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader input = new BufferedReader (new InputStreamReader(System.in));
    static StringBuilder output = new StringBuilder();
    static int T,N,M,MAX;
    static int MAP[][];
    public static void main(String[] args) throws NumberFormatException, IOException {
        // TODO Auto-generated method stub
        T = Integer.parseInt(input.readLine());
        for(int t=1;t<=T;t++) {
            StringTokenizer tokens = new StringTokenizer(input.readLine(), " ");
            N = Integer.parseInt(tokens.nextToken());
            M = Integer.parseInt(tokens.nextToken());
            MAP = new int [N][N];
            MAX = Integer.MIN_VALUE;
            for(int row=0;row<N; row++) {
                StringTokenizer mapTokens = new StringTokenizer(input.readLine(), " ");
                for(int col=0;col<N;col++) {
                    MAP[row][col] = Integer.parseInt(mapTokens.nextToken());
                }
            }
            int CNT = N-M+1;
            for(int row=0; row<CNT; row++) {
                for(int col=0; col<CNT; col++) {
                    int SUM = 0;
                    for(int r=row; r<row+M; r++) {
                        for(int c=col; c<col+M; c++) {
                            SUM += MAP[r][c];
                        }
                    }if (SUM>MAX) MAX = SUM;
                }
            }
            output.append("#").append(t).append(" ").append(MAX).append("\n");
        }
        System.out.println(output);

    }

}
