import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
	static StringTokenizer tokens;
	static int T, R,C, nR, nC, MAX;
	static char [][] MAP;
	static boolean [] VISITED;
	static int [][] DIR = {{-1,0},{1,0},{0,-1},{0,1}};
	public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for(int t=1; t<=T; t++){
            tokens = new StringTokenizer(br.readLine(), " ");
            R = Integer.parseInt(tokens.nextToken());
            C = Integer.parseInt(tokens.nextToken());
            MAX = 1;
            MAP = new char[R][C];
            VISITED = new boolean[26];
            for(int r=0; r<R; r++) MAP[r] = br.readLine().toCharArray();
            DFS(0,0,0);
            sb.append("#").append(t).append(" ").append(MAX).append("\n");
        }
        System.out.println(sb);
	}
	static void DFS(int r, int c, int d) {
        if(MAX == 26) return;
		if(VISITED[MAP[r][c]-'A']) {
			MAX = Math.max(MAX, d);
			return;
		}else {
			VISITED[MAP[r][c]-'A']=true;
			for(int i=0; i<4; i++) {
				nR = r+DIR[i][0];
				nC = c+DIR[i][1];
				if(nR>=0&&nR<R&&nC>=0&&nC<C) DFS(nR,nC,d+1);
			}
			VISITED[MAP[r][c]-'A']=false;
		}
	}
}