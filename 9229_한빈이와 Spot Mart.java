import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer tokens;
	static int N,M,T,MAX;
	static int weights[], ans[];
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		T = Integer.parseInt(br.readLine());
		for(int t=1; t<=T; t++) {
			
			sb.append("#").append(t).append(" ");
			tokens = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(tokens.nextToken());
			M = Integer.parseInt(tokens.nextToken());
			weights = new int[N];
			ans = new int[2];
			tokens = new StringTokenizer(br.readLine(), " ");
			for(int idx=0;idx<N; idx++) {
				weights[idx] = Integer.parseInt(tokens.nextToken());
			}
			MAX = -1;
			// 조합을 써서 2개를 뽑아요
			combi(0,0);
			sb.append(MAX);
			sb.append("\n");
		}
		System.out.println(sb);
	}
	static void combi(int cnt, int start) {
		if(cnt == 2) {
			int sum = ans[0]+ans[1];
			if(sum<=M && sum>MAX) {MAX = sum;}
			return;
		}
		for(int idx=start; idx<N; idx++) {
			ans[cnt] = weights[idx];
			combi(cnt+1, idx+1);
		}
	}
}